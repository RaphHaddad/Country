#this example shows how to use the JSON file of countries. 
#this example simply makes a CSV files
f = open("countries.csv",'a')
import requests
call = "https://raw2.github.com/RaphAustralia/Country/master/countries.json"
r = requests.get(call)
countries = r.json()
toWrite = ""
for country in countries:
        code=country["code"]
        name=country["name"]
        division=country["division"]
        if "lat" in country:
                lat=country["lat"]
        if "lng" in country:                
                lng=country["lng"]
        toWrite += "{0},{1},{2},{3},{4}\n".format(code.encode('utf-8'),name.encode('utf-8'),division.encode('utf-8'),lat,lng)

f.write(toWrite)        
f.close()       
