import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("275x300")
        self.board = [["" for x in range(3)] for y in range(3)]
        self.turn = "X"
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(master, text=" ", font=("Helvetica", 20),
                                   height=2, width=4,
                                   command=lambda row=i, col=j: self.play(row, col))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

    def play(self, row, col):
        if self.board[row][col] != "":
            return
        self.buttons[row][col].config(text=self.turn)
        self.board[row][col] = self.turn
        if self.check_win(row, col):
            self.master.title("Player " + self.turn + " Wins!")
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(state="disabled")
        elif self.check_draw():
            self.master.title("Draw")
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(state="disabled")
        else:
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def check_win(self, row, col):
        # Check row
        if all(cell == self.turn for cell in self.board[row]):
            return True
        # Check column
        if all(cell == self.turn for cell in [self.board[i][col] for i in range(3)]):
            return True
        # Check diagonal
        if row == col:
            if all(cell == self.turn for cell in [self.board[i][i] for i in range(3)]):
                return True
        if row + col == 2:
            if all(cell == self.turn for cell in [self.board[i][2 - i] for i in range(3)]):
                return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

