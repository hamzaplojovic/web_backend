from repo import courses
from schemas import course
from repo.role_checker import RoleChecker
from fastapi import APIRouter, status, Depends

allowed_roles = RoleChecker(["admin", "instructor"])

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
    dependencies=[Depends(allowed_roles)]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_courses() -> list:
    return courses.get_all()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_course(request: course.Course) -> course.Course:
    return courses.create_course(request)

@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_course_by_name(name) -> course.Course or 404:
    return courses.get_by_name(name)

@router.put("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def change_course(request: course.Course) -> course.Course:
    return courses.change_course(request)

@router.delete("/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(name):
    return courses.delete_course(name)

@router.post("/assign", status_code=status.HTTP_202_ACCEPTED)
async def assign_user_to_course(course_name, username):
    return courses.assign_to_course(course_name, username)

@router.get("/{name}/students", status_code=status.HTTP_200_OK)
async def get_students_from_course(name:str):
    return courses.get_students_from_course(name)