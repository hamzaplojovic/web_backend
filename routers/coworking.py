from repo import coworking
from fastapi import APIRouter, status

router = APIRouter(prefix="/coworking", tags=["Coworking"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all():
    return coworking.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_floor(floor_number: int):
    return coworking.create_table(floor_number)


@router.post("/{floor_number}", status_code=status.HTTP_201_CREATED)
async def create_table(floor_number: int, table_number: int):
    return coworking.create_table(floor_number, table_number)


@router.get("/{floor_number}", status_code=status.HTTP_200_OK)
async def get_all_from_floor(floor_number: int):
    return coworking.get_all_from_floor(floor_number)
