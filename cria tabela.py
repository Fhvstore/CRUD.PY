import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aqwaqwaqw",
  database="crud"
)
mycursor = mydb.cursor()

mycursor.execute("""
  CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  nome VARCHAR(255) NOT NULL,
  descricao TEXT NOT NULL,
  caracteristicas TEXT NOT NULL,
  indicacao_uso TEXT NOT NULL,
  dados_tecnicos TEXT NOT NULL,
  foto INT NOT NULL,
  ficha_tecnica TEXT NOT NULL,
  manual_instrucoes TEXT NOT NULL,
  preco INT NOT NULL,
  tipo_loja INT NOT NULL
  )
""") 
mydb.commit()


