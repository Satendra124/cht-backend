import requests
from report.models import Location,Index
class Mapbox:
    tilesetIdBuildings = "satendra124.2vcxds0t"
    tilesetIdCampus = "satendra124.6lcp2e06"
    ACCESS_TOKEN = "pk.eyJ1Ijoic2F0ZW5kcmExMjQiLCJhIjoiY2tsbDNvaWZuMTM1NDJwbm1pZWZtZmt2ZSJ9.LbmaxYdRppOSYsS3kU0SOQ"
    @classmethod
    def get_place_from_lat_lng(self,lat,lng):
        queryUrlOncampus = f"https://api.mapbox.com/v4/{self.tilesetIdCampus}/tilequery/{lng},{lat}.json?access_token={self.ACCESS_TOKEN}"
        response1 = requests.get(queryUrlOncampus)
        response1 = response1.json()
        if(len(response1['features'])==0): 
            return "Out Of Campus"

        radius = 50
        queryUrlOnBuildings =f"https://api.mapbox.com/v4/{self.tilesetIdBuildings}/tilequery/{lng},{lat}.json?radius={radius}&access_token={self.ACCESS_TOKEN}"
        response2 = requests.get(queryUrlOnBuildings)
        response2 = response2.json()
        if(len(response2['features'])==0):
            return "Inside Campus"
        else: 
            return response2['features'][0]['properties']['Source']

    @classmethod
    def get_place(self,placeName):
        place = Location.objects.filter(name=placeName)
        if(len(place)==0): 
            print("PLACE NOT FOUND!"+placeName) #TODO: SOME ERROR LOG HERE
            return Location.objects.filter(name="Inside Campus")[0]
        return place[0]
    @classmethod
    def get_index(self,place):
        return place.index


    place_to_index = {
        "Out Of Campus":8,
        "Inside Campus":10,
        "ABLT inner part":1,
        "Administrative":1,
        "Applied physics internal department":3,
        "Aryabhatt 1 inner layer":2,
        "ASN Bose inner part":1,
        "Behind DO's Innerpart":1,
        "Chemical Departmentt Innerpart":3,
        "Civil Department Inner Parts":3,
        "Concrete Geology inner parts":3,
        "Corridor":2,
        "CSE innerpart":3,
        "CVR inner part":1,
        "DG innerpart":1,
        "Director Office Inner part":1,
        "Electrical Department inner parts":3,
        "Electronics Inner Part":3,
        "General Buildings":10,
        "General Builduings":10,
        "GSMC ext inner part":10,
        "GSMC inner parts":10,
        "Gymkhana inner parts":5,
        "Hostels":2,
        "Humanities Inner Parts":3,
        "Inner Part":10,
        "Library Inner Part":1,
        "Limbdi Inner Parts":6,
        "LT1 inner parts":3,
        "LT-3 Inner Parts":3,
        "Main Workshop Inner Parts":4,
        "Morvi Inner parts":2,
        "NCC Lab Inner Parts":1,
        "Pharma Inner Parts":3,
        "proffessor's quarter":1,
        "Rajputana Inner part":2,
        "Ramanujan Innerpart":2,
        "Rampur Hall Inner Parts":1,
        "SC Dey Inner Parts":2,
        "SMST Inner parts":2,
        "Sports and Grounds":5,
        "Sports and Grounds Inner Parts":5,
        "Vishweshwaraya Inner Part":2,
        "Vivekananda Corridor":2,
        "Vivekananda Inner Parts":2,
        "Water Bodies":10
    }
    index = {
        0:"Sleeping",
        1:"Admin",
        2:"Hostel",
        3:"Department",
        4:"workshop",
        5:"sports",
        6:"campus corners",
        7:"institute canteen",
        8:"Out of campus",
        9:"Hostel mess",
        10:"Others"
    }