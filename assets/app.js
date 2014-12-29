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


    $scope.getAvg = function(){
        var no_elements = 1
        var total = 10;
        angular.forEach($scope.data, function(value, key) {
            var len = parseInt(value.length)
            if (isNaN(len)) {
                len=0
            }
            no_elements++
            total += len
        });

        console.log('AVG' + total/no_elements)
        return total/no_elements
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