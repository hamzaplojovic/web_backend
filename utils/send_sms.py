import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_ACCOUNT_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]

def twillio_send(contacts, context) -> 200:
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_ACCOUNT_TOKEN )

    for x in contacts:
        _ = client.messages.create(
                body=context,
                from_=TWILIO_PHONE_NUMBER,
                to=x
            )
    return 200