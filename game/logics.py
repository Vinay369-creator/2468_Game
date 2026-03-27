import constrains as c

def compress(row):
    new_row = [no for no in row if no != 0]
    new_row += [0] * (c.GRID_SIZE - len(new_row))
    return new_row

def merge(row, game):
    for i in range(c.GRID_SIZE - 1): 
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
            game.score += row[i]  
    return row

def move_left(game):
    new_board = []
    changed = False

    for row in game.board:
        comp = compress(row)
        merg = merge(comp, game)
        final = compress(merg)

        if final != row:
            changed = True
        new_board.append(final)

    game.board = new_board
    return changed

def move_right(game):
    game.board = [row[::-1] for row in game.board]
    changed = move_left(game)
    game.board = [row[::-1] for row in game.board]
    return changed

def transpose(game):
    dummy=[]
    for col in range(c.GRID_SIZE):
        temp=[]
        for r in range(c.GRID_SIZE):
            temp.append(game.board[r][col])
        dummy.append(temp)

    game.board=dummy

def move_up(game):
    transpose(game)
    changed = move_left(game) 
    transpose(game)
    return changed

def move_down(game):
    transpose(game)
    changed = move_right(game) 
    transpose(game)
    return changed

def handle_keys(game, event):
    moved = False 
    key=event.keysym.lower()
    if key == 'a':
        moved = move_left(game)
    elif key == 'd':
        moved = move_right(game)
    elif key == 'w':
        moved = move_up(game)
    elif key == 's':
        moved = move_down(game)

    if moved:
        game.add_new_tile()  
        game.draw_board()

    if game_over(game):
        game.canvas.create_text(
            c.GRID_SIZE * c.CELL_SIZE // 2,
            c.GRID_SIZE * c.CELL_SIZE // 2,
            text='YOU LOSE',
            font=('Arial', 30, 'bold'),
            fill='red'
        )

def game_over(game):
    for row in game.board:
        if 0 in row:
            return False

    for r in range(c.GRID_SIZE):
        for col in range(c.GRID_SIZE - 1):
            if game.board[r][col] == game.board[r][col + 1]:
                return False

    for col in range(c.GRID_SIZE):
        for r in range(c.GRID_SIZE - 1):
            if game.board[r][col] == game.board[r + 1][col]:
                return False

    return True