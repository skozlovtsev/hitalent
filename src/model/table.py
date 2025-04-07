from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .model import Base


class Table(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    seats: Mapped[int]
    location: Mapped[str]

    def __repr__(self) -> str:
        return f"Table(id={self.id!r}, name={self.name!r}, fullname={self.seats!r}, location={self.location!r})"