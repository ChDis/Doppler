import pygame
import math
from pygame.sprite import Sprite

class Point(Sprite):
    def __init__(self, coordinates, velocity, size, screen, color):
        '''Method to initialice the point object'''
        super().__init__()
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[1]
        self.size = size
        self.thickness = 0
        self.screen = screen
        self.color = color
        self.display()

    #paints the particle in the screen
    def display(self):
        pygame.draw.circle(self.screen, self.color, (self.x_coordinate, self.y_coordinate), self.size, self.thickness)
    

    #controls the movement and the bounce of the particle
    def update(self):
        screen_dimensions = pygame.display.get_window_size()
        if self.x_coordinate - self.size + self.x_velocity < 0 or self.x_coordinate + self.size + self.x_velocity > screen_dimensions[0]:
            self.x_velocity = -self.x_velocity
        if self.y_coordinate - self.size + self.y_velocity < 0 or self.y_coordinate + self.size + self.y_velocity > screen_dimensions[1]:
            self.y_velocity = -self.y_velocity

        
        self.x_coordinate += self.x_velocity
        self.y_coordinate += self.y_velocity

    def update(self, value, option):
        if option == 1:
            self.x_velocity = float(value)/60 #we divide by 60 because it will run to 60 fps, that means that it will move 1/60 of the real velocity each frame
        elif option == 2:
            self.y_velocity = float(value)/60 

    
    #returns the coordinates of the point
    def get_coordinates(self):
        return (self.x_coordinate, self.y_coordinate)

    def get_velocity_components(self):
        return (self.x_velocity*60, self.y_velocity*60)

    def get_velocity(self):
        return math.sqrt(math.pow(self.x_velocity*60, 2) + math.pow(self.y_velocity*60, 2))
    

        