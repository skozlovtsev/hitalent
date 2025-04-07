from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .model import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str]
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id"))
    reservation_time: Mapped[DateTime]
    duration_minutes: Mapped[int]

    def __repr__(self) -> str:
        return f"Reservation(id={self.id!r}, customer_name={self.customer_name!r},\
             table_id={self.table_id!r}, reservation_time={self.reservation_time!r}, duration_minutes={self.duration_minutes!r})"