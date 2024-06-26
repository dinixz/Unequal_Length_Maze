from algorithms import *

def possible_moves_player(state:Maze): #obtém o resultado de cada movimento (None se não for possível)
    return {'up': state.up(), 'down': state.down(), 'left': state.left(), 'right': state.right(), '-': state}

def get_hint(maze:Maze, final_maze:Maze) -> str: #output é a direção para onde nos temos de mover comparativamente ao maze_final
    hint = {up_symbol: 'up', down_symbol: 'down', left_symbol: 'left', right_symbol: 'right'}
    next_move = final_maze.maze[maze.cur_line, maze.cur_col]
    return hint.get(next_move)

def game_over(maze:Maze, final_maze:Maze) -> bool:
    #compara se todas as casas vizinhas do maze atual e compara-se ao final_maze, excluindo se a casa for vazia ou a casa de target
    if maze.cur_line != 0:
        if maze.maze[maze.cur_line - 1, maze.cur_col] != final_maze.maze[maze.cur_line - 1, maze.cur_col] and not maze.maze[maze.cur_line - 1, maze.cur_col] in {None, objetivo}:
            return True
    if maze.cur_line != maze.lines - 1:
        if maze.maze[maze.cur_line + 1, maze.cur_col] != final_maze.maze[maze.cur_line + 1, maze.cur_col] and not maze.maze[maze.cur_line + 1, maze.cur_col] in {None, objetivo}:
            return True
    if maze.cur_col != 0:
        if maze.maze[maze.cur_line, maze.cur_col - 1] != final_maze.maze[maze.cur_line, maze.cur_col - 1] and not maze.maze[maze.cur_line, maze.cur_col - 1] in {None, objetivo}:
            return True
    if maze.cur_col != maze.columns - 1:
        if maze.maze[maze.cur_line, maze.cur_col + 1] != final_maze.maze[maze.cur_line, maze.cur_col + 1] and not maze.maze[maze.cur_line, maze.cur_col + 1] in {None, objetivo}:
            return True
    return False