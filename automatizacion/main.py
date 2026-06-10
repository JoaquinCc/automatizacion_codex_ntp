from config import get_rango_hoy, PIPELINES
from extractor import extraer_documentos
from normalizer import normalizar
from transformer import transformar
from loader import cargar


def main():
    hoy_inicio, hoy_fin = get_rango_hoy()
    # hoy_inicio es UTC 05:00 = medianoche Lima, su fecha coincide con la fecha Lima
    fecha_hoy = hoy_inicio.strftime("%Y-%m-%d")

    for pipeline in PIPELINES:
        cola_id = pipeline["cola_id"]
        db_name = pipeline["db_name"]

        print("=" * 50)
        print(f"Pipeline NTP WIN Outbound | cola_id={cola_id} | db={db_name}")
        print("=" * 50)
        print(f"Fecha: {fecha_hoy} (hora Peru)")
        print(f"Rango UTC  : {hoy_inicio}  ->  {hoy_fin}")

        docs = extraer_documentos(hoy_inicio, hoy_fin, cola_id)
        if not docs:
            print("Sin documentos para procesar.")
            continue

        rows = normalizar(docs)
        df = transformar(rows)
        print(f"DataFrame listo: {df.shape[0]} filas x {df.shape[1]} columnas")

        cargar(df, fecha_hoy, db_name)

        print(f"Pipeline cola_id={cola_id} finalizado correctamente")

    print("=" * 50)
    print("Todos los pipelines finalizados")
    print("=" * 50)


if __name__ == "__main__":
    main()
