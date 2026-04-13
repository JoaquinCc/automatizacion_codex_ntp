import json
from datetime import datetime, timezone
from bson import ObjectId
from config import LIMA_TZ


def safe(val):
    """Convierte tipos no serializables a string."""
    if isinstance(val, ObjectId):
        return str(val)
    if isinstance(val, datetime):
        return val.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(val, (list, dict)):
        return json.dumps(val, default=str, ensure_ascii=False)
    return val


def to_lima_date(val):
    """Retorna la FECHA (datetime.date) en hora Peru."""
    if not isinstance(val, datetime):
        return None
    if val.tzinfo is None:
        val = val.replace(tzinfo=timezone.utc)
    return val.astimezone(LIMA_TZ).date()


def to_lima_time(val):
    """Retorna la HORA como string HH:MM:SS en hora Peru."""
    if not isinstance(val, datetime):
        return None
    if val.tzinfo is None:
        val = val.replace(tzinfo=timezone.utc)
    return val.astimezone(LIMA_TZ).strftime("%H:%M:%S")


def flatten_doc(doc: dict) -> dict:
    """Aplana un documento MongoDB al schema de columnas requerido."""
    marcador  = doc.get("marcador_info") or {}
    gestiones = doc.get("gestiones")     or []
    g         = gestiones[-1] if gestiones else {}

    hora_inicio_atencion = to_lima_time(doc.get("fecha_inicio_atencion"))

    return {
        "fecha_inicio_comunicacion" : to_lima_date(doc.get("fecha_inicio_comunicacion")),
        "hora_inicio_comunicacion"  : to_lima_time(doc.get("fecha_inicio_comunicacion")),
        "telefono"                  : safe(doc.get("identificacion")),
        "tipo_comunicacion_id"      : safe(doc.get("tipo_comunicacion_id")),
        "lote_id"                   : safe(doc.get("lote_id")),
        "tiempo_timbrado_marcador"  : safe(doc.get("tiempo_timbrado_marcador")),
        "tiempo_ring"               : safe(doc.get("tiempo_ring")),
        "tiempo_ring_agente"        : safe(doc.get("tiempo_ring_agente")),
        "tiempo_ring_acumulado"     : safe(doc.get("tiempo_ring_acumulado")),
        "tiempo_cola"               : safe(doc.get("tiempo_cola")),
        "tiempo_conversacion"       : safe(doc.get("tiempo_conversacion")),
        "tiempo_gestion"            : safe(doc.get("tiempo_gestion")),
        "tiempo_atencion"           : safe(doc.get("tiempo_atencion")),
        "fecha_inicio_atencion"     : to_lima_date(doc.get("fecha_inicio_atencion")),
        "hora_inicio_atencion"      : hora_inicio_atencion,
        "hora_inicio_conversacion"  : hora_inicio_atencion,
        "fecha_fin_atencion"        : to_lima_date(doc.get("fecha_fin_atencion")),
        "hora_fin_atencion"         : to_lima_time(doc.get("fecha_fin_atencion")),
        "resultado_id"              : safe(doc.get("resultado_id")),
        "resultado_marcador_nombre" : safe(doc.get("resultado_marcador_nombre")),
        "finalizada_por"            : safe(doc.get("finalizada_por")),
        "agente_id"                 : safe(doc.get("agente_id")),
        "base_nombre"               : safe(marcador.get("dato2")),
        "documento"                 : safe(marcador.get("dato1")),
        "departamento"              : safe(marcador.get("dato3")),
        "provincia"                 : safe(marcador.get("dato4")),
        "distrito"                  : safe(marcador.get("dato5")),
        "tipificacion_nivel_1"      : safe(g.get("nivel1_nombre")),
        "tipificacion_nivel_2"      : safe(g.get("nivel2_nombre")),
        "tipificacion_nivel_3"      : safe(g.get("nivel3_nombre")),
        "tipificacion_nivel_4"      : safe(g.get("nivel4_nombre")),
    }


def normalizar(docs: list) -> list:
    """Aplana todos los documentos."""
    return [flatten_doc(d) for d in docs]
