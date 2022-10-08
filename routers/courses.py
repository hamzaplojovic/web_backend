from fastapi import APIRouter,status
from repo import courses
from schemas import course

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses.get_all()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_course(request: course.Course):
    return courses.create_course(request)

@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_course_by_name(name):
    return courses.get_by_name(name)

@router.put("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def change_course(request: course.Course):
    return courses.change_course(request)

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(name):
    return courses.delete_course(name)