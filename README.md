# Check om årsopgørelsen er klar hos Skat
## _For research purposes only!_

check_skat.py is a simple script that login to tastselv.skat.dk/borger and check for a predefined text is present at årsopgørelsen. If the text is not present, a SMS message will be sent through Twilio rest API to inform a predefined list of recipients.
Script is written for python3.

## Features

- Logs in to tastselv.skat.dk/borger and checks for a predefined text string.
- Sends a SMS to a predefinded list of recipients when text is not found.
- Uses a timer to randomize logins.
- Breaks the script when SMS are sent.

## Configuration

To configure the script, edit check_skat.py
```sh
Script setup:
cpr = "your_cpr_id"
password = "your_password"
checktxt = "2020 er tidligst klar i marts"
message = "Aarsopgoerelse er klar!"
notify = ['+4511111111', '+4522222222']

Twilio stuff:
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
messaging_service_sid='your_twilio_messaging_sid'
```

## Requirements
Setup your environment (or virtual environment)
```sh
python3 -m pip install -r requirements.txt
```
For SMS integration to work you will need to have an account at twilio.com with a attached phone number set up for SMS service.
If not needed SMS integration can be removed from the script before running it.
