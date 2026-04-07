<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🧠 AI Enemy Dungeon Game</title>
</head>
<body>

<h1 align="center">🧠 AI Enemy Dungeon Game 🎮</h1>

<p align="center">
  <b>A 2D dungeon game built from scratch in Python where enemies learn using Reinforcement Learning.</b><br>
  <i>Not just a game — an AI experiment you can play.</i>
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>
<strong>AI Enemy Dungeon Game</strong> is a <b>2D top-down dungeon game</b> developed using
<b>Python + Pygame</b>, where enemies are powered by <b>Reinforcement Learning (Q-Learning)</b>.
</p>

<p>
Unlike traditional games with fixed enemy behavior, enemies in this game
<b>learn from player actions</b>, adapt strategies, and become smarter over time.
</p>

<p>
🎯 This project is designed for:
</p>

<ul>
  <li>🧑‍🎓 Students & beginners in AI</li>
  <li>🎮 Game development learners</li>
  <li>🤖 Understanding Reinforcement Learning visually</li>
  <li>📂 Portfolio & GitHub showcase</li>
</ul>
🔗 **ENJOY😍TO🥰PLAY🎮GAME:**  https://ai-enemy-attack-game-cs15.vercel.app/

<h2>🎬 Game Start Screen</h2>

<p>
The game begins with a clean and minimal start menu.
</p>

<p align="center">
  <img src="assets/readme/start_screen.png.png" width="70%" alt="Start Screen">
</p>

<ul>
  <li>▶️ Press <b>ENTER</b> to start the game</li>
  <li>🎨 Simple UI for instant understanding</li>
</ul>

<hr>

<h2>🕹️ Gameplay & HUD</h2>

<p>
During gameplay, the player sees a real-time HUD showing:
</p>

<ul>
  <li>❤️ Player Health</li>
  <li>⭐ Score</li>
  <li>📈 Level Progression</li>
  <li>🧠 Enemy Learning Status</li>
</ul>

<p align="center">
  <img src="assets/readme/gameplay_ui.png.png" width="80%" alt="Gameplay HUD">
</p>

<hr>

<h2>🧍 Player Character</h2>

<p>
You control the player using keyboard controls.
</p>

<p align="center">
  <img src="assets/readme/player.png.jpeg" width="200" alt="Player Character">
</p>

<ul>
  <li>⌨️ Controls: <b>W A S D</b></li>
  <li>🚶 Smooth movement</li>
  <li>🧱 Boundary-restricted inside the dungeon</li>
</ul>

<hr>

<h2>👾 AI Enemy (Reinforcement Learning)</h2>

<p>
Enemies are not scripted — they <b>learn using Q-Learning</b>.
</p>

<p align="center">
  <img src="assets/readme/enemy.png.jpeg" width="250" alt="Enemy Character">
</p>

<p>
Enemy behavior includes:
</p>

<ul>
  <li>🔁 Observing player position</li>
  <li>🎯 Choosing actions (CHASE / RUN / ATTACK)</li>
  <li>📊 Receiving rewards & penalties</li>
  <li>🧠 Improving decisions over time</li>
</ul>

<p>
The enemy’s learning is saved and loaded automatically using <code>pickle</code>.
</p>

<hr>

<h2>🗺️ Dungeon Floor & Environment</h2>

<p>
The dungeon world is created using a <b>tile-based map system</b>.
</p>

<p align="center">
  <img src="assets/readme/game_map.png.jpeg" width="80%" alt="Game Map">
</p>

<ul>
  <li>🟩 Repeating floor tiles</li>
  <li>📐 Grid-based movement</li>
  <li>🎨 Pixel-art style environment</li>
</ul>

<hr>

<h2>📈 Level Progression</h2>

<p>
As the score increases:
</p>

<ul>
  <li>⬆️ Level increases</li>
  <li>👾 New enemies spawn</li>
  <li>⚡ Difficulty increases</li>
</ul>

<p>
This ensures replayability and challenge.
</p>

<hr>

<h2>🔊 Sound Effects</h2>

<ul>
  <li>💥 Collision sound using <code>pygame.mixer</code></li>
  <li>🎧 Improves game feel and feedback</li>
</ul>

<hr>

<h2>⌨️ Controls</h2>

<table border="1" cellpadding="6">
<tr><th>Key</th><th>Action</th></tr>
<tr><td>ENTER</td><td>Start Game</td></tr>
<tr><td>W A S D</td><td>Move Player</td></tr>
<tr><td>R</td><td>Restart Game</td></tr>
<tr><td>Close Window</td><td>Exit Game</td></tr>
</table>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>🐍 Python</li>
  <li>🎮 Pygame</li>
  <li>🧠 Reinforcement Learning (Q-Learning)</li>
  <li>💾 Pickle (AI memory)</li>
</ul>

<hr>

<h2>🏁 Final Note</h2>

<p>
This project demonstrates that:
</p>

<ul>
  <li>✅ Games can teach AI concepts</li>
  <li>✅ Reinforcement Learning can be visual</li>
  <li>✅ Python is powerful for game + AI projects</li>
</ul>

<p align="center">
  <b>⭐ If you like this project, consider giving it a star!</b>
</p>

</body>
</html>
