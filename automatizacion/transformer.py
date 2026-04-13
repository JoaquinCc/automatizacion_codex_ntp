import pandas as pd
from datetime import timedelta

COLUMNAS = [
    "fecha_inicio_comunicacion",
    "hora_inicio_comunicacion",
    "tramo_inicio",
    "telefono",
    "tipo_comunicacion_id",
    "base_nombre",
    "lote_id",
    "tiempo_timbrado_marcador",
    "tiempo_ring",
    "tiempo_ring_agente",
    "tiempo_ring_acumulado",
    "tiempo_cola",
    "tiempo_conversacion",
    "tiempo_gestion",
    "tiempo_atencion",
    "tiempo_espera",
    "fecha_inicio_atencion",
    "hora_inicio_atencion",
    "hora_inicio_conversacion",
    "hora_fin_conversacion",
    "fecha_fin_atencion",
    "hora_fin_atencion",
    "resultado_id",
    "resultado_marcador_nombre",
    "finalizada_por",
    "documento",
    "departamento",
    "provincia",
    "distrito",
    "agente_id",
    "tipificacion_nivel_1",
    "tipificacion_nivel_2",
    "tipificacion_nivel_3",
    "tipificacion_nivel_4",
]


def sumar_segundos(hora_str, segundos):
    """Suma segundos a un string HH:MM:SS y retorna el resultado como HH:MM:SS."""
    if pd.isna(hora_str) or pd.isna(segundos):
        return None
    try:
        h, m, s   = map(int, str(hora_str).split(":"))
        base      = timedelta(hours=h, minutes=m, seconds=s)
        resultado = base + timedelta(seconds=int(segundos))
        total_s   = int(resultado.total_seconds())
        return f"{total_s // 3600:02d}:{(total_s % 3600) // 60:02d}:{total_s % 60:02d}"
    except Exception:
        return None


def calc_hora_fin_atencion(r):
    if r["resultado_id"] == 3:
        segundos = (r["tiempo_conversacion"] or 0) + (r["tiempo_gestion"] or 0)
    else:
        segundos = r["tiempo_gestion"] or 0
    return sumar_segundos(r["hora_inicio_atencion"], segundos)


def calc_tramo(hora_str):
    if pd.isna(hora_str) or hora_str is None:
        return None
    try:
        h, m, _ = map(int, str(hora_str).split(":"))
        tramo_m = 0 if m < 30 else 30
        return f"{h:02d}:{tramo_m:02d}"
    except Exception:
        return None


def transformar(rows: list) -> pd.DataFrame:
    """Construye el DataFrame final con todas las columnas calculadas."""
    if rows:
        df = pd.DataFrame(rows)
    else:
        df = pd.DataFrame(columns=COLUMNAS)

    # ── Convertir campos numericos
    df["tipo_comunicacion_id"]    = pd.to_numeric(df["tipo_comunicacion_id"],    errors="coerce")
    df["tiempo_cola"]              = pd.to_numeric(df["tiempo_cola"],              errors="coerce")
    df["tiempo_ring_acumulado"]    = pd.to_numeric(df["tiempo_ring_acumulado"],    errors="coerce")
    df["tiempo_conversacion"]      = pd.to_numeric(df["tiempo_conversacion"],      errors="coerce")
    df["tiempo_gestion"]           = pd.to_numeric(df["tiempo_gestion"],           errors="coerce")
    df["resultado_id"]             = pd.to_numeric(df["resultado_id"],             errors="coerce")
    df["tiempo_timbrado_marcador"] = pd.to_numeric(df["tiempo_timbrado_marcador"], errors="coerce")

    # ── tiempo_espera
    df["tiempo_espera"] = df.apply(
        lambda r: r["tiempo_cola"]
                  if r["tipo_comunicacion_id"] == 2
                  else r["tiempo_cola"] - r["tiempo_ring_acumulado"],
        axis=1
    )

    # ── hora_fin_conversacion
    df["hora_fin_conversacion"] = df.apply(
        lambda r: sumar_segundos(r["hora_inicio_comunicacion"], r["tiempo_conversacion"]),
        axis=1
    )

    # ── hora_fin_atencion
    df["hora_fin_atencion"] = df.apply(calc_hora_fin_atencion, axis=1)

    # ── Forzar int64 con fillna(0): tiempo_timbrado_marcador, tiempo_ring_acumulado, tiempo_espera
    ref_dtype = df["tiempo_conversacion"].dtype
    for col in ["tiempo_timbrado_marcador", "tiempo_ring_acumulado", "tiempo_espera"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(ref_dtype)

    # ── tramo_inicio (tramos de 30 min)
    df["tramo_inicio"] = df["hora_inicio_comunicacion"].apply(calc_tramo)

    # Garantizar todas las columnas y orden correcto
    for c in COLUMNAS:
        if c not in df.columns:
            df[c] = None

    return df[COLUMNAS]
