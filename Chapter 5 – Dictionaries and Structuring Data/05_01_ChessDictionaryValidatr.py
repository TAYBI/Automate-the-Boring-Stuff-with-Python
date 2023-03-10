# #!python3
# def isValidChessBoard(board):
#       """Validate counts and location of pieces on board"""

#       # Define pieces and colors
#       pieces = ['king','queen','rook', 'knight','bishop', 'pawn']
#       colors = ['b', 'w']
#       # Set of all chess pieces
#       all_pieces = set(color+piece for piece in pieces for color in colors)

#       # Define valid range for count of chess pieces by type (low, high) tuples
#       valid_counts = {'king': (1, 1),
#                   'queen': (0, 1),
#                   'rook': (0, 2),
#                   'bishop': (0, 2),
#                   'knight': (0, 2),
#                   'pawn': (0, 8)}

#       # Get count of pieces on the board
#       piece_cnt = {}
#       for v in board.values():
#         if v in all_pieces:
#           piece_cnt.setdefault(v, 0)
#           piece_cnt[v] += 1

#       # Check if there are a valid number of pieces
#       for piece in all_pieces:
#         cnt = piece_cnt.get(piece, 0)
#         lo, hi = valid_counts[piece[1:]]
#         if not lo <= cnt <= hi:   # Count needs to be between lo and hi
#           if lo != hi:
#             print(f"There should between {lo} and {hi} {piece} but there are {cnt}")
#           else:
#             print(f"There should be {lo} {piece} but there are {cnt})")
#           return False

#       # Check if locations are valid
#       for location in board.keys():
#         row = int(location[:1])
#         column = location[1:]
#         if not ((1 <= row <= 8) and ('a' <= column <= "h")):
#           print(f"Invaid to have {board[location]} at postion {location}")
#           return False

#       # Check if all pieces have valid names
#       for loc, piece in board.items():
#         if piece:
#           if not piece in all_pieces:
#             print(f"{piece} is not a valid chess piece at postion {loc}")
#             return False

#       return True


# fboard = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
# '5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
# '1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
# '5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
# '1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
# '5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
# '1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
# '5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
# '1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
# '1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
# '1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}


# print(isValidChessBoard(fboard))

# X
# spam = {
#     'cat': 42
# }


# print('cat' in spam.keys())

# spam.setdefault('color', 'black')

# print(spam)


# import pprint
# X


# Pretty Printing
import pprint

# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# count = {}

# for charactere in message:
#     count.setdefault(charactere, 0)
#     count[charactere] = count[charactere] + 1

# pprint.pprint(count)


# Nested Dictionaries and Lists

allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


def totalBrought(guests, item):
    numBrought = 0
    # print(guests.items())
    for k, v in guests.items():
        numBrought += v.get(item, 0)

    return numBrought


# totalBrought(allGuests, 'apples')


# creatin a list of all the Items that the gesses brought
allItemsBrought = []
for v in allGuests.values():
    for item in v:
        if item not in allItemsBrought:
            allItemsBrought.append(item)


# printing theme out

print("Number of things being brought:")
for gift in allItemsBrought:
    print(" - ", gift, " " + str(totalBrought(allGuests, gift)))
