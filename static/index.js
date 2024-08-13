//Getting data location based on HTML Geolocation API
function getlocation()
{
    navigator.geolocation.getCurrentPosition(showlocation);
}
function showlocation(position)
{
    let lat = position.coords.latitude;
    let lon = position.coords.longitude;
    const dict_value = {lat,lon};
    const string = JSON.stringify(dict_value);
    $.ajax(
        {
        url:"/",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(string),
        success: function(response){
            $('#main').text(response)
        }  
    });
    
    }
getlocation()
