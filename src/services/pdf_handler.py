import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import Config


def processar_pdf(uploaded_file):
    """Salva temporariamente, lê e fatia o PDF."""
    try:
        # 1. Salvar arquivo temporário (Windows friendly)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # 2. Carregar
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()

        # 3. Limpeza
        try:
            os.remove(tmp_path)
        except:
            pass  # Ignora erro de permissão no Windows se ocorrer

        # 4. Fatiamento (Chunking)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        return splitter.split_documents(docs)

    except Exception as e:
        print(f"Erro no PDF Handler: {e}")
        return None