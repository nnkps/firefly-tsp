(function () {

    angular.module('tsp.main').factory('SolverService', SolverService);
    SolverService.$inject = ['$resource'];

    function SolverService($resource) {
        return $resource("/run", {}, {
            run: {
                method: 'POST',
                isArray: false
            }
        });
    }

})();
