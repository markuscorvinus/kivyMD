import os, sys
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty,StringProperty,NumericProperty
from kivy.resources import resource_add_path, resource_find
from kivymd.uix.snackbar import BaseSnackbar
from kivy.lang import Builder

#Builder.load_file('test.kv')
#Define our different screens
    
class MainLayout(FloatLayout):
    screen_mngr = ObjectProperty(None)
    
    



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
