#!/usr/bin/python

from string import ascii_lowercase

class Board:

    board = [['-' for x in range(8)] for y in range(8)]
    winner = ''
    playerMoves = []
    compMoves = []

    def printBoard(self):

        print ' ',
        for i in range(8):

            print i + 1,

        print ''
        i = ord('A')
        for y in self.board:

            print chr(i),
            i += 1
            for x in y:

                print x,

            print ''

    def update(self, move, player):

        move = list(move)
        if len(move) > 2:

            print "Invalid move"
            return False

        y = ord(move[0]) - ord('A') 
        x = int(move[1]) - 1

        if player:

            try:

                if self.board[y][x] == '-':

                    self.board[y][x] = 'O'
                    self.playerMoves.append([x,y])
                    return True

                else:

                    print "Already taken"
                    return False

            except Exception:

                print "Invalid move"
                return False

        else:

            self.board[y][x] = 'X'
            self.compMoves.append([x,y])

    def checkBoard(self):

        x = sorted(self.playerMoves, key=lambda tup:tup[0])
        for move in x:

            check = move[0]
            y = move[1]
            if [check + 1, y] in x and [check + 2, y] in x and [check + 3, y] in x:

                self.winner = 1 
                return True

        y = sorted(self.playerMoves, key=lambda tup:tup[1])
        for move in y:

            check = move[1]
            x = move[0]
            if [x, check + 1] in y and [x, check + 2] in y and [x, check + 3] in y:

                self.winner = 1 
                return True

        x = sorted(self.compMoves, key=lambda tup:tup[0])
        for move in x:

            check = move[0]
            y = move[1]
            if [check + 1, y] in x and [check + 2, y] in x and [check + 3, y] in x:

                self.winner = 0 
                return True

        y = sorted(self.compMoves, key=lambda tup:tup[1])
        for move in y:

            chekc = move[1]
            x = move[0]
            if [x, check + 1] in y and [x, check + 2] in y and [x, check + 3] in y:

                self.winner = 0 
                return True

        return False

def main():

    choice = raw_input("Would you like to go first? (y/n): ")
    time = raw_input("How long should the computer think about its moves (in seconds)?: ")

    b = Board()
    b.printBoard()
    player = False

    if choice.upper() == 'Y':
        player = True

    while(not b.checkBoard()):

        if player:
            valid = False

            while (not valid):

                move = raw_input("Choose your next move: ")
                print ''
                valid = b.update(move.upper(), player)

            b.printBoard()
            player = False

        else:

            # computer's move
            # move = alphaBeta()
            # b.update(move, player)
            # b.printBoard()
            player = True

    if b.winner:

        print "You win!"

    else:

        print "Computer wins!"

    print "Game over!"

if __name__ == '__main__':

    main()
