const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
// const markers1 = JSON.parse(document.getElementById('markers-data-1').textContent);
const markers2 = JSON.parse(document.getElementById('markers-data-2').textContent);
let feature1 = L.geoJSON(markers2, {style: getStyle()}).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
// let feature2 = L.geoJSON(markers2, {style: getStyle()}).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.fitBounds(feature1.getBounds(), { padding: [100, 100] });

// L.geoJson(markers1)
//   .on('click', function(e){
//       var popLocation= e.latlng;
//       var popup = L.popup()
//       .setLatLng(popLocation)
//       .setContent("polygon id:  " + JSON.stringify(e.sourceTarget.feature["id"]))
//       .openOn(map);
//       console.log(e.sourceTarget.feature);
//   })
//   .addTo(map)

  function getStyle(feature) {
    return {
        // weight: 0.1,
        weight: 0.1,
        // opacity: 0.1,
        fillColor: 'black',
        color: 'black',
        lineJoin: 'miter',
        fillOpacity: 1,
        offset: -4,
        // fillColor: "rgb(255, 0, 0)"
    };
}

  L.geoJson(markers2)
  .on('click', function(e){
      var popLocation= e.latlng;
      var popup = L.popup()
      .setLatLng(popLocation)
      .setContent("polygon id:  " + JSON.stringify(e.sourceTarget.feature["id"]))
      .openOn(map);
      console.log(e.sourceTarget.feature);
  })
  .addTo(map)