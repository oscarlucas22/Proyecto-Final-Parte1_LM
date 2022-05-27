import requests
import os 
import json

url_base = "https://app.sportdataapi.com/api/v1/"
key = os.environ["apikey"]
id = input("Dime un id de un pais (4-131): ")

payload = {'apikey':key,"country_id":id}

url = url_base + "soccer/" + "leagues"
r = requests.get(url,params = payload)
if r.status_code == 200:
    datos=r.json()
    print(json.dumps(datos,indent=4,sort_keys=True))
    respuesta = input("¿Quieres ver una vista simplificada? (S/N): ")
    if respuesta == "S":
        ip = input("¿Que id quieres que muestre información?: ")
        var = input("¿Que quieres que muestre?: ")
        print(json.dumps(datos.get("data").get(ip).get(var),indent=4,sort_keys=True))
    else:
        print("OK")
else:
    print("Error en la API")
    print(r.status_code)