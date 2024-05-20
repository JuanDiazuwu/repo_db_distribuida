from customers import (create_customer, read_customer, 
                       update_customer, delete_customer,
                       get_region)

def menu():
    while True:
        print("\n\033[96m...: MENU :...\033[0m")
        print("1. Customers")
        print("2. Order Items")
        print("3. Orders")
        print("4. Product Information")
        print("5. Exit")

        choice = input("Introduzca un número: ")

        if choice == '1':
            submenu('Customers')

        elif choice == '2':
            submenu('Order Items')

        elif choice == '3':
            submenu('Orders')

        elif choice == '4':
            submenu('Product Information')

        elif choice == '5':
            break

        else:
            print('Introduzca un número valido')

def submenu(inpt:str):
    while True:
        print(f'\n\033[96m...: Menu {inpt} :...\033[0m')
        print("1. Crear")           #C
        print("2. Obtener")         #R
        print("3. Actualizar")      #U
        print("4. Eliminar")        #D
        print("5. Regresar al menú anterior")

        choice_submenu = input("Introduzca un número: ")
        if choice_submenu == '1':
            if inpt == 'Customers':
                create_customer()
            '''elif inpt == 'Order Items':
                create_order_item()
            elif inpt == 'Orders':
                create_order()
            elif inpt == 'Product Information':
                create_product_info()'''
            
        elif choice_submenu == '2':
            if inpt == 'Customers':
                read_customer()

        elif choice_submenu == '3':
            if inpt == 'Customers':
                update_customer()

        elif choice_submenu == '4':
            if inpt == 'Customers':
                delete_customer()

        elif choice_submenu == '5':
            break

        elif choice_submenu == '6':
            print(get_region(201))

        else:
            print('Introduzca un número valido')