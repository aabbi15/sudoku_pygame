import pygame
import random
import dragndrop


grid= [[0] * 9  for _ in range(9)]


#randomiser
for i in range(5):
    grid[random.randint(0,8)][random.randint(0,8)]=random.randint(1,9)


def isvalid(grid,row,col,num):
    for i in range(9):
        if grid[row][i]== num:
            return False
    
    for i in range(9):
        if grid[i][col]==num:
            return False
    
    startrow= (row//3)*3
    startcol = (col//3)*3

    for i in range(3):
        for j in range(3):
            if grid[startrow+i][startcol+j]==num:
                return False
    
    return True


def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                for num in range(1,10):
                    if isvalid(grid,i,j,num):
                        grid[i][j]=num
                        
                        if solver(grid):
                            return True
                        grid[i][j]=0  
                return False
    return True






def generatepuzzle(difficulty,key):

    solver(grid)
    if difficulty=="easy":
        remove=1+(random.randint(1,6)+(key*456))%6
    if difficulty=="medium":
        remove=30+(random.randint(20 ,30)+(key*456))%10
    if difficulty=="hard":
        remove=61+(random.randint(1,6)+(key*456))%10
    
    
    while remove:
        
        row=((random.randint(0,8))+(key*123))%9
        col=((random.randint(0,8))+(key*123))%9
        store=grid[row][col]
        grid[row][col]=0
        if single_ans_checker(grid):
            remove-=1
        else:
            grid[row][col]=store
    return grid


def single_ans_checker(grid):
    tempgrid = grid.copy()
    for i in range(0,9):
        for j in range(0,9):
            if tempgrid[i][j]==0:
                counter=0
                for num in range(1,10):
                    if isvalid(grid,i,j,num): 
                        tempans=num
                        counter+=1
                if counter>1:
                    return False
                
    return True
                        




                                

