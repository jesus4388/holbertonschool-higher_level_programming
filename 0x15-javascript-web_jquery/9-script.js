$(document).ready(function(){
    const url = "https://fourtonfish.com/hellosalut/?lang=fr";
    $.get(url, function(solicitud){
       $("DIV#hello").text(solicitud.hello);
    });
});