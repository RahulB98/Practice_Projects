import os
from twilio.rest import Client

client = Client()
print(os.environ['MY_PHONE_NUMBER'])
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

client.messages.create(body='Hellope',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)