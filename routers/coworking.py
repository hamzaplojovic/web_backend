from repo import coworking
from fastapi import APIRouter, status, BackgroundTasks
from schemas.coworking import Table, Floor, UserInTable

router = APIRouter(prefix="/coworking", tags=["Coworking"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all():
    return coworking.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_floor(request: Floor, background_tasks: BackgroundTasks):
    background_tasks.add_task(coworking.create_floor, request)
    return request


@router.get("/{floor_number}", status_code=status.HTTP_200_OK)
async def get_all_from_floor(floor_number: int):
    return coworking.get_floor_by_number(floor_number)


@router.post("/{floor_number}/create_table",
             status_code=status.HTTP_201_CREATED)
async def create_table(floor_number, request: Table):
    return coworking.create_table(floor_number, request)


@router.get("/{floor_number}/{table_number}", status_code=status.HTTP_200_OK)
async def get_table(floor_number: int, table_number: int):
    return coworking.get_table(floor_number, table_number)


@router.put("/{floor_number}/{table_number}",
            status_code=status.HTTP_202_ACCEPTED)
async def update_table(floor_number: int, request: Table):
    return coworking.update_table(floor_number, request)


@router.delete("/{floor_number}/{table_number}",
               status_code=status.HTTP_202_ACCEPTED)
async def delete_table(floor_number: int, table_number: int):
    return coworking.delete_table(floor_number, table_number)


@router.get("/{floor_number}/{table_number}/people",
            status_code=status.HTTP_200_OK)
async def get_people_in_table(floor_number: int, table_number: int):
    return coworking.get_people_in_table(floor_number, table_number)


@router.post("/{floor_number}/{table_number}/{username}",
             status_code=status.HTTP_201_CREATED)
async def add_person_to_table(request: UserInTable, action: str):
    return coworking.add_person_to_table(dict(request), action)


@router.delete("/{floor_number}/{table_number}/{username}",
               status_code=status.HTTP_202_ACCEPTED)
async def remove_person_from_table(request: UserInTable, action: str):
    return coworking.remove_person_from_table(dict(request), action)
