from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.config import Config
from src.models import PerfilCandidato, AnaliseGap, CVOtimizado  # <--- Importe o novo modelo
from datetime import datetime


class AIEngine:
    def __init__(self):
        # Motor Local (HuggingFace) para evitar erros de API
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # Cérebro (Gemini)
        self.llm = ChatGoogleGenerativeAI(
            model=Config.MODEL_NAME,
            temperature=0.2,  # Criatividade leve para reescrever bem
            google_api_key=Config.GOOGLE_API_KEY
        )

    def analisar_documentos(self, splits, texto_vaga=None):
        vector_store = FAISS.from_documents(splits, self.embeddings)
        retriever = vector_store.as_retriever(search_kwargs={"k": 7})

        query = "experiência projetos impacto ferramentas datas"
        if texto_vaga:
            query += f" {texto_vaga[:300]}"

        docs = retriever.invoke(query)
        contexto = "\n\n".join([d.page_content for d in docs])

        if texto_vaga:
            return self._executar_gap_analysis(contexto, texto_vaga)
        else:
            return self._executar_extracao_perfil(contexto)

    # --- NOVA FUNÇÃO QUE ESTAVA FALTANDO ---
    def otimizar_cv(self, splits, vaga=None):
        # 1. Recupera o Contexto
        vector_store = FAISS.from_documents(splits, self.embeddings)
        docs = vector_store.as_retriever(search_kwargs={"k": 10}).invoke("experiência profissional projetos resumo")
        contexto = "\n\n".join([d.page_content for d in docs])

        # 2. Define a Data Dinâmica (Isso faltava!)
        data_hoje = datetime.now().strftime("%d de %B de %Y")

        parser = JsonOutputParser(pydantic_object=CVOtimizado)

        # 3. Prompt com Consciência Temporal
        prompt_template = """
        Você é um Especialista em Carreira e "Ghostwriter" Sênior.

        CONTEXTO TEMPORAL (CRÍTICO):
        Hoje é dia: {data_hoje}
        Use esta data para validar se as experiências são atuais, passadas ou futuras.

        FASE 1: A OTIMIZAÇÃO (Copywriting)
        Reescreva o perfil para torná-lo de ALTO IMPACTO.
        - Use método STAR e verbos de ação.
        - Invente placeholders numéricos ([X]%) onde faltar métrica.

        FASE 2: O REALITY CHECK (Auditoria)
        Analise o texto gerado vs. Original.
        - Identifique exageros de senioridade.
        - DATAS: Compare rigorosamente com a data de hoje ({data_hoje}).
          - Se a data do CV for ANTERIOR a hoje, NÃO marque como erro de "data futura".
          - Se a data do CV for POSTERIOR a hoje (Futuro): Alerte APENAS se não houver indicação de "Início Confirmado".

        CONTEXTO ORIGINAL:
        {contexto}

        VAGA ALVO:
        {vaga}

        FORMATO JSON:
        {format_instructions}
        """

        prompt = ChatPromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm | parser

        # 4. Injeta a data na execução
        return chain.invoke({
            "contexto": contexto,
            "vaga": vaga if vaga else "Genérica de Dados",
            "data_hoje": data_hoje,  # <--- A correção está aqui
            "format_instructions": parser.get_format_instructions()
        })

    def _executar_extracao_perfil(self, contexto):
        parser = JsonOutputParser(pydantic_object=PerfilCandidato)
        data_hoje = datetime.now().strftime("%B de %Y")
        prompt = ChatPromptTemplate.from_template(
            """Você é um CTO e Headhunter rigoroso. Analise o CV abaixo.
            DATA DE HOJE: {data_hoje}
            1. CÁLCULO DE EXPERIÊNCIA: Some apenas períodos em tecnologia. Resultado: "X anos e Y meses".
            2. SCORING (0-100): Penalize falta de métricas e clichês.
            3. PERGUNTAS: Gere 3 perguntas técnicas.
            CV: {contexto}
            JSON: {format_instructions}"""
        )
        chain = prompt | self.llm | parser
        return chain.invoke(
            {"contexto": contexto, "data_hoje": data_hoje, "format_instructions": parser.get_format_instructions()})

    def _executar_gap_analysis(self, contexto, vaga):
        parser = JsonOutputParser(pydantic_object=AnaliseGap)
        prompt = ChatPromptTemplate.from_template(
            """Compare CV vs Vaga. Seja binário nos skills. Gere perguntas Tira-Teima.
            VAGA: {vaga}
            CV: {contexto}
            JSON: {format_instructions}"""
        )
        chain = prompt | self.llm | parser
        return chain.invoke(
            {"contexto": contexto, "vaga": vaga, "format_instructions": parser.get_format_instructions()})