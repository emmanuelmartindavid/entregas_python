class Client:
    def __init__(self, name, lastname, email, adress, phone_number):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.adress = adress
        self.phone_number = phone_number
        self.shopping_list = []

    def add_product(self, product):
        self.shopping_list.append(product)

    def delete_product(self, product):
        self.shopping_list.remove(product)

    def confirm_sale(self):
        return print(f"Se envio un correo electronico de confirmacion de compra a "
                     f"{self.email} con sus productos{self.shopping_list}")

    def clean_shopping_list(self):
        self.shopping_list = []

    def show_shopping_list(self):
        print("Lista de compras de", self.name, self.lastname)
        if len(self.shopping_list) == 0:
            print("No hay productos en la lista de compras.")
        else:
            for product in self.shopping_list:
                print(product)

    def __str__(self):
        return f"{self.name} {self.lastname}"

