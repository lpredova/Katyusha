'use strict';


var katyusha = angular.module('KatyushaApp', []);

katyusha.controller('MainCtrl', function ($scope, dataProvider) {
    $scope.test = "test"

    dataProvider.fetch()
        .then(function (data) {
            $scope.data = data;
        }, function (err) {
            console.log("jebika")
        })

});


katyusha.factory('dataProvider', function ($q, $timeout, $http, $location) {
    var data = {
        fetch: function (callback) {
            var deferred = $q.defer();
            $timeout(function () {
                //$http.get('results/test.json').success(function (data) {
                //console.log($location.search)
                //var result = $location.search()

                //console.log(result)

                $http.get('results/' + $location.path()).success(function (data) {
                    deferred.resolve(data);
                });
            }, 30);
            return deferred.promise;
        }
    };

    return data;
});