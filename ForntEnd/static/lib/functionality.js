function trashMarkerPlacement() {
	var points = [];
	var example;
	
	console.log("placing makers")
	
	$.ajax({
	    type: 'GET',
	    
	    url: "{{ url_for('interactive2') }}",
	    data:  "{{ data }}", // serializes the form's elements.
	    success: function (data) {

	for (var i = 0; i<data.length; i++){
	        console.log(data[i]);

	        fountains = JSON.parse(JSON.stringify(data[i]));

	        var utm = "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"
	        var geo = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs";

	        var geo = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs";
	                       var x = fountains['geometry']['coordinates'][0];
	                
	                       var y = fountains['geometry']['coordinates'][1];
	  

	                       var popupText = fountains['properties']["road"];
	                       var lat = x;
	                       var lon = y;

	                       var markerLocation = new L.LatLng(lat, lon);
	                       trashMarker = new L.Marker(trashMarker);
	                       
	                       map.addLayer(trashMarker);
	                       trashMarker.bindPopup(popupText);  
	                       }       


	    }});
}