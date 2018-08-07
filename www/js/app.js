var app = angular.module('myApp', []);
app.controller('MyCtrl', function($scope, $window, $http) {
    var vm = this;

    vm.param1 = "";
	//  vm.param2 = 3;
	//  vm.param3 = 54.3;
	//  vm.rez = '-';
    //vm.nesto = '';

	vm.preporuka = function(){
		var data = {
			'param1': vm.param1
			//'param2': parseFloat(vm.param2),
			//'param3': parseFloat(vm.param3)
		}
		var req = {
			method: 'POST',
			data: data,
			url: '/api/preporuka'
		}
		$http(req).then(
			function(respOk){
				console.log(respOk)
		vm.rez = respOk.data.rez[0];
		console.log(vm.rez);
        //vm.nesto = respOk.data.rez[1];
			},
			function(respErr){
				console.log(respErr)
			});
	}
});
