from gamestate import GameState


def read_level(level):
    y_pointer = 0
    x_pointer = 0
    gamestate = GameState()
    with open("./boards/" + level + '.txt', "r") as f:
        f = f.read().splitlines()
        gamestate.dimensions = [len(f), len(f[0])]
    return gamestate


s = (read_level("level-2"))
z =2
def translate_input_symbol_to_object(position, gamestate, symbol):
    if symbol == "P":
        gamestate.pacman = Pacman(position, gamestate)
    if symbol == "o":
        gamestate.fruits.append(Fruit(position, gamestate))
        gamestate.num_fruits_left += 1
    if symbol == "%":
        gamestate.walls.append(Wall(position, gamestate))
        gamestate.wall_positions.append(position)
    if symbol == "G":
        gamestate.ghosts.append(Ghost(position, gamestate))
    if symbol == ".":
        gamestate.dots.append(Dot(position, gamestate))
        gamestate.num_dots_left += 1