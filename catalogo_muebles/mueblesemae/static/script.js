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




//MENSAJE DE ALERTA//
// function mensaje_alerta(){
//     window.alert("")
//     if (botoneliminar = estapresionado){
//         window.alert("¿Estas seguro de eliminar?")

//     }
// }


// function agregarevento() {   
//     var elemento = document.querySelector("section > button"); 
//     elemento.addEventListener("click", mostrarmensaje); 
// } 


// function mostrarmensaje() {   
//     confirmacion = window.confirm("Presionó el botón"); 
//     var btn_borrar = document.getElementById("borrar");
//     if(confirmacion == true)
//     {
//         alert(btn_borrar)
//     }
    
// } 
// window.addEventListener("load", agregarevento);