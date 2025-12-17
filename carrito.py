class Cart:
    def __init__(self):
        self.items = {} # {product_id:{"product": obj, "qty": cantidad}}
        
    def add_to_cart(self, product, qty):
        if product.stock < qty:
            print("Not enough stock available.")
            return
        
        if product.id in self.items:
            self.items[product.id]["qty"] += qty
        else:
            self.items[product.id] = {"product": product, "qty": qty}
            
        product.stock -= qty
        print (f"{qty} unit(s) of {product.name} added to cart.")
        
    def view_cart(self):
        print("\n-- Shopping cart --")
        if not self.items:
            print("Cart is empty.")
            return
        
        total = 0
        for item in self.items.values():
            p = item["product"]
            q = item["qty"]
            subtotal = p.price * q
            total += subtotal
            print(f"{p.name} x{q} = ${subtotal}")
            
        print(f"Total: ${total}")
        
    def clear_cart(self):
        self.items.clear()
        print("Cart has emptied.")