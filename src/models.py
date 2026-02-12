from pydantic import BaseModel, Field
from typing import List


class PerfilCandidato(BaseModel):
    # (Mantenha igual ao anterior)
    nome: str = Field(description="Nome completo")
    cargo_atual: str = Field(description="Cargo mais recente")
    tempo_experiencia: str = Field(description="Tempo calculado de experiência em Dados/Tech")
    skills_tecnicas: List[str] = Field(description="Lista de hard skills")
    score_geral: int = Field(description="Nota de 0 a 100")
    justificativa_score: str = Field(description="Por que essa nota foi dada?")
    pontos_fortes: List[str]
    pontos_atencao: List[str]
    perguntas_entrevista: List[str]


class AnaliseGap(BaseModel):
    # (Mantenha igual ao anterior)
    match_percentual: int
    analise_comparativa: str
    pontos_fortes: List[str]
    gaps_tecnicos: List[str]
    perguntas_tira_teima: List[str]


class CVOtimizado(BaseModel):
    resumo_profissional_novo: str = Field(description="Versão reescrita do resumo, focado em impacto e senioridade.")

    bullets_experiencia_star: List[str] = Field(description="""
        5 bullet points de experiência reescritos usando o método STAR.
        Devem incluir placeholders numéricos (ex: 'melhorando a performance em [X]%') onde faltarem dados.
    """)

    melhorias_realizadas: List[str] = Field(description="Lista curta explicando o que foi melhorado no texto.")

    # --- NOVO CAMPO: O Reality Check ---
    reality_check: List[str] = Field(description="""
        Lista de 3 a 5 alertas críticos de veracidade. 
        Exemplo: "Eu assumi que você liderou o projeto X, se você foi apenas participante, mude para 'Colaborei com...'".
        Exemplo: "O termo 'Sênior' no resumo pode ser arriscado para seu tempo de XP, esteja pronto para defender."
    """)