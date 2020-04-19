
  var country_layer;

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

  function style_states(feature) {
    return {
      fillColor: getStateColorByNGO(feature.properties.ngo_count),
      weight: 1,
      opacity: 1,
      color: 'grey',
      dashArray: '0',
      fillOpacity: 1
    };
  }

  function style_blank(feature) {
    return {
      fillColor: '#666',
      weight: 1,
      opacity: 1,
      color: 'grey',
      dashArray: '0',
      fillOpacity: 0.7
    };
  }


  function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
      weight: 3,
      color: '#666',
      dashArray: '',
      fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
      layer.bringToFront();
    }

    e.target.openPopup()
  }

  function resetHighlight(e) {
    country_layer.resetStyle(e.target);
    e.target.closePopup()
  }

  function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
  }

  var layer_list = {};

  function onEachFeatureInCountry(feature, layer) {
  	layer_list[feature.properties.name] = layer;
    layer.bindPopup('<span class="btn-link"><b>'+ feature.properties.name + '</b></span> <br/> \
      <b style="color:#333">Total NGOs</b>:&nbsp;' + feature.properties.ngo_count + '<br/>\
      <b style="color:#333">Population reach</b>:&nbsp;' + feature.properties.population_reach + '&nbsp;(approx)&nbsp;&nbsp;&nbsp; \
      <b style="color:#333">Staff count</b>:&nbsp;'+ feature.properties.staff_count);


    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
        // click: zoomToFeature
      });
  }


  function onEachFeatureInState(feature, layer) {
    layer.bindPopup('<span class="btn-link"><b>'+ feature.properties.name + '</b></span> <br/> \
      <b style="color:#333">Total NGOs</b>:&nbsp;' + feature.properties.ngo_count + '<br/>\
      <b style="color:#333">Population reach</b>:&nbsp;' + feature.properties.population_reach + '&nbsp;(approx)&nbsp;&nbsp;&nbsp; \
      <b style="color:#333">Staff count</b>:&nbsp;'+ feature.properties.staff_count);


    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
        // click: zoomToFeature
      });
  }

  var map = L.map('mapIndia1',{zoomSnap: .25}).setView([22.805, 82.0], 4.50);
  // Blank Layer to get us started
  var myLayer = L.geoJSON().addTo(map);


  var background_layer = L.geoJson(states_geojson, {
                            style: style_blank
                          });

  country_layer = L.geoJson(states_geojson, {
                    style: style_states,
                    onEachFeature: onEachFeatureInCountry
                  });

  country_layer.addTo(map);

  // var districts_layer 

// L.geoJson(districts_geojson, {
//   style: style_states,
//   // onEachFeature: onEachFeature
// }).addTo(map);


// Add OSM tile layer with correct attribution
var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12, attribution: osmAttrib}); 
map.addLayer(osm);  


function onStateLinkClick(stateName, divToShow){
  //set zoom level
	map.fitBounds(layer_list[stateName].getBounds());

  //remove any other active state layers
  if(active_state_layer){
    map.removeLayer(active_state_layer);
  }

  // remove the country level layer
  map.removeLayer(country_layer);

  //hide all the right side district details for any state that was shown previously
  $(".district_data").hide();


  // show the right side data for selected state
  $("#"+divToShow).show();

  //add the transaprent background country layer
  map.addLayer(background_layer);

  //add new active state layer
  active_state_layer = L.geoJson(districts_geojson[stateName], {
    style: style_states,
    onEachFeature: onEachFeatureInState
  }).addTo(map);
}

function onAllIndiaLinkClick(){
  map.fitBounds(country_layer.getBounds());
  //remove any active state layers
  if(active_state_layer){
    map.removeLayer(active_state_layer);
  }
 
  if(!map.hasLayer(country_layer)){
    map.addLayer(country_layer);    
  }

  //hide all the right side district details for any state that was shown previously
  $(".district_data").hide();

  // show the right side data for selected state
  // $("#"+countryDataDiv).show();



}