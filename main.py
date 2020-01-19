from game import Game

if __name__ == "__main__":
    gamemode = input('Please type game mode: "2players" or "AI" and press enter: ')
    pawn = input('Please select pawn "X" or "O" and press enter: ')
    if pawn == 'X':
        current_game = Game(gamemode, 'X', 'O')
    elif pawn == 'O':
        current_game = Game(gamemode, 'O', 'X')
    print('Here is list of commands')
    Game.printlist()

    while True:
        command = input('Please select the field and type "X" or "O eg.(UL-O)')
        if current_game.write_to_board(command):
            current_game.printboard()
            if current_game.check_win_conditions():
                break
