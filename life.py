from random import randint

from pygame import gfxdraw


class Life:

    def __init__(self, screen, width, height, starting_points, color, size):
        self.color = color
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.size = size
        self.points = [0] * self.get_width()
        for x in range(self.get_width()):
            self.points[x] = [0] * self.get_height()
        for n in range(starting_points):
            point = self.generate_random_point()
            self.points[point[0]][point[1]] = 1


    def get_width(self, width=-1):
        if (width == -1):
            width = self.screen_width
        return int(width/self.size)


    def get_height(self, height=-1):
        if (height == -1):
            height = self.screen_height
        return int(height/self.size)


    def generate_random_point(self):
        return randint(0, self.get_width() - 1), randint(0, self.get_height() - 1)

    
    def count_neighbours(self, x, y):
        count = 0
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
        
        for i in x_range:
            for j in y_range:
                if self.points[i][j] == 1:
                    count = count + 1

        if self.points[x][y] == 1:
            count = count - 1

        return count


    def next_gen(self):
        new_gen = self.points.copy()
        for x in range(0, self.get_width()):
            for y in range(0, self.get_height()):
                neighbours = self.count_neighbours(x, y)
                if self.points[x][y] == 1 and (neighbours < 2 or neighbours > 3):
                    new_gen[x][y] = 0
                elif self.points[x][y] == 0 and neighbours == 3:
                    new_gen[x][y] = 1
        self.points = new_gen


    def update(self):
        for x in range(0, self.get_width()):
            for y in range(0, self.get_height()):
                if self.points[x][y] == 1:
                    gfxdraw.box(self.screen, (x*self.size, y*self.size, self.size, self.size), self.color)
        self.next_gen()


    def toggle_clicked(self, pos):
        x, y = pos
        #print(f'Mouse clicked on x:{x}, y:{y}')

        current_value = self.points[self.get_width(x)][self.get_height(y)]
        if current_value == 0:
            self.points[self.get_width(x)][self.get_height(y)] = 1
        else:
            self.points[self.get_width(x)][self.get_height(y)] = 0
