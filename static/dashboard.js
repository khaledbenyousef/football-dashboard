// Fetch the standings data from our Flask API
fetch("/api/standings")
  .then(response => response.json())
  .then(teams => {
    buildTable(teams);
    buildChart(teams);
  });

function buildTable(teams) {
  const container = document.getElementById("table-container");

  let html = `
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Team</th>
          <th>P</th>
          <th>W</th>
          <th>D</th>
          <th>L</th>
          <th>GF</th>
          <th>GA</th>
          <th>GD</th>
          <th>Pts</th>
        </tr>
      </thead>
      <tbody>
  `;

  teams.forEach(team => {
    html += `
      <tr>
        <td class="pos">${team.position}</td>
        <td>
          <img class="crest" src="${team.crest}" />
          ${team.name}
        </td>
        <td>${team.played}</td>
        <td>${team.won}</td>
        <td>${team.drawn}</td>
        <td>${team.lost}</td>
        <td>${team.gf}</td>
        <td>${team.ga}</td>
        <td>${team.gd}</td>
        <td class="pts">${team.points}</td>
      </tr>
    `;
  });

  html += `</tbody></table>`;
  container.innerHTML = html;
}

function buildChart(teams) {
  const ctx = document.getElementById("points-chart").getContext("2d");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: teams.map(t => t.name),
      datasets: [{
        label: "Points",
        data: teams.map(t => t.points),
        backgroundColor: "#1f6feb",
        borderRadius: 4,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          ticks: { color: "#8b949e", font: { size: 11 } },
          grid: { color: "#21262d" }
        },
        y: {
          ticks: { color: "#8b949e" },
          grid: { color: "#21262d" }
        }
      }
    }
  });
}
// Fetch scorers from our new Flask route
fetch("/api/scorers")
  .then(response => response.json())
  .then(players => {
    buildScorers(players);
  });

function buildScorers(players) {
  const container = document.getElementById("scorers-container");

  // .map() transforms every item in an array into something new
  // here we turn each player object into an HTML string
  const rows = players.map((player, index) => `
    <div class="scorer-row">
      <div class="scorer-rank">${index + 1}</div>
      <div class="scorer-info">
        <div class="scorer-name">${player.name}</div>
        <div class="scorer-team">
          <img class="crest" src="${player.crest}" style="width:16px;height:16px;" />
          ${player.team}
        </div>
      </div>
      <div class="scorer-stats">
        <div class="stat-box">
          <div class="stat-value">${player.goals}</div>
          <div class="stat-label">Goals</div>
        </div>
        <div class="stat-box">
          <div class="stat-value">${player.assists}</div>
          <div class="stat-label">Assists</div>
        </div>
      </div>
    </div>
  `);

  // .join("") merges the array of strings into one big HTML string
  container.innerHTML = rows.join("");
}