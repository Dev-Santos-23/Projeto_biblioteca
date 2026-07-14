import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

senha = os.getenv("DB_PASSWORD")

def conectar():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = senha,
            database = "loja_de_livros"
        )
        print("Conectado com Sucesso!")
        
        return conn
    
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        
def _close(conn):
    if conn:
        conn.close()
    print("Conexão encerrada!")
    
if __name__ == "__main__":
    conectar()               