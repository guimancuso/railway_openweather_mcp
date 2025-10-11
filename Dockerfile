# Usar imagem oficial do Python
FROM python:3.11-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY pyproject.toml uv.lock ./

# Instalar dependências usando uv
RUN uv sync --frozen --no-dev

# Copiar o código da aplicação
COPY . .

# Expor a porta (Railway define via variável PORT)
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uv", "run", "weather_mcp_server_http.py"]
