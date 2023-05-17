import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aqwaqwaqw",
  database="crud"
)

mycursor = mydb.cursor()

#CRIAR CADASTRO #CRIAR CADASTRO #CRIAR CADASTRO#CRIAR CADASTRO#CRIAR CADASTRO #CRIAR CADASTRO

def create_cadastro(id, nome, email, telefone, endereco, tipo_loja, logo, descricao):
    cursor = mydb.cursor()
    sql = "INSERT INTO cadastro (id, nome, email, telefone, endereco, tipo_loja, logo, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, nome, email, telefone, endereco, tipo_loja, logo, descricao)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "cadastro adicionado")

#create_cadastro("1","Jq23", "joao.silva@gmail.com", "1199999999", "Rua da Paz, 123", 1, "logo.jpg", "Descrição da loja")

#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --

def delete_cadastro(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM cadastro WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "cadastro deletado")

#delete_cadastro(1)

# Atualizar   # Atualizar#  Atualizar # Atualizar # Atualizar # Atualizar 

def atualizar_cadastro(id, nome, email, telefone, endereco, tipo_loja, logo, descricao):
    cursor = mydb.cursor()
    sql = "UPDATE cadastro SET nome = %s, email = %s, telefone = %s, endereco = %s, tipo_loja = %s, logo = %s, descricao = %s WHERE id = %s"
    val = (nome, email, telefone, endereco, tipo_loja, logo, descricao, id)
    cursor.execute(sql, val)
    mydb.commit()
    
    print(cursor.rowcount, "cadastro atualizado")
    
#atualizar_cadastro("2","Jq2322122333", "j@gmail.com", "1199999999", "Rua da Paz, 123", 1, "logo.jpg", "Descri234ção da loja")

# Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler 

def ler_cadastro(id):
    mycursor = mydb.cursor()
    sql = "SELECT nome, email, telefone, endereco, tipo_loja, logo, descricao, id FROM cadastro WHERE id=%s"
    val = (id,)
    mycursor.execute(sql, val)
    resultado = mycursor.fetchone()

    if resultado is None:
        print("Não há cadastro com esse ID.")
    else:
        print(resultado)

#ler_cadastro(2)

