var map;
var markers = [];

function moveMarker(e) {
    e.target._latlng.lat.toFixed(3);
    e.target._latlng.lng.toFixed(3);
    $('#lat').val(e.latlng.lat);
    $('#lng').val(e.latlng.lng);
}

function addMarker(e) {
    var marker = DG.marker([e.latlng.lat, e.latlng.lng], {
        draggable: true
    }).addTo(map);
    marker.on('drag', moveMarker);
    $('#lat').val(e.latlng.lat);
    $('#lng').val(e.latlng.lng);
}

DG.then(function () {
    map = DG.map('map', {
        center: [51.152929, 71.424160],
        zoom: 13
    });
    map.on('click', addMarker);
});
