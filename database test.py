import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    password="123456",
    user="root",
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )

