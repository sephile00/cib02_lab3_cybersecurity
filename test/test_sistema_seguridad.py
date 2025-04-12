import pytest
from src.sistema_seguridad import SistemaSeguridad

def test_bloquear_ip():
    sistema = SistemaSeguridad()
    ip_sospechosa = "192.168.0.10"
    sistema.bloquear_ip(ip_sospechosa)
    assert ip_sospechosa in sistema.ips_bloqueadas

def test_desbloquear_ip():
    sistema = SistemaSeguridad()
    ip_sospechosa = "192.168.0.10"
    sistema.bloquear_ip(ip_sospechosa)
    sistema.desbloquear_ip(ip_sospechosa)
    assert ip_sospechosa not in sistema.ips_bloqueadas

def test_bloquear_ip_repetida():
    sistema = SistemaSeguridad()
    ip_sospechosa = "192.168.0.10"
    sistema.bloquear_ip(ip_sospechosa)
    sistema.bloquear_ip(ip_sospechosa)  # se intenta bloquear 2 veces
    assert len(sistema.ips_bloqueadas) == 1, "Solo debería estar registrada 1 vez"
