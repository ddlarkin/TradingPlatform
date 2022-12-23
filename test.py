
import mariadb


db = mariadb.connect(
    user="root",
    password="Inuvik",
    host="localhost",
    port=3306,
    database="stockSuggestionInfo"

)

myCursor = db.cursor(buffered=True)
myCursor.execute("USE userinfo;")

input = 'fDare'

myCursor.execute(f"SELECT username FROM userlogininfo WHERE EXISTS (SELECT username FROM userlogininfo WHERE username = '{input}')")
result = myCursor.fetchall()
print(result)
if len(result) == 0:
    print("False")
else:
    print("True")
