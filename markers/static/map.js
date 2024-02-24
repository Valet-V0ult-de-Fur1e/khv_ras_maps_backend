const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const map = L.map('map')

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);
console.log(markers)
let list_of_crop_sort = [];
markers['features'].forEach(element => {
  if (list_of_crop_sort.indexOf(element.properties['id_crop_sort_fact']) == -1) {
    list_of_crop_sort.push(element.properties['id_crop_sort_fact'])
  }
});
let list_or_markers = [];
for (let i = 0; i <= list_of_crop_sort.length; ++i) {
  let marker = JSON.parse(document.getElementById('markers-data').textContent);
  marker.features = marker.features.filter(item => item.properties['id_crop_sort_fact'] == list_of_crop_sort[i])
  let feature = L.geoJSON(marker, {style: {
    fillColor: (list_of_crop_sort[i] == null)? "rgb(255, 255, 255)" : marker.features[0]["properties"]['crop_color'],
    fillOpacity: 1
  }}).on('click', function(e){
    var popLocation= e.latlng;
    var popup = L.popup()
    .setLatLng(popLocation)
    .setContent(
      "<div>год 2019</div>" +
      "<div>id полигона:    " + JSON.stringify(e.sourceTarget.feature["id"]) + "\n" + "</div>"+
      "<div>площадь:    " + JSON.stringify(e.sourceTarget.feature.properties["area"]) + "</div>"+
      "<div>номер реестра:    " + JSON.stringify(e.sourceTarget.feature.properties["reestr_number"]) + "</div>" +
      "<div>культура:    " + JSON.stringify(e.sourceTarget.feature.properties["crop_name"]) + "</div>" 
      )
    .openOn(map);
}).addTo(map);
  list_or_markers.push(feature);
}

map.fitBounds(list_or_markers[0].getBounds(), { padding: [100, 100] });