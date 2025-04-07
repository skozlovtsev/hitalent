from fastapi import Depends, FastAPI


tables_router = FastAPI(root_path="/tables/")


@tables_router.get("/")
async def get_tablse():
    pass


@tables_router.post("/")
async def create_table():
    pass


@tables_router.delete("/{id}")
async def delete_table():
    pass


reservations_router = FastAPI(root_path="/reservations/")


@reservations_router.get("/")
async def get_reservations():
    pass


@reservations_router.post("/")
async def create_reservation():
    pass


@reservations_router.delete("/{id}")
async def delete_reservation():
    pass