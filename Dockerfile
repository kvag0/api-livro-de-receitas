# 1. Usar uma imagem oficial e leve do Python como base.
FROM python:3.9-slim

# 2. Definir o diretório de trabalho dentro do contêiner.
WORKDIR /app

# 3. Copiar o ficheiro de dependências primeiro para otimizar o cache.
COPY requirements.txt ./

# 4. Instalar as dependências usando pip.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o resto do código da nossa aplicação.
COPY . .

# 6. Expor a porta 5000, que é a que a nossa aplicação usa.
EXPOSE 5000

# 7. O comando para iniciar a nossa aplicação quando o contêiner arrancar.
CMD ["python3", "app.py"]