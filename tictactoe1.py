# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:15:46 2023

@author: anton
"""

import numpy as np
import random

def show(game:np.array):
    
    count = 0
    for row in game:
        count += 1
        if count > 1:
            print('-----')
        rowcount = 0
        for item in row:
            rowcount += 1
            if rowcount == 3:
                print(item)
            else:
                print(item, end = '|')


def complete(game:np.array):
    
    x = np.count_nonzero(game == 'X')
    o = np.count_nonzero(game == 'O')
    
    if (x+o) == 9:
        return(True, 'full')
        print('AAAA')
    elif game[0][0] == game[1][1] and game[1][1] == game[2][2]:
        return(True, game[1][1])
    elif game[0][2] == game[1][1] and game[1][1] == game[2][0]:
        return(True, game[1][1])
    
    for i in range(3):
        if game[i][0] == game[i][1] and game[i][0] == game[i][2]:
            return(True, game[i][0])
    
    for i in range(3):
        if game[0][i] == game[1][i] and game[0][i] == game[2][i]:
            return(True, game[0][i])
    
    return(False,False)


def edit(game:np.array, i:str, xo:str):
    
    if i not in game or i == 'X' or i == 'O':
        return(False)
        
    index = np.where(game == i)
    game[index] = xo
    return(True)

def turn(game:np.array, xo:str):
    
    print(f"{xo}'s turn, input a number on the grid to mark")
    while True:
        inp = input('')
        if edit(game, inp, xo) == False:
            print('Something was not right there, try again')
        else:
            edit(game, inp, xo)
            break
        
def rungame():
    
    tictac = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
    count = 0
    
    for i in range(20):
        
        count += 1
        if count == 1:
            print('X goes first, two player game')
            show(tictac)
        else:
            show(tictac)
        
        if count % 2 == 0:
            turn(tictac, 'O')
        else:
            turn(tictac, 'X')
        
        check = complete(tictac)
        if check[0] == True:
            if check[1] == 'full':
                print('Game has ended in a draw')
                show(tictac)
                break
            else:
                print(f"{check[1]}'s have won the game!")
                show(tictac)
                break
        print()


def aicheckrow(game:np.array, xo):
    
    temp = []
    for count, row in enumerate(game):
        if len([i for i in row if i == xo]) == 2:
            for x in row:
                if x == 'X' or x == 'O':
                    temp.append(True)
                else:
                    temp.append(False)
            
            if False not in temp:
                temp = []
                continue
            else:    
                return(game[count][temp.index(False)])
    return(None)
            

def aicheckcol(game:np.array, xo):
    
    temp = []
    cgame = np.copy(game)
    for i in range(3):
        col = cgame[:, i]
        if len([i for i in col if i == xo]) == 2:
            for x in col:
                if x == 'X' or x == 'O':
                    temp.append(True)
                else:
                    temp.append(False)
            
            if False not in temp:
                temp = []
                continue
            else:
                return(game[temp.index(False)][i])
    return(None)

def aicheckdiag(game:np.array, xo):
    
    cgame = np.copy(game)
    temp = []
    diag = [cgame[0][0], cgame[1][1], cgame[2][2]]
    if len([i for i in diag if i == xo]) == 2:
        for x in diag:
            if x == 'X' or x == 'O':
                temp.append(True)
            else:
                temp.append(False)
        if False not in temp:
            temp = []
        else:
            return(game[temp.index(False)][temp.index(False)])
    
    diag = [cgame[0][2], cgame[1][1], cgame[2][0]]
    if len([i for i in diag if i == xo]) == 2:
        for x in diag:
            if x == 'X' or x == 'O':
                temp.append(True)
            else:
                temp.append(False)
        if False not in temp:
            temp = []
        else:
            return(game[temp.index(False)][2 - temp.index(False)])
    
    return(None)        
            
        
def rungameai():
    
    tictac = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
    print('Who goes first ai or human? \n')
    inp = input('')
    inp = inp.lower()
    if inp == 'ai':
        print("AI goes first as O's")
        count = 1
    else:
        count = 0
    
    for i in range(20):
        
        check = complete(tictac)
        if check[0] == True:
            if check[1] == 'full':
                print('Game has ended in a draw')
                show(tictac)
                break
            else:
                print(f"{check[1]}'s have won the game!")
                show(tictac)
                break
            
        count += 1
        if count % 2 == 0:
            print("AI's turn")
            if aicheckrow(tictac, 'O') is not None:
                temp = aicheckrow(tictac, 'O')
                edit(tictac, temp, 'O')
                continue
            elif aicheckcol(tictac, 'O') is not None:
                temp = aicheckcol(tictac, 'O')
                edit(tictac, temp, 'O')
                continue
            elif aicheckdiag(tictac, 'O') is not None:
                temp = aicheckdiag(tictac, 'O')
                edit(tictac, temp, 'O')
                continue
            elif aicheckrow(tictac, 'X') is not None:
                temp = aicheckrow(tictac, 'X')
                edit(tictac, temp, 'O')
                continue
            elif aicheckcol(tictac, 'X') is not None:
                temp = aicheckcol(tictac, 'X')
                edit(tictac, temp, 'O')
                continue
            elif aicheckdiag(tictac, 'X') is not None:
                temp = aicheckdiag(tictac, 'X')
                edit(tictac, temp, 'O')
                continue
            else:
                random_choice = ['1','2','3','4','5','6','7','8','9']
                choice = random_choice[random.randint(0,8)]
                for i in range(10):
                    if edit(tictac, choice, 'O') == False:
                        continue
                    else:
                        break
        else:
            show(tictac)
            turn(tictac, 'X')
        
        print()
    
rungameai()
        






        