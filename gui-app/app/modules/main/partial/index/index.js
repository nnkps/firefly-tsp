(function () {
    angular.module('tsp.main').controller('IndexCtrl', IndexCtrl);

    IndexCtrl.$inject = ['SolverService', '$scope', '$q'];

    function IndexCtrl(SolverService, $scope, $q) {
        var vm = this;
        var id;
        vm.run = run;
        vm.addConfiguration = addConfiguration;
        vm.configurations = [];
        vm.parameters = {
            tsplib_data: ''
        };
        vm.results = [];


        $scope.$watch('vm.configurations', function (newData) {
            _.forEach(newData, function (c) {
                var firstPart = c.slider[0];
                var secondPart = c.slider[1];

                c.heurestics = {
                    nearest_neighbour: Math.round(firstPart * 100) / 100,
                    nearest_insertion: Math.round((1 - secondPart) * 100) / 100,
                    random: Math.round((secondPart - firstPart) * 100) / 100
                }

            })
        }, true);


        function run() {
            var jobs = [];
            _.forEach(vm.configurations, function (conf) {
                var request = {
                    tsplib_data: vm.parameters.tsplib_data,
                    number_of_individuals: conf.number_of_individuals,
                    iterations: conf.iterations,
                    heurestics: conf.heurestics
                };

                var deferred = $q.defer();
                SolverService.run(request, function (data) {
                    deferred.resolve(data);
                });
                jobs.push(deferred.promise)
            });


            $q.all(jobs).then(function (result) {
                vm.results = result;
                startPolling(result);
            })

        }

        function addConfiguration() {
            vm.configurations.push({
                number_of_individuals: 25,
                iterations: 200,
                slider: [0.3, 0.6],
                heurestics: {
                    nearest_neighbour: 0.2,
                    nearest_insertion: 0.6,
                    random: 0.2
                }
            })
        }

        function startPolling(confs) {
            var interval = setInterval(function () {
                var results = [];


                _.forEach(confs, function (c) {
                    var deferred = $q.defer();

                    SolverService.state({id: c.id}, function (data) {
                        deferred.resolve(data);
                    });

                    results.push(deferred.promise);
                });

                $q.all(results).then(function (results) {
                    vm.results = results;

                    var allDone = _.every(results, function (r) {
                        return r.done
                    });

                    if (allDone) {
                        clearInterval(interval)
                    }
                });

            }, 300);
        }

    }
})();
