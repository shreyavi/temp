print "Access-Control-Allow-Origin: *"
import geocoder
g = geocoder.google('Mountain View, CA')
return g.latlng