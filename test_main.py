from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Teste 1: Verificar se a Home está online
def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Sistema da Pousada Online"}

# Teste 2: Verificar se a lista de eventos começa vazia
def test_list_empty_events():
    response = client.get("/eventos")
    assert response.status_code == 200
    assert response.json() == []

# Teste 3: Criar um evento com sucesso
def test_create_event():
    payload = {
        "id": 1,
        "cliente": "Rodrigo QA",
        "data": "2026-12-25",
        "espaco": "Salão Principal",
        "tipo_evento": "Confraternização"
    }
    response = client.post("/eventos", json=payload)
    assert response.status_code == 201
    assert response.json()["mensagem"] == "Evento agendado com sucesso!"

# Teste 4: Tentar buscar um evento que não existe (Erro 404)
def test_get_nonexistent_event():
    response = client.get("/eventos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Evento não encontrado"

# Teste 5: Tentar criar evento com ID duplicado (Erro 400)
def test_create_duplicate_event():
    payload = {
        "id": 1,
        "cliente": "Rodrigo Replicado",
        "data": "2026-12-25",
        "espaco": "Jardim",
        "tipo_evento": "Casamento"
    }
    # O ID 1 já foi criado no Teste 3
    response = client.post("/eventos", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "ID já existe"#