$(document).ready(function() {

    $(document).on('click', '#imgpaquet', function(){
        //alert('ok');
        $.get("/draw/", function(data, status){
            $('#defausse').html(data);
            console.log($('#paquetcompteur').html());
            $('#paquetcompteur').html((parseInt($('#paquetcompteur').html())-1).toString());

        });
    });

    $(document).on('click', '#imgtrash', function(){
        //alert('ok');
        $.get("/vider/", function(data, status){
            $('#defausse').html('');
            $('#trashcompteur').html(data);
        });
    });
});