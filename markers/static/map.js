const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const map = L.map('map')

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);
// console.log(markers.properties)
let list_of_crop_sort = [];
console.log(markers)
markers['features'].forEach(element => {
  if (list_of_crop_sort.indexOf(element.properties['id_crop_sort_fact']) == -1) {
    list_of_crop_sort.push(element.properties['id_crop_sort_fact'])
  }
});
let list_or_markers = [];
for (let i = 0; i <= list_of_crop_sort.length; ++i) {
  let marker = JSON.parse(document.getElementById('markers-data').textContent);
  // console.log(marker.features.filter(item => item.properties['id_crop_sort_fact'] == list_of_crop_sort[i]))
  marker.features = marker.features.filter(item => item.properties['id_crop_sort_fact'] == list_of_crop_sort[i])
  
  let year_rgb = getRandomArbitrary() + ", " + getRandomArbitrary() + ", " + getRandomArbitrary()
  let feature = L.geoJSON(marker, {style: {
    fillColor:"rgb(" + year_rgb + ")",
    fillOpacity: 1
  }}).addTo(map);
  list_or_markers.push(feature);
}

console.log(list_of_crop_sort);

// map.fitWorld();
map.fitBounds(list_or_markers[0].getBounds(), { padding: [100, 100] });
function getRandomArbitrary() {
  maximum = 255
  minimum = 0
  return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;;
}