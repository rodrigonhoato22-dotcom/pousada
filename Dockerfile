# Usa uma imagem leve do Python
FROM python:3.10-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# Comando para rodar a API (mesmo que você usou no terminal)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]