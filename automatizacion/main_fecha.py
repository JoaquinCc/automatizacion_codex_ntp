from config import get_rango_fecha, PIPELINES
from extractor import extraer_documentos
from normalizer import normalizar
from transformer import transformar
from loader import cargar

# ── COLOCA AQUI LA FECHA ESPECIFICA EN FORMATO YYYY-MM-DD ────────────────────
FECHA = "2026-06-09"
# ─────────────────────────────────────────────────────────────────────────────


def main():
    inicio, fin = get_rango_fecha(FECHA)

    for pipeline in PIPELINES:
        cola_id = pipeline["cola_id"]
        db_name = pipeline["db_name"]

        print("=" * 50)
        print(f"Pipeline NTP | cola_id={cola_id} | db={db_name}")
        print("=" * 50)
        print(f"Fecha especifica: {FECHA}")
        print(f"Rango UTC  : {inicio}  ->  {fin}")

        docs = extraer_documentos(inicio, fin, cola_id)
        if not docs:
            print("Sin documentos para procesar.")
            continue

        rows = normalizar(docs)
        df = transformar(rows)
        print(f"DataFrame listo: {df.shape[0]} filas x {df.shape[1]} columnas")

        cargar(df, FECHA, db_name)

        print(f"Pipeline cola_id={cola_id} finalizado correctamente")

    print("=" * 50)
    print("Todos los pipelines finalizados")
    print("=" * 50)


if __name__ == "__main__":
    main()
