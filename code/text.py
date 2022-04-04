from twilio.rest import Client
account_sid = os.environ['AC53316d8a3ff6a2505e4938e4633a238a']
auth_token = os.environ['27dfd13e4b38b07470431d57798292f1']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="What should we do to RJ",
                     from_='+17579727923',
                     to='+18122232748'
                 )

print(message.sid)
