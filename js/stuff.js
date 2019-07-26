var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
  // Initialize and add the map
  function initMap() {
  // The location of Louisville
  var louisville = {lat: 38.2568, lng: -85.7552};
  // The map, centered at Louisville
  var map = new google.maps.Map(
  document.getElementById('map'), {zoom: 4, center: louisville});
  // The marker, positioned at Louisville1
  var marker = new google.maps.Marker({position: louisville, map: map});
}