function initMap() {
    var map = new google.maps.Map(document.getElementById('maps'), {
      zoom: 8,
      center: {lat: -34.397, lng: 150.644}
    });
    var marker = new google.maps.Marker({
      position: {lat: -34.397, lng: 150.644},
      map: map
    });
  }


