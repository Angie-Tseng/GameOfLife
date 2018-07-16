import math

'''
This is a class for generating map with certain image.
'''

class Map:
    #Initialize
    def __init__(self, w = 0, h = 0):
        self.set_map(w, h)
        
    
    def set_map(self, w = 0, h = 0):
        self.map = [[0] * w for i in range(h)]
        self.w = w
        self.h = h
    
    #Generate a glider image in the middle of map
    def glider(self):
        centerx = math.ceil(self.w / 2) - 1
        centery = math.ceil(self.h / 2) - 1
        
        try:
            self.map[centery - 1][centerx - 1] = 1
            self.map[centery - 1][centerx    ] = 1
            self.map[centery - 1][centerx + 1] = 1
            self.map[centery    ][centerx - 1] = 1
            self.map[centery + 1][centerx    ] = 1
        except:
            pass

    #Generate a lightweight image in the middle of map
    def lightweight(self):
        centerx = math.ceil(self.w / 2) - 1
        centery = math.ceil(self.h / 2) - 1

        try:
            self.map[centery - 1][centerx - 1] = 1
            self.map[centery - 1][centerx + 2] = 1

            self.map[centery    ][centerx - 2] = 1
            self.map[centery + 1][centerx - 2] = 1
            self.map[centery + 1][centerx + 2] = 1

            for i in range(centerx - 2, centerx + 2):
                self.map[centery + 2][i] = 1
        except:
            pass

    #Generate a puslar image in the middle of map
    def puslar(self):
        centerx = math.ceil(self.w / 2) - 1
        centery = math.ceil(self.h / 2) - 1

        dirs = [
            [-1,-1],[-1,1],[1,-1],[1,1]
        ]

        pic = [
                  [2,1],[3,1],[4,1],
            [1,2],      [3,2],      [5,2],
            [1,3],[2,3],      [4,3],[5,3],[6,3],
            [1,4],      [3,4],            [6,4],
                  [2,5],[3,5],
                        [3,6],[4,6]
        ]

        for d in dirs:
            for p in pic:
                try:
                    self.map[centery + d[0]*p[0]][centerx + d[1]*p[1]] = 1
                except:
                    continue
        #self.map[centery - 5][centerx + 2] = 0
