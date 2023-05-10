from sqlalchemy import Table, Column, Integer, String, TIMESTAMP
from sqlalchemy import MetaData

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quanity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=False),
    Column("date", TIMESTAMP),
    Column("type", String),
)