from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'AC8ce5d0f9b9f6c771979323a81a3f66fb' # replace with your Account SID
TWILIO_AUTH_TOKEN = '6f3528ebbd747c9a2c292a7aebe29cb5' # replace with your Auth Token
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

send_text_alert('adam is absent')