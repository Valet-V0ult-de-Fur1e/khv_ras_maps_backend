const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
let count_of_years = 5
let data_of_years = new Map();
for (i = 19; i < 19+count_of_years; ++i) {
  data_of_years[i] = JSON.parse(document.getElementById('markers-data-' + i).textContent);
}

let data_of_features = new Map();

for (i = 19; i < 19+count_of_years; ++i) {
  let year_rgb = getRandomArbitrary() + ", " + getRandomArbitrary() + ", " + getRandomArbitrary()
  data_of_features[i] = L.geoJSON(data_of_years[i], {style: {fillColor:"rgb(" + year_rgb + ")",fillOpacity: 0.5}})
}

let feature1 = data_of_features[19]
let list_of_using_layers = [19]
feature1.addTo(map)
map.fitBounds(feature1.getBounds(), { padding: [100, 100] });

const update_button = document.querySelector('updateMap')
update_button.addEventListener('click', () => {
  // When there is a "click"
  // it shows an alert in the browser
  alert('Oh, you clicked me!')
})

// let feature2 = data_of_features[22]


// for (i = 21; i < 19+count_of_years - 2; ++i) {
//   L.geoJson(data_of_years[i+1]).on('click', function(e){
//     var popLocation = e.latlng;
//     L.popup()
//     .setLatLng(popLocation)
//     .setContent(
//       "<div>20" + i + "</div>" +
//       "<div>polygon id:    " + JSON.stringify(e.sourceTarget.feature["id"]) + "\n" + "</div>"+
//       "<div>area:    " + JSON.stringify(e.sourceTarget.feature.properties["area"]) + "</div>"+
//       "<div>reestr_number:    " + JSON.stringify(e.sourceTarget.feature.properties["reestr_number"]) + "</div>" +
//       "<div>comment:    " + JSON.stringify(e.sourceTarget.feature.properties["comment"]) + "</div>" 
//       ).openOn(map);}).addTo(map)
// }

function getRandomArbitrary() {
  maximum = 255
  minimum = 0
  return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;;
}