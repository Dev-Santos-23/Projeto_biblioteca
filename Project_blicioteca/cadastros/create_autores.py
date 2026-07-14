"""  Como rodar o projeto no seu vscode:
 
    Primiero rode no terminal:
    cd "C:\Users\Lucas\Desktop\Nova pasta (2)\Project_blicioteca"
    
    Depois rode:
    python -m casdastro.create_autores
    
"""

from comandos_SQL_postgre import comandos
from tests_and_validations.back_of_create_autores import buscar_pais, validar_autor

        
def cadastro_autor():
    
    autor = input("Digite seu nome: ")
    pais_autor = input("Digite o seu pais (NA ESCRITA AMERICANA): ")
    
    autor = validar_autor(autor)
    pais_autor = buscar_pais(pais_autor)
    
    inject_values = autor, pais_autor
    comandos.injetando_autores_no_banco(inject_values)

if __name__ == "__main__":
    
    cadastro_autor()

    
                                