from twilio.rest import Client

client = Client('AC45c3830dde541d0ff1529933c8d22f98', 'a16173ec6ef7f8c4ab19ea5ca4d3ff96')

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919873602153'

client.messages.create(body='Hellope',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
