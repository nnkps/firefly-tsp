(function () {
    angular.module('tsp.main').controller('IndexCtrl', IndexCtrl);

    IndexCtrl.$inject = ['SolverService'];

    function IndexCtrl(SolverService) {
        var vm = this;
        var id;
        vm.run = run;

        vm.parameters = {
            number_of_individuals: 25,
            alpha: 1,
            beta: 1,
            gamma: 1,
            iterations: 200
        };

        vm.nodes = [
            {x: 100, y: 100},
            {x: 200, y: 230},
            {x: 90, y: 129},
            {x: 100, y: 220},
            {x: 79, y: 100}
        ];

        function run() {
            SolverService.run(vm.parameters, function (data) {
                vm.nodes = data.route;
                startPolling(data.id);
            });
        }

        function startPolling(id) {
            var interval = setInterval(function () {
                SolverService.state({id: id}, function (data) {
                    vm.nodes = data.route;
                    if (data.done === true) {
                        clearInterval(interval);
                    }
                })
            }, 100);
        }

    }
})();
