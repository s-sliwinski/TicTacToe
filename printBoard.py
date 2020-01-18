import game


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


def printboard():
    print(f'''
{game.gameBoard['UL']}|{game.gameBoard['UM']}|{game.gameBoard['UR']}
{game.gameBoard['ML']}|{game.gameBoard['MM']}|{game.gameBoard['MR']}
{game.gameBoard['LL']}|{game.gameBoard['LM']}|{game.gameBoard['LR']}''')


