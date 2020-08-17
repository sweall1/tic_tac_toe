board = []
x = 0
while x != 3:
    board.append([" " for i in range(3)])
    x += 1

def print_board():
    for i in board[0:3]:
        print("| {} | {} | {} |".format(i[0], i[1], i[2]))

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    while True:
        choice = input("Your turn player {}! Enter your move (1-9): ".format(number)).strip()
        if choice in "123456789" and choice != "":
            choice = int(choice)
            if choice in [1, 2, 3]:
                if board[0][choice - 1] == " ":
                    board[0][choice - 1] = icon
                    print_board()
                    break
                else:
                    print("That space is already taken!")
                    continue
            elif choice in [4, 5, 6]:
                if board[1][choice - 4] == " ":
                    board[1][choice - 4] = icon
                    print_board()
                    break
                else:
                    print("That space is already taken!")
                    continue
            elif choice in [7, 8, 9]:
                if board[2][choice - 7] == " ":
                    board[2][choice - 7] = icon
                    print_board()
                    break
                else:
                    print("That space is already taken!")
                    continue
            else:
                print("That space does not exist!")
                continue
        else:
            print("That space does not exist!")
            continue

def is_victory(icon):
    if (board[0][0] == icon and board[0][1] == icon and board[0][2] == icon) or \
       (board[1][0] == icon and board[1][1] == icon and board[1][2] == icon) or \
       (board[2][0] == icon and board[2][1] == icon and board[2][2] == icon) or \
       (board[0][0] == icon and board[1][0] == icon and board[2][0] == icon) or \
       (board[0][1] == icon and board[1][1] == icon and board[2][1] == icon) or \
       (board[0][2] == icon and board[1][2] == icon and board[2][2] == icon) or \
       (board[0][0] == icon and board[1][1] == icon and board[2][2] == icon) or \
       (board[0][2] == icon and board[1][1] == icon and board[2][0] == icon):
           return True
    else:
        return False

def is_draw():
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return True
    else:
        return False

print_board()
while True:
    player_move("X")
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
input("\n")