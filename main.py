from game import Game
import sys

if __name__ == "__main__":
    init_flag = 0
    while True:
        if not init_flag:
            while True:
                gamemode = input('Please type game mode: "2players" or "AI" and press enter: ')
                if gamemode == '2players' or gamemode == 'AI':
                    break
                else:
                    print(f'Wrong command! You typed {gamemode}')
            while True:
                pawn = input('Please select pawn "X" or "O" and press enter: ')
                if pawn == 'X':
                    current_game = Game(gamemode, 'X', 'O')
                    break
                elif pawn == 'O':
                    current_game = Game(gamemode, 'O', 'X')
                    break
                else:
                    print(f'Wrong command! You typed: {pawn}')
            print('Here is list of commands')
            Game.printlist()
            init_flag = 1
        else:
            #game loops
            if current_game.get_game_mode() == '2players':
                while True:
                    field = input('Please select the field and type field name: ')
                    if current_game.write_to_board(field):
                        current_game.printboard()
                        if current_game.check_win_conditions():
                            while True:
                                command = input('What you want to do? "EXIT" or "RESET": ')
                                if command == "RESET":
                                    init_flag = 0
                                    break
                                elif command == "EXIT":
                                    sys.exit()
                                else:
                                    print(f'Wrong command! You typed: {command}')
                            break
            elif current_game.get_game_mode() == 'AI':
                while True:
                    field = input('Please select the field and type field name: ')
                    if current_game.write_to_board(field):
                        current_game.bot_moves()
                        current_game.printboard()
                        if current_game.check_win_conditions():
                            while True:
                                command = input('What you want to do? "EXIT" or "RESET": ')
                                if command == "RESET":
                                    init_flag = 0
                                    break
                                elif command == "EXIT":
                                    sys.exit()
                                else:
                                    print(f'Wrong command! You typed: {command}')
                            break