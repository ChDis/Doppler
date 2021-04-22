import pygame
class Settings:
    '''A class to store all the configurations of the doppler effect project'''
    def __init__(self):
        self.screen_width = 1380
        self.screen_height = 680
        self.observer_size = 10
        self.source_size = 10
        self.bg_color = (0,0,0)
        self.observer_color = (255,255,255)
        self.source_color = (0,255,0)
        self.wave_color = (255,255,255)
        self.limit_observers = 3
        self.limit_sources = 1
        self.events_allowed = [pygame.MOUSEBUTTONDOWN, pygame.USEREVENT, pygame.QUIT]

    def get_screen_dimensions(self):
        return (self.screen_width, self.screen_height)

    def get_observer_color(self):
        return self.observer_color

    def get_source_color(self):
        return self.source_color

    def get_bg_color(self):
        return self.bg_color

    def get_observers_allowed(self):
        return self.limit_observers

    def get_sources_allowed(self):
        return self.limit_sources

    def get_observer_size(self):
        return self.observer_size
    
    def get_source_size(self):
        return self.source_size

    def get_events_allowed(self):
        return self.events_allowed

        
