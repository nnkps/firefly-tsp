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
    "                    <div class=\"form-group\">\n" +
    "                        <label for=\"fCount\" class=\"col-sm-2 control-label\">Firefly count:</label>\n" +
    "\n" +
    "                        <div class=\"col-sm-10\">\n" +
    "                            <input type=\"number\" class=\"form-control\" id=\"fCount\"\n" +
    "                                   ng-model=\"vm.parameters.number_of_individuals\">\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                    <div class=\"form-group\">\n" +
    "                        <label for=\"fCount2\" class=\"col-sm-2 control-label\">Number of cities:</label>\n" +
    "\n" +
    "                        <div class=\"col-sm-10\">\n" +
    "                            <input type=\"number\" class=\"form-control\" id=\"fCount2\"\n" +
    "                                   ng-model=\"vm.parameters.number_of_cities\">\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                    <!--<div class=\"form-group\">-->\n" +
    "                    <!--<label for=\"fFactorAlpha\" class=\"col-sm-2 control-label\">Factor &alpha;:</label>-->\n" +
    "\n" +
    "                    <!--<div class=\"col-sm-10\">-->\n" +
    "                    <!--<input type=\"number\" class=\"form-control\" id=\"fFactorAlpha\" ng-model=\"vm.parameters.alpha\">-->\n" +
    "                    <!--</div>-->\n" +
    "                    <!--</div>-->\n" +
    "                    <!--<div class=\"form-group\">-->\n" +
    "                    <!--<label for=\"fFactorBeta\" class=\"col-sm-2 control-label\">Factor &beta;:</label>-->\n" +
    "\n" +
    "                    <!--<div class=\"col-sm-10\">-->\n" +
    "                    <!--<input type=\"number\" class=\"form-control\" id=\"fFactorBeta\" ng-model=\"vm.parameters.beta\">-->\n" +
    "                    <!--</div>-->\n" +
    "                    <!--</div>-->\n" +
    "                    <!--<div class=\"form-group\">-->\n" +
    "                    <!--<label for=\"fFactorGamma\" class=\"col-sm-2 control-label\">Factor &gamma;:</label>-->\n" +
    "\n" +
    "                    <!--<div class=\"col-sm-10\">-->\n" +
    "                    <!--<input type=\"number\" class=\"form-control\" id=\"fFactorGamma\" ng-model=\"vm.parameters.gamma\">-->\n" +
    "                    <!--</div>-->\n" +
    "                    <!--</div>-->\n" +
    "\n" +
    "                    <div class=\"form-group\">\n" +
    "                        <label for=\"fIterationsCount\" class=\"col-sm-2 control-label\">Iterations count:</label>\n" +
    "\n" +
    "                        <div class=\"col-sm-10\">\n" +
    "                            <input type=\"number\" class=\"form-control\" id=\"fIterationsCount\"\n" +
    "                                   ng-model=\"vm.parameters.iterations\">\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                    <div class=\"form-group\">\n" +
    "                        <div class=\"col-sm-offset-2 col-sm-10 text-center\">\n" +
    "                            <button type=\"submit\" class=\"btn btn-default\" ng-click=\"vm.run()\">Run It</button>\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                </form>\n" +
    "\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"row\">\n" +
    "            <div class=\"col-lg-12\">\n" +
    "                <graph nodes=\"vm.nodes\"></graph>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "    </div>\n" +
    "\n" +
    "</div>\n" +
    "");
}]);
})();

(function(module) {
try { module = angular.module("templates"); }
catch(err) { module = angular.module("templates", []); }
module.run(["$templateCache", function($templateCache) {
  "use strict";
  $templateCache.put("modules/main/directive/graph/graph.html",
    "<div id=\"graph-workspace\">\n" +
    "\n" +
    "\n" +
    "</div>\n" +
    "");
}]);
})();
