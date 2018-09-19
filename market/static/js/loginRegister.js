$(document).ready(function() {

  $('.login').submit(function (e) {
    e.preventDefault();
    /*console.log('Login',e.currentTarget);
    console.log(e.currentTarget[0].value); // csrf
    console.log(e.currentTarget[2].value); // email
    console.log(e.currentTarget[3].value); // password*/
    $.post('/login/',{
      csrfmiddlewaretoken:e.currentTarget[0].value,
      email:e.currentTarget[2].value,
      password:e.currentTarget[3].value
    }).done(function (result) {
      console.log('--->',result);
      if (result.code==200) {
        window.location.href = '/'
      }else {
        //poner un tootip
        alertify.error('intente de nuevo '+result.message);
      }
    }).fail(function(error) {
      console.log(error.responseText);
    });
   });

  $('#msform').submit(function (e) {
    e.preventDefault();
    /*console.log('Registro',e.currentTarget);
    console.log(e.currentTarget[1].value); // email
    console.log(e.currentTarget[2].value); // password
    console.log(e.currentTarget[3].value); // confir password

    console.log(e.currentTarget[6].value); // name
    console.log(e.currentTarget[7].value); // lastname
    console.log(e.currentTarget[8].value); // phone
    console.log(e.currentTarget[9].value); // direction

    console.log(e.currentTarget[13].value); // Tw
    console.log(e.currentTarget[14].value); // Fb
    console.log(e.currentTarget[15].value); // Goo*/

    if (e.currentTarget[2].value.length>0 && e.currentTarget[3].value.length>0 &&
      e.currentTarget[1].value.length>0 && e.currentTarget[6].value.length>0 &&
      e.currentTarget[7].value.length>0 && e.currentTarget[8].value && e.currentTarget[9].value) {

      $.post('/profile/',{
        csrfmiddlewaretoken:e.currentTarget[0].value,
        email:e.currentTarget[1].value,
        password:e.currentTarget[2].value,
        name:e.currentTarget[6].value,
        lastname:e.currentTarget[7].value,
        phone:e.currentTarget[8].value,
        direction:e.currentTarget[9].value,
        Tw:e.currentTarget[13].value,
        Fb:e.currentTarget[14].value,
        Goo:e.currentTarget[15].value
      }).done(function (result) {
        if (result.code==200) {
          alertify.success('Usuario Creado con Éxito');
          var delayInMilliseconds = 1000; //menos de 1 second
          setTimeout(function() {
            window.location.href = '/'
          }, delayInMilliseconds);
        }else {
          //poner un tootip
          alertify.error(result.error[0]);
        }
      }).fail(function(error) {
        console.log(error.responseText);
      });

    }else {
      alertify.error('Hace falta llenar un campo requerido');
    }



   });

});
