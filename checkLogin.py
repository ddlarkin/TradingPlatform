import mariadb
import hashlib
import uuid

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
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email

    def checkUsername(self):
        myCursor.execute(
            f"SELECT username FROM userlogininfo WHERE EXISTS (SELECT username FROM userlogininfo WHERE username = '{self.username}');")
        if len(myCursor.fetchall()) == 0:
            return False
        else:
            return True

    def checkPassword(self):
        myCursor.execute(
            f"SELECT password FROM userlogininfo WHERE username = '{self.username}';")
        hashedPassword = myCursor.fetchall()[0][0]
        hashedPassword, salt = hashedPassword.split(':')
        hashedAttempt = hashlib.sha256(salt.encode() + self.password.encode()).hexdigest()
        if hashedAttempt == hashedPassword:
            return True
        else:
            return False

    def checkEmail(self):
        myCursor.execute(
            f"SELECT email FROM userlogininfo WHERE EXISTS (SELECT email FROM userlogininfo WHERE email = '{self.email}');")
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
            return "Account name already in use."
        elif self.checkEmail():
            return "Email already in use."
        else:
            salt = uuid.uuid4().hex
            hashedPassword = hashlib.sha256(salt.encode() + self.password.encode()).hexdigest() + ':' + salt
            myCursor.execute(f"INSERT INTO userlogininfo (username, password, email) values ('{self.username}', '{hashedPassword}', '{self.email}');")
            db.commit()
            return "Account Created."
