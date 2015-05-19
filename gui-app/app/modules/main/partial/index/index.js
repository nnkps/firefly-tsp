(function () {
    angular.module('tsp.main').controller('IndexCtrl', IndexCtrl);

    IndexCtrl.$inject = ['SolverService', '$scope', '$q'];

    function IndexCtrl(SolverService, $scope, $q) {
        var vm = this;
        var id;
        vm.run = run;
        vm.stop = stop;
        vm.addConfiguration = addConfiguration;
        vm.configurations = [];
        vm.parameters = {
            tsplib_data: ''
        };
        vm.results = [];
        vm.running = false;
        vm.chartConfig = [];

        var interval = null;
        var colors = [
            "rgba(247,221,134,1)",
            "rgba(235,158,104,1)",
            "rgba(230,124,116,1)",
            "rgba(99,98,128,1)",
            "rgba(78,145,144,1)"
        ];


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
            vm.chartConfig.length = 0;
            vm.running = true;
            vm.results.lenght = 0;

            var i = 0;
            _.forEach(vm.configurations, function (conf) {
                i++;
                var request = {
                    tsplib_data: vm.parameters.tsplib_data,
                    number_of_individuals: conf.number_of_individuals,
                    iterations: conf.iterations,
                    heurestics: conf.heurestics
                };

                vm.chartConfig.push({
                    label: "Configuration " + i,
                    color: colors[i - 1]
                });

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
            interval = setInterval(function () {
                var results = [];


                _.forEach(confs, function (c) {
                    var deferred = $q.defer();

                    SolverService.state({id: c.id}, function (data) {
                        deferred.resolve(data);
                    });

                    results.push(deferred.promise);
                });

                $q.all(results).then(function (results) {
                    if (!vm.running) {
                        return;
                    }
                    vm.results = results;

                    var allDone = _.every(results, function (r) {
                        return r.done
                    });

                    if (allDone) {
                        clearInterval(interval);
                        vm.running = false;
                    }
                });

            }, 300);
        }

        function stop() {
            clearInterval(interval);
            vm.running = false;
            vm.results.lenght = 0;
            vm.chartConf.lenght = 0;
        }

    }
})();
