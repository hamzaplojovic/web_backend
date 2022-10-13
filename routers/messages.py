from fastapi import APIRouter,status
from schemas import message
from repo import messages

router = APIRouter(
    prefix="/notify",
    tags=["Notifications"]
)

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def send_sms(request:message.Message):
    return messages.send_message(request)