import tkinter as tk
import random
from constrains import *
import logics as lg

class Game():
    def __init__(self, root):
        self.root = root
        self.root.title('2048 Game')

        self.score = 0
        self.board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

        self.canvas = tk.Canvas(
            root,
            height=GRID_SIZE * CELL_SIZE + 50,
            width=GRID_SIZE * CELL_SIZE,
            bg=BACKGROUND_COLOR
        )
        self.canvas.pack()

        self.add_new_tile()
        self.add_new_tile()
        self.draw_board()
        self.root.bind('<Key>', lambda event: lg.handle_keys(self, event))

    def add_new_tile(self):
        emp = []
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if self.board[r][c] == 0:
                    emp.append((r, c))

        if emp: 
            r, c = random.choice(emp)
            self.board[r][c] = random.choice([2, 4])

    def draw_board(self):
        self.canvas.delete('all')

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE + 50
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                value = self.board[r][c]
                color = TAIL_COL.get(value, EMP_COL)

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline='black'
                )

                if value != 0:
                    self.canvas.create_text(
                        x1 + CELL_SIZE // 2,
                        y1 + CELL_SIZE // 2,
                        text=str(value),
                        font=('Arial', 26, 'bold'),
                        fill=TEXT_COL.get(value, "#094bf3")
                    )

        self.canvas.create_text(
            GRID_SIZE * CELL_SIZE // 2,
            25,
            text=f'Score: {self.score}',
            font=('Arial', 20, 'bold'),
            fill='purple'
        )


root = tk.Tk()
game1 = Game(root)
root.mainloop()
