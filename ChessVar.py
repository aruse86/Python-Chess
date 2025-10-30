# Author: Aaron Ruse
# GitHub username: aruse86
# Date: 12/10/2023
# Description: This program allows two users to play a variant of Chess. All the rules for normal Chess are followed
#              except for a change to winning the game. Instead of capturing the King to win the game, now the first
#              player to capture all of an opponent's pieces of one type wins the game. Example: capture all the
#              knights (two pieces), capture all the pawns (eight pieces), capture the queen (one piece), etc. Either
#              of these scenarios wins the game. Finally, the king is not special, so there is no check or checkmate.

class ChessVar:
    """This creates a chess game object that allows two players to play each other in a variant version of chess as
       described in the program description above."""

    def __init__(self):
        """Initializes data members of the Chess game object."""

        self._square_locations = {'a1': 'WR1', 'b1': 'WN1', 'c1': 'WB1', 'd1': 'WQ1', 'e1': 'WK1', 'f1': 'WB2', 'g1': 'WN2', 'h1': 'WR2',
                                  'a2': 'WP1', 'b2': 'WP2', 'c2': 'WP3', 'd2': 'WP4', 'e2': 'WP5', 'f2': 'WP6', 'g2': 'WP7', 'h2': 'WP8',
                                  'a3': '---', 'b3': '---', 'c3': '---', 'd3': '---', 'e3': '---', 'f3': '---', 'g3': '---', 'h3': '---',
                                  'a4': '---', 'b4': '---', 'c4': '---', 'd4': '---', 'e4': '---', 'f4': '---', 'g4': '---', 'h4': '---',
                                  'a5': '---', 'b5': '---', 'c5': '---', 'd5': '---', 'e5': '---', 'f5': '---', 'g5': '---', 'h5': '---',
                                  'a6': '---', 'b6': '---', 'c6': '---', 'd6': '---', 'e6': '---', 'f6': '---', 'g6': '---', 'h6': '---',
                                  'a7': 'BP8', 'b7': 'BP7', 'c7': 'BP6', 'd7': 'BP5', 'e7': 'BP4', 'f7': 'BP3', 'g7': 'BP2', 'h7': 'BP1',
                                  'a8': 'BR2', 'b8': 'BN2', 'c8': 'BB2', 'd8': 'BQ1', 'e8': 'BK1', 'f8': 'BB1', 'g8': 'BN1', 'h8': 'BR1'}

        # self._square_locations = {'a1': '---', 'b1': '---', 'c1': '---', 'd1': '---', 'e1': '---', 'f1': '---', 'g1': '---', 'h1': '---',
        #                           'a2': '---', 'b2': '---', 'c2': '---', 'd2': '---', 'e2': '---', 'f2': '---', 'g2': '---', 'h2': '---',
        #                           'a3': '---', 'b3': '---', 'c3': '---', 'd3': '---', 'e3': '---', 'f3': '---', 'g3': '---', 'h3': '---',
        #                           'a4': '---', 'b4': '---', 'c4': '---', 'd4': 'WQ1', 'e4': '---', 'f4': '---', 'g4': '---', 'h4': '---',
        #                           'a5': '---', 'b5': '---', 'c5': '---', 'd5': '---', 'e5': '---', 'f5': '---', 'g5': '---', 'h5': '---',
        #                           'a6': '---', 'b6': '---', 'c6': '---', 'd6': '---', 'e6': '---', 'f6': '---', 'g6': '---', 'h6': '---',
        #                           'a7': '---', 'b7': '---', 'c7': '---', 'd7': '---', 'e7': '---', 'f7': '---', 'g7': '---', 'h7': '---',
        #                           'a8': '---', 'b8': '---', 'c8': '---', 'd8': '---', 'e8': '---', 'f8': '---', 'g8': '---', 'h8': '---'}

        # Contains the number of moves each piece made and their current position on the board.
        # {'player piece': [# of moves][current board position]}
        self._black_piece_movements = {'BK1': [0, 'd8'], 'BQ1': [0, 'e8'],
                                       'BB1': [0, 'f8'], 'BB2': [0, 'c8'],
                                       'BN1': [0, 'g8'], 'BN2': [0, 'b8'],
                                       'BR1': [0, 'h8'], 'BR2': [0, 'a8'],
                                       'BP1': [0, 'h7'], 'BP2': [0, 'g7'],
                                       'BP3': [0, 'f7'], 'BP4': [0, 'e7'],
                                       'BP5': [0, 'd7'], 'BP6': [0, 'c7'],
                                       'BP7': [0, 'b7'], 'BP8': [0, 'a7']}

        self._white_piece_movements = {'WK1': [0, 'd1'], 'WQ1': [0, 'e1'],
                                       'WB1': [0, 'c1'], 'WB2': [0, 'f1'],
                                       'WN1': [0, 'b1'], 'WN2': [0, 'g1'],
                                       'WR1': [0, 'a1'], 'WR2': [0, 'h1'],
                                       'WP1': [0, 'a2'], 'WP2': [0, 'b2'],
                                       'WP3': [0, 'c2'], 'WP4': [0, 'd2'],
                                       'WP5': [0, 'e2'], 'WP6': [0, 'f2'],
                                       'WP7': [0, 'g2'], 'WP8': [0, 'h8']}

        # self._chess_board contains the current board position of every piece, it is regularly updated throughout
        # the game.
        self._chess_board = [[self._square_locations['a1'], self._square_locations['b1'], self._square_locations['c1'],
                              self._square_locations['d1'], self._square_locations['e1'], self._square_locations['f1'],
                              self._square_locations['g1'], self._square_locations['h1']],
                             [self._square_locations['a2'], self._square_locations['b2'], self._square_locations['c2'],
                              self._square_locations['d2'], self._square_locations['e2'], self._square_locations['f2'],
                              self._square_locations['g2'], self._square_locations['h2']],
                             [self._square_locations['a3'], self._square_locations['b3'], self._square_locations['c3'],
                              self._square_locations['d3'], self._square_locations['e3'], self._square_locations['f3'],
                              self._square_locations['g3'], self._square_locations['h3']],
                             [self._square_locations['a4'], self._square_locations['b4'], self._square_locations['c4'],
                              self._square_locations['d4'], self._square_locations['e4'], self._square_locations['f4'],
                              self._square_locations['g4'], self._square_locations['h4']],
                             [self._square_locations['a5'], self._square_locations['b5'], self._square_locations['c5'],
                              self._square_locations['d5'], self._square_locations['e5'], self._square_locations['f5'],
                              self._square_locations['g5'], self._square_locations['h5']],
                             [self._square_locations['a6'], self._square_locations['b6'], self._square_locations['c6'],
                              self._square_locations['d6'], self._square_locations['e6'], self._square_locations['f6'],
                              self._square_locations['g6'], self._square_locations['h6']],
                             [self._square_locations['a7'], self._square_locations['b7'], self._square_locations['c7'],
                              self._square_locations['d7'], self._square_locations['e7'], self._square_locations['f7'],
                              self._square_locations['g7'], self._square_locations['h7']],
                             [self._square_locations['a8'], self._square_locations['b8'], self._square_locations['c8'],
                              self._square_locations['d8'], self._square_locations['e8'], self._square_locations['f8'],
                              self._square_locations['g8'], self._square_locations['h8']]]
        # These two keep track of the remaining board pieces each player has. If any element reaches 0, the game is over.
        self._black_pieces_remaining = [1, 1, 2, 2, 2, 8]  # King, Queen, Bishop, Knight, Rook, Pawn
        self._white_pieces_remaining = [1, 1, 2, 2, 2, 8]  # King, Queen, Bishop, Knight, Rook, Pawn

        self._letter_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self._number_letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

        # White goes first, this keeps track of who's turn it is. Changes to 'BLACK' when it is black's turn.
        self._player_turn = 'WHITE'

        self._current_game_state = 'UNFINISHED'  # Initialize the current game state to unfinished

    def show_chess_board(self):
        """Prints out the current state of the chess board, a --- in a spot indicates that that spot is not occupied by a
           game piece."""

        print('\nThe current state of the game is shown below:\n')

        for row_index in reversed(range(10)):  # prints row 8 (black side) as the top row and row 1 (white side)
            # as the bottom row. Column 'a' is on the left and column 'h' on the right.
            if row_index == 0 or row_index == 9:
                print(f'    a    b    c    d    e    f    g    h')
            else:
                for col_index in range(10):
                    if col_index == 0:
                        print(f'{row_index} ', end='')
                    elif col_index == 9:
                        print(f'  {row_index}')
                    else:
                        print(f' {self._chess_board[row_index - 1][col_index - 1]}', end=" ")
        print('')

    def get_player_turn(self):
        """Returns White or Black, depending on which players turn it is."""
        return self._player_turn

    def get_game_state(self):
        """Returns UNFINISHED, WHITE WON, or BLACK WON, depending on the current state of the game."""
        return self._current_game_state

    def make_move(self, moved_from, moved_to):
        """Returns False if the square being moved does not contain the current player's piece, the requested move is
         illegal, or if the gams has already been won. Otherwise, it makes the requested move for the current player,
         removes any captured piece, updates the game state, updates whose turn it is, and returns True."""

        if self.is_move_legal(moved_from, moved_to) is False:
            return False
        elif self.is_move_legal(moved_from, moved_to) is True:
            if self._square_locations[moved_from][0] == 'W':
                self._white_piece_movements[self._square_locations[moved_from]][0] += 1  # updates number of moves counter for a chess piece self._white_piece_movements
                self._white_piece_movements[self._square_locations[moved_from]][1] = moved_to  # updates the current location of the chess piece self._white_piece_movements
                self._player_turn = 'BLACK'  # update the next turn's player to 'BLACK'
                if self._square_locations[moved_to][0] == 'B':
                    if self._square_locations[moved_to][1] == 'K':
                        self._black_pieces_remaining[0] -= 1
                    elif self._square_locations[moved_to][1] == 'Q':
                        self._black_pieces_remaining[1] -= 1
                    elif self._square_locations[moved_to][1] == 'B':
                        self._black_pieces_remaining[2] -= 1
                    elif self._square_locations[moved_to][1] == 'N':
                        self._black_pieces_remaining[3] -= 1
                    elif self._square_locations[moved_to][1] == 'R':
                        self._black_pieces_remaining[4] -= 1
                    elif self._square_locations[moved_to][1] == 'P':
                        self._black_pieces_remaining[5] -= 1

                    if 0 in self._black_pieces_remaining:
                        self._current_game_state = "WHITE_WON"
            elif self._square_locations[moved_from][0] == 'B':
                self._black_piece_movements[self._square_locations[moved_from]][0] += 1  # updates number of moves counter for a chess piece in self._black_piece_movements
                self._black_piece_movements[self._square_locations[moved_from]][1] = moved_to  # updates the current location of the chess piece in self._black_piece_movements
                self._player_turn = 'WHITE'  # update the next turn's player to 'WHITE'
                if self._square_locations[moved_to][0] == 'W':
                    if self._square_locations[moved_to][1] == 'K':
                        self._white_pieces_remaining[0] -= 1
                    elif self._square_locations[moved_to][1] == 'Q':
                        self._white_pieces_remaining[1] -= 1
                    elif self._square_locations[moved_to][1] == 'B':
                        self._white_pieces_remaining[2] -= 1
                    elif self._square_locations[moved_to][1] == 'N':
                        self._white_pieces_remaining[3] -= 1
                    elif self._square_locations[moved_to][1] == 'R':
                        self._white_pieces_remaining[4] -= 1
                    elif self._square_locations[moved_to][1] == 'P':
                        self._white_pieces_remaining[5] -= 1

                    if 0 in self._white_pieces_remaining:
                        self._current_game_state = "BLACK_WON"

            self._square_locations[moved_to] = self._square_locations[moved_from]  # assigns chess piece to the new location in self._square_locations
            self._square_locations[moved_from] = '---'  # marks the moved_from square as empty in self._square_locations
            self.update_chess_board()  # self._chess_board updates with the new location of every piece using self._square_locations
            return True

    def update_chess_board(self):
        """Updates the chess board list after a move."""
        self._chess_board = [[self._square_locations['a1'], self._square_locations['b1'], self._square_locations['c1'],
                              self._square_locations['d1'], self._square_locations['e1'], self._square_locations['f1'],
                              self._square_locations['g1'], self._square_locations['h1']],
                             [self._square_locations['a2'], self._square_locations['b2'], self._square_locations['c2'],
                              self._square_locations['d2'], self._square_locations['e2'], self._square_locations['f2'],
                              self._square_locations['g2'], self._square_locations['h2']],
                             [self._square_locations['a3'], self._square_locations['b3'], self._square_locations['c3'],
                              self._square_locations['d3'], self._square_locations['e3'], self._square_locations['f3'],
                              self._square_locations['g3'], self._square_locations['h3']],
                             [self._square_locations['a4'], self._square_locations['b4'], self._square_locations['c4'],
                              self._square_locations['d4'], self._square_locations['e4'], self._square_locations['f4'],
                              self._square_locations['g4'], self._square_locations['h4']],
                             [self._square_locations['a5'], self._square_locations['b5'], self._square_locations['c5'],
                              self._square_locations['d5'], self._square_locations['e5'], self._square_locations['f5'],
                              self._square_locations['g5'], self._square_locations['h5']],
                             [self._square_locations['a6'], self._square_locations['b6'], self._square_locations['c6'],
                              self._square_locations['d6'], self._square_locations['e6'], self._square_locations['f6'],
                              self._square_locations['g6'], self._square_locations['h6']],
                             [self._square_locations['a7'], self._square_locations['b7'], self._square_locations['c7'],
                              self._square_locations['d7'], self._square_locations['e7'], self._square_locations['f7'],
                              self._square_locations['g7'], self._square_locations['h7']],
                             [self._square_locations['a8'], self._square_locations['b8'], self._square_locations['c8'],
                              self._square_locations['d8'], self._square_locations['e8'], self._square_locations['f8'],
                              self._square_locations['g8'], self._square_locations['h8']]]

    def is_move_legal(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        if self.get_game_state() == 'BLACK_WON' or self.get_game_state() == 'WHITE_WON':
            return False  # returns False if game is won by black or white
        elif self._square_locations[moved_from][0] != self.get_player_turn()[0]:  # matches first character in dictionary strings
            return False  # returns False if the current player does not have a chess piece located at the moved_from location.
        elif int(moved_to[1]) < 1 or int(moved_to[1]) > 8:  # checks if move takes the chess piece off the bottom or top of the board
            return False
        elif moved_to[0] < 'a' or moved_to[0] > 'h':   # checks if move takes the chess piece off the sides of the board
            return False
        elif self._square_locations[moved_to][0] == self.get_player_turn()[0]:
            return False  # player cannot capture their own piece
        elif self._square_locations[moved_from] == self._square_locations[moved_to]:
            return False  # player piece cannot move to its original destination.

        # Determines what type of chess piece is at the moved_from location.
        if self._square_locations[moved_from][1] == 'P':
            return self.check_pawn_move(moved_from, moved_to)
        elif self._square_locations[moved_from][1] == 'N':
            return self.check_knight_move(moved_from, moved_to)
        elif self._square_locations[moved_from][1] == 'B':
            return self.check_bishop_move(moved_from, moved_to)
        elif self._square_locations[moved_from][1] == 'R':
            return self.check_rook_move(moved_from, moved_to)
        elif self._square_locations[moved_from][1] == 'Q':
            return self.check_queen_move(moved_from, moved_to)
        elif self._square_locations[moved_from][1] == 'K':
            return self.check_king_move(moved_from, moved_to)

    def check_pawn_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if side_squares_away > 1:
            return False  # pawn can not move more than one adjacent column.
        elif num_squares_away > 2:
            return False  # pawn can not move more than two squares forward.
        elif side_squares_away == 0:
            if self._square_locations[moved_to] != '---':
                return False  # pawn can't move to a non-empty square unless it is capturing diagonally

        if self._square_locations[moved_from][0] == 'W':
            if int(moved_from[1]) >= int(moved_to[1]):
                return False  # pawn cannot move to the side or back.

            if num_squares_away == 2:
                if side_squares_away > 0:
                    return False  # pawn cannot move to an adjacent row if it is moving two squares forward.
                elif self._white_piece_movements[self._square_locations[moved_from]][0] != 0:
                    return False  # pawn cannot be moved two spaces forward after it's first move.
                else:
                    spot_before = int(moved_to[1]) - 1
                    spot_before = moved_to[0] + str(spot_before)
                    if self._square_locations[spot_before] != '---':
                        return False  # pawn can't move two spaces ahead if there is a non-empty square one space ahead.
            elif num_squares_away == 1 and side_squares_away == 1:
                if self._square_locations[moved_to][0] != 'B':
                    return False
        elif self._square_locations[moved_from][0] == 'B':
            if int(moved_from[1]) <= int(moved_to[1]):
                return False  # pawn cannot move to the side or back.

            if num_squares_away == 2:
                if side_squares_away > 0:
                    return False  # pawn cannot move to an adjacent row if it is moving two squares forward.
                elif self._black_piece_movements[self._square_locations[moved_from]][0] != 0:
                    return False  # pawn cannot be moved two spaces forward after it's first move.
                else:
                    spot_before = int(moved_to[1]) + 1
                    spot_before = moved_to[0] + str(spot_before)
                    if self._square_locations[spot_before] != '---':
                        return False  # pawn can't move two spaces ahead if there is a non-empty square one space ahead.
            elif num_squares_away == 1 and side_squares_away == 1:
                if self._square_locations[moved_to][0] != 'W':
                    return False  # pawn cannot move diagonal one square if there is not an opposing players piece located there.
        return True

    def check_knight_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if num_squares_away >= 3 or side_squares_away >= 3:
            return False  # knight cannot move more than 2 squares in a perpendicular direction away
        elif num_squares_away == 1 and side_squares_away == 1:
            return False  # knight cannot move one square diagonal
        elif num_squares_away == 0 or side_squares_away == 0:
            return False  # knight cannot move to the same row or column
        elif num_squares_away == 2 and side_squares_away == 2:
            return False  # knight cannot go two squares in one direction and another two squares perpendicular.
        else:
            return True

    def check_bishop_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if num_squares_away == 0 or side_squares_away == 0:
            return False  # the bishop cannot move only vertical or only horizontal.
        elif num_squares_away != side_squares_away:
            return False  # the bishop can only move on a diagonal.

        if int(moved_to[1]) - int(moved_from[1]) > 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 0:
            # indicates a move that is up and right
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col += 1
                current_row += 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # bishop can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) > 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < 0:
            # indicates a move that is up and left
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col -= 1
                current_row += 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # bishop can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) < 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < 0:
            # indicates a move that is down and left
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col -= 1
                current_row -= 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # bishop can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) < 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 0:
            # indicates a move that is down and right
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col += 1
                current_row -= 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # bishop can't move to final destination if there is a non-empty square one diagonal before.
        return True

    def check_rook_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if num_squares_away != 0 and side_squares_away != 0:
            return False  # the rook can only move through a col or row, so one of these variable must = 0.
        elif num_squares_away == 0:
            square_num = self._letter_numbers[moved_from[0]]
            for square in range(side_squares_away - 1):
                if self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 1:
                    square_num += 1
                    if self._square_locations[self._number_letters[square_num] + moved_from[1]] != '---':
                        return False  # rook can't move to final destination if there is a non-empty square one space ahead.
                elif self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < -1:
                    square_num -= 1
                    if self._square_locations[self._number_letters[square_num] + moved_from[1]] != '---':
                        return False  # rook can't move to final destination if there is a non-empty square one space ahead.
        elif side_squares_away == 0:
            square_num = int(moved_from[1])
            for square in range(num_squares_away - 1):
                if int(moved_to[1]) - int(moved_from[1]) > 1:
                    square_num += 1
                    if self._square_locations[moved_to[0] + str(square_num)] != '---':
                        return False  # rook can't move to final destination if there is a non-empty square one space ahead.
                elif int(moved_to[1]) - int(moved_from[1]) < -1:
                    square_num -= 1
                    if self._square_locations[moved_to[0] + str(square_num)] != '---':
                        return False  # rook can't move to final destination if there is a non-empty square one space ahead.
        return True

    def check_queen_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if num_squares_away != side_squares_away:
            if num_squares_away != 0 and side_squares_away != 0:
                return False  # the queen must move only vertical or only horizontal if it is not moving diagonally.
            elif num_squares_away == 0:
                square_num = self._letter_numbers[moved_from[0]]
                for square in range(side_squares_away - 1):
                    if self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 1:
                        square_num += 1
                        if self._square_locations[self._number_letters[square_num] + moved_from[1]] != '---':
                            return False  # queen can't move to final destination if there is a non-empty square one space ahead.
                    elif self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < -1:
                        square_num -= 1
                        if self._square_locations[self._number_letters[square_num] + moved_from[1]] != '---':
                            return False  # queen can't move to final destination if there is a non-empty square one space ahead.
            elif side_squares_away == 0:
                square_num = int(moved_from[1])
                for square in range(num_squares_away - 1):
                    if int(moved_to[1]) - int(moved_from[1]) > 1:
                        square_num += 1
                        if self._square_locations[moved_to[0] + str(square_num)] != '---':
                            return False  # queen can't move to final destination if there is a non-empty square one space ahead.
                    elif int(moved_to[1]) - int(moved_from[1]) < -1:
                        square_num -= 1
                        if self._square_locations[moved_to[0] + str(square_num)] != '---':
                            return False  # queen can't move to final destination if there is a non-empty square one space ahead.
        elif int(moved_to[1]) - int(moved_from[1]) > 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 0:
            # indicates a move that is up and right
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col += 1
                current_row += 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # queen can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) > 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < 0:
            # indicates a move that is up and left
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col -= 1
                current_row += 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # queen can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) < 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] < 0:
            # indicates a move that is down and left
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col -= 1
                current_row -= 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # queen can't move to final destination if there is a non-empty square one diagonal before.
        elif int(moved_to[1]) - int(moved_from[1]) < 0 and self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]] > 0:
            # indicates a move that is down and right
            current_col = self._letter_numbers[moved_from[0]]
            current_row = int(moved_from[1])
            for square in range(num_squares_away - 1):
                current_col += 1
                current_row -= 1
                if self._square_locations[self._number_letters[current_col] + str(current_row)] != '---':
                    return False  # queen can't move to final destination if there is a non-empty square one diagonal before.
        return True

    def check_king_move(self, moved_from, moved_to):
        """Calculates if the requested move is legal or not. If it is legal, returns True. Otherwise, returns False."""
        num_squares_away = abs(int(moved_to[1]) - int(moved_from[1]))
        side_squares_away = abs(self._letter_numbers[moved_to[0]] - self._letter_numbers[moved_from[0]])

        if num_squares_away > 1 or side_squares_away > 1:
            return False  # king can't move more than one square at a time
        return True


