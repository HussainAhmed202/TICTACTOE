from tkinter import *

root = Tk()
root.title('TIC TAC TOE')
root.geometry('300x400')
root.iconbitmap("icons\Tic-tac-toe_39453.ico")

# win message new window
'''winner player who every wins it'''

show = Label(root, text='Turn P1', justify='center', font=('Terminal 20'), bg="#fa7610")
show.grid(row=0, column=0, columnspan=4, pady=15, padx=20, ipadx=60, ipady=15)

player = 1
mat = [[{}, {}, {}], [{}, {}, {}], [{}, {}, {}]]


def switch(x):
    """Switch player turn"""
    if x == 1:  # if player 1
        return 2  # given turn to player 2
    return 1  # else it must be player 2 so give turn to player 1


def win_pattern():
    """After p1 plays it switches to p2
    That is why I have switched the weapons of players
    so when it is p2 turn check for pattern of p1 who has completed their turn """

    global mat, player
    m = []

    for row in mat:
        for col in row:
            if col == 'X' or col == 'O':
                m.append(col)

    # p1='X' ; p2='O'
    if player == 2:
        choice = 'X'
    else:
        choice = 'O'

    # row and column wise
    for x in range(3):
        row_check = choice == mat[x][0] and choice == mat[x][1] and choice == mat[x][2]
        col_check = choice == mat[0][x] and choice == mat[1][x] and choice == mat[2][x]
        if row_check or col_check:
            msg = Label(root, bg='#53ef0f', justify='left', font=('Terminal 22'),
                        text=' Winner P{}'.format(switch(player)))
            msg.grid(row=0, column=0, columnspan=3, pady=15, padx=20, ipadx=38, ipady=15)
            root.after(1000, root.quit)

    else:
        if len(m) == 9:
            msg = Label(root, bg='#e4d00a', justify='center', font=('Terminal 22'), text='DRAW'.format(switch(player)))
            msg.grid(row=0, column=0, columnspan=3, pady=15, padx=20, ipadx=83, ipady=15)
            root.after(1000, root.quit)

        # diagonally
        else:
            left_diagonal = choice == mat[0][0] and choice == mat[1][1] and choice == mat[2][2]
            right_diagonal = choice == mat[0][2] and choice == mat[1][1] and choice == mat[2][0]
            if left_diagonal or right_diagonal:
                msg = Label(root, bg='#53ef0f', justify='left', font=('Terminal 22'),
                            text=' Winner P{}'.format(switch(player)))
                msg.grid(row=0, column=0, columnspan=3, pady=15, padx=20, ipadx=38, ipady=15)
                root.after(1000, root.quit)


def turn():
    global player
    new_player = switch(player)
    player = new_player

    if player == 1:
        msg = Label(root, text='Turn P{}'.format(player), justify='center', font=('Terminal 20'), bg="#fa7610")
        msg.grid(row=0, column=0, columnspan=4, pady=15, padx=20, ipadx=60, ipady=15)
    else:
        msg = Label(root, text='Turn P{}'.format(player), justify='center', font=('Terminal 20'), bg="#4d1c7c")
        msg.grid(row=0, column=0, columnspan=4, pady=15, padx=20, ipadx=60, ipady=15)

    win_pattern()


def press(x, y):
    global mat

    if y != 0:
        if player == 1:
            change = Label(root, text='X', font='Serif 25')
            change.grid(row=x, column=y, ipadx=30, ipady=14, padx=0)
            mat[x - 1][y] = 'X'
        else:
            change = Label(root, text='O', font='Serif 25')
            change.grid(row=x, column=y, ipadx=28, ipady=14, padx=0)
            mat[x - 1][y] = 'O'
    else:
        if player == 1:
            change = Label(root, text='X', font='Serif 25', borderwidth=2)
            change.grid(row=x, column=y, ipadx=30, ipady=14, padx=(10, 0))
            mat[x - 1][y] = 'X'
        else:
            change = Label(root, text='O', font='Serif 25')
            change.grid(row=x, column=y, ipadx=28, ipady=14, padx=(10, 0))
            mat[x - 1][y] = 'O'

    turn()


b1 = Button(root, anchor='nw', compound='left', command=lambda: press(1, 0), relief='solid')
b1.grid(row=1, column=0, ipadx=40, ipady=25, padx=(10, 0))

b2 = Button(root, anchor='n', compound='center', command=lambda: press(1, 1), relief='solid')
b2.grid(row=1, column=1, ipadx=40, ipady=25)

b3 = Button(root, anchor='ne', compound='right', command=lambda: press(1, 2), relief='solid')
b3.grid(row=1, column=2, ipadx=40, ipady=25)

b4 = Button(root, anchor='w', compound='left', command=lambda: press(2, 0), relief='solid')
b4.grid(row=2, column=0, ipadx=40, ipady=25, padx=(10, 0))

b5 = Button(root, anchor='center', compound='center', command=lambda: press(2, 1), relief='solid')
b5.grid(row=2, column=1, ipadx=40, ipady=25)

b6 = Button(root, anchor='e', compound='right', command=lambda: press(2, 2), relief='solid')
b6.grid(row=2, column=2, ipadx=40, ipady=25)

b7 = Button(root, anchor='sw', compound='left', command=lambda: press(3, 0), relief='solid')
b7.grid(row=3, column=0, ipadx=40, ipady=25, padx=(10, 0))

b8 = Button(root, anchor='s', compound='center', command=lambda: press(3, 1), relief='solid')
b8.grid(row=3, column=1, ipadx=40, ipady=25)

b9 = Button(root, anchor='se', compound='right', command=lambda: press(3, 2), relief='solid')
b9.grid(row=3, column=2, ipadx=40, ipady=25)

root.mainloop()

