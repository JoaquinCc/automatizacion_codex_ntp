from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

# ── Timezone ──────────────────────────────────────────────────────────────────
LIMA_TZ = ZoneInfo("America/Lima")

# ── MongoDB ───────────────────────────────────────────────────────────────────
MONGO_HOST       = "44.195.114.98"
MONGO_USER       = "bi_guest"
MONGO_PASSWORD   = "gu3$t202X#"
MONGO_DB         = "reportes"
MONGO_COLLECTION = "log_comunicaciones"
MONGO_URI        = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:27017/{MONGO_DB}"

COLA_ID = 43

# ── MariaDB ───────────────────────────────────────────────────────────────────
DB_HOST     = "intranetpbx.net.pe"
DB_PORT     = 33306
DB_USER     = "biuser"
DB_PASSWORD = "{b1us3r;3v0x}"
DB_NAME     = "db_ntp_win_outbound"
DB_TABLE    = "fact_comunicaciones"

# ── Rango de fecha: hoy en hora Peru (UTC-5) ──────────────────────────────────
def get_rango_hoy():
    """Retorna (inicio, fin) UTC para el dia de hoy en hora Peru."""
    ahora      = datetime.now(timezone.utc)
    hoy_inicio = ahora.replace(hour=5, minute=0, second=0, microsecond=0)
    hoy_fin    = hoy_inicio + timedelta(hours=23, minutes=59, seconds=59)
    if ahora < hoy_inicio:
        hoy_inicio -= timedelta(days=1)
        hoy_fin    -= timedelta(days=1)
    return hoy_inicio, hoy_fin


def get_rango_fecha(fecha_str: str):
    """Retorna (inicio, fin) UTC para una fecha especifica en formato YYYY-MM-DD.

    Ejemplo: get_rango_fecha('2026-04-08')
    """
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    inicio = datetime(fecha.year, fecha.month, fecha.day, 5, 0, 0, tzinfo=timezone.utc)
    fin    = inicio + timedelta(hours=23, minutes=59, seconds=59)
    return inicio, fin
