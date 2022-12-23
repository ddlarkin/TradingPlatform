# Uses the DB to find the top suggestions for stocks based on current search entry
import json

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


def suggestions(search='A', noSuggestions=5):

    myCursor.execute(f"SELECT * FROM stockInfo WHERE SUBSTRING(Ticker, 1, {len(search)}) = '{search}';")
    possibleAnswers = myCursor.fetchall()
    possibleAnswers.sort(key=lambda x: x[2]*x[3])
    possibleAnswers.reverse()

    if len(possibleAnswers) < noSuggestions:
        noSuggestions = len(possibleAnswers)

    suggestionList = []
    for i in range(noSuggestions):
        suggestionList.append([possibleAnswers[i][0], possibleAnswers[i][1]])

    return json.dumps(suggestionList)


