(function () {
    angular.module('tsp.main').directive('graph', GraphDirective);

    function GraphDirective() {
        return {
            restrict: 'E',
            replace: true,
            scope: {
                nodes: "=nodes"
            },
            templateUrl: 'modules/main/directive/graph/graph.html',
            link: function ($scope, element, attrs, fn) {

                var width = $('#graph-workspace').width();
                var height = $('#graph-workspace').height();
                var path;
                var circle;

                var svg = d3.select("#graph-workspace").append("svg:svg")
                    .attr("width", width)
                    .attr("height", height);


                svg.append("svg:defs").selectAll("marker")
                    .data(["suit", "licensing", "resolved"])
                    .enter().append("svg:marker")
                    .attr("id", String)
                    .attr("viewBox", "0 -5 10 10")
                    .attr("refX", 15)
                    .attr("refY", -1.5)
                    .attr("markerWidth", 6)
                    .attr("markerHeight", 6)
                    .attr("orient", "auto")
                    .append("svg:path")
                    .attr("d", "M0,-5L10,0L0,5");

                function tick() {
                    path.attr("d", function (d) {
                        var dx = d.target.x - d.source.x,
                            dy = d.target.y - d.source.y,
                            dr = Math.sqrt(dx * dx + dy * dy);
                        return "M" + d.source.x + "," + d.source.y + "A" + 0 + "," + 0 + " 0 0,1 " + d.target.x + "," + d.target.y;
                    });
                }


                $scope.$watch('nodes', function (nodes) {
                    var links = createLinks(nodes);

                    if (path != undefined) {
                        path.remove();
                    }

                    if (circle != undefined) {
                        circle.remove();
                    }

                    path = svg.append("svg:g").selectAll("path")
                        .data(links)
                        .enter().append("svg:path")
                        .attr("class", function (d) {
                            return "link " + d.type;
                        });

                    circle = svg.append("svg:g").selectAll("circle")
                        .data(nodes)
                        .enter().append("svg:circle")
                        .attr("r", 6)
                        .attr("cx", function (d) {
                            return d.x;
                        })
                        .attr("cy", function (d) {
                            return d.y;
                        });

                    tick();

                }, true);


                function createLinks(nodes) {
                    var links = [];
                    var current;
                    var last;

                    _.forEach(nodes, function (node) {
                        if (current == undefined) {
                            current = node;
                        } else {
                            last = current;
                            current = node;
                            links.push({source: last, target: current})
                        }
                    });

                    links.push({source: current, target: nodes[0]});
                    return links;
                }


            }
        }
    }

})();
