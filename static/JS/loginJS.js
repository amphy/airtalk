function init(){
		$("#button").click(function(){
			verify();
		});
}

function verify(){
	if ($("#flightInputId").val() == "" || $("#emailInputId").val() == ""){
		alert("Not all fields filled out");
	}
	
	$.ajax({
		url: dfsdd,
		type: 'GET',
		success: function(data){
			alert(data)
		},
		error: function(error){
			alert(error);
		}
	});
}