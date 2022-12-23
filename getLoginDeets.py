from flask import Flask
import json
from checkLogin import User

loginServer = Flask(__name__)


@loginServer.route("/loginData/<string:userInfo>", methods=["GET"])
def getData(userInfo):
    userInfo = json.loads(userInfo)
    print(userInfo)
    currentUser = User(userInfo[1], userInfo[2])
    return json.dumps(currentUser.main(loginAttempt=userInfo[0]))


if __name__ == "__main__":
    loginServer.run(debug=True)
