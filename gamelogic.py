import pygame
import sys
import sudokumaker

def gameover(current_tries,answer):

    if current_tries==0:
        return False
    if answer == False:
        current_tries-=1
    
    return True



    