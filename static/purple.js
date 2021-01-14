const controls=[
    ['rouge','/static/cards/PNG/Cards/cardBack_red5.png'],
    ['noir','/static/cards/PNG/Cards/cardBack_blue5.png'],
    ['purple','/static/cards/PNG/Cards/cardBack_green5.png']];

$(document).on('click', '#imgpaquet', function(){
    //alert('ok');
    for (var i;i<length(controls);i++){
        <div id='{{controls[i][0]}}' class='paquet'>
        <img id="img{{controls[i][0]}}"  src={{controls[i][1]}}/>
        <div id='{{controls[i][0]}}compteur' class='compteur'>0</div>
      </div>
    }
    $.get("/draw/", function(data, status){
        $('#defausse').html(data);
        console.log($('#paquetcompteur').html());
        $('#paquetcompteur').html((parseInt($('#paquetcompteur').html())-1).toString());

    });
});
