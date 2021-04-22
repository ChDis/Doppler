import pygame
class Wave:

    def __init__(self, coordinates, size, screen):
        '''Function to define an Waves class object'''
        self.color = (255,255,255)
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]
        self.size = size
        self.screen = screen
        self.expand_rate =  5.6 #the expand rate is calculated from the fps cap of the program, in this case 60, with the formula vOfSound/fps
    
    def display(self):
        '''Function to display the circle with the conditions declared'''
        pygame.draw.circle(self.screen, self.color, (self.x_coordinate, self.y_coordinate), self.size, 1)

    def expand_wave(self):
        '''Function to change the radius of the circle to be displayed'''
        self.size += self.expand_rate

    def get_size(self):
        '''Function to get the size value of the object'''
        return self.size
    
    def get_expand_rate(self):
        '''Function to get the expand rate of the circle'''
        return self.expand_rate

    
        
