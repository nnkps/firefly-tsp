(function () {
    angular
        .module('tsp', [
            'ui.bootstrap',
            'ui.utils',
            'ui.router',
            'ui.slider',
            'ngAnimate',
            'ngResource',
            'templates',
            'tsp.main'
        ])
        .config(configure)
        .run(runBlock);

    configure.$inject = ['$urlRouterProvider', '$locationProvider'];
    runBlock.$inject = ['$rootScope'];

    function configure($urlRouterProvider, $locationProvider) {
        $locationProvider.html5Mode({
            enabled: false,
            requireBase: false
        });

        /* Add New States Above */
        $urlRouterProvider.otherwise('/');

    }


    function runBlock($rootScope) {
        $rootScope.safeApply = function (fn) {
            var phase = $rootScope.$$phase;
            if (phase === '$apply' || phase === '$digest') {
                if (fn && (typeof(fn) === 'function')) {
                    fn();
                }
            } else {
                this.$apply(fn);
            }
        };
    }


})();
