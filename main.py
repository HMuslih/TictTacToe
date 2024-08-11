import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_score = 0
        self.computer_score = 0
        self.setup_gui()

    def setup_gui(self):
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(padx=10, pady=10)

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.button_frame, text='', font=('Arial', 40), width=4, height=2,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        reset_game_button = tk.Button(self.window, text='Play', font=('Arial', 14), command=self.reset_game)
        reset_game_button.pack(pady=5)

        reset_score_button = tk.Button(self.window, text='Reset Score', font=('Arial', 14), command=self.reset_score)
        reset_score_button.pack(pady=5)

        score_frame = tk.Frame(self.window)
        score_frame.pack()

        player_label = tk.Label(score_frame, text='Player:', font=('Arial', 16))
        player_label.grid(row=0, column=0, padx=5, pady=5)
        player_score_label = tk.Label(score_frame, text=self.player_score, font=('Arial', 16))
        player_score_label.grid(row=0, column=1, padx=5, pady=5)

        computer_label = tk.Label(score_frame, text='Computer:', font=('Arial', 16))
        computer_label.grid(row=1, column=0, padx=5, pady=5)
        computer_score_label = tk.Label(score_frame, text=self.computer_score, font=('Arial', 16))
        computer_score_label.grid(row=1, column=1, padx=5, pady=5)

        self.score_labels = {
            'player': player_score_label,
            'computer': computer_score_label
        }

    def button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state='disabled', bg='white')
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.update_score('player')
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = 'O'
                self.make_computer_move()

    def make_computer_move(self):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    available_moves.append((i, j))

        # Cek apakah ada langkah yang dapat memenangkan permainan
        for move in available_moves:
            self.board[move[0]][move[1]] = 'O'
            if self.check_winner('O'):
                self.buttons[move[0]][move[1]].config(text='O', state='disabled', bg='white')
                messagebox.showinfo("Game Over", "Computer wins!")
                self.update_score('computer')
                self.disable_buttons()
                return
            self.board[move[0]][move[1]] = ' '

        # Cek apakah ada langkah yang dapat menghalangi pemain menang di langkah selanjutnya
        for move in available_moves:
            self.board[move[0]][move[1]] = 'X'
            if self.check_winner('X'):
                self.board[move[0]][move[1]] = 'O'
                self.buttons[move[0]][move[1]].config(text='O', state='disabled', bg='white')
                self.current_player = 'X'
                return
            self.board[move[0]][move[1]] = ' '

        # Jika tidak ada langkah yang memenuhi kondisi di atas, pilih langkah secara acak
        move = random.choice(available_moves)
        self.board[move[0]][move[1]] = 'O'
        self.buttons[move[0]][move[1]].config(text='O', state='disabled', bg='white')
        self.current_player = 'X'

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def update_score(self, player):
        if player == 'player':
            self.player_score += 1
        elif player == 'computer':
            self.computer_score += 1
        self.score_labels['player'].config(text=self.player_score)
        self.score_labels['computer'].config(text=self.computer_score)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal', bg='light gray')
        self.current_player = 'X'

    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_labels['player'].config(text=self.player_score)
        self.score_labels['computer'].config(text=self.computer_score)

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
