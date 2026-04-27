from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List

app = FastAPI(title="Pousada Eventos - v3.0.0 (QA Edition)")

class Reserva(BaseModel):
    id: int
    cliente: str
    data: date
    espaco: str
    tipo_evento: str

db_eventos = []

@app.get("/")
def home():
    return {"status": "Sistema da Pousada Online"}

@app.get("/eventos", response_model=List[Reserva])
def listar_eventos():
    return db_eventos

@app.post("/eventos", status_code=201)
def criar_evento(reserva: Reserva):
    # Validação simples: não permitir ID duplicado
    for evento in db_eventos:
        if evento["id"] == reserva.id:
            raise HTTPException(status_code=400, detail="ID já existe")
            
    db_eventos.append(reserva.dict())
    return {"mensagem": "Evento agendado com sucesso!"}

@app.get("/eventos/{evento_id}")
def obter_evento(evento_id: int):
    for evento in db_eventos:
        if evento["id"] == evento_id:
            return evento
    raise HTTPException(status_code=404, detail="Evento não encontrado")