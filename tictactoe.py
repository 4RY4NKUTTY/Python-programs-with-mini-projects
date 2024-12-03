import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", width=10, height=3,
                                               font=('Helvetica', 24),
                                               bg='lightblue',
                                               activebackground='lightgreen',
                                               command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
    def make_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O"
                self.ai_move()
    
    def ai_move(self):
        row, col = self.find_best_move()
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        if self.check_winner(self.current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_board()
        elif self.is_board_full():
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.reset_board()
        else:
            self.current_player = "X"
    
    def find_best_move(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    if self.check_winner("O"):
                        return i, j
                    self.board[i][j] = " "
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    if self.check_winner("X"):
                        self.board[i][j] = " "
                        return i, j
                    self.board[i][j] = " "
        
        if self.board[1][1] == " ":
            return 1, 1
        
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        random.shuffle(corners)
        for i, j in corners:
            if self.board[i][j] == " ":
                return i, j
        
        sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
        random.shuffle(sides)
        for i, j in sides:
            if self.board[i][j] == " ":
                return i, j
        
        return -1, -1
    
    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False
    
    def is_board_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)
    
    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
