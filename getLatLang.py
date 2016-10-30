import geocoder
self.send_header("Access-Control-Allow-Origin","*");
self.send_header("Access-Control-Expose-Headers: Access-Control-Allow-Origin");
self.send_header(("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
self.send_header("Content-type", "application/json")
self.end_headers()
g = geocoder.google('Mountain View, CA')
return g.latlng