(function () {
    angular.module('tsp.main').controller('IndexCtrl', IndexCtrl);

    IndexCtrl.$inject = ['SolverService'];

    function IndexCtrl(SolverService) {
        var vm = this;
        vm.run = run;

        vm.parameters = {
            number_of_individuals: 25,
            alpha: 1,
            beta: 1,
            gamma: 1,
            iterations: 200
        };


        function run() {
            SolverService.run(vm.parameters);
        }

    }
})();
