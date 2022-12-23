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


class User:
    # Comes as a list from JS as ["Login '0' or Create account '1'", "Username", "Password"]
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def checkUsername(self):
        myCursor.execute(
            f"SELECT username FROM userlogininfo WHERE EXISTS (SELECT username FROM userlogininfo WHERE username = '{self.username}');")
        if len(myCursor.fetchall()) == 0:
            return False
        else:
            return True

    def checkPassword(self):
        myCursor.execute(
            f"SELECT username FROM userlogininfo WHERE EXISTS (SELECT username FROM userlogininfo WHERE username = '{self.username}' AND password = '{self.password}');")
        if len(myCursor.fetchall()) == 0:
            return False
        else:
            return True

    def checkAccount(self):
        if self.checkUsername():
            if self.checkPassword():
                return "Login was valid."
            else:
                return "Password was incorrect."
        else:
            return "Account does not exist."

    def createAccount(self):
        if self.checkUsername():
            return "Account already exists."
        else:
            myCursor.execute(f"INSERT INTO userlogininfo (username, password) values ('{self.username}', '{self.password}');")
            db.commit()
            return "Account Created."

    def main(self, loginAttempt):
        if loginAttempt == 0:
            return self.checkAccount()
        elif loginAttempt == 1:
            return self.createAccount()
