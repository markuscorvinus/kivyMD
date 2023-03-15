import os, sys
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.resources import resource_add_path, resource_find


    
class MainLayout(MDBoxLayout):
    def function_name(self,app):
        pass
             
class mdAppComponents2(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    mdAppComponents2().run()