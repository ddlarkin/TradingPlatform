

import mariadb


db = mariadb.connect(
    user="root",
    password="Inuvik",
    host="localhost",
    port=3306,
    database="stockSuggestionInfo"

)

myCursor = db.cursor(buffered=True)
myCursor.execute("USE stockSuggestionInfo;")
# myCursor.execute("INSERT INTO stockInfo (Ticker, CompanyName, Volume, Price) values ('AAPL', 'APPLE Inc', 110011, 138.38);")
# myCursor.execute("SELECT COUNT(*) FROM stockInfo;")
# db.commit()
myCursor.execute("SELECT * FROM stockINFO;")
print(myCursor.fetchall())
print('succesful connection')