from pysqlite2 import dbapi2 as sqlite

connection = sqlite.connect("example.db")
cursor = connection.cursor()
cursor.execute("SELECT FirstName, LastName FROM Person ORDER BY LastName;")
results = cursor.fetchall();
for r in results:
    print r
cursor.close();
connection.close();
