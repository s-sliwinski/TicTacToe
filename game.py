import random


class Game:

    def __init__(self, gamemode=None, fpawn=None, spawn=None):
        self.__gameBoard = {'UL': ['', (83, 62)], 'UM': ['', (282, 62)], 'UR': ['', (479, 62)],
                            'ML': ['', (83, 237)],'MM': ['', (282, 237)], 'MR': ['', (479, 237)],
                            'LL': ['', (83, 412)], 'LM': ['', (282, 412)], 'LR': ['', (479, 412)]}
        self.__game_mode = gamemode
        self.__f_player_pawn = fpawn
        self.__s_player_pawn = spawn
        self.__move_counter = 0
        self.__max_number_of_moves = 9
        print(f'Selected {self.__game_mode} mode first player pawn is {self.__f_player_pawn}')

    def set_game_mode(self, gamemode):
        self.__game_mode = gamemode

    def set_game_board_field_pawn(self, index, pawn):
        self.__gameBoard[index][0] = pawn

    def get_game_mode(self):
        return self.__game_mode

    def get_move_counter(self):
        return self.__move_counter

    def get_game_board(self):
        return self.__gameBoard

    def get_game_board_keys(self):
        lst = list(self.__gameBoard.keys())
        return lst

    def get_game_board_field(self, index):
        return self.__gameBoard[index]

    def get_game_board_field_pawn(self, index):
        return self.__gameBoard[index][0]

    def get_game_board_field_pos(self, index):
        return self.__gameBoard[index][1]

    def bot_moves(self):
        while True:
            place = random.choice(list(self.__gameBoard))
            if self.__check_if_field_available(place):
                self.write_to_board(place)
                break

    def __check_if_field_available(self, index):
        check_flag = False
        if self.get_game_board_field_pawn(index) == '':
            check_flag = True
        return check_flag

    def write_to_board(self, command):
            write_flag = False
            # decoding command
            place = command[0] + command[1]
            if self.__check_if_field_available(place):
                if not self.__move_counter % 2:
                    self.set_game_board_field_pawn(place, self.__f_player_pawn)
                    write_flag = True
                    self.__move_counter += 1
                else:
                    self.set_game_board_field_pawn(place, self.__s_player_pawn)
                    write_flag = True
                    self.__move_counter += 1
            else:
                print('Field taken select other one!')

            return write_flag

    def check_win_conditions(self):
            win_flag = False
            #check rows
            if (self.__gameBoard['UL'][0] == self.__gameBoard['UM'][0] == self.__gameBoard['UR'][0]) and self.__gameBoard['UL'][0] != '':
                print(f"{self.__gameBoard['UL']} You won!")
                win_flag = True
                return win_flag
            elif (self.__gameBoard['ML'][0] == self.__gameBoard['MM'][0] == self.__gameBoard['MR'][0]) and self.__gameBoard['ML'][0] != '':
                print(f"{self.__gameBoard['ML']} You won!")
                win_flag = True
                return win_flag
            elif (self.__gameBoard['LL'][0] == self.__gameBoard['LM'][0] == self.__gameBoard['LR'][0]) and self.__gameBoard['LL'][0] != '':
                print(f"{self.__gameBoard['LL']} You won!")
                win_flag = True
                return win_flag
            #chcek columns
            elif (self.__gameBoard['UL'][0] == self.__gameBoard['ML'][0] == self.__gameBoard['LL'][0]) and self.__gameBoard['UL'][0] != '':
                print(f"{self.__gameBoard['UL']} You won!")
                win_flag = True
                return win_flag
            elif (self.__gameBoard['UM'][0] == self.__gameBoard['MM'][0] == self.__gameBoard['LM'][0]) and self.__gameBoard['UM'][0] != '':
                print(f"{self.__gameBoard['UM']} You won!")
                win_flag = True
                return win_flag
            elif (self.__gameBoard['UR'][0] == self.__gameBoard['MR'][0] == self.__gameBoard['LR'][0]) and self.__gameBoard['UR'][0] != '':
                print(f"{self.__gameBoard['UR']} You won!")
                win_flag = True
                return win_flag
            #check diagonals
            if not win_flag:
                if (self.__gameBoard['UL'][0] == self.__gameBoard['MM'][0] == self.__gameBoard['LR'][0]) and self.__gameBoard['UL'][0] != '':
                    print(f'{self.__gameBoard["UL"]} You won!')
                    win_flag = True
                    return win_flag
                if (self.__gameBoard['UR'][0] == self.__gameBoard['MM'][0] == self.__gameBoard['LL'][0]) and self.__gameBoard['UR'][0] != '':
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
    {self.__gameBoard['UL'][0]}|{self.__gameBoard['UM'][0]}|{self.__gameBoard['UR'][0]}
    {self.__gameBoard['ML'][0]}|{self.__gameBoard['MM'][0]}|{self.__gameBoard['MR'][0]}
    {self.__gameBoard['LL'][0]}|{self.__gameBoard['LM'][0]}|{self.__gameBoard['LR'][0]}''')

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


