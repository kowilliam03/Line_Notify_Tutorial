import requests

def send_line_notify_message(token, message):
    header = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "message": message
    }

    r = requests.post(" https://notify-api.line.me/api/notify",
                      headers=header, params=payload)

    return r.status_code


# 讀取Token
with open("token.txt", "r") as f:
    token = f.read()

message = "Hello~~"

status = send_line_notify_message(token, message)

resp_status = {
    200: "Success",
    400: "Bad request",
    401: "Invalid access token"
}

if status in resp_status:
    print(resp_status[status])
else:
    print("其他錯誤")
