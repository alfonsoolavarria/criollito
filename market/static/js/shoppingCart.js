$(document).ready(function() {
  /*Carrito de compras*/

  /*reviso si cuando cargue la pagina hay data en el local la pongo*/
  if(localStorage.getItem("carrito")){
    var carrito = JSON.parse(localStorage.getItem("carrito"));
    $('#cartCesta').attr('data-notify',carrito.length);
  }

  /*click en add al carro*/
  document.addEventListener("click",function(ev){
    ev.preventDefault();

    if(!localStorage.getItem("carrito")){
      localStorage.setItem('carrito','[]');
    }

    if(ev.target.id === "addItem"){
        var id = ev.target.dataset;
        agregarItem(id);//mando lo que agregare
    }
  });


  /*add al carro*/
  function agregarItem(item){
    console.log('----ITEM',item);
    var carrito = JSON.parse(localStorage.getItem("carrito"));
    if (carrito && carrito.length>0) {
      for (i of carrito){
        if(i.id === item.id){
          if (item.cantidad){
            i.cantidad = parseInt(i.cantidad)+parseInt(item.cantidad);//agrego y aumento 1 porque ya existe el item en el carrito
          }else{
            i.cantidad=parseInt(i.cantidad)+1;
          }
          //valido que la cantidad de productos no exceda la cantidad del stock
          if (parseInt(i.cantidad)>parseInt(item.cant)){
            i.cantidad=parseInt(item.cant);
          }
          localStorage.setItem("carrito",JSON.stringify(carrito));
          $('#cartCesta').attr('data-notify',carrito.length);//notificacion de cantidad de productos en el carrito
          return;
        }
      }
      if (!item.cantidad){
        item.cantidad = 1;//inserto un item nuevo al carrito
      }
      carrito.push(item);
      localStorage.setItem("carrito",JSON.stringify(carrito));
      $('#cartCesta').attr('data-notify',carrito.length);//notificacion de cantidad de productos en el carrito
      return;
    }else {
      if (!item.cantidad){
        item.cantidad = 1;//inserto un item nuevo al carrito
      }
      carrito.push(item);
      localStorage.setItem("carrito",JSON.stringify(carrito));
      $('#cartCesta').attr('data-notify',carrito.length);//notificacion de cantidad de productos en el carrito
    }


  }

});
