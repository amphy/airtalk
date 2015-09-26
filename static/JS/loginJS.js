function init(){
		$("#button").click(function(){
			verify();
		});
}

function verify(){
	if ($("#flightInputId").val() == "" || $("#emailInputId").val() == ""){
		alert("Not all fields filled out");
	}
}