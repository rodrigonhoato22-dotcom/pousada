from fastapi import FastAPI
app = FastAPI(title="Pousada Eventos")
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