from service.notify import send_line_notify_message
from service.stock import get_stock_price

stock_id = 3008
stock_price = get_stock_price(stock_id)

with open("../token.txt", "r") as f:
    token = f.read()

message = f"大立光(3008)  {stock_price}"
status = send_line_notify_message(token, message)
print(status)
