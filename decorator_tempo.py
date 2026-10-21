import time
import logging
from functools import wraps

# logger que grava em arquivo (execucao.log) e também mostra na tela
logger = logging.getLogger("tempo_execucao")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    arquivo_log = logging.FileHandler("execucao.log", encoding="utf-8")
    arquivo_log.setFormatter(formato)
    logger.addHandler(arquivo_log)

    console = logging.StreamHandler()
    console.setFormatter(formato)
    logger.addHandler(console)

def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função e grava no log."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        duracao = time.perf_counter() - inicio
        logger.info(f"Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper
