import os, sys
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.resources import resource_add_path, resource_find

#Builder.load_file('test.kv')
#Define our different screens

class MainLayout(FloatLayout):
    screen_mngr = ObjectProperty(None)
 
    def function_name(self,screen_name,direction):
        self.ids.screen_mngr1.current = screen_name
        self.ids.screen_mngr1.transition.direction = direction
        
    def register(self): 
        inp_username  = self.ids.username.text
        inp_firstname = self.ids.firstname.text
        inp_lastname  = self.ids.lastname.text
        inp_email     = self.ids.email.text
        inp_password  = self.ids.password.text
        
    
    def login(self):    
        inp_username  = self.ids.log_username.text
        inp_password = self.ids.log_firstname.text
             
# Designate Our .kv design file 



class screenManagerApp(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    screenManagerApp().run()
