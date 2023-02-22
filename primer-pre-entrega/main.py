from userPaquete.user import *

while True:
    option = print_information()
    if option == 1:
        print("Ingrese sus datos por favor:\n")
        new_user = user_registration()
        user_dictionary[new_user['username']] = new_user
        save_user_data(user_dictionary)
        print("\nRegistro exitoso!\n")
    if option == 2:
        if login_user(user_dictionary):
            print("Ha iniciado sesion.\n")
    elif option == 3:
        print(read_user_data())
    elif option == 4:
        print("Adios!!")
        break
    else:
        print("\nOpcion incorrecta. Reintente.\n")