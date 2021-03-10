#!/usr/bin/python3
# -*- coding: utf-8 -*-
from twill.commands import *
import twill
from io import StringIO
from twilio.rest import Client
from random import randint
import time

cpr = "dit_cprnr"
password = "dit_password"
checktxt = "2020 er tidligst klar i marts"
message = "Aarsopgoerelse er klar!"
notify = ['+4511111111', '+4522222222']

while True:
  sio = StringIO()
  twill.set_output(sio)
  go('https://www.tastselv.skat.dk//borger/loginpin')
  fv("1", "pnr", cpr)
  fv("1", "tastselvKode", password)
  formaction('mainForm', 'https://www.tastselv.skat.dk/TSADG_BORGER/loginpin.do')
  submit()
  go('https://www.tastselv.skat.dk/borger/seaaropg2020/VisListe.do')
  content = show()

  if not checktxt in content:
    for sendsms in notify:
      account_sid = 'dit_account_sid'
      auth_token = 'dit_auth_token'
      client = Client(account_sid, auth_token)
      message = client.messages.create(
        messaging_service_sid='din_messaging_sid',
        body=message,
        to=sendsms
      )
    break
  else:
    sleep(randint(600,800))
