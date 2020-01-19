from game import Game

if __name__ == "__main__":

    # gamemode = input('Please type game mode: "2players" or "AI" and press enter')
    # game.game_mode_set(gamemode)
    print('Hello! here is list of commands')
    current_game = Game('2players', 'X')
    Game.printlist()

    while True:
        command = input('Please select the field and type "X" or "O eg.(UL-O)')
        current_game.write_to_board(command)
        current_game.printboard()
        if current_game.check_win_conditions():
            break
