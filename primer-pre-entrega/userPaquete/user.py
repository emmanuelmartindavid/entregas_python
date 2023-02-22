import logging

def user_registration():
    username = input("Nombre de usuario: ")
    password = input("Contrasenia: ")
    user = {
        'username': username,
        'password': password
    }
    return user


def login_user(data):
    username = input("Ingrese su nombre de usuario por favor: ")
    if username in data:
        password = input("Ingrese su contrasenia por favor: ")
        if data[username]["password"] == password:
            return True
        elif data[username]["password"] != password:
            logging.error("Contrasenia incorrecta.\n")
            return False
    elif username not in data:
        logging.error("No existe tal usuario.\n")
        return False


def save_user_data(data):
    with open("data-user.txt", "a") as file:
        for username in data:
            file.write("Usuario: " + username + ", " + "Contrasenia: " + data[username]["password"] + "\n")


def read_user_data():
    with open("data-user.txt", "r") as file:
        data = file.read()
        return data


user_dictionary = {}


def print_information():
    print("1. Registro de usuario.\n"
          "2. Incio de sesion.\n"
          "3. Ver datos registrados en archivo de texto.\n"
          "4. Salir del programa.\n")
    return int(input("Ingrese una opcion por favor: \n"))

