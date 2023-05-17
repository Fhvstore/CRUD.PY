import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aqwaqwaqw",
  database="crud"
)
mycursor = mydb.cursor()


####################################### CRUD DOS PARCEIROS ####################################
####################################### CRUD DOS PARCEIROS ####################################


def criar_cadastro(id, nome, email, telefone, endereco, tipo_loja, logo, descricao):
    cursor = mydb.cursor()
    sql = "INSERT INTO cadastro (id, nome, email, telefone, endereco, tipo_loja, logo, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, nome, email, telefone, endereco, tipo_loja, logo, descricao)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "cadastro adicionado")

#criar_cadastro("66","Jq23", "joao.silva@gmail.com", "1199999999", "Rua da Paz, 123", 1, "logo.jpg", "Descrição da loja")

#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --

def deletar_cadastro(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM cadastro WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "cadastro deletado")

#deletar_cadastro(1)

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


####################################### CRUD DOS PRODUTOS ####################################
####################################### CRUD DOS PRODUTOS ####################################

#CRIAR CADASTRO #CRIAR CADASTRO #CRIAR CADASTRO#CRIAR CADASTRO#CRIAR CADASTRO #CRIAR CADASTRO
async def cadastrar_produto(id, nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja):
    cursor = mydb.cursor()
    sql = "INSERT INTO produtos (id, nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "Produto inserido:")

#cadastrar_produto("77", "Produto c", "Descrição do produto A", "Características do produto A", "Indicaçãewe", "Dados técnicos do produto A", 1, "ficha_tecnica_a.pdf", "manual_instrucoes_a.pdf", 1050, 1)


#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --#DELETE -- #DELETE --

def deletar_produto(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM produtos WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Produto deletado")

#deletar_produto(1)

# Atualizar   # Atualizar#  Atualizar # Atualizar # Atualizar # Atualizar 

def atualizar_produto(id, nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja):
    cursor = mydb.cursor()
    sql = "UPDATE produtos SET nome=%s, descricao=%s, caracteristicas=%s, indicacao_uso=%s, dados_tecnicos=%s, foto=%s, ficha_tecnica=%s, manual_instrucoes=%s, preco=%s, tipo_loja=%s WHERE id=%s"
    val = (nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja, id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "Produto atualizado.")

#atualizar_produto(145553, "1212", "Nova descrição do Produto A", "Novas características do Produto A", "Nova indicação de uso do Produto A", "Novos dados técnicos do Produto A", 12, "nova_ficha_tecnica_a.pdf", "novo_manual_instrucoes_a.pdf", 150.50, 1)

# Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler # Ler 

def listar_produto(id):
    mycursor = mydb.cursor()
    sql = "SELECT nome, descricao, caracteristicas, indicacao_uso, dados_tecnicos, foto, ficha_tecnica, manual_instrucoes, preco, tipo_loja id FROM produtos WHERE id=%s"
    val = (id,)
    mycursor.execute(sql, val)
    resultado = mycursor.fetchone()

    if resultado is None:
        print("Não há Produto cadastrado com esse ID.")
    else:
        print(resultado)

listar_produto(3)

