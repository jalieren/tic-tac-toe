# map
board = list(range(1, 10))


# drawing board
def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)


# getting input
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('Where will we put ' + player_token + ' ?')  # input
        # catching error
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Incorrect input. Enter a number')
            continue
        if 1 <= player_answer <= 9:
            # checking if cell is occupied
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print('This cell is already occupied!')
        else:
            print('Incorrect input. Enter a number from 1 to 9')


def check_win(board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        temp = check_win(board)
        if temp:
            print(temp, 'wins!')
            win = True
            break
        if counter == 9:
            print('Draw!')
            break


main(board)
input('Click Enter to exit')
