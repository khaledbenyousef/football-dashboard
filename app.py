from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

# This route serves the main HTML page
@app.route("/")
def index():
    return render_template("index.html")

# This route sends the standings data as JSON to the browser
@app.route("/api/standings")
def standings():
    with open("data/standings.json", "r") as f:
        data = json.load(f)
    
    table = data["standings"][0]["table"]
    
    teams = []
    for team in table:
        teams.append({
            "position": team["position"],
            "name": team["team"]["name"],
            "crest": team["team"]["crest"],
            "played": team["playedGames"],
            "won": team["won"],
            "drawn": team["draw"],
            "lost": team["lost"],
            "gf": team["goalsFor"],
            "ga": team["goalsAgainst"],
            "gd": team["goalDifference"],
            "points": team["points"]
        })
    
    return jsonify(teams)

# This route sends the scorers data as JSON to the browser
@app.route("/api/scorers")
def scorers():
    with open("data/scorers.json", "r") as f:
        data = json.load(f)

    players = []
    for player in data["scorers"]:
        players.append({
            "name": player["player"]["name"],
            "team": player["team"]["name"],
            "crest": player["team"]["crest"],
            "goals": player["goals"],
            "assists": player["assists"] if player["assists"] else 0,
            "penalties": player["penalties"] if player["penalties"] else 0,
        })

    return jsonify(players)

# This must always be the very last thing in the file
if __name__ == "__main__":
    app.run(debug=True)