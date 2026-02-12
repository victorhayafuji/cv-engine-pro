import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-flash-latest"  # Ou gemini-pro
    EMBEDDING_MODEL = "models/embedding-001"
    CHUNK_SIZE = 2000
    CHUNK_OVERLAP = 100

    @staticmethod
    def validar():
        if not Config.GOOGLE_API_KEY:
            raise ValueError("A chave GOOGLE_API_KEY não foi encontrada no .env")