from twilio.rest import Client
from time import sleep
from datetime import date, datetime, timedelta
import json, urllib.request

try:
    from auth import account_sid, auth_token, twilio_num, your_number
except ImportError:
    raise IOError("Create a `auth.py` file with fields according to the README instructions.")

def send_message(message):
    # Sends the user a specified message
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=twilio_num, to=your_number)

def main():
    check_class()
    print("Found new section! Check API")

def check_class():
    base_url = "https://api.umd.io/v0/courses/engl393"
    initial = 48

    while True:
        with urllib.request.urlopen(base_url) as url:
            data = json.loads(url.read().decode())
            if len(data["sections"]) > 48:
                send_message("New section opened for ENGL393!")
                return
            else:
                print(f"Nothing @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" \
                       " for ENGL393. Checking in 5 minutes...")
                sleep(300)
                

if __name__ == "__main__":
    main()