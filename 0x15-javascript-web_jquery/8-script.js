$(document).ready(function(){
    const url = "https://swapi-api.hbtn.io/api/films/?format=json";
    $.getJSON(url, function(solicitud){
        console.log(solicitud.results)
        for (const value of Object.values(solicitud.results)) {
            console.log(value.title);
            $("UL#list_movies").append("<li>" + value.title + "</li>");
        }
    });
});