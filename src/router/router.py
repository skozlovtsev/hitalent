from fastapi import Depends, FastAPI
from datetime import datetime
from sqlalchemy import insert, select, delete
from pydantic import BaseModel
from ..connector.connection import connection
from ..model.reservation import reservations
from ..model.table import tables


tables_router = FastAPI(root_path="/tables/")


class TableDTO(BaseModel):
    id: int
    name: str
    seats: int
    location: str


@tables_router.get("/")
async def get_tablse():
    pass


@tables_router.post("/")
async def create_table(t: TableDTO):
    stmt = insert(tables).values(name=t.name, seats=t.seats, location=t.location)
    connection.exec(stmt)


@tables_router.delete("/{id}")
async def delete_table(id: int):
    pass


reservations_router = FastAPI(root_path="/reservations/")


class ReservationsDTO(BaseModel):
    id: int
    name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


@reservations_router.get("/")
async def get_reservations():
    pass


@reservations_router.post("/")
async def create_reservation(r: ReservationsDTO):
    stmt = insert(reservations).values(name=r.name, 
                                       table_id=r.table_id, 
                                       reservation_time=r.reservation_time, 
                                       duration_minutes=r.duration_minutes
                                       )
    connection.exec(stmt)


@reservations_router.delete("/{id}")
async def delete_reservation(id: int):
    pass