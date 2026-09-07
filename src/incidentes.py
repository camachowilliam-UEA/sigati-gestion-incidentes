"""
Módulo de Lógica de Negocio: Validación y Registro de Incidentes de TI (SIGA-TI)
Universidad Estatal Amazónica - Ingeniería de Software
"""
from datetime import datetime

PRIORIDADES_VALIDAS = {"Baja", "Media", "Alta", "Critica"}

def validar_incidente(id_activo: str, descripcion: str, prioridad: str, solicitante: str) -> dict:
    """
    Valida las reglas de negocio para la apertura de un ticket de soporte técnico (RF-004):
    - El identificador del activo debe cumplir con el formato institucional (ej: ACT-XXXX o SRV-XXXX).
    - La descripción del fallo técnico debe ser exhaustiva (mínimo 10 caracteres).
    - La prioridad debe pertenecer a los rangos operativos autorizados.
    - El solicitante debe estar identificado.
    """
    if not id_activo or not isinstance(id_activo, str):
        return {"valido": False, "mensaje": "El código del activo es obligatorio."}
    
    id_activo_limpio = id_activo.strip().upper()
    if not (id_activo_limpio.startswith("ACT-") or id_activo_limpio.startswith("SRV-")):
        return {"valido": False, "mensaje": "Formato de activo no reconocido por el inventario municipal."}

    if not descripcion or len(descripcion.strip()) < 10:
        return {"valido": False, "mensaje": "La descripción técnica del incidente es insuficiente (mínimo 10 caracteres)."}

    if prioridad not in PRIORIDADES_VALIDAS:
        return {"valido": False, "mensaje": f"Prioridad inválida. Opciones admitidas: {', '.join(PRIORIDADES_VALIDAS)}."}

    if not solicitante or len(solicitante.strip()) < 3:
        return {"valido": False, "mensaje": "El nombre del funcionario solicitante no es válido."}

    return {
        "valido": True,
        "mensaje": "Ticket de soporte validado y listo para persistencia en base de datos.",
        "codigo_ticket": f"TCK-{datetime.now().strftime('%Y%m%d')}-{id_activo_limpio}",
        "estado": "Abierto"
    }