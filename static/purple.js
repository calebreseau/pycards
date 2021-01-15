$(document).ready(function() {
    function spec_update(data){
    var score=parseInt(data.split(',')[0]);
    if (score==0) alert('Buvez '+$('#scorecompteur').html()+' gorgees')
    $('#scorecompteur').html(parseInt(score+1));
    }

    window.spec_update=spec_update;
});