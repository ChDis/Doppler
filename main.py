import pygame
import sys
import pygame_gui
from pygame.sprite import Group, GroupSingle
from observer import Observer
from source import Source
from settings import Settings
from interface import Interface
from functions import Functions

def run_simulation():
    #initializes pygame
    pygame.init()
    settings = Settings()
    #initializes window and manager object for the graphic side of the program
    window = pygame.display.set_mode(settings.get_screen_dimensions())
    manager = pygame_gui.UIManager(settings.get_screen_dimensions())
    interface = Interface(manager)
    clock = pygame.time.Clock()
    #sets the allowed events in the program
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(settings.get_events_allowed())
    #Make 2 groups, one to store observers and other to store sources
    observers = Group()
    sources = GroupSingle()
    #initializes the interface
    interface.initialize()
    #creates an instance of the functions class
    functions = Functions(sources, observers, interface, manager, window, settings)
    #point = Observer((320, 240), (1,1), 10, window, settings.get_observer_color())
    #source = Source((320, 240), (-5.6,-5.6), 10, window, settings.get_source_color(), 10)

    while True:
        time_delta = clock.tick(60)/1000
        functions.update_screen(time_delta)
        
        

if __name__ =="__main__":
    run_simulation()