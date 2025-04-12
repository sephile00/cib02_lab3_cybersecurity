import pytest
from src.analizador import Analizador

def test_analizar_trafico_sospechoso():
    analizador = Analizador(umbral_intentos=3)
    # Simulamos más de 3 intentos fallidos
    trafico = {
        'ip': '192.168.0.10',
        'intentos_fallidos': 5
    }
    es_sospechoso = analizador.analizar(trafico)
    assert es_sospechoso is True, "Debería detectar tráfico sospechoso"

def test_analizar_trafico_normal():
    analizador = Analizador(umbral_intentos=3)
    # Solo 2 intentos fallidos => No es sospechoso
    trafico = {
        'ip': '192.168.0.20',
        'intentos_fallidos': 2
    }
    es_sospechoso = analizador.analizar(trafico)
    assert es_sospechoso is False, "No debería marcar como sospechoso"
