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
let list_of_using_layers = ['19']
feature1.addTo(map)
map.fitBounds(feature1.getBounds(), { padding: [100, 100] });

let list_of_qboxes = document.querySelectorAll('input[type="checkbox"]')

const update_button = document.getElementById('updateMap')
update_button.onclick = () => {
  list_of_qboxes.forEach((checkbox) => {
    if (checkbox.checked){
      if (list_of_using_layers.indexOf(checkbox.value) == -1) {
        data_of_features[checkbox.value].addTo(map)
        list_of_using_layers.push(checkbox.value)
      }
    }
    else {
      if (list_of_using_layers.indexOf(checkbox.value) != -1) {
        data_of_features[checkbox.value].removeFrom(map)
        list_of_using_layers.splice(list_of_using_layers.indexOf(checkbox.value), 1);
      }
    }
  });
}

function getRandomArbitrary() {
  maximum = 255
  minimum = 0
  return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;;
}