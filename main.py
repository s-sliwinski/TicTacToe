import printBoard
import game

if __name__ == "__main__":
    print('Hello! her is board and list of commands')
    printBoard.printlist()
    while True:
        command = input('Please select the field and type "X" or "O eg.(UL-O)')
        game.write_to_board(command)
        printBoard.printboard()
        if game.check_win_conditions():
            break
