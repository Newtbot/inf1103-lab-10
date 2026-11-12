from src.modules.product import Product 
from src.modules.orderline import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []  

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        return self._order_lines

    def add_order_line(self, product: Product, quantity: int) -> None: 
        order_line = OrderLine(product, quantity)
        self._order_lines.append(order_line)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self._order_lines)

