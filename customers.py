from connection import get_connection

VALID_REGION = ['A', 'B', 'C', 'D']

def get_region(customer_id:int):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM all_cust WHERE customer_id = :customer_id"
    cursor.execute(query, customer_id=customer_id)
    
    region = cursor.fetchone()[6]

    cursor.close()
    connection.close()
    return region

def create_customer():
    print('\n\033[96mCREATE CUSTOMER:\033[0m')
    customer_id = int(input('ID to customer (int): '))
    customer_name = str(input('Name customer (str): '))
    customer_last_name = str(input('Last name customer (str): '))
    customer_credit_limit = int(input('Credit limit to customer (int): '))
    customer_email = str(input('Email to customer (email): '))
    customer_income_level = str(input('Income level to customer (str): '))
    while True:
        customer_region = str(input('Region to customer (A, B, C, D): ')).upper()
        if customer_region in VALID_REGION:
            break
        else:
            print("Invalid region. Please enter 'A', 'B', 'C', or 'D'.")

    params = {
        "p_customer_id": customer_id,
        "p_cust_first_name": customer_name,
        "p_cust_last_name": customer_last_name,
        "p_credit_limit": customer_credit_limit,
        "p_cust_email": customer_email,
        "p_income_level": customer_income_level,
        "p_region": customer_region
    }

    connection = get_connection()  
    cursor = connection.cursor()  
    cursor.callproc("Insert_Customer", list(params.values()))
    connection.commit()  
    cursor.close()  
    connection.close() 
    print('Customer created successfully') 

def read_customer():
    print('\n\033[96mREAD CUSTOMER:\033[0m')
    customer_id = int(input('ID to customer to search (int): '))

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM all_cust WHERE customer_id = :customer_id"
    cursor.execute(query, customer_id=customer_id)
    for row in cursor:
        print(f"Customer ID: {row[0]}")
        print(f'Customer Name: {row[1]}')
        print(f'Customer Last Name: {row[2]}')
        print(f'Customer credit limit: {row[3]}')
        print(f'Customer email: {row[4]}')
        print(f'Customer income level: {row[5]}')
        print(f'Customer region: {row[6]}')


def update_customer():
    print('\n\033[96mUPDATE CUSTOMER:\033[0m')
    customer_id = int(input('ID of customer to update (int): '))
    customer_name = str(input('New name for customer (str): '))
    customer_last_name = str(input('New last name for customer (str): '))
    customer_credit_limit = int(input('New credit limit for customer (int): '))
    customer_email = str(input('New email for customer (email): '))
    customer_income_level = str(input('New income level for customer (str): '))

    # Validación de la región actual del cliente
    current_region = get_region(customer_id)

    params = {
        "p_customer_id": customer_id,
        "p_cust_first_name": customer_name,
        "p_cust_last_name": customer_last_name,
        "p_credit_limit": customer_credit_limit,
        "p_cust_email": customer_email,
        "p_income_level": customer_income_level,
        "p_region": current_region
    }

    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc("Update_Customer", [params[key] for key in params])
    connection.commit()
    cursor.close()
    connection.close()
    print('Customer updated successfully')

def delete_customer():
    print('\n\033[96mDELETE CUSTOMER:\033[0m')
    customer_id = int(input('ID of the customer to delete (int): '))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.callproc('Delete_Customer', [customer_id])
    connection.commit()

    cursor.close()
    connection.close()
    print('Customer deleted successfully')
