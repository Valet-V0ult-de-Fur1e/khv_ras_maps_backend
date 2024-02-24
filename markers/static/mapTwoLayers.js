const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const markers1 = JSON.parse(document.getElementById('markers-data-1').textContent);
const markers2 = JSON.parse(document.getElementById('markers-data-2').textContent);
let second_year_rgb = getRandomArbitrary() + ", " + getRandomArbitrary() + ", " + getRandomArbitrary()
console.log(second_year_rgb)
let feature1 = L.geoJSON(markers1
).on('click', function(e){
  var popLocation= e.latlng;
  var popup = L.popup()
  .setLatLng(popLocation)
  .setContent(
    "<div>2019</div>" +
    "<div>polygon id:    " + JSON.stringify(e.sourceTarget.feature["id"]) + "\n" + "</div>"+
    "<div>area:    " + JSON.stringify(e.sourceTarget.feature.properties["area"]) + "</div>"+
    "<div>reestr_number:    " + JSON.stringify(e.sourceTarget.feature.properties["reestr_number"]) + "</div>" +
    "<div>культура:    " + JSON.stringify(e.sourceTarget.feature.properties["crop_name"]) + "</div>" +
    "<div>comment:    " + JSON.stringify(e.sourceTarget.feature.properties["comment"]) + "</div>" 
    )
  .openOn(map);
}).addTo(map);
let feature2 = L.geoJSON(markers2, {style: {
  fillColor:"rgb(" + second_year_rgb + ")",
  fillOpacity: 1
}}).on('click', function(e){
  var popLocation= e.latlng;
  var popup = L.popup()
  .setLatLng(popLocation)
  .setContent(
    "<div>2022</div>" +
    "<div>polygon id:    " + JSON.stringify(e.sourceTarget.feature["id"]) + "\n" + "</div>"+
    "<div>area:    " + JSON.stringify(e.sourceTarget.feature.properties["area"]) + "</div>"+
    "<div>reestr_number:    " + JSON.stringify(e.sourceTarget.feature.properties["reestr_number"]) + "</div>" +
    "<div>культура:    " + JSON.stringify(e.sourceTarget.feature.properties["crop_name"]) + "</div>" +
    "<div>comment:    " + JSON.stringify(e.sourceTarget.feature.properties["comment"]) + "</div>" 
    )
  .openOn(map);
}).addTo(map);
map.fitBounds(feature1.getBounds(), { padding: [100, 100] });

function getRandomArbitrary() {
  maximum = 255
  minimum = 0
  return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;;
}