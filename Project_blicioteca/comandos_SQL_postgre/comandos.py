from take_conection import conectar, _close

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
        
def injetando_editoras_no_banco(inject):
    
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