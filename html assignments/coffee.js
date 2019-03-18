let getAllOrders = document.getElementsByClassName("getAllOrders")[0]
let coffee = document.getElementsByClassName("coffee")[0]

getAllOrders.addEventListener('click',function(){

let url = "http://dc-coffeerun.herokuapp.com/api/coffeeorders/"
 console.log(JSON.stringify(url))

 fetch('http://dc-coffeerun.herokuapp.com/api/coffeeorders/')
.then(function(response){
 return response.json()
}).then(function(json){
 console.log(json)
 let keys = Object.keys(json)
 console.log(keys)

 let userData = keys.map(function(key) {
   let order = json[key]
   return `<div>
           <li>${order.emailAddress}</li>
           <li>${order.coffee}</li>
           </div>`
 })

 coffee.innerHTML = userData.join('')

})


})

//
