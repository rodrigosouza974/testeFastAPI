import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

class Inputs(BaseModel):
    inp:int
    inp2:str

@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}

@app.post("/exemplo2")
def exemplo_2(inputs: Inputs) -> str:
    return f"Você digitou {inputs.inp} e {inputs.inp2}"

if __name__ == "__main__":
    uvicorn.run(app, port=8000)