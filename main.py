from fastapi import FastAPI
app = FastAPI(title="Pousada Eventos - v2.0.0 (CI/CD)")
from pydantic import BaseModel
from datetime import date

class Reserva(BaseModel):
    cliente: str
    data: date
    espaco: str
    tipo_evento: str

db_eventos = []
@app.get("/eventos")
def listar_eventos():
    return db_eventos
@app.post("/eventos")
def criar_evento(reserva: Reserva):
    db_eventos.append(reserva.dict())
    return {"mensagem": "Evento agendado com sucesso! "}