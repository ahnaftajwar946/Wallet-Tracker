# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC0d8e2d42fd74c6a0b7a06a5e359a05ec'
auth_token = '092aee8fab8b98cae336cfe8f291c9b7'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Welcome to Wallet Tracker",
                     from_='+13604958615',
                     to='+16822986185'
                 )

print(message.sid)
