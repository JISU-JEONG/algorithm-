import sys
sys.stdin = open('12100.txt')
from pprint import pprint
from itertools import product as pd
from copy import  deepcopy
def rotate(a):
    n = len(a)
    copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n-1-i] = a[i][j]
    return copy

def push(a):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 0:
                a[i].insert(a[i].pop(j),0)
def add(a):
    for i in range(N):
        for j in range(N-1,0,-1):
            if a[i][j] ==a[i][j-1]:
                a[i][j] *= 2
                a[i].pop(j-1)
                a[i].insert(0,0)

def mymax(a):
    mxtmp = 0
    for i in range(N):
        if mxtmp < max(a[i]):
            mxtmp = max(a[i])
    return mxtmp

def solve(S, board):
    if S == 1:
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
    elif S == 2:
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
    elif S == 3:
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
    else:
        push(board)
        add(board)
    return board​


# 1,u 2,d,3,l
N = int(input())
board = []
tmp = []
S = 1
for i in range(N):
    board.append(list(map(int, input().split())))
original = deepcopy(board)
for i in list(pd([1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4])):
    new_board = original
    for j in range(5):
        new_board = solve(i[j],new_board)
    tmp.append(mymax(new_board))

print(max(tmp))