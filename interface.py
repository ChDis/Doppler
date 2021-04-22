import pygame
import pygame_gui

class Interface:
    def __init__(self, manager):
        self.manager = manager
        self.menu_button_dimensions = (100,50)
        self.panel_button_dimensions = (130,30)

    def initialize(self):
        '''Function to create all the elements of the GUI'''
        self.menu_button = self.create_button(self.menu_button_dimensions, (10,10), 'Menu', self.manager)

        self.menu_window = self.create_window((325, 150), (10,70), self.manager)

        self. add_observer =  self.create_button(self.panel_button_dimensions, (10,10), 'Add observer', self.manager, self.menu_window)

        self.delete_observer = self.create_button(self.panel_button_dimensions, (140, 10), 'Delete observer', self.manager, self.menu_window)

        self.add_source = self.create_button(self.panel_button_dimensions, (10,42), 'Add source', self.manager, self.menu_window)

        self.delete_source = self.create_button(self.panel_button_dimensions, (140, 42), 'Delete source', self.manager, self.menu_window)

        self.conditions_button = self.create_button(self.menu_button_dimensions, (120, 10), 'Conditions', self.manager)

        self.conditions_window = self.create_window((260, 250), (120, 70), self.manager)

        self.velocity_x_label = self.create_label((80, 35), (20, 20), 'X velocity', self.manager, self.conditions_window)

        self.velocity_y_label = self.create_label((80, 35), (20, 70), 'Y velocity', self.manager, self.conditions_window)

        self.frecuency_entry_label = self.create_label((80, 35), (20, 120), 'Frecuency', self.manager, self.conditions_window)

        self.velocity_x_box_entry = self.create_text_entry((70, 35), (130, 20), self.manager, self.conditions_window)

        self.velocity_y_box_entry = self.create_text_entry((70, 35), (130, 70), self.manager, self.conditions_window)

        self.frecuency_box_entry =  self.create_text_entry((70, 35), (130, 120), self.manager, self.conditions_window)

        self.velocity_label = self.create_label((80, 30), (660, 10), 'Velocity', self.manager)
        
        self.velocity_box = self.create_text_entry((80, 30), (760, 10), self.manager)

        self.frecuency_box_Label = self.create_label((80, 30), (860, 10), 'Frecuency', self.manager)

        self.frecuency_box = self.create_text_entry((80, 30), (960, 10), self.manager)

        #disable the text entry lines so it is not interactive to evitate errors
        self.frecuency_box.disable()
        self.velocity_box.disable()


    def get_menu_button(self):
        '''Function to get the menu_button object'''
        return self.menu_button
    
    def get_conditions_button(self):
        '''Function to get the conditions_button object'''
        return self.conditions_button

    def get_velocity_x_box_entry(self):
        '''Function to get the velocity_x_box_entry object'''
        return self.velocity_x_box_entry

    def get_velocity_y_box_entry(self):
        '''Function to get the velocity_y_box_entry object'''
        return self.velocity_y_box_entry

    def get_frecuency_box_entry(self):
        '''Function to get the frecuency_box_entry object'''
        return self.frecuency_box_entry

    def get_add_observer_button(self):
        '''Function to get the add_observer button object'''
        return self.add_observer
    
    def get_add_source_button(self):
        '''Function to get the add_source button object'''
        return self.add_source

    def get_delete_observer_button(self):
        '''Function to get the delete_observer button object'''
        return self.delete_observer
    
    def get_delete_source_button(self):
        '''Function to get the delete_source button object'''
        return self.delete_source
    
    def get_menu_window_visibility(self):
        '''Function to get visibility of the menu_window object'''
        return self.menu_window.visible

    def get_conditions_window_visibility(self):
        '''Function to get visibility of the conditions_window object'''
        return self.conditions_window.visible

    def set_x_velocity_box_entry_text(self, x_velocity):
        '''Function to set the text of the velocity_x_box_entry object'''
        self.velocity_x_box_entry.set_text(str(x_velocity))
    
    def set_y_velocity_box_entry_text(self, y_velocity):
        '''Function to set the text of the velocity_y_box_entry object'''
        self.velocity_y_box_entry.set_text(str(y_velocity))
    
    def set_frecuency_box_entry_text(self, frecuency):
        '''Function to set the text of the frecuency_box_entry object'''
        self.frecuency_box_entry.set_text(str(frecuency))

    def set_velocity_box_text(self, velocity):
        '''Function to set the text of the velocity_box_text object'''
        self.velocity_box.set_text(str(velocity))
    
    def set_frecuency_box_text(self, frecuency):
        '''Function to set the text of the frecuency_box_text object'''
        self.frecuency_box.set_text(str(frecuency))

    def show_menu_window(self):
        '''Function to show the menu_window object'''
        self.menu_window.show()

    def show_conditions_window(self):
        '''Function to show the conditions_window object'''
        self.conditions_window.show()
    
    def hide_all_windows(self):
        '''Function to hide all the objects of type panel'''
        self.menu_window.hide()
        self.conditions_window.hide()

    def hide_frecuency_information(self):
        self.frecuency_box_entry.hide()
        self.frecuency_entry_label.hide()

    def show_frecuency_information(self):
        self.frecuency_box_entry.show()
        self.frecuency_entry_label.show()

    def check_menu_window_clicked(self, event):
        return self.menu_window.check_clicked_inside_or_blocking(event)

    def check_conditions_window_clicked(self, event):
        return self.conditions_window.check_clicked_inside_or_blocking(event)

    def create_label(self, dimensions, position, text, manager, container=None, visibility=1):
        '''Function to hide all the GUI objects of type panel'''
        return pygame_gui.elements.UILabel(relative_rect=pygame.Rect(position, dimensions), text=text, manager=manager, container=container)

    def create_window(self, dimensions, position, manager):
        '''Function to create GUI objects of type panel'''
        return pygame_gui.elements.UIWindow(rect=pygame.Rect((position, dimensions)), manager=manager, visible=0)

    def create_button(self, dimensions, position, text, manager, container=None):
        '''Function to create GUI objects of type button'''
        return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(position, dimensions),text=text, manager=manager, container=container)

    def create_text_box(self,dimensions, position, manager, text=''):
        '''Function to create GUI objects of type text_box'''
        return pygame_gui.elements.UITextBox(html_text=text, relative_rect=pygame.Rect(position, dimensions), manager=manager )

    def create_text_entry(self, dimensions, position, manager, container=None):
        '''Function to create GUI objects of type TextEntryLine'''
        return pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(position, dimensions), manager=manager, container=container)

