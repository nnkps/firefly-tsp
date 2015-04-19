(function () {

    angular.module('tsp.main').factory('SolverService', SolverService);
    SolverService.$inject = ['$resource'];

    function SolverService($resource) {
        return $resource("/:type/:id", {}, {
            run: {
                method: 'POST',
                isArray: false,
                params: {type: 'run'}
            },
            state: {
                method: 'GET',
                isArray: false,
                params: {type: 'state'}
            }
        });
    }

})();
