# config.py

# =====================================================
# CONFIGURAÇÕES DO ROBÔ DE ATUALIZAÇÃO POWER BI
# =====================================================


# Caminho do executável do Power BI Desktop
POWERBI_PATH = r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe"


# Arquivos PBIX que serão atualizados
DASHBOARDS = [
    r"C:\Users\lucas.costa\Desktop\ADM24H - GOV.pbix",
    r"C:\Users\lucas.costa\Desktop\ADM24h - Detalhamento.pbix",
    r"C:\Users\lucas.costa\Desktop\ADM24H Cidadão V3.pbix"
]


# =====================================================
# TEMPOS DE EXECUÇÃO
# =====================================================

# Tempo para o Power BI abrir e carregar o arquivo
TEMPO_ABERTURA = 60


# Tempo máximo aguardando atualização
TEMPO_REFRESH = 300


# Intervalo entre verificações
INTERVALO_VERIFICACAO = 10


# Número máximo de tentativas caso ocorra erro
TENTATIVAS_MAX = 5


# =====================================================
# PASTAS DO PROJETO
# =====================================================

PASTA_LOGS = "logs"

PASTA_SCREENSHOTS = "screenshots"
