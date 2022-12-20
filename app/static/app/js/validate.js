// TODO codigo Javascript debajo de esto

$(document).ready(function() {
    // cuando presiono el boton btnSubmit 
    // hace una llamada a la funcion onclick
    $("#btnSubmit").click(function(){

        //var contenido = $("#miParrafo").text();

        var campo_nombre = $("#user").val();
        var campo_contraseña =$("#pass").val();

        if (campo_nombre.length == 0 && campo_contraseña.length == 0){
            alert("Los campos no pueden estar vacíos.");

        }else
        if (campo_nombre.length == 0) {
            alert("El campo nombre no puede estar vacío.");
        }
        else if(campo_contraseña.length == 0){
            alert("La contraseña no debe estar vacía.");
        }
        else if(campo_contraseña.length <= 5){
                alert("Su contraseña debe exceder los 5 caracteres.");
        }
        
        // esto me permite redirigir mi sitio hacia otra pagina, 
        // solo si los campos estan validados
        else{            
            // me redirecciona a otra pagina
            window.location.href = 'Principal.html';                     
        }

    });
});