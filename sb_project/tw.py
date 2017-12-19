from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC819e285399a13897370bcc8f7f160ffa"
# Your Auth Token from twilio.com/console
auth_token  = "c516d4d8c58b54da9422271521fa2a81"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+263774199931", 
    from_="+13345642095",
    body="Hello from Python!")

print(message.sid)


