def validar_autor(autor):

    while True:

        if not autor:
            autor = input("Digite seu nome: ")
            continue

        if any(char.isdigit() for char in autor):
            autor = input("O nome não pode conter números. Digite novamente: ")
            continue

        if len(autor) <= 2:
            resposta = input(
                "Nome muito curto. Tem certeza? (sim/não): "
            )

            if resposta.lower() == "sim":
                break

            autor = input("Digite o nome novamente: ")
            continue

        break

        
        
    print("Cadastro concluido!")    
    return autor

import os
import requests
from dotenv import load_dotenv

from pprint import pprint as pp
load_dotenv()

api_key = os.getenv("DB_API_KAY")
table_paises = []

def buscar_pais(pais_autor):
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
            tanlr = pais["names"]["common"]
            table_paises.append(normalizar(tanlr)) 
        if not dados["meta"]["more"]:
            break
        
        offset += 100
    
   
   return validando_pais(pais_autor)
    

def validando_pais(pais):

    while True:

        if not pais:
            pais = input("Digite o país novamente: ")
            continue

        if any(char.isdigit() for char in pais):
            pais = input("O nome não pode conter números. Digite novamente: ")
            continue

        if len(pais) <= 2:
            resposta = input("Nome muito curto. Tem certeza? (sim/não): ")

            if resposta.lower() == "sim":
                break

            pais = input("Digite o país novamente: ")
            continue

        pais = normalizar(pais)

        if pais in table_paises:
            break

        pais = input("País não encontrado. Digite novamente: ")

    return pais   
    

def normalizar(texto):
    import unicodedata
    
    texto = texto.lower()

    return ''.join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )

                    
if __name__ == "__main__":
    
    autor = input("Digite seu nome: ")                            
    pais_autor = input("Digite o seu pais (Pais de Origem): ") 
    
    validar_autor(autor) 
    buscar_pais() 
    