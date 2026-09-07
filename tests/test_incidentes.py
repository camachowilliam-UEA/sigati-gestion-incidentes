"""
Batería de Pruebas Automatizadas para el Módulo de Incidentes (SIGA-TI)
Framework: pytest
"""
import pytest
from src.incidentes import validar_incidente

def test_cp01_registro_incidente_exitoso():
    """CP-01 (Unitaria): Valida el registro correcto de un ticket con datos válidos."""
    resultado = validar_incidente(
        id_activo="ACT-1042",
        descripcion="Falla en la fuente de poder de la estación de trabajo",
        prioridad="Media",
        solicitante="Ing. Carlos Gomez"
    )
    assert resultado["valido"] is True
    assert resultado["estado"] == "Abierto"
    assert "TCK-" in resultado["codigo_ticket"]

def test_cp02_rechazo_codigo_activo_invalido():
    """CP-02 (Unitaria - Caso Crítico): Rechazo ante activos sin prefijo municipal autorizado."""
    resultado = validar_incidente(
        id_activo="LAPTOP-PISO2",
        descripcion="Pantalla parpadea intermitentemente al encender",
        prioridad="Baja",
        solicitante="Lic. Martha Rios"
    )
    assert resultado["valido"] is False
    assert "Formato de activo no reconocido" in resultado["mensaje"]

def test_cp03_rechazo_descripcion_insuficiente():
    """CP-03 (Unitaria): Rechazo de reportes con descripciones ambiguas o menores a 10 caracteres."""
    resultado = validar_incidente(
        id_activo="SRV-001",
        descripcion="No sirve",
        prioridad="Critica",
        solicitante="Admin TI"
    )
    assert resultado["valido"] is False
    assert "insuficiente" in resultado["mensaje"]

def test_cp04_rechazo_prioridad_no_autorizada():
    """CP-04 (Unitaria): Rechazo de niveles de severidad fuera del catálogo institucional."""
    resultado = validar_incidente(
        id_activo="ACT-5001",
        descripcion="El puerto Ethernet del switch no sincroniza enlace",
        prioridad="SuperUrgente",
        solicitante="William Camacho"
    )
    assert resultado["valido"] is False
    assert "Prioridad inválida" in resultado["mensaje"]