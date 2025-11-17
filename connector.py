from mysql.connector import connect,Error
try:
    db = connect(
        host="localhost",
        user="root",
        password="45874556",
        use_pure=True,
        port=3306
    ) 
    c = db.cursor()
    c.execute("USE SYS")
except Error as e:
    print(e)
