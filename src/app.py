from typing import Annotated

from fastapi import Depends, FastAPI

from .router.router import reservations_router, tables_router

app = FastAPI()

app.include_router(reservations_router, prefix='/reservations/')
app.include_router(tables_router, prefix='/tables/')


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


if __name__ == "__main__":
    app.host