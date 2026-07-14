
import os
import requests
from dotenv import load_dotenv

from pprint import pprint as pp
load_dotenv()

api_key = os.getenv("DB_API_KAY")
table_paises = []

def buscar_pais():
  offset = 0
 
  while True:
      response = requests.get(
          f"https://api.restcountries.com/countries/v5?limit=100&offset={offset}&response_fields=names.common",
          headers={
              "Authorization": f"Bearer {api_key}"
          }
      )

      dados = response.json()["data"]

      for pais in dados["objects"]:
          #print(pais["names"]["common"])
          table_paises.append(pais["names"]["common"]) 
      if not dados["meta"]["more"]:
          break

      offset += 100
     
buscar_pais()     
pp(table_paises)
