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
		url: '/_confirm',
		type: 'POST',
		success: function(data){
			alert(data.toString())
		},
		error: function(error){
			alert(error.toString());
		}
	});
}
