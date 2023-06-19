import pygame
import sys
import sudokumaker

def gameover(current_tries):

    if current_tries==0:
        return False
    
    
    return True


def wrongtry(current_tries):
    current_tries-=1

    