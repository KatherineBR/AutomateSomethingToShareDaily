import os
from twilio.rest import Client
import time
import random

import schedule

y = 0

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

haiku = ["Hydrogen, H \nYour single proton \nfundamental, essential. \nWater. Life. Star fuel.", "Sodium, Na \nRacing to trigger \nevery kiss, every kind act; \nbehind every thought.", "Carbon, C \nShow-stealing diva,\nthrow yourself at anyone, \ndecked out in diamonds.", "Yttrium, Y \nThat is not a name. \nThat is a spelling error. \nOr a Scrabble bluff.", "Potassium, K\nLeftmost seat, fourth row, \nyearning for the halogens \non the other side.", "Oganesson, Og \nThe end of the line, \nyour millisecond half-life \nbrings down the curtain.", "Ununennium, Uue \nWill the curtain rise? \nWill you open the eighth act? \nClaim the center stage?"]

def sendsms():
  print("function entered")
  message = client.messages \
    .create(
          body=random.choice(haiku) + "\n \nalso puff!",
          from_='+14158493465',
          to=os.environ['TEST_PHONE_NUMBER']
      )
  print(message.sid)
  

while y < 10:
  schedule.every().day.at("15:00").do(sendsms)
  #schedule.every().minute.do(sendsms)
  print("scheduled")
  y+=1

while True:
  schedule.run_pending()
  time.sleep(1)
