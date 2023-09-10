import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text=" ", font=("Helvetica", 20), height=2, width=4, command=lambda x=i: self.play(x))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.player = "X"

    def play(self, i):
        if self.buttons[i]["text"] == " ":
            self.buttons[i].config(text=self.player)
            self.check_for_win()
            self.player = "O" if self.player == "X" else "X"

    def check_for_win(self):
        for i in range(3):
            if (self.buttons[i * 3]["text"] == self.buttons[i * 3 + 1]["text"] == self.buttons[i * 3 + 2]["text"] and self.buttons[i * 3]["text"] != " ") or \
               (self.buttons[i]["text"] == self.buttons[i + 3]["text"] == self.buttons[i + 6]["text"] and self.buttons[i]["text"] != " "):
                self.end_game(self.buttons[i]["text"] + " wins!")
        for i in range(3):
            if (self.buttons[i]["text"] == self.buttons[3 + i]["text"] == self.buttons[6 + i]["text"] and self.buttons[i]["text"] != " ") or \
               (self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"] and self.buttons[0]["text"] != " ") or \
               (self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"] and self.buttons[2]["text"] != " "):
                self.end_game(self.buttons[i]["text"] + " wins!")

    def end_game(self, message):
        for button in self.buttons:
            button.config(state="disabled")
        tk.Label(self.root, text=message, font=("Helvetica", 20)).grid(row=3, column=0, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
