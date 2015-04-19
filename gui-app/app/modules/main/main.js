(function () {
    angular.module('tsp.main', ['ui.bootstrap', 'ui.utils', 'ui.router', 'ngAnimate']);

    angular.module('tsp.main').config(function ($stateProvider) {
        $stateProvider.state('main', {
            url: '/',
            templateUrl: 'modules/main/partial/index/index.html',
            controller: 'IndexCtrl',
            controllerAs: 'vm'
        });
        /* Add New States Above */

    });
})();
