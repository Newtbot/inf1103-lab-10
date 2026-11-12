from src.modules.supplier import Supplier
from src.modules.physicalProduct import PhysicalProduct
from src.modules.digitalProduct import DigitalProduct
from src.modules.order import Order
from src.modules.inventory import Inventory, show_product_details


def main() -> None:
    print("--- 1. Testing Supplier & Products ---")
    sup = Supplier("SUP-01", "TechDistro Inc.", "orders@techdistro.com")
    
    keyboard = PhysicalProduct("P01", "Mechanical Keyboard", 100.0, 50, 1.2, sup)
    ebook = DigitalProduct("P02", "Python Guide PDF", 25.0, 999, 15.0, sup)
    
    keyboard.display_information()
    ebook.display_information()

    print("\n--- 2. Testing Order & OrderLine Composition ---")
    order1 = Order("ORD-001")
    order1.add_order_line(keyboard, 2)  # 2 keyboards @ $100 = $200
    order1.add_order_line(ebook, 3)     # 3 ebooks @ $25 = $75

    for line in order1.order_lines:
        print(f"Item: {line.product.name} | Qty: {line.quantity} | Subtotal: ${line.calculate_subtotal():.2f}")

    print("\n--- 3. Testing Exercise 4.3 (Same Product in 2 Orders) ---")
    order2 = Order("ORD-002")
    order2.add_order_line(keyboard, 5)

    line_order1 = order1.order_lines[0]
    line_order2 = order2.order_lines[0]

    # Verify OrderLines are 2 distinct objects (Composition)
    print("Are the two OrderLine objects distinct?", line_order1 is not line_order2)

    # Verify they share the exact same Product in memory (Association)
    print("Do both OrderLines reference the same Product object?", line_order1.product is line_order2.product)

    print("\n--- 4. Testing show_product_details (Polymorphism) ---")
    print("[Physical Product Details]:")
    show_product_details(keyboard)

    print("\n[Digital Product Details]:")
    show_product_details(ebook)

    print("\n--- 5. Testing Inventory Product Collection (Polymorphism & LSP) ---")
    inventory = Inventory()
    inventory.add_product(keyboard)
    inventory.add_product(ebook)

    # Single loop through the product collection, no isinstance checks
    for product in inventory.products:
        product.display_information()
        print(product.get_fulfillment_info())


if __name__ == "__main__":
    main()
