# Introduction to Minesweeper and Its Rules​
## Game Introduction​
Minesweeper is a classic single - player puzzle game that has been popular for decades. The game's interface typically consists of a rectangular grid of squares. Each square can either contain a hidden mine or be a safe space with a number. The objective of the game is to uncover all the squares that do not contain mines without triggering any of the mines.​
## Rules​
### Initial Setup​
At the start of the game, mines are randomly placed throughout the grid. The number of mines is usually specified at the beginning, and the player is also informed of the size of the grid (e.g., a 10x10 grid with 10 mines).​
### Revealing Squares​
To play, the player clicks on a square. If the square is safe (does not contain a mine), one of two things can happen:​<br>
  <br>1. If the square is adjacent to no mines, it will reveal a large area of connected safe squares. This is because if a square has no adjacent mines, all the squares around it must also be safe, and the game algorithm automatically uncovers these safe areas.​<br>
  <br>2. If the square is adjacent to mines, it will display a number. This number indicates how many of the adjacent squares (up, down, left, right, and diagonally) contain mines. <br><br>For example, if a square shows the number '3', it means that there are 3 mines in the 8 adjacent squares.​
However, if the player clicks on a square that contains a mine, the game is over. The mine will be revealed, usually with a visual indication such as an explosion or a red 'X', and the player loses the game.​
### Flagging Mines​
The player can use the right - click option (or a designated key in some versions) to flag squares that they suspect contain mines. When a square is flagged, it is marked with a flag icon (usually a small flag). This is a useful strategy to mark squares that you think are mines so that you can avoid clicking on them accidentally and also to help you keep track of where the mines might be located as you progress through the game.​
### Winning the Game​
The player wins the game when all the non - mine squares have been revealed. This means that every square that does not contain a mine has been uncovered, and all the mines have been correctly identified and flagged (or left un - clicked).
