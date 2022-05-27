import requests
import os 
import json

url_base = "https://app.sportdataapi.com/api/v1/"
key = os.environ["apikey"]
id = input("Dime un id de una liga (314-346): ")

payload = {'apikey':key,"league_id":id}

url = url_base + "soccer/" + "seasons"
r = requests.get(url,params = payload)
if r.status_code == 200:
    datos=r.json()
    print(json.dumps(datos,indent=4,sort_keys=True))
    respuesta = input("¿Quieres ver una vista simplificada? (S/N): ")
    if respuesta == "S":
        var = input("¿Que quieres que muestre?: ")
        for a in datos.get("data"):
            print(json.dumps(a.get(var),indent=4,sort_keys=True))
    else:
        print("Ok")
else:
    print("Error en la API")
    print(r.status_code)
