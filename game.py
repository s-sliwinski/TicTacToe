class Game:

    def __init__(self, gamemode = None, player = None):
        self.__gameBoard = {'UL': 'X', 'UM': '', 'UR': '', 'ML': '', 'MM': '', 'MR': '', 'LL': '', 'LM': '', 'LR': ''}
        self.__game_mode = gamemode
        self.__player = player

    def set_game_mode(self, gamemode):
        self.__game_mode = gamemode

    def get_game_mode(self):
        return self.__game_mode

    def write_to_board(self, command):
        #decoding command
        place = command[0] + command[1]
        sign = command[3]
        self.__gameBoard[place] = sign

    def get_game_board(self):
        return self.__gameBoard

    def get_game_board_field(self, index):
        return self.__gameBoard[index]

    def check_win_conditions(self):
        win_flag = False
        keyfirstletterindex = 0
        keysecondletterindex = 1
        #check rows
        for k, v in self.__gameBoard.items():
            if v == '':
                continue
            else:
                key = k[keyfirstletterindex]
                value = v
                chflag = 0
                for K, V in self.__gameBoard.items():
                    if K[keyfirstletterindex] == key and V == value:
                        chflag += 1
                if chflag == 3:
                    print(f"{value} You won!")
                    win_flag = True
                    break
        #chcek columns
        if not win_flag:
            for k, v in self.__gameBoard.items():
                if v == '':
                    continue
                else:
                    key = k[keysecondletterindex]
                    value = v
                    chflag = 0
                    for K, V in self.__gameBoard.items():
                        if K[keysecondletterindex] == key and V == value:
                            chflag += 1
                    if chflag == 3:
                        print(f"{value} You won!")
                        win_flag = True
                        break
        #check diagonals
        if not win_flag:
            if (self.__gameBoard['UL'] == self.__gameBoard['MM'] == self.__gameBoard['LR']) and self.__gameBoard['UL'] != '' and self.__gameBoard['MM'] != '' and self.__gameBoard['LR'] != '':
                print(f'{self.__gameBoard["UL"]} You won!')
                win_flag = True
            if (self.__gameBoard['UR'] == self.__gameBoard['MM'] == self.__gameBoard['LL']) and self.__gameBoard['UR'] != '' and self.__gameBoard['MM'] != '' and self.__gameBoard['LL'] != '':
                print(f'{self.__gameBoard["UR"]} You won!')
                win_flag = True

        return win_flag

    def printboard(self):
        print(f'''
    {self.__gameBoard['UL']}|{self.__gameBoard['UM']}|{self.__gameBoard['UR']}
    {self.__gameBoard['ML']}|{self.__gameBoard['MM']}|{self.__gameBoard['MR']}
    {self.__gameBoard['LL']}|{self.__gameBoard['LM']}|{self.__gameBoard['LR']}''')

    @staticmethod
    def printlist():
        print('''
                UL - Upper Left Corner
                UM - Upper Middle Field
                UR - Upper Right Corner
                ML - Middle Left Field
                MM - Middle Middle(center) Field
                MR - Middle Right Field
                LL - Lower Left Corner
                LM - Lower Middle Field
                LR - Lower Right Corner''')
