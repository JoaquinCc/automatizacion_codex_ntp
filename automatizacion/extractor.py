from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION, COLA_ID


PROYECCION = {
    "fecha_inicio_comunicacion" : 1,
    "identificacion"            : 1,
    "tipo_comunicacion_id"      : 1,
    "marcador_info.dato1"       : 1,
    "marcador_info.dato2"       : 1,
    "marcador_info.dato3"       : 1,
    "marcador_info.dato4"       : 1,
    "marcador_info.dato5"       : 1,
    "marcador_info.lote_nombre" : 1,
    "marcador_info.lote_id"     : 1,
    "lote_nombre"               : 1,
    "lote_id"                   : 1,
    "tiempo_timbrado_marcador"  : 1,
    "tiempo_ring"               : 1,
    "tiempo_ring_agente"        : 1,
    "tiempo_ring_acumulado"     : 1,
    "tiempo_cola"               : 1,
    "tiempo_conversacion"       : 1,
    "tiempo_gestion"            : 1,
    "tiempo_atencion"           : 1,
    "fecha_inicio_atencion"     : 1,
    "fecha_fin_atencion"        : 1,
    "resultado_id"              : 1,
    "resultado_marcador_nombre" : 1,
    "finalizada_por"            : 1,
    "agente_id"                 : 1,
    "gestiones"                 : 1,
}


def extraer_documentos(hoy_inicio, hoy_fin):
    """Conecta a MongoDB y extrae documentos de cola_id=43 para el rango de fecha."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=8000)

    try:
        client.admin.command("ping")
        print("Conexion MongoDB exitosa")
    except Exception as e:
        print(f"Error de conexion MongoDB: {e}")
        raise

    col = client[MONGO_DB][MONGO_COLLECTION]

    filtro = {
        "cola_id": COLA_ID,
        "fecha_inicio_comunicacion": {"$gte": hoy_inicio, "$lte": hoy_fin}
    }

    docs = list(col.find(filtro, PROYECCION))
    client.close()
    print(f"Documentos extraidos: {len(docs)}")
    return docs
