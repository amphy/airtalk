function init(){
<<<<<<< HEAD
	var socket = io('turing.iamdevnull.info');
=======

	//var socket = io.connect('23.94.96.224');
  var socket = io.connect('heabuh.com');	

>>>>>>> origin/master
	
	socket.on("update", function(msg){
		if (ready){
			alert(msg);
		}
	});
	
	socket.on("update-people", function(people){
		if (ready){
			alert(people);
		}
	});
	
	socket.on("chat", function(who, msg){
		if (ready){
			alert(who + "  " + msg);
		}
	});
	
	socket.on("disconnect", function(){
		alert("disconnect");
	})
}
