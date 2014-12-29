'use strict';


var katyusha = angular.module('KatyushaApp', ['ui.bootstrap']);

katyusha.controller('MainCtrl', function ($scope, dataProvider) {

    var avg
    $scope.test = "test"
    $scope.oneAtATime = true;

    $scope.status = {
        isFirstOpen: true,
        isFirstDisabled: false
    };


    dataProvider.fetch()
        .then(function (data) {
            $scope.data = data;

            var no_elements = 0
            var total = 10;
            angular.forEach($scope.data, function(value, key) {
                var len = parseInt(value.length)
                if (isNaN(len)) {
                    len=0
                }
                no_elements++
                total += len
            });
            avg = total/no_elements

        }, function (err) {
            console.log("jebika")
        })


    $scope.getAvg = function(){
        return avg
    }

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