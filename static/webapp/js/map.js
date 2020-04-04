
  var geojson;

  function getStateColorByNGO(d) {
    return d > 100 ? '#800026' :
    d > 50  ? '#BD0026' :
    d > 20  ? '#E31A1C' :
    d > 10  ? '#FC4E2A' :
    d > 5   ? '#FD8D3C' :
    d > 2   ? '#FEB24C' :
    d > 0  ? '#FED976' :
    '#FFEDA0';
  }

  function style_states1(feature) {
    return {
      fillColor: getStateColorByNGO(feature.properties.ngo_count),
      weight: 1,
      opacity: 1,
      color: 'grey',
      dashArray: '0',
      fillOpacity: 1
    };
  }


  function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
      weight: 5,
      color: '#666',
      dashArray: '',
      fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
      layer.bringToFront();
    }
  }

  function resetHighlight(e) {
    geojson.resetStyle(e.target);
  }

  function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
  }

  var layer_list = {};

  function onEachFeature(feature, layer) {
  	layer_list[feature.properties.ST_NM] = layer;
    layer.bindPopup('<span class="btn-link"><b>'+ feature.properties.ST_NM + '</b></span> <br/> \
      <b style="color:#333">Total NGOs</b>:' + feature.properties.ngo_count + '<br/>\
      <b style="color:#333">Population reach</b>:' + feature.properties.population_reach + '&nbsp;&nbsp;&nbsp;&nbsp; \
      <b style="color:#333">Staff count</b>:'+ feature.properties.staff_count);


    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
        // click: zoomToFeature
      });
  }

  var map = L.map('mapIndia1',{zoomSnap: .25}).setView([22.805, 82.0], 4.50);
// Blank Layer to get us started
var myLayer = L.geoJSON().addTo(map);


geojson = L.geoJson(states_geojson, {
  style: style_states1,
  onEachFeature: onEachFeature
}).addTo(map);


// Add OSM tile layer with correct attribution
var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12, attribution: osmAttrib}); 
map.addLayer(osm);  


function onStatLinkClick(stateName){
	map.fitBounds(layer_list[stateName].getBounds());
}