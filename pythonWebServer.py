
from flask import Flask
import json



app = Flask(__name__)


def testFunc(currentSearch):
    print(currentSearch)
    return json.dumps(["blue"])

# Create the receiver API POST endpoint:
@app.route("/searchRecommendations/<string:currentSearch>", methods=["GET"])
def postME(currentSearch):
    return testFunc(currentSearch)



if __name__ == "__main__":
   app.run(debug=True)
