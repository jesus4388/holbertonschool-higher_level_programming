$(document).ready(function(){
    const url = "https://fourtonfish.com/hellosalut/?lang=fr";
    $.getJSON(url, function(solicitud){
       $("DIV#hello").append(solicitud.hello);
    });
});