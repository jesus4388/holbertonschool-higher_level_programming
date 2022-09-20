$(document).ready(function() {
    const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    $.getJSON(url, function(solicitud){
    $("DIV#character").append(solicitud.name);
    });
});