import os, sys
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
Config.set('graphics','resizable',0)
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from kivy.resources import resource_add_path, resource_find

#Builder.load_file('test.kv')
#Define our different screens

class MainLayout(FloatLayout):
	login_screen = ObjectProperty(None)
	reg_screen = ObjectProperty(None)
 
	def change_screen(self):
		self.ids.screen_mngr1.current = self.ids.screen_mngr1.screen2.name

    
class Login(Screen):
	home = ObjectProperty(None)
class Registration(Screen):
	pass

# Designate Our .kv design file 



class AwesomeApp(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    AwesomeApp().run()
