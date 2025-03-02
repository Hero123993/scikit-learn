import requests
from Untitled1 import coin

print(requests.__version__)

def send_line_notify(total_value, coin_10, coin_5, coin_1, token):
    message = (f"Total Value: {total_value}, "
               f"Coin 10 count: {coin_10}, "
               f"Coin 5 count: {coin_5}, "
               f"Coin 1 count: {coin_1}")

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification: {response.status_code}")