# 🧩 CV Engine Pro

> **Sistema de Inteligência Artificial para Análise, Scoring e Otimização de Currículos.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![AI](https://img.shields.io/badge/AI-LangChain%20%7C%20Gemini-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)

O **CV Engine Pro** é uma ferramenta de **Engenharia de Prompt e RAG (Retrieval-Augmented Generation)** que atua como um "Mentor de Carreira com IA". Ele lê arquivos PDF, extrai informações semânticas, calcula um score de mercado e, através de agentes inteligentes, reescreve o conteúdo para aumentar o impacto do candidato em processos seletivos.

---

## 🚀 Funcionalidades Principais

* **📊 Análise Profunda (Scoring):** Avalia o perfil com critérios de Headhunter (Experiência Real, Stack Técnica, Impacto).
* **🔎 Gap Analysis:** Compara o currículo linha a linha com uma **Vaga Real**, gerando um *match* percentual e identificando lacunas técnicas.
* **✨ Otimizador de Texto (AI Writer):** Reescreve resumos e experiências utilizando o método **STAR** (Situação, Tarefa, Ação, Resultado) e verbos de ação.
* **🕵️ Reality Check:** Um auditor automático que verifica se a IA não "alucinou" ou exagerou na reescrita, garantindo integridade e evitando datas futuras incorretas.
* **⚡ Processamento Híbrido:** Embeddings rodando localmente (CPU) para privacidade e velocidade, com raciocínio complexo na nuvem (Gemini).

---

## 🛠️ Arquitetura Técnica

O projeto segue uma arquitetura modular baseada em microserviços internos:

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Frontend** | `Streamlit` | Interface reativa, gestão de estado (Session State) e Cache. |
| **Orquestração** | `LangChain` | Cadeias de raciocínio (Chains), conexão com modelos e parsers. |
| **LLM (Cérebro)** | `Gemini 1.5 Flash` | Geração de texto, raciocínio lógico e análise crítica. |
| **Embeddings** | `HuggingFace (Local)` | `sentence-transformers/all-MiniLM-L6-v2` para vetorização semântica. |
| **Vector DB** | `FAISS` | Busca de alta performance por similaridade (In-Memory). |
| **Validação** | `Pydantic` | Tipagem forte e garantia de esquema JSON na saída da IA. |

---

## 📦 Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente.

### 1. Pré-requisitos
* Python 3.10 ou superior instalado.
* Uma chave de API do Google AI Studio (Gemini).

### 2. Clonar e Instalar Dependências

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/cv-engine-pro.git
cd cv-engine-pro

# Crie um ambiente virtual (Recomendado)
python -m venv .venv

# Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate

# Instale as bibliotecas
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave:

```env
GOOGLE_API_KEY="Sua_Chave_Aqui_AIzaSy..."
MODEL_NAME="gemini-1.5-flash"
```

### 4. Executar a Aplicação
```bash
streamlit run src/ui/dashboard.py
```
O navegador abrirá automaticamente no endereço `http://localhost:8501`.

---

## 📂 Estrutura do Projeto

```text
cv-engine-pro/
├── src/
│   ├── config.py           # Gerenciamento de chaves e variáveis
│   ├── models.py           # Schemas de dados (Pydantic)
│   ├── services/
│   │   ├── ai_engine.py    # Cérebro: LangChain + Gemini + FAISS
│   │   └── pdf_handler.py  # Leitura e processamento de arquivos
│   └── ui/
│       └── dashboard.py    # Interface Streamlit
├── .env                    # Chaves (Não comitar!)
├── main.py
├── .gitignore              # Arquivos ignorados pelo Git
├── requirements.txt        # Lista de dependências
└── README.md               # Documentação
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

**Desenvolvido por Victor Ryuichi.**
