(function () {
    angular.module('tsp.main').directive('chart', chart);

    function chart() {
        return {
            restrict: 'E',
            scope: {
                configurations: "=configurations",
                results: "=results"
            },
            link: function (scope, element, attrs, fn) {
                var chart;

                scope.$watch("configurations", function (configurations) {
                    if (configurations == undefined || configurations.length <= 0) {
                        return;
                    }

                    var i = 0;
                    var datasets = _.map(configurations, function (conf) {
                        i++;
                        return {
                            label: conf.label,
                            strokeColor: conf.color,
                            pointHighlightStroke: conf.color,
                            data: []
                        }
                    });

                    var data = {
                        labels: [],
                        datasets: datasets
                    };

                    var canvas = $('<canvas/>');
                    canvas.width('100%');
                    canvas.height('350px');
                    var ctx = canvas.get(0).getContext('2d');
                    $(element).children().remove();
                    $(element).append(canvas);

                    console.log(configurations);
                    console.log(data);

                    chart = new Chart(ctx).Line(data, {
                        bezierCurve: false,
                        datasetFill: false
                    });
                }, true);


                scope.$watch("results", function (results) {
                    if (results == undefined || results.length <= 0) {
                        return;
                    }
                    var data = _.filter(results, function (x) {
                        return x.route_cost != undefined
                    }).map(function (result) {
                        return result.route_cost;
                    });

                    if (data == undefined || data.length <= 0) {
                        return;
                    }

                    chart.addData(data, "");
                }, true);

            }
        };
    }

})
();
