import copy


class Field:
    EMPTY = 0
    MARU = 1
    BATSU = -1

    def __init__(self):
        self.step = 0
        self.field = []
        for _ in range(0, 9):
            self.field.append(Field.EMPTY)
    
    def get_display_value(self, value):
        if value == Field.MARU:
            return 'O'
        elif value == Field.BATSU:
            return 'X'
        return ' '

    def display(self):
        indent = '   '
        bar = indent + ' --- --- --- ' + indent +  '  --- --- ---'
        print(bar)
        for r in range(0, 3):
            o = indent + '| '
            g = indent + '| '
            for c in range(0, 3):
                i = r * 3 + c
                o += str(self.get_display_value(self.field[i]))
                o += ' | '

                g += str(i)
                g += ' | '
            
            print(o + g)
            print(bar)
        
        print("Press 'x' to exit")

    def input(self, pos, player):
        self.field[pos] = player

    def check_winner(self):
        winner = Field.EMPTY
        for r in range(0, 9, 3):
            if self.field[r] != Field.EMPTY:
                if self.field[r] == self.field[r + 1] == self.field[r + 2]:
                    winner = self.field[r]
        if winner == Field.EMPTY:
            for c in range(0, 3):
                if self.field[c] != Field.EMPTY:
                    if self.field[c] == self.field[c + 3] == self.field[c + 6]:
                        winner = self.field[c]
        if winner == Field.EMPTY:
            if self.field[0] == self.field[4] == self.field[8]:
                winner = self.field[0]
        if winner == Field.EMPTY:
            if self.field[2] == self.field[4] == self.field[6]:
                winner = self.field[2]
        
        print('winner = ' + str(winner))

        return winner
        




if __name__ == '__main__':
    field = Field()
    field.display()

    game_over = False

    player = Field.BATSU
    while not game_over:
        try:
            key = input()
            if key == 'x':
                break
            pos = int(key)
            if 0 <= pos < 9:
                field.input(pos, player)
                field.display()

                winner = field.check_winner()
                if winner != Field.EMPTY:
                    print('winner = ' + str(winner))
                    break
        except:
            field.display()

