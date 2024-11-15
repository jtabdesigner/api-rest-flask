import os
import datetime

class Config:
    # Configuração do banco de dados para ambiente local e variáveis de ambiente para produção
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mydatabase.db")  # SQLite como padrão local
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Chave secreta para JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")  # Use variável de ambiente para produção

    # Tempo de expiração do token JWT para autenticação avançada
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)  # Tokens expiram em 1 hora

    # Configurações de cache
    CACHE_TYPE = 'simple'  # Tipo de cache simples para desenvolvimento local
    CACHE_DEFAULT_TIMEOUT = 300  # Tempo de expiração do cache em segundos (5 minutos)
