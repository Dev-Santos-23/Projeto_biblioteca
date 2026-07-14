from take_conection import conectar, _close
from Project_blicioteca.tests_and_validations.back_of_create_autores import buscar_pais, validar_autor

def injetando_autores_no_banco(inject):
    
    try:
        conection = conectar()
        cursor = conection.cursor()
        
        cmd_select = "INSERT INTO autores (nome, pais) VALUES (%s, %s)"
        values = inject
        cursor.execute(cmd_select, values)
        conection.commit()
        _close(conection)
    
    except Exception as e:
        print(f"Não foi possivel fazer a conexão: {e}")
        
def cadastro_autor():
    
    autor = input("Digite seu nome: ")
    pais_autor = input("Digite o seu pais (NA ESCRITA AMERICANA): ")
    
    autor = validar_autor(autor)
    pais_autor = buscar_pais(pais_autor)
    
    inject_values = autor, pais_autor
    injetando_autores_no_banco(inject_values)

if __name__ == "__main__":
    
    cadastro_autor()

    
                                