
$(document).ready(function() {
     $('#trans').on('submit', function(event) {
         event.preventDefault();
         $.ajax({
          data : {
              address : $('#address').val(),
              opt: $('#opt').val(),
              value: $('#value').val(),
                 },
             type : 'POST',
             url : '/transaccion/'
            })
        .done(function(data) {
          if (data.status === "error") {
              alert("Direccion u opt no validos!!!!");
          }else{
              $("#exampleModal").modal('hide');
              alert("Transacción realizada existosamente!!");
          }

      });
      });
});


// $('#transaccion').on('click', function() {
//     var address = document.getElementById('address').value;
//     var opt = document.getElementById('opt').value;
//     var value = document.getElementById('value').value;
//     console.log(address);
//     var data = {address: address, opt: opt, value: value};
//     var url = '/transaccion/';
//    fetch(url, {
//      method: 'POST', // or 'PUT'
//      body: JSON.stringify(data), // data can be `string` or {object}!
//      headers:{
//        'Content-Type': 'application/json'
//      }
//    }).then(res => res.json())
//     .catch(error => console.error('Error:', error))
//     .then(response => console.log('Success:', response));
// });