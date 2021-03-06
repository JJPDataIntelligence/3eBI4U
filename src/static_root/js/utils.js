// CEP AUTOCOMPLETE ADDRESSES ON ADDRESS INFO PAGE
$(document).ready(function(){

    $('.js-cep').blur(function(){
        var cep = this.value.replace(/[^0-9]/, "");

        if(cep.length != 8){
            return false;
        }
        
       var url = "https://viacep.com.br/ws/"+cep+"/json/";
       
        $.getJSON(url, function(dadosRetorno){
            try{
                $('.js-end').val(dadosRetorno.logradouro);
                $('.js-bairro').val(dadosRetorno.bairro);
                $('.js-municipio').val(dadosRetorno.localidade);
                $('.js-estado').val(dadosRetorno.uf);
            }catch(ex){}
        });
    });

});

//MAKE VISIBLE SELECTION FIELD BAR ON FORM WIZARD TEMPLATES - VISIBILITY
function showField(x, y) {

    var checkbox    = $('#x');
    var elem     = $('#y');

    if (checkbox.checked == true){
        checkbox.prop('checked', true);
        elem.style.visibility = "visible";
    } else{
        checkbox.prop('checked', false);
        elem.style.visibility = "hidden";
    }
}

//MAKE VISIBLE SELECTION FIELD BAR ON FORM WIZARD TEMPLATES - DISPLAY
function displayField(x, y) {

    var checkbox    = $('#x');
    var elem     = $('#y');

    if (checkbox.checked == true){
        checkbox.prop('checked', true);
        elem.show();
    } else{
        checkbox.prop('checked', false);
        elem.hide();
    }
}



