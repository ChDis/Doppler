from point import Point
from wave import Wave
import pygame


class Source(Point):
    #class to define a source object
    def __init__(self, coordinates, velocity, size, screen, color, frecuency):
        super().__init__(coordinates, velocity, size, screen, color)
        self.frecuency = frecuency
        self.waves = []


    def emit(self):
        self.create_wave()
        self.expand_waves()
    
    def create_wave(self):
        '''Function to create new waves'''
        if len(self.waves) == 0 or self.waves[-1].get_size() > self.size + 80:
            self.waves.append(Wave((self.x_coordinate, self.y_coordinate), self.size, self.screen))

    def expand_waves(self):
        '''Function to change the size of the existing waves'''
        screen_dimensions = pygame.display.get_window_size()
        position = 0
        while position < len(self.waves):
            if (self.waves[position].get_expand_rate() + self.waves[position].get_size()) > screen_dimensions[0] and (self.waves[position].get_expand_rate() + self.waves[position].get_size()) > screen_dimensions[1]:
                del self.waves[position]
                continue
            else:
                self.waves[position].expand_wave()
                self.waves[position].display()
            position += 1

    def get_frecuency(self):
        return self.frecuency

    def update(self, value, option):
        if option == 1:
            self.x_velocity = float(value)/60
        elif option == 2:
            self.y_velocity = float(value)/60
        elif option == 3:
            self.frecuency = float(value)
