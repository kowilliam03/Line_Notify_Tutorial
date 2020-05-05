import requests


def send_line_notify_message(token, message):
    header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {
        "message": message
    }

    r = requests.post(" https://notify-api.line.me/api/notify",
                      headers=header, params=params)

    return r.status_code
