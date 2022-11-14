import os
from twilio.rest import Client

account_sid = os.environ['AC8ce5d0f9b9f6c771979323a81a3f66fb']
auth_token = os.environ['6f3528ebbd747c9a2c292a7aebe29cb5']
client = Client(account_sid, auth_token)

message = client.messages.create(
  body='Hi there',
  from_='+15097785509',
  to='+12365917334'
)

print(message.sid)