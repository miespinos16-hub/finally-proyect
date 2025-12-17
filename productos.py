class Product:
    def __init__ (self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"{self.id} - {self.name} |${self.price} | Stock: {self.stock}"
    
    def show_products(products):
        print("\n--Product List--")
        for p in products:
            print(p)