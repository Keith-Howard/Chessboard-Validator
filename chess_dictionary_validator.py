def is_valid_chess_board(board):
    rules = {'br': 2, 'bn': 2, 'bb': 2, 'bk': 1, 'bq': 1, 'bp': 8, 'wp': 8, 'wr': 2, 'wn': 2, 'wb': 2, 'wq': 1, 'wk': 1}
    counter = {}
    # counting each piece on the board
    for piece in board.values():
        if piece != ' ':
            counter.setdefault(piece, 0)
            counter[piece] += 1

    # return false if there are to many pieces on the board, otherwise return true
    for piece in counter.items():
        piece_key = piece[0]
        piece_count = piece[1]
        piece_limit = rules[piece_key]
        if piece_count > piece_limit:
            print('too many ' + piece_key)
            return False
    return True

# use cases
# 1. less than or equal to full amount of pieces returns True
# 2. more than the correct amount of pieces returns False


def is_valid_chess_board2(board):
    rules = {'br': 2, 'bn': 2, 'bb': 2, 'bk': 1, 'bq': 1, 'bp': 8, 'wp': 8, 'wr': 2, 'wn': 2, 'wb': 2, 'wq': 1, 'wk': 1}
    # returns false if to many pieces on the board, otherwise return true
    for piece in board.values():
        if piece in rules.keys():
            rules[piece] -= 1
            if rules[piece] < 0:
                print("too many " + piece + "'s")
                return False
    return True


chess_board = {'a8': 'br', 'b8': 'bn', 'c8': 'bb', 'd8': 'bk', 'e8': 'bq', 'f8': 'bb', 'g8': 'bn', 'h8': 'br',
               'a7': 'bp', 'b7': 'bp', 'c7': 'bp', 'd7': 'bp', 'e7': 'bp', 'f7': 'bp', 'g7': 'bp', 'h7': 'bp',
               'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
               'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
               'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
               'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
               'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp', 'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp',
               'a1': 'wr', 'b1': 'wn', 'c1': 'wb', 'd1': 'wq', 'e1': 'wk', 'f1': 'wb', 'g1': 'wn', 'h1': 'wr'}

print(is_valid_chess_board(chess_board))
print(is_valid_chess_board2(chess_board))
