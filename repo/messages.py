from schemas import message
from utils.send_sms import twillio_send


def send_message(message: message.Message) -> int:
    notify = twillio_send(message.contacts, message.context)
    return notify
