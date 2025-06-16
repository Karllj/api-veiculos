from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos em /static (não em /)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

def conectar():
    conn = sqlite3.connect("veiculos.db")
    conn.row_factory = sqlite3.Row
    return conn

class Veiculo(BaseModel):
    modelo: str
    marca: str
    ano: int

class VeiculoDB(Veiculo):
    id: int

@app.on_event("startup")
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT,
            marca TEXT,
            ano INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.get("/veiculos", response_model=List[VeiculoDB])
def listar_veiculos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculos")
    veiculos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return veiculos

@app.post("/veiculos")
def adicionar_veiculo(veiculo: Veiculo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO veiculos (modelo, marca, ano) VALUES (?, ?, ?)",
        (veiculo.modelo, veiculo.marca, veiculo.ano)
    )
    conn.commit()
    conn.close()
    return {"mensagem": "Veículo adicionado com sucesso"}

@app.delete("/veiculos/{veiculo_id}")
def excluir_veiculo(veiculo_id: int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM veiculos WHERE id = ?", (veiculo_id,))
    conn.commit()
    conn.close()
    return {"mensagem": "Veículo excluído com sucesso"}

from fastapi import HTTPException

@app.put("/veiculos/{veiculo_id}")
def atualizar_veiculo(veiculo_id: int, veiculo: Veiculo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculos WHERE id = ?", (veiculo_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    cursor.execute(
        "UPDATE veiculos SET modelo = ?, marca = ?, ano = ? WHERE id = ?",
        (veiculo.modelo, veiculo.marca, veiculo.ano, veiculo_id)
    )
    conn.commit()
    conn.close()
    return {"mensagem": "Veículo atualizado com sucesso"}
