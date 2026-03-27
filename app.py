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
    
    # Pull out just the table we need
    table = data["standings"][0]["table"]
    
    # Simplify each team to only what we need
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

if __name__ == "__main__":
    app.run(debug=True)