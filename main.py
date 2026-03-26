from pydantic import BaseModel
from datetime import date

class Reserva(BaseModel):
    cliente: str
    data: date
    espaco: str
    tipo_evento: str

db_eventos = []