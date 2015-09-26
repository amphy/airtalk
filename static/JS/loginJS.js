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
		url: 'confirm',
		type: 'GET',
		success: function(data){
			alert(data.toString())
		},
		error: function(error){
			alert(error.toString());
		}
	});
}