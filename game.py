import tkinter as tk
from tkinter import messagebox

class TicTakToe :
    def __init__(self, board_size=3) :
        self.board_size = board_size
        self.window = tk.Tk()
        self.window.title('Tic Tak Toe')
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'x'
        self.create_buttons()
    
    def create_buttons(self):
        self.buttons = [[tk.Button(self.window, text=' ', font=('Arial', 24), width=3, height=1,
                                   command=lambda row=row, col=col: self.make_move(row,col)) for col in range(self.board_size)]
                                   for row in range(self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win(self.current_player):
                pass
            elif self.is_full():
                pass
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

        else:
            messagebox.showerror("Invalid move", "Cell is already taken. Try again!")

    def check_win(self, player):
        pass

    def is_full(self):
        pass
    


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    board_size = int(input("enter the size of the board(e.g., 3 for 3*3, 4 for 4*4, etc.): "))
    tic_tac_toe = TicTakToe(board_size)
    tic_tac_toe.run()