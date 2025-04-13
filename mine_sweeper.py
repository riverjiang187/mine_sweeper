import tkinter as tk
import random


class Minesweeper:
    def __init__(self, root, rows, cols, mines):
        self.root = root
        self.root.title("Mine Sweeper")
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.board = [[0] * cols for _ in range(rows)]
        self.revealed = [[False] * cols for _ in range(rows)]
        self.flagged = [[False] * cols for _ in range(rows)]
        self.game_over = False
        self.win = False
        self.create_board()
        self.place_mines()
        self.calculate_numbers()
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=rows + 2, columnspan=cols)

    def create_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                button = tk.Button(self.root, width=2, height=1,
                                   command=lambda r=i, c=j: self.reveal(r, c))
                button.bind("<Button-3>", lambda event, r=i, c=j: self.flag(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def place_mines(self):
        count = 0
        while count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                count += 1

    def calculate_numbers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1:
                    for x in range(max(0, i - 1), min(self.rows, i + 2)):
                        for y in range(max(0, j - 1), min(self.cols, j + 2)):
                            if self.board[x][y] == -1:
                                self.board[i][j] += 1

    def reveal(self, row, col):
        if self.game_over or self.revealed[row][col] or self.flagged[row][col]:
            return
        if self.board[row][col] == -1:
            self.game_over = True
            self.show_all_mines()
            self.display_message("Game Over!")
        else:
            self.revealed[row][col] = True
            self.buttons[row][col].config(text=str(self.board[row][col]) if self.board[row][col] != 0 else "",
                                          state=tk.DISABLED)
            if self.board[row][col] == 0:
                for x in range(max(0, row - 1), min(self.rows, row + 2)):
                    for y in range(max(0, col - 1), min(self.cols, col + 2)):
                        self.reveal(x, y)
            self.check_win()

    def flag(self, row, col):
        if self.game_over or self.revealed[row][col]:
            return
        self.flagged[row][col] = not self.flagged[row][col]
        if self.flagged[row][col]:
            self.buttons[row][col].config(text="🚩")
        else:
            self.buttons[row][col].config(text="")

    def show_all_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="💣", state=tk.DISABLED)

    def check_win(self):
        unrevealed = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.revealed[i][j] and self.board[i][j] != -1:
                    unrevealed += 1
        if unrevealed == 0:
            self.game_over = True
            self.win = True
            self.display_message("You Win!")

    def display_message(self, message):
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(state=tk.DISABLED)
        label = tk.Label(self.root, text=message, font=("Arial", 20))
        label.grid(row=self.rows, columnspan=self.cols)

    def restart_game(self):
        self.game_over = False
        self.win = False
        self.board = [[0] * self.cols for _ in range(self.rows)]
        self.revealed = [[False] * self.cols for _ in range(self.rows)]
        self.flagged = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Label):
                widget.destroy()
        self.place_mines()
        self.calculate_numbers()


root = tk.Tk()
game = Minesweeper(root, 10, 10, 10)  # change rows, col, and numbers of mines here, or use random
root.mainloop()