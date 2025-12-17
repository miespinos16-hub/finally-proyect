import json, os, re

class usuario:
    def __init__(self):
        self.datos = []
        
    def __str__(self):
        return f"email: {self.email}, passware: {self.passware}"
    
    def data (self):
        while True:
            self.email = input("add email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                break
            else:
                print("email is invalid")
        self.passware = input("add passware: ")
        
    def login(self, datos):
        email = input("email: ")
        passware = input("passware: ")

        for u in datos:
            if u["email"] == email and u["passware"] == passware:
                print("Login exitoso")
                return True
        print("The user is not registered")
        return False

        
    
user = usuario()
user.data()

if os.path.exists("datos.json"):
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
else:
    datos = []
    
existe = any(u["email"] == user.email for u in datos)

if existe:
    print("existing user.")
else:
    datos.append({"email": user.email, "passware": user.passware})
    print(f"User added successfully")

with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2, ensure_ascii=False)
