import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Rotas para cadastro de usuários
@app.get("/criar_cadastro")
async def criar_cadastro():
    return {"message": "Cadastro criado com sucesso"}

@app.delete("/deletar_cadastro/{user_id}")
async def deletar_cadastro(user_id: int):
    return {"message": "Cadastro deletado com sucesso"}

@app.put("/atualizar_cadastro/{user_id}")
async def atualizar_cadastro(user_id: int):
    return {"message": "Cadastro atualizado com sucesso"}

@app.get("/ler_cadastro/{user_id}")
async def ler_cadastro(user_id: int):
    return {"message": "Cadastro lido com sucesso"}



# Rotas para produtos
@app.get("/cadastrar_produto")
async def cadastrar_produto():
    return {"message": "Produto cadastrado com sucesso"}

@app.delete("/deletar_produto/{product_id}")
async def deletar_produto(product_id: int):
    return {"message": "Produto deletado com sucesso"}

@app.put("/atualizar_produto/{product_id}")
async def atualizar_produto(product_id: int):
    return {"message": "Produto atualizado com sucesso"}

@app.get("/listar_produtos")
async def listar_produtos():
    return {"message": "Produtos listados com sucesso"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
