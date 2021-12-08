const buttons = document.querySelectorAll('.add-btn');
const delete_buttons = document.querySelectorAll('.btn');
// console.log(buttons);

function removing_prod(){
	const modal = this.parentNode.parentNode;
	console.log(modal)
	const name  = modal.querySelector('.prod-name').textContent;
	console.log(name)
	

	var req = new XMLHttpRequest();
    // var user_id = document.querySelector('.logo_fi').innerHTML;
    var link = null;
    var url = "/cart/remove";
    var send = name;

req.open("POST", url, true);
req.setRequestHeader("Content-type", "application/json");
req.send(JSON.stringify(send));
}


function sendingdata(){
    const modal = this.parentNode;
	console.log(modal)
    
    const title =  modal.querySelector("#title").textContent;
    const price = modal.querySelector("#price").textContent;
    console.log(title  ,price)
    var req = new XMLHttpRequest();
    // var user_id = document.querySelector('.logo_fi').innerHTML;
    var link = null;
    var url = "/test/ajax";
    var send = {"price": price, "title": title}

req.open("POST", url, true);
req.setRequestHeader("Content-type", "application/json");
req.send(JSON.stringify(send));
}
for (button of buttons){
    button.addEventListener('click' , sendingdata);
}
for (delete_button of delete_buttons) {
	delete_button.addEventListener('click' , removing_prod)
}


























// var title = document.quer




			// var server = "http://127.0.0.1:5000";
			// var op_num = {'sum':[3,4]};
			// function update_var()
			// {
			// 	var n1 = parseFloat($("#n1").val());
			// 	var n2 = parseFloat($("#n2").val());
			// 	op_num['sum']=[n1,n2];
			// }
			// $( function() {
			// 	$( "#sum" ).click(function() {
			// 		var appdir='/sum';
			// 		var send_msg = "<p>Sending numbers</p>";
			// 		var received_msg = "<p>Result returned</p>";
			// 		update_var();
			// 		console.log(send_msg);
			// 		$('#message').html(send_msg);
			// 		$.ajax({
  			// 			type: "POST",
  			// 			url:server+appdir,
  			// 			data: JSON.stringify(op_num),
  			// 			dataType: 'json'
			// 		}).done(function(data) { 
			// 			console.log(data);
			// 			$('#n3').val(data['sum']);
			// 			$('#message').html(received_msg+data['msg']);
			// 		});
			// 	});
  			// });




