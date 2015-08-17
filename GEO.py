import sys
import googlemaps
import json
class GEO:
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyBRdNZzB7aSpQQvpACvI7hiEkClCgrSKrs')
    def geocode(self,text):
        result = self.gmaps.geocode(text)
        if len(result) != 0:
            return result[0]['geometry']['location']
        else:
            return None
#For Test

if __name__ == "__main__":
    maps = GEO()
    response = maps.geocode(sys.argv[1])
    if response is not None:
        print json.dumps(response, indent = 4 )
