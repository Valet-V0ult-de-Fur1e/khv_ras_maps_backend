const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const markers = JSON.parse(document.getElementById('markers-data').textContent);
let feature = L.geoJSON(markers).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });

L.geoJson(markers)
  .on('click', function(e){
      var popLocation= e.latlng;
      var popup = L.popup()
      .setLatLng(popLocation)
      .setContent("polygon id:  " + JSON.stringify(e.sourceTarget.feature["id"]))
      .openOn(map);
      console.log(e.sourceTarget.feature);
  })
  .addTo(map)