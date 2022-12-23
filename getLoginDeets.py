from flask import Flask
import json
from checkLogin import User

loginServer = Flask(__name__)


@loginServer.route("/loginData/<string:userInfo>", methods=["GET"])
def getData(userInfo):
    userInfo = json.loads(userInfo)
    print(userInfo)

    if userInfo[0] == 0:
        currentUser = User(userInfo[1], userInfo[2])
        return json.dumps(currentUser.checkAccount())
    elif userInfo[0] == 1:
        try:
            currentUser = User(userInfo[1], userInfo[2], userInfo[3])
            return json.dumps(currentUser.createAccount())
        except IndexError:
            return json.dumps("Error in input: IndexError")
    elif userInfo[0] == 2:


if __name__ == "__main__":
    loginServer.run(debug=True)
