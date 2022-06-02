def validity():
    """It makes sure suer enters valid rows and columns without
     raising index error """

    while True:
        try:
            r = int(input('Enter the row number'))
            if r > 2:
                raise IndexError

            c = int(input('Enter the column number'))
            if c > 2:
                raise IndexError

            return r, c

        except IndexError:
            print('Wrong Row or Column Number')


def begin():
    """Displays the front page to the user"""

    print('=' * 60)
    print('\t\t\t\t\tTIC TAC TOE')
    print('=' * 60)
    start = input('Press any key to start')


def display_board(l):
    """Displays the TIC-TAC-TOE Board"""

    for r in range(len(l)):
        for c in range(len(l[0])):
            print(end='      ')
            print(l[r][c], end='     |')
        print()
        print('---------------------------------------------')


def player():
    """ Allows player choice selection and returns them"""
    c = ['X', 'O']
    choice = input("Select Weapon of choice\nX          O\n")
    if choice == 'x':
        a = c[0]
        b = c[1]
    else:
        a = c[1]
        b = c[0]

    return a, b


def is_empty(r, c):
    """Checks that the current position is not occupied
    if not it returns the valid row and column numbers"""

    while True:
        if mat[r][c] == ' ':  # if current position empty
            return r, c  # return the valid row and column
        print('Enter correct row or column')
        try:
            r = int(input('Enter the row'))
            if r > 2:
                raise IndexError
            c = int(input('Enter the column'))
            if c > 2:
                raise IndexError

        except IndexError:
            print('Wrong Row or Column')


def win_pattern(matrix, choice):
    """Checks for the winning pattern"""

    found = False

    # row and column wise
    for _ in range(3):
        row_check = choice == matrix[_][0] and choice == matrix[_][1] and choice == matrix[_][2]
        col_check = choice == matrix[0][_] and choice == matrix[1][_] and choice == matrix[2][_]
        if row_check or col_check:
            found = True
            return found

    # diagonally
    left_diagonal = choice == matrix[0][0] and choice == matrix[1][1] and choice == matrix[2][2]
    right_diagonal = choice == matrix[0][2] and choice == matrix[1][1] and choice == matrix[2][0]
    if left_diagonal or right_diagonal:
        found = True
        return found

    return found


def board_initialize():
    """Initializes the board and returns it"""

    board = []
    for x in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)

    return board


begin()
choices = player()  # stores player choices such as (p1_choice,p2_choice)
print('Player 1: ', choices[0])
print('Player 2: ', choices[1])

mat = board_initialize()  # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
display_board(mat)

for i in range(9):
    if i % 2 == 0:
        print('Turn Player 1')
        tup = validity()  # tup stores row and column number within range
        tup = is_empty(tup[0], tup[1])  # tup stores valid row and column number

        mat[tup[0]][tup[1]] = choices[0]  # assign to matrix the weapon of player 1

        display_board(mat)

        if win_pattern(mat, choices[0]):
            print('Player 1 wins')
            break

    else:
        print('Turn Player 2')
        tup = validity()
        tup = is_empty(tup[0], tup[1])

        mat[tup[0]][tup[1]] = choices[1]

        display_board(mat)

        if win_pattern(mat, choices[1]):
            print('Player 2 wins')
            break

if i == 8:  # runs if loop iterates till completion so no winning pattern seen
    print('Draw')