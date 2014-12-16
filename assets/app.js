'use strict';


var katyusha = angular.module('KatyushaApp', ['ui.bootstrap']);

katyusha.controller('MainCtrl', function ($scope, dataProvider) {
    $scope.test = "test"
    $scope.oneAtATime = true;

    $scope.status = {
        isFirstOpen: true,
        isFirstDisabled: false
    };


    dataProvider.fetch()
        .then(function (data) {
            $scope.data = data;
        }, function (err) {
            console.log("jebika")
        })

});


katyusha.factory('dataProvider', function ($q, $timeout, $http, $location) {
    var data = {
        fetch: function () {
            var deferred = $q.defer();
            $timeout(function () {

                $http.get('results/' + $location.path()).success(function (data) {
                    deferred.resolve(data);
                });
            }, 30);
            return deferred.promise;
        }
    };

    return data;
});