from paqueteCliente import client

client_1 = client.Client("Emmanuel", "Martin", "emma.martin@gmail.com", "742 Evergreen Terrace", "1140385674")

client_1.add_product("Camisa")
client_1.add_product("Remera")
client_1.add_product("Pantalon")
client_1.add_product("Zapatos")

client_1.show_shopping_list()

client_1.confirm_sale()

client_1.delete_product("Camisa")

client_1.show_shopping_list()

client_1.clean_shopping_list()

client_1.show_shopping_list()

print(client_1)
