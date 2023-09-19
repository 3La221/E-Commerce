var updateBtns = document.getElementsByClassName('update-cart')
var resetBtn = document.getElementById('reset-cart')


resetBtn.addEventListener('click',function(){

    var orderId = this.dataset.order
    var action  = this.dataset.action

    if (user == "AnonymousUser") {
        console.log("USER")

    }else{

        resetUserOrder(orderId,action)

    }



})




for (var i = 0 ;  i < updateBtns.length ; i++) {

	updateBtns[i].addEventListener('click',function(){
		var productId = this.dataset.product
		var action = this.dataset.action 
        var quantity = parseInt($('#quantity-input').val()); // Get the quantity from the input field

		console.log('productId : ',productId,'action:',action)
		console.log('USER : ',user)
        console.log(quantity)


		if(user == "AnonymousUser"){
			console.log('User is not authenticated')
		}else{
			updateUserOrder(productId,action,quantity)
		}

	})
}

function resetUserOrder(orderId,action) {
   console.log("User is authenticated, sending data...");
   var url ='/reset_order/'

   fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
         body:JSON.stringify({'orderId':orderId , 'action':action}),
    })
    .then((response) => {
        return response.json(); // Fixed typo here from 'josn' to 'json'
    })
    .then((data) => {
        console.log('data:', data);
        location.reload()
    })



}

function updateUserOrder(productId, action,quantity) {
    console.log("User is authenticated, sending data...");
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action ,'quantity':quantity}),
    })
    .then((response) => {
        return response.json(); // Fixed typo here from 'josn' to 'json'
    })
    .then((data) => {
        console.log('data:', data);
        location.reload()
    })
   
}



