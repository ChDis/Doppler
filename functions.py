import pygame, pygame_gui
import sys
import math
from interface import Interface
from observer import Observer
from source import Source

class Functions:
    def __init__(self):
        self.selected_point = None

    def check_events(self, window, manager, settings, interface, observers, sources):
        '''Function to check events in the simulation'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = pygame.mouse.get_pos()
                if not (interface.check_menu_window_clicked(event) or interface.check_conditions_window_clicked(event)):
                    if coordinates != None:
                        self.selected_point = self.get_source(coordinates, sources, settings)
                        if self.selected_point == None:
                            self.selected_point = self.get_observer(coordinates, observers, settings)
                        if self.selected_point != None:
                            self.load_information(interface)


            elif event.type == pygame.USEREVENT:
                self.check_interface_events(event, window, settings, interface, observers, sources)

            
            manager.process_events(event)


    def check_interface_events(self, event, window, settings, interface, observers, sources):
        '''Function to check events related to the interface of the simulation'''
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == interface.get_menu_button():
                if interface.get_menu_window_visibility() == 0:
                    interface.hide_all_windows()
                    interface.show_menu_window()
                else:
                    interface.hide_all_windows()

            elif event.ui_element == interface.get_conditions_button():
                if interface.get_conditions_window_visibility() == 0:
                    interface.hide_all_windows()
                    interface.show_conditions_window()
                else:
                    interface.hide_all_windows()

            elif event.ui_element == interface.get_add_observer_button():
                if len(observers) < settings.get_observers_allowed():
                    coordinates = self.get_mouse_coordinates()
                    if coordinates != None:
                        new_observer = Observer(coordinates, (0,0), settings.get_observer_size(), window,  settings.get_observer_color())
                        observers.add(new_observer)

            elif event.ui_element == interface.get_add_source_button():
                if len(sources) < settings.get_sources_allowed():
                    coordinates = self.get_mouse_coordinates()
                    if coordinates != None:
                        new_source = Source(coordinates, (0,0), settings.get_source_size(), window, settings.get_source_color(), 0)
                        sources.add(new_source)

            elif event.ui_element == interface.get_delete_observer_button():
                coordinates = self.get_mouse_coordinates()
                if coordinates != None:
                    point = self.get_observer(coordinates, observers, settings)
                    if point != None:
                        self.delete_point(coordinates, observers, point)

            elif event.ui_element == interface.get_delete_source_button():
                coordinates = self.get_mouse_coordinates()
                if coordinates != None:
                    point = self.get_source(coordinates, sources, settings)
                    if point != None:
                        self.delete_point(coordinates, sources, point)

        elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            print('After entering the check finished',self.selected_point)
            if event.ui_element == interface.get_velocity_x_box_entry():
                value = event.ui_element.get_text()
                self.modify_point(sources, observers, self.selected_point, 1, value)
                
            


    def update_screen(self, manager, window, settings, interface, observers, sources, time_delta):
        self.check_events(window, manager, settings, interface, observers, sources)
        window.fill(settings.get_bg_color())
        manager.update(time_delta)
        for observer in observers.sprites():
            observer.display()
        for source in sources.sprites():
            source.display()
            source.emit()
        manager.draw_ui(window)
        pygame.display.flip()


    def get_mouse_coordinates(self):
        coordinates = None
        clock = pygame.time.Clock()
        time = 0
        while time < 5000:
            if pygame.event.peek(pygame.MOUSEBUTTONDOWN):
                event = pygame.event.get(pygame.MOUSEBUTTONDOWN)
                if event[0].button == 1:
                    coordinates = event[0].pos
                    break
            time += clock.get_rawtime()
        return coordinates


    def get_observer(self, coordinates, observers, settings):
        for observer in observers:
            observer_coord = observer.get_coordinates()
            if math.hypot(observer_coord[0]-coordinates[0], observer_coord[1]-coordinates[1]) <=settings.get_observer_size():
                return observer
        return None


    def get_source(self, coordinates, sources, settings):
        
        for source in sources:
            source_coord = source.get_coordinates()
            if math.hypot(source_coord[0]-coordinates[0], source_coord[1]-coordinates[1]) <=settings.get_source_size():
                return source
        return None


    def delete_point(self, coordinates, group, point):
        for element in group:
            element_coordinates = element.get_coordinates()
            if element_coordinates == coordinates:
                group.remove(element)




    def load_information(self, interface):
        velocity_components = self.selected_point.get_velocity_components()
        interface.set_x_velocity_box_entry_text(velocity_components[0])
        interface.set_y_velocity_box_entry_text(velocity_components[1])
        interface.set_velocity_box_text(self.selected_point.get_velocity())
        interface.hide_all_windows()
        interface.show_conditions_window()

        try:
            frecuency = self.selected_point.get_frecuency()
        except:
            interface.hide_frecuency_information()
        else:
            interface.show_frecuency_information()
            interface.set_frecuency_box_entry_text(frecuency)
            interface.set_frecuency_box_text(frecuency)


        