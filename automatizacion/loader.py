import datetime
import urllib.parse

import pandas as pd
from sqlalchemy import create_engine, text

from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_TABLE


def cargar(df: pd.DataFrame, fecha: str, db_name: str) -> int:
    """Elimina registros existentes para la fecha dada e inserta el DataFrame en MariaDB."""
    pwd_encoded = urllib.parse.quote_plus(DB_PASSWORD)
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{pwd_encoded}@{DB_HOST}:{DB_PORT}/{db_name}",
        connect_args={"charset": "utf8mb4"}
    )

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Conexion MariaDB exitosa")
    except Exception as e:
        print(f"Error de conexion MariaDB: {e}")
        raise

    # Eliminar registros existentes para la fecha antes de insertar
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(f"DELETE FROM {DB_TABLE} WHERE fecha_inicio_comunicacion = :fecha"),
                {"fecha": fecha}
            )
            conn.commit()
            eliminados = result.rowcount
            if eliminados > 0:
                print(f"Eliminados {eliminados} registros existentes para la fecha {fecha}")
            else:
                print(f"Sin registros previos para la fecha {fecha}, se procedera a insertar")
    except Exception as e:
        print(f"Error al eliminar registros previos: {e}")
        raise

    df_insert = df.copy()

    # Convertir Int64 nullable a int64 estandar (pymysql no acepta pd.NA)
    for col in df_insert.select_dtypes(include=["Int64", "Int32"]).columns:
        df_insert[col] = df_insert[col].astype("float64").fillna(0).astype("int64")

    # Convertir datetime.date a string YYYY-MM-DD
    for col in df_insert.columns:
        if df_insert[col].apply(lambda x: isinstance(x, datetime.date)).any():
            df_insert[col] = df_insert[col].apply(
                lambda x: x.strftime("%Y-%m-%d") if isinstance(x, datetime.date) else None
            )

    # Reemplazar NaN/None por None (NULL en MySQL)
    df_insert = df_insert.where(pd.notnull(df_insert), None)

    try:
        df_insert.to_sql(
            name      = DB_TABLE,
            con       = engine,
            if_exists = "append",
            index     = False,
            chunksize = 500,
            method    = "multi",
        )
        print(f"Insercion exitosa: {len(df_insert)} filas insertadas en {db_name}.{DB_TABLE}")
        return len(df_insert)
    except Exception as e:
        print(f"Error al insertar: {e}")
        raise
    finally:
        engine.dispose()
