
$(document).ready(function() {
    // cuando presiono el boton btnSubmit 
    // hace una llamada a la funcion onclick
    $("#guardar").click(function(){

        var campo_nombre = $("#user").val();
        var campo_contraseña =$("#pass").val();
        var campo_confirm_pass =$ ("#confirm_pass").val();

        if (campo_nombre.length == 0) {
            alert("El campo nombre no puede estar vacío.");
        }
        else if(campo_contraseña.length == 0){
            alert("La contraseña no debe estar vacía.");
        }else if(campo_confirm_pass.length == 0){
            alert("El campo de confirmaciòn de la contraseña no debe estar vacío.");
        }
        else if(campo_contraseña.length <= 5){
                alert("Su contraseña debe exceder los 5 caracteres.");
        }else if(!campo_contraseña.length == !campo_confirm_pass.length){
            alert("Ambas contraseñas deben ser igualess.");

        }
        
        // esto me permite redirigir mi sitio hacia otra pagina, 
        // solo si los campos estan validados
        else{            
            // me redirecciona a otra pagina
            window.location.href = 'Principal.html';                     
        }

    });
   /* $("#cancelar").click(function(){
        window.location.href = 'autentication.html';                     

    }*/

});