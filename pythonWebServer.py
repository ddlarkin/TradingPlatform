
from flask import Flask
from flask_cors import CORS
import json



app = Flask(__name__)

cors = CORS(app)


def testFunc(currentSearch):
    print(currentSearch)
    return json.dumps(["blue"])

# Create the receiver API POST endpoint:
@app.route("/searchRecommendations/<string:currentSearch>", methods=["GET"])
def postME(currentSearch):
    return testFunc(currentSearch)



if __name__ == "__main__":
   app.run(debug=True)
