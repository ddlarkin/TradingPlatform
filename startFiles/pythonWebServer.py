
from flask import Flask
from flask_cors import CORS
import suggestionFinder


app = Flask(__name__)

cors = CORS(app)


# Create the receiver API POST endpoint:
@app.route("/searchRecommendations/<string:currentSearch>", methods=["GET"])
def postME(currentSearch):
     return suggestionFinder.suggestions(search=currentSearch)
if __name__ == "__main__":
   app.run(debug=True)


