from src.modules.product import Product 
from src.modules.orderline import OrderLine


class Order():
    def __init__(self, order_id: str, order_lines: str   ):
        self._order_id = order_id
        self._order_lines: list[OrderLine] = []  


#The Order should create and manage its own OrderLine objects. Do not create an OrderLine elsewhere and
#pass it into the Order. Instead, provide an add_order_line() method that accepts a Product and quantity, creates
#the OrderLine internally, and adds it to the order.

    def add_order_line(self, product: Product, quantity: int) -> None: 
        order_line = OrderLine(product, quantity)
        self.order_line.append(order_line)

