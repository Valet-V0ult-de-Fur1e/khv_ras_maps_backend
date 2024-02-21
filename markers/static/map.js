const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

const map = L.map('map')

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);

let data = new Map();

markers['features'].forEach(element => {
  if (!data[element.properties['id_crop_sort_fact']]) {
    data[element.properties['id_crop_sort_fact']] = [];
  }
  data[element.properties['id_crop_sort_fact']].push(element);
});

console.log(data)
// let feature_list = []
// data.forEach((values, keys) => {
//   L.geoJSON(values, {style: getStyle()}).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map)
// }) 

L.geoJSON(data['none'], {style: getStyle()}).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map)

console.log(feature_list)

map.fitWorld();

// map.fitBounds(feature_list.getBounds(), { padding: [100, 100] });
console.log(getRandomArbitrary())
// console.log(markers)

// L.geoJson(markers)
//   .on('click', function(e){
//       var popLocation= e.latlng;
//       var popup = L.popup()
//       .setLatLng(popLocation)
//       .setContent("polygon id:  " + JSON.stringify(e.sourceTarget.feature["id"]))
//       .openOn(map);
//       console.log(e.sourceTarget.feature);
//   })
//   .addTo(map)


function getStyle() {
  let color_str = "rgb(" + getRandomArbitrary() + ", " + getRandomArbitrary() + ", " + getRandomArbitrary() + ")"
    return {
      fillColor: 'black',
      weight: 2,
      opacity: 1,
      color: 'black',  //Outline color
      fillOpacity: 0.7
    };
}

function getRandomArbitrary() {
  maximum = 255
  minimum = 0
  return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;;
}