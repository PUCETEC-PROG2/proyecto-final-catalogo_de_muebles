function calculateTotal() {
    var total = 0;
    var checkboxes = document.querySelectorAll('.product');
  
    for (var i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        total += parseFloat(checkboxes[i].dataset.price);
      }
    }
  
    document.getElementById('total').textContent = total.toFixed(2);

  }

//MENSAJE ALERTA
// function confirmDelete() {
//   var confirmacion = confirm("¿Estás seguro de que quieres eliminar esto?");
  

//   if (confirmacion) {
//       // Aquí va el código para eliminar el elemento, por ejemplo:
//       alert("Elemento eliminado");
//       // O el código real para eliminar un item, como hacer una solicitud o removerlo del DOM.
//   } else {
//       alert("Eliminación cancelada");
//   }
// }

function confirmDelete(event) {
  var confirmacion = confirm("¿Estás seguro de que quieres eliminar esto?");

  if (!confirmacion) {
      // Si el usuario cancela, evita que el enlace se ejecute.
      event.preventDefault();
  } else {
      // Si confirma, puedes permitir que el enlace haga su acción normal.
      // Si quieres hacer algo diferente, como redirigir o hacer una acción AJAX, hazlo aquí.
  }
}

