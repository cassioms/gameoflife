from copy import deepcopy
from random import randint

from pygame import gfxdraw


class Life:

    def __init__(self, screen, width, height, offset_width, offset_height, starting_points, color, size):
        self.color = color
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.screen_offset_width = offset_width
        self.screen_offset_height = offset_height
        self.size = size
        self.points = [0] * self.get_height()
        for y in range(self.get_height()):
            self.points[y] = [0] * self.get_width()
        for n in range(starting_points):
            point = self.generate_random_point()
            self.points[point[1]][point[0]] = 1
        self.neighbours = [0] * self.get_height()
        for y in range(self.get_height()):
            self.neighbours[y] = [0] * self.get_width()
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.neighbours[y][x] = self.get_neighbours(y, x)


    def get_width(self, width=-1):
        if (width == -1):
            width = self.screen_width
        return int(width/self.size)


    def get_height(self, height=-1):
        if (height == -1):
            height = self.screen_height
        return int(height/self.size)


    def generate_random_point(self):
        return randint(0, self.get_height() - 1), randint(0, self.get_width() - 1)

    
    def get_neighbours(self, y, x):
        x_range = [x-1, x, x+1]
        y_range = [y-1, y, y+1]

        if x == 0:
            x_range[0] = self.get_width() - 1
        if x == self.get_width() - 1:
            x_range[2] = 0
        if y == 0:
            y_range[0] = self.get_height() - 1
        if y == self.get_height() - 1:
            y_range[2] = 0

        return y_range, x_range


    def count_neighbours(self, y, x):
        count = 0
        y_range, x_range = self.neighbours[y][x]
        
        for i in y_range:
            for j in x_range:
                if self.points[i][j] == 1:
                    count = count + 1

        if self.points[y][x] == 1 and count > 0:
            count = count - 1
        
        return count


    def next_gen(self):
        new_gen = deepcopy(self.points)
        for y in range(0, self.get_height()):
            neighbours = 0
            for x in range(0, self.get_width()):
                neighbours = self.count_neighbours(y, x)
                if self.points[y][x] == 1 and (neighbours < 2 or neighbours > 3):
                    new_gen[y][x] = 0
                elif self.points[y][x] == 0 and neighbours == 3:
                    new_gen[y][x] = 1

        self.points = new_gen


    def update(self):
        for y in range(0, self.get_height()):
            for x in range(0, self.get_width()):
                if self.points[y][x] == 1:
                    gfxdraw.box(self.screen, 
                        (x*self.size + self.screen_offset_width, y*self.size + self.screen_offset_height, 
                            self.size, self.size), 
                        self.color)


    def toggle_clicked(self, pos):
        x, y = pos
        if x < self.screen_offset_width or x >= self.screen_width \
            or y < self.screen_offset_height or y >= self.screen_height:
            return

        #print(f'Mouse clicked on x:{x}, y:{y}')

        y_off = y - self.screen_offset_height
        x_off = x - self.screen_offset_width

        current_value = self.points[self.get_height(y_off)][self.get_width(x_off)]
        if current_value == 0:
            self.points[self.get_height(y_off)][self.get_width(x_off)] = 1
        else:
            self.points[self.get_height(y_off)][self.get_width(x_off)] = 0
