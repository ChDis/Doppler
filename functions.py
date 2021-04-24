import pygame
import sys
import pygame_gui
from observer import Observer
from source import Source
from pygame.sprite import GroupSingle
import math

class Functions:
    
    def __init__(self, sources, observers, interface, manager, window, settings):

        self.sources = sources
        self.observers = observers
        self.interface = interface
        self.manager = manager
        self.window = window
        self.settings = settings
        self.selected_point = GroupSingle()


    def update_screen(self, time_delta):
        '''Function to update, draw objects in the screen'''
        self.check_events()
        self.window.fill(self.settings.get_bg_color())
        self.manager.update(time_delta)
        self.observers.update()
        self.sources.update()
        self.display_observers()
        self.display_sources()
        self.update_frecuency_received()
        self.manager.draw_ui(self.window)
        pygame.display.flip()


    def display_observers(self):
        '''Function to display all the observers in th observers group'''
        for observer in self.observers:
            observer.display()

    def display_sources(self):
        '''Function to display all the sources in the sources group'''
        for source in self.sources:
            source.display()
            source.emit()


    def check_events(self):
        '''Function to check general events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT:
                self.check_interface_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_mouse_events(event)


            self.manager.process_events(event)


    def check_interface_events(self, event):
        '''Function to check for events of the interface'''
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            self.check_buttons_events(event)
        
        if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.interface.get_velocity_x_box_entry():
                value = event.ui_element.get_text()
                self.modify_point(value, 1)
                self.load_information()
            
            elif event.ui_element == self.interface.get_velocity_y_box_entry():
                value = event.ui_element.get_text()
                self.modify_point(value, 2)
                self.load_information()

            elif event.ui_element == self.interface.get_frecuency_box_entry():
                value = event.ui_element.get_text()
                self.modify_point(value, 3)
                self.load_information()



    def check_buttons_events(self, event):
        '''Function to check events generated from the buttons'''
        if event.ui_element == self.interface.get_menu_button():
            if self.interface.get_menu_window_visibility():
                self.interface.hide_all_windows()
                
            else:
                self.interface.hide_all_windows()
                self.interface.show_menu_window()

        elif event.ui_element == self.interface.get_conditions_button():
            if self.interface.get_conditions_window_visibility():
                self.interface.hide_all_windows()
            else:
                self.interface.hide_all_windows()
                self.interface.show_conditions_window()

        elif event.ui_element == self.interface.get_add_observer_button():
            if len(self.observers) < self.settings.get_observers_allowed():
                coordinates = self.get_mouse_coordinates()
                if coordinates != None:
                    new_observer = Observer(coordinates, (0,0), self.settings.get_observer_size(), self.window,  self.settings.get_observer_color())
                    self.observers.add(new_observer)

        elif event.ui_element == self.interface.get_add_source_button():
            if not len(self.sources):
                coordinates = self.get_mouse_coordinates()
                new_source = Source(coordinates, (0,0), self.settings.get_source_size(), self.window, self.settings.get_source_color(), 0)
                self.sources.add(new_source)

        elif event.ui_element == self.interface.get_delete_observer_button():
            coordinates = self.get_mouse_coordinates()
            if coordinates != None:
                observer = self.get_observer(coordinates)
                if observer != None:
                    self.delete_observer(observer)

        elif event.ui_element == self.interface.get_delete_source_button():
            self.sources.empty()




    def check_mouse_events(self, event):
        '''Function to check mouse events'''
        if not (self.interface.check_menu_window_clicked(event) or self.interface.check_conditions_window_clicked(event)):
                coordinates = pygame.mouse.get_pos()
                if coordinates != None:
                    selected = self.get_source(coordinates)
                    if selected == None:
                        selected = self.get_observer(coordinates)
                    if selected != None:
                        self.selected_point.add(selected)
                        self.load_information()
                    else:
                        self.selected_point.empty()
                        self.load_information()


    def get_mouse_coordinates(self):
        '''Function to get the mouse coordinates in a given moment'''
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


    def get_observer(self, coordinates):
        '''Function to return the observer if it matches with the coordinates given'''
        for observer in self.observers:
            observer_coord = observer.get_coordinates()
            if math.hypot(observer_coord[0]-coordinates[0], observer_coord[1]-coordinates[1]) <=self.settings.get_observer_size():
                return observer
        return None
    
    def get_source(self, coordinates):
        '''Function to return the source if it matches the coordinates given'''
        for source in self.sources:
            source_coord = source.get_coordinates()
            if math.hypot(source_coord[0]-coordinates[0], source_coord[1]-coordinates[1]) <=self.settings.get_source_size():
                return source
        return None


    def delete_observer(self, point):
        '''Function to delete an observer from a certain froup'''
        for observer in self.observers:
            if observer.get_coordinates() == point.get_coordinates():
                self.observers.remove(observer)


    def load_information(self):
        '''Function to load the information of a point in the interface'''
        if len(self.selected_point.sprites()):
            for selected in self.selected_point:
                velocity_components = selected.get_velocity_components()
                self.interface.set_x_velocity_box_entry_text(velocity_components[0])
                self.interface.set_y_velocity_box_entry_text(velocity_components[1])
                self.interface.set_velocity_box_text(selected.get_velocity())
                self.interface.hide_all_windows()
                self.interface.show_conditions_window()
                try:
                    frecuency = selected.get_frecuency()
                except:
                    self.interface.hide_frecuency_information()
                else:
                    self.interface.show_frecuency_information()
                    self.interface.set_frecuency_box_entry_text(frecuency)
                    self.interface.set_frecuency_box_text(frecuency)
                self.update_frecuency_received()
        else:
            self.interface.set_x_velocity_box_entry_text(0)
            self.interface.set_y_velocity_box_entry_text(0)
            self.interface.set_velocity_box_text(0)
            self.interface.set_frecuency_box_text(0)
            self.interface.hide_frecuency_information()


    def update_frecuency_received(self):
        '''Function to update the frecuency received by an observer'''
        if self.observers.has(self.selected_point.sprites()):
            received_frecuency = self.calculate_received_frecuency()
            self.interface.set_frecuency_box_text(received_frecuency)


    def modify_point(self, value, option):
        '''Function to modify the member variables of the point'''
        if len(self.selected_point):
            selected = self.selected_point.sprites()
            selected = selected[0]
            if self.sources.has(selected):
                for source in self.sources:
                    if source.get_coordinates() == selected.get_coordinates() and source.get_velocity_components() == selected.get_velocity_components():
                        source.modify(value, option)
            elif self.observers.has(selected):
                for observer in self.observers:
                    if observer.get_coordinates() == selected.get_coordinates() and observer.get_velocity_components() == selected.get_velocity_components():
                        observer.modify(value, option)


    def calculate_received_frecuency(self):
        '''Calculates the received frecuency by an observer'''
        if self.sources.sprites() != None and self.observers.sprites() != None:
            selected_point = self.selected_point.sprites()
            selected_point = selected_point[0]
            source = self.sources.sprites()
            source = source[0]

            vectors = self.calculate_vectors(selected_point, source)
            angle_selected = self.calculate_angle_between_vectors(selected_point.get_velocity_components(), vectors[0])
            angle_source = self.calculate_angle_between_vectors(selected_point.get_velocity_components(), vectors[1])
            print('vectors, angle of the selected and angle of the source', vectors, angle_selected, angle_source)

            frecuency = source.get_frecuency() * (343 + selected_point.get_velocity() * math.cos(angle_selected)) / (343 - source.get_velocity() * math.cos(angle_source))

            return round(frecuency, 2)
        
        return 0


    def calculate_vectors(self, selected_point, source):
        '''Function to calculate the 2 vectors that are used in the calculus of the
        final frecuency perceived'''
        
        source_position = source.get_coordinates()
        selected_position = selected_point.get_coordinates()
        selected_to_source_vector = [source_position[0] - selected_position[0], source_position[1]-selected_position[1]]
        source_to_selected_vector = [selected_to_source_vector[0]*-1, selected_to_source_vector[1]*-1]

        return (selected_to_source_vector, source_to_selected_vector)


    def calculate_angle_between_vectors(self, vector1, vector2):
        '''Calculates the angle in radians between the normalized vector1 and vector2'''
        point_product = self.point_product(vector1, vector2)
        module_selected = self.module_of_vector(vector1)
        module_selected_to_point = self.module_of_vector(vector2)

        if module_selected != 0 and module_selected_to_point != 0:
            return math.acos(point_product/(module_selected*module_selected_to_point))

        elif module_selected == 0:

            return 1.5707


    def point_product(self, vector1, vector2):
        '''Function to find the vector generated subtracting each component of the vectors'''
        return (vector1[0]*vector2[0] + vector1[1]*vector2[1])


    def module_of_vector(self, vector):
        '''Function to normalice the given vector'''
        return math.hypot(vector[0], vector[1])
