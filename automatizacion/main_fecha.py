from config import get_rango_fecha
from extractor import extraer_documentos
from normalizer import normalizar
from transformer import transformar
from loader import cargar

# ── COLOCA AQUI LA FECHA ESPECIFICA EN FORMATO YYYY-MM-DD ────────────────────
FECHA = "2026-04-10"
# ─────────────────────────────────────────────────────────────────────────────


def main():
    print("=" * 50)
    print("Inicio del pipeline NTP WIN Outbound")
    print("=" * 50)

    # 1. Rango de fecha especifica
    inicio, fin = get_rango_fecha(FECHA)
    print(f"Fecha especifica: {FECHA}")
    print(f"Rango UTC  : {inicio}  ->  {fin}")

    # 2. Extraccion MongoDB
    docs = extraer_documentos(inicio, fin)
    if not docs:
        print("Sin documentos para procesar. Fin.")
        return

    # 3. Normalizacion (flatten)
    rows = normalizar(docs)

    # 4. Transformacion (columnas calculadas, tipos)
    df = transformar(rows)
    print(f"DataFrame listo: {df.shape[0]} filas x {df.shape[1]} columnas")

    # 5. Carga en MariaDB
    cargar(df)

    print("=" * 50)
    print("Pipeline finalizado correctamente")
    print("=" * 50)


if __name__ == "__main__":
    main()
