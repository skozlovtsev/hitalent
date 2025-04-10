from typing import Annotated

from fastapi import Depends, FastAPI

from .router.router import reservations_router, tables_router

app = FastAPI()

app.include_router(reservations_router, prefix='/reservations/')
app.include_router(tables_router, prefix='/tables/')


if __name__ == "__main__":
    app.host()