import requests
import os 
import json

url_base = "https://app.sportdataapi.com/api/v1/"
key = os.environ["apikey"]
continente = input("Dime un continente: ")

payload = {'apikey':key,"continent":continente}

url = url_base + "soccer/" + "countries"
r = requests.get(url,params = payload)
if r.status_code == 200:
    datos=r.json()
    for resultado in datos["data"]:
        print(resultado)
    id = input("¿Que id quieres que muestre información?: ")
    var = input("¿Que quieres que muestre? (continent, contry_code, contry_id, name): ")
    print(json.dumps(datos.get("data").get(id).get(var),indent=4,sort_keys=True))
else:
    print("Error en la API")
    print(r.status_code)
