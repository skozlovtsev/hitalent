from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from meta import metadata_obj

    
reservations = Table(
    "reservations",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("table_id", Integer, ForeignKey("tables"), nullable=False),
    Column("reservation_time", DateTime),
    Column("duration_minutes", Integer),
)