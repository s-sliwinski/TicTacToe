
gameBoard = {'UL': '', 'UM': '', 'UR': '', 'ML': '', 'MM': '', 'MR': '', 'LL': '', 'LM': '', 'LR': ''}


def write_to_board(command):
    #decoding command
    place = command[0] + command[1]
    sign = command[3]
    gameBoard[place] = sign


def check_win_conditions():
    win_flag = False
    keyfirstletterindex = 0
    keysecondletterindex = 1

    #check rows
    for k, v in gameBoard.items():
        if v == '':
            continue
        else:
            key = k[keyfirstletterindex]
            value = v
            chflag = 0
            for K, V in gameBoard.items():
                if K[keyfirstletterindex] == key and V == value:
                    chflag += 1
            if chflag == 3:
                print(f"{value} You won!")
                win_flag = True
                break
    #chcek columns
    if not win_flag:
        for k, v in gameBoard.items():
            if v == '':
                continue
            else:
                key = k[keysecondletterindex]
                value = v
                chflag = 0
                for K, V in gameBoard.items():
                    if K[keysecondletterindex] == key and V == value:
                        chflag += 1
                if chflag == 3:
                    print(f"{value} You won!")
                    win_flag = True
                    break
    #check diagonals
    if not win_flag:
        if (gameBoard['UL'] == gameBoard['MM'] == gameBoard['LR']) and gameBoard['UL'] != '' and gameBoard['MM'] != '' and gameBoard['LR'] != '':
            print(f'{gameBoard["UL"]} You won!')
            win_flag = True
        if (gameBoard['UR'] == gameBoard['MM'] == gameBoard['LL']) and gameBoard['UR'] != '' and gameBoard['MM'] != '' and gameBoard['LL'] != '':
            print(f'{gameBoard["UR"]} You won!')
            win_flag = True

    return win_flag


if __name__ == "__main__":
    check_win_conditions()
