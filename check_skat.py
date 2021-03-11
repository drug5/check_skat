#!/usr/bin/python3
# -*- coding: utf-8 -*-
from twill.commands import *
import twill
from random import randint
import time
from twilio.rest import Client

udbetal = 'Du skal have penge'
betal = 'Du mangler at betale'
cpr = 'your_cpr'
password = 'your_password'
notify = ['+4511111111', '+4522222222', '+4533333333']
message = 'Aarsopgoerelse er klar!'
counter = 0

while True:
  go('https://www.tastselv.skat.dk/TSADG_BORGER/loginpin.do')
  fv('1', 'pnr', cpr)
  fv('1', 'tastselvKode', password)
  formaction('mainForm', 'https://www.tastselv.skat.dk/TSADG_BORGER/loginpin.do')
  submit()
  go('https://www.tastselv.skat.dk/borger/seaaropg2020/VisListe.do')
  content = show()

  if not betal or not udbetal in content:
    counter = counter + 1
    print('Ikke klar endnu - Try number '+str(counter))
    sleep(randint(650, 850))
  else:
    print('Den er klar! Sender SMS')
    for sendsms in notify:
      account_sid = 'your_account_sid'
      auth_token = 'your_auth_token'
      client = Client(account_sid, auth_token)
      message = client.messages.create(
        messaging_service_sid='your_service_sid',
        body=message,
        to=sendsms
      )
    break