# def main():
#     """Calls the ChessVar class to start a game."""
    # print('This game is a variation on classical chess. All the rules for classical Chess apply except the following:')
    # print("Instead of capturing the King to win the game, the first player to capture all of an opponent's pieces of one")
    # print('type wins the game. Example: capture all the knights (two pieces), capture all the pawns (eight pieces),')
    # print('capture the queen (one piece), etc. Either of these scenarios wins the game. Finally, the king is not special,')
    # print('so there is no check or checkmate.')
    #
    # play_game = input('Ready to start? (y or n) ').lower()
    #
    # while play_game == 'y':
    #     game = ChessVar()
    #     print('\nFirst letter indicates chess piece color: B = Black, W = White')
    #     print('Second letter indicates the type of chess piece: K = King, Q = Queen, B = Bishop, N = Knight, R = Rook, P = Pawn')
    #     print('Number indicates the number of the chess piece')
    #     print('An empty square is indicated by ---')
    #     print('Example: BN2 = Black Knight # 2')
    #     game.show_chess_board()
    #
    #     while game.get_game_state() == 'UNFINISHED':
    #         print(f"It is {game.get_player_turn()}'s turn:")
    #         start_square = input('Enter what square you want to move from: ')
    #         end_square = input('Enter what square you want to move to: ')
    #         move = game.make_move(start_square, end_square)
    #         print('Move Result:', move)
    #
    #         while move is False:
    #             print('That move is not allowed. Please try again.')
    #             start_square = input('Enter what square you want to move from: ')
    #             end_square = input('Enter what square you want to move to: ')
    #             move = game.make_move(start_square, end_square)
    #             print('Move Result:', move)
    #
    #         game.show_chess_board()
    #         print(f'White Pieces Remaining: {game._white_pieces_remaining}')
    #         print(f'Black Pieces Remaining: {game._black_pieces_remaining}')
    #         print(f'Current Game State: {game.get_game_state()}\n')
    #         print('-----------------------------------------------------------------------------------------------------')
    #
    #     play_game = input('Play another game? (y or n) ').lower()

    # if __name__ == '__main__':
#     main()
