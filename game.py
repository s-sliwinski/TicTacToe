class Game:

    def __init__(self, gamemode=None, fpawn=None, spawn=None):
        self.__gameBoard = {'UL': '', 'UM': '', 'UR': '', 'ML': '', 'MM': '', 'MR': '', 'LL': '', 'LM': '', 'LR': ''}
        self.__game_mode = gamemode
        self.__f_player_pawn = fpawn
        self.__s_player_pawn = spawn
        self.__move_counter = 0
        self.__max_number_of_moves = 9
        print(f'Selected {self.__game_mode} mode first player pawn is {self.__f_player_pawn}')

    def set_game_mode(self, gamemode):
        self.__game_mode = gamemode

    def get_game_mode(self):
        return self.__game_mode

    def get_game_board(self):
        return self.__gameBoard

    def get_move_counter(self):
        return self.__move_counter

    def get_game_board_field(self, index):
        return self.__gameBoard[index]

    def __check_if_field_available(self, index):
        check_flag = False
        if self.__gameBoard[index] == '':
            check_flag = True
        return check_flag

    def write_to_board(self, command):
            #add zmieniające ruchy raz pl1 raz pl2 na podstawie __move_counter/2!
            write_flag = False
            # decoding command
            place = command[0] + command[1]
            if self.__check_if_field_available(place):
                if not self.__move_counter % 2:
                    self.__gameBoard[place] = self.__f_player_pawn
                    write_flag = True
                    self.__move_counter += 1
                else:
                    self.__gameBoard[place] = self.__s_player_pawn
                    write_flag = True
                    self.__move_counter += 1
            else:
                print('Field taken select other one!')

            return write_flag




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
                        return win_flag
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
                            return win_flag
            #check diagonals
            if not win_flag:
                if (self.__gameBoard['UL'] == self.__gameBoard['MM'] == self.__gameBoard['LR']) and self.__gameBoard['UL'] != '' and self.__gameBoard['MM'] != '' and self.__gameBoard['LR'] != '':
                    print(f'{self.__gameBoard["UL"]} You won!')
                    win_flag = True
                    return win_flag
                if (self.__gameBoard['UR'] == self.__gameBoard['MM'] == self.__gameBoard['LL']) and self.__gameBoard['UR'] != '' and self.__gameBoard['MM'] != '' and self.__gameBoard['LL'] != '':
                    print(f'{self.__gameBoard["UR"]} You won!')
                    win_flag = True
                    return win_flag
            #check if end of moves
            if self.__move_counter == self.__max_number_of_moves:
                print('DRAW!')
                return True
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
