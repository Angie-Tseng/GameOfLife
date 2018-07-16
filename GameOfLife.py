import time
import random
import math
from map import *

'''
This is a class for generating a game manager for Game of Life.

__init__(int w, int h):
    generate a w*h map.

void initialize(int p): 
    initialize the map according to p.
    if p = 1~3: generate certain image by using map.py.
    else: generate w*h*p% cells.

void proceed(int t):
    Display t generations.

void display():
    Display the map.

'''

class GameOfLife:    
    neighbor = [
        [-1,-1], [-1,0], [-1,1],
        [ 0,-1],         [ 0,1],
        [ 1,-1], [ 1,0], [1, 1]
    ]

    #initialize: set the map
    def __init__(self, w = 60, h = 23):
        self.__map = [[0] * w for i in range(h)]
        self.__w = w
        self.__h = h

    def proceed(self, t = 1):
        for k in range(t):
            #show the map
            self.display()

            def copy(a):
                b = []
                for i in a:
                    b.append(i[:])
                return b

            #copy the map
            new_map = copy(self.__map)

            #for every cell in the map live or die
            for y in range(self.__h):
                for x in range(self.__w):
                    new_map[y][x] = self.rule(y=y,x=x)

            #reload
            self.__map = copy(new_map)
            time.sleep(1)

    def display(self):
        for i in self.__map:
            for j in i:
                if j == 1: print('O', end = '')
                else: print(' ', end = '')
            print()
        print("*" * self.__w)

    def initialize(self, p = 1):
        if p >= 4:
            n = int(self.__w * self.__h * p / 100)
            cells = random.sample(range(self.__w*self.__h), n)
            for cell in cells:
                self.__map[int(cell / self.__w)] [int(cell % self.__w)] = 1
            return

        generate = Map(self.__w, self.__h)
        if p == 1:
            generate.glider()
        elif p == 2:
            generate.lightweight()
        else:
            generate.puslar()
        
        self.__map = generate.map

    def rule(self, y, x):
        sum = 0
        for pos in self.neighbor:
            try:
                if self.__map[y + pos[0]] [x + pos[1]]:
                    sum += 1
            except:
                continue
                
        if self.__map[y][x] == 1:
            if sum < 2 or sum > 3: return 0
            else: return 1
        else:
            if sum == 3: return 1
        return 0