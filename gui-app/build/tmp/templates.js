(function(module) {
try { module = angular.module("templates"); }
catch(err) { module = angular.module("templates", []); }
module.run(["$templateCache", function($templateCache) {
  "use strict";
  $templateCache.put("modules/main/partial/index/index.html",
    "<div class=\"row\">\n" +
    "    <div class=\"col-lg-12\">\n" +
    "        <h1>Solve TSP with firefly solver</h1>\n" +
    "\n" +
    "        <div class=\"row\">\n" +
    "            <div class=\"col-lg-12\">\n" +
    "                <form class=\"form-horizontal\">\n" +
    "                    <div class=\"panel panel-info\">\n" +
    "                        <div class=\"panel-heading\">Main configuration</div>\n" +
    "                        <div class=\"panel-body\">\n" +
    "                            <div class=\"form-group\">\n" +
    "                                <label for=\"fCount\" class=\"col-sm-2 control-label\">TSP input file:</label>\n" +
    "\n" +
    "                                <div class=\"col-sm-10\">\n" +
    "                                    <textarea class=\"form-control\" id=\"fInputFile\" ng-model=\"vm.parameters.tsplib_data\"\n" +
    "                                              rows=\"4\"/>\n" +
    "                                </div>\n" +
    "                            </div>\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "\n" +
    "\n" +
    "                    <div class=\"panel panel-info\" ng-repeat=\"c in vm.configurations\">\n" +
    "                        <div class=\"panel-heading\">Configuration {{$index + 1}}.</div>\n" +
    "                        <div class=\"panel-body\">\n" +
    "                            <div class=\"form-group\">\n" +
    "                                <label for=\"fCount\" class=\"col-sm-2 control-label\">Firefly count:</label>\n" +
    "\n" +
    "                                <div class=\"col-sm-10\">\n" +
    "                                    <input type=\"number\" class=\"form-control\" id=\"fCount\"\n" +
    "                                           ng-model=\"c.number_of_individuals\">\n" +
    "                                </div>\n" +
    "                            </div>\n" +
    "                            <div class=\"form-group\">\n" +
    "                                <label for=\"fIterationsCount\" class=\"col-sm-2 control-label\">Iterations count:</label>\n" +
    "\n" +
    "                                <div class=\"col-sm-10\">\n" +
    "                                    <input type=\"number\" class=\"form-control\" id=\"fIterationsCount\"\n" +
    "                                           ng-model=\"c.iterations\">\n" +
    "                                </div>\n" +
    "                            </div>\n" +
    "                            <div class=\"form-group\">\n" +
    "                                <label class=\"col-sm-2 control-label\">Heuristics configuration:</label>\n" +
    "\n" +
    "                                <div class=\"col-sm-10\">\n" +
    "                                    <div style=\"margin-top: 10px\" ui-slider=\"{range: true}\" min=\"0\" max=\"1.00\"\n" +
    "                                         step=\"0.01\" use-decimals ng-model=\"c.slider\"></div>\n" +
    "                                    <div style=\"margin-top: 10px\">\n" +
    "                                        <span class=\"label label-default\">Nearest neighbour: {{c.heurestics.nearest_neighbour}}</span>\n" +
    "                                        <span class=\"label label-default\">Nearest insertion: {{c.heurestics.nearest_insertion}}</span>\n" +
    "                                        <span class=\"label label-default\">Random: {{c.heurestics.random}}</span>\n" +
    "                                    </div>\n" +
    "                                </div>\n" +
    "                            </div>\n" +
    "\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                    <div class=\"form-group\">\n" +
    "                        <div class=\"col-sm-offset-2 col-sm-10 text-center\">\n" +
    "                            <button type=\"submit\" class=\"btn btn-default\" ng-click=\"vm.addConfiguration()\">Add\n" +
    "                                configration\n" +
    "                            </button>\n" +
    "                            <button type=\"submit\" class=\"btn btn-primary\" ng-click=\"vm.run()\"\n" +
    "                                    ng-show=\"!vm.running && vm.configurations.length > 0\">Run It\n" +
    "                            </button>\n" +
    "                            <button type=\"submit\" class=\"btn btn-danger\" ng-click=\"vm.stop()\"\n" +
    "                                    ng-show=\"vm.running && vm.configurations.length > 0\">Stop It\n" +
    "                            </button>\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                </form>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"row\">\n" +
    "            <div class=\"col-lg-6\" ng-repeat=\"r in vm.results\">\n" +
    "                <div class=\"panel panel-default\">\n" +
    "                    <div class=\"panel-heading\">\n" +
    "                        <span>Configuration {{$index + 1}}</span>\n" +
    "                        <span class=\"label label-danger\">Solution: {{r.route_cost}}, Iteration: {{r.iteration}}</span>\n" +
    "                        <span class=\"label label-default\" ng-show=\"!r.done\">Running...</span>\n" +
    "                    </div>\n" +
    "                    <div class=\"panel-body\">\n" +
    "                        <graph nodes=\"r.route\" class=\"graph-workspace\"></graph>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "\n" +
    "        <div class=\"row\">\n" +
    "            <div class=\"col-lg-12\">\n" +
    "                <chart configurations=\"vm.chartConfig\" results=\"vm.results\"></chart>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "    </div>\n" +
    "</div>\n" +
    "");
}]);
})();
