#!/usr/bin/python

import random

class Game:
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

            check = move[1]
            x = move[0]
            if [x, check + 1] in y and [x, check + 2] in y and [x, check + 3] in y:

                self.winner = 0
                return True

        return False

    def available_moves(self):
        """what spots are left empty?"""
        list = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is '-':
                    list.append([i, j])
        for i in range(len(list)):
            if i == 0:
                list[i][0] = 'A'
            elif i == 1:
                list[i][0] = 'B'
            elif i == 2:
                list[i][0] = 'C'
            elif i == 3:
                list[i][0] = 'D'
            elif i == 4:
                list[i][0] = 'E'
            elif i == 5:
                list[i][0] = 'F'
            elif i == 6:
                list[i][0] = 'G'
            elif i == 7:
                list[i][0] = 'H'
        return list

    def get_squares_for(self, symbol):
        list = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is symbol:
                    list.append([i, j])
        return list

    def complete(self):
        list = self.available_moves()
        if not list or self.checkBoard():
            return True
        return False

    def update(self, move, player):
        move = list(move)
        y = ord(move[0]) - ord('A')
        x = int(move[1]) - 1
        if player is 'O':
            if self.board[y][x] == '-':
                self.board[y][x] = 'O'
                return True
        elif player is 'X':
            if self.board[y][x] == '-':
                self.board[y][x] = 'X'
                return True
        elif player is '-':
            self.board[y][x] = '-'

    # move
    '''
    def update(self, move, player):

        move = list(move)
        if len(move) > 2:

            print "Invalid move"
            return False

        y = ord(move[0]) - ord('A')
        x = int(move[1]) - 1

        if player is 'O':

            try:

                if self.board[y][x] == '-':

                    self.board[y][x] = 'O'
                    #self.playerMoves.append([x,y])
                    return True

                else:

                    print "Already taken"
                    return False

            except Exception:

                print "Invalid move"
                return False

        elif player is 'X':

            self.board[y][x] = 'X'
            #self.compMoves.append([x,y])

        elif player is '-':
            self.board[y][x] = '-'
        '''

    def X_won(self):
        if self.checkBoard():
            if self.winner == 0:
                return True
        return False

    def O_won(self):
        if self.checkBoard():
            if self.winner == 1:
                return True
        return False

    def tied(self):
        if self.complete() and not self.checkBoard():
            if not self.winner:
                return True
        return False

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1
        for move in node.available_moves():
            node.update(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            print val
            node.update(move, '-')
            if player is 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            elif player is 'X':
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player is 'O':
            return alpha
        elif player is 'X':
            return beta


def evaluate(grid, player):
    a = -2
    choices = []
    if len(grid.available_moves()) == 64:
        return 4
    for m in grid.available_moves():
        print m
        grid.update(m, player)
        val = grid.alphabeta(grid, get_enemy(player), -2, 2)
        grid.update(m, None)
        if val > a:
            a = val
            choices = [m]
        elif val == a:
            choices.append(m)
    return random.choice(choices)



def get_enemy(player):
    if player is 'X':
        return 'O'
    return 'X'


if __name__ == "__main__":
    grid = Game()
    grid.printBoard()
    player = 'O'
    while not grid.checkBoard():
        if player is 'O':
            valid = False
            while not valid:
                move = raw_input("Choose next move: ")
                print ''
                grid.update(move.upper(), player)
                valid = True
            grid.printBoard()

        elif player is 'X':
            computer_move = evaluate(grid, player)
            grid.update(computer_move, player)
            grid.printBoard()
        player = get_enemy(player)
    if grid.X_won():
        print "X wins"
    elif grid.O_won():
        print "O wins"
    elif grid.tied():
        print "Tie"
