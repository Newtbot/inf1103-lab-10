#only handle product obj?
# - __product_id:String
# - __name:String
# - __price:float
# - __stock:int
# + update_stock(quantity : int):void
# + display_information():voidclass Product: 

#__ = private 
# + = public 
# # = protected


# wat methods we need??
# store products
# add product
# searches product??
# display products?

#inventory class
# - self.product:List
# +
from src.modules.product import Product                                                                                                                                                                                                                                                                 

class Inventory:
    def __init__(self):
        self.products: list[Product] = []  

    def add_product(self, product: Product) -> None:
        if (isinstance(product, Product)):
            self.products.append(product)
        else: 
            print("invalid data")

    def remove_product(self, product_id) -> None: 
        product = self.search_product(product_id)
        if product: 
            self.products.remove(product)

    def search_product(self, product_id: str) -> Product | None: 
        for prod in self.products: 
            if prod.product_id == product_id:
                return prod
        return None

    def display_products(self) -> None:
        for prod in self.products:
            prod.display_information()

    def show_product_details(self, product: Product) -> None: 
        product.display_information()
        print(product.get_fulfillment_info())


def show_product_details(product: Product) -> None: 
    product.display_information()
    print(product.get_fulfillment_info())
