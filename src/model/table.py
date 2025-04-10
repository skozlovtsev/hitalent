from sqlalchemy import Table, Column, Integer, String
from meta import metadata_obj

    
tables = Table(
    "tables",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("seats", Integer),
    Column("location", String)
)