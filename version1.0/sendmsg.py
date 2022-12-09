#send envirnoment variables before use
import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID'] # replace with your Account SID
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN'] # replace with your Auth Token
TWILIO_PHONE_SENDER = "+15097785509" # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "+12365917334" # replace with your phone number

def send_text_alert(message):
    """Sends an SMS text alert."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=TWILIO_PHONE_RECIPIENT,
        from_=TWILIO_PHONE_SENDER,
        body=message)
    print(message.sid)

send_text_alert('mary is absent')