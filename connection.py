import cx_Oracle

def get_connection():
    connection = cx_Oracle.connect('user_one/abcd@localhost:1521/free')
    return connection

'''connection = cx_Oracle.connect('user_one/abcd@localhost:1521/free')
cursor = connection.cursor()

query = "SELECT * FROM all_cust WHERE customer_id = :customer_id"
cursor.execute(query, customer_id=339)
for row in cursor:
    print(f"Customer ID: {row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}")
    '''