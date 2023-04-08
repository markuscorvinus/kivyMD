import os, sys
import sqlite3      #FOR sqlite3 connection
import datetime     #FOR date saving of current date
import base64       #FOR password encoding

# from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
Config.set('graphics','resizable',0)
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
# from kivy.core.window import Window
# from kivymd.uix.button import MDRaisedButton,MDFillRoundFlatButton
# from kivymd.uix.screenmanager import MDScreenManager
# from kivy.metrics import dp
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from kivy.resources import resource_add_path, resource_find
# from kivymd.uix.dialog import MDDialog

    


class MainLayout(BoxLayout):
    
    def pressMe(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        if username == 'sdca.itpe02' and password == '@itpe02':
            return True
        else:
            return False
    
    def clearFields(self):
        self.ids.username.text = ''
        self.ids.password.text = ''
        
                
        
        
    
    
class CustomPasswordField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class CustomPasswordRegField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()      
    pass_text = ObjectProperty(None)

class RegDialogContent(MDBoxLayout):
    pass      
    
    
class testComponentApp(MDApp):
    title="Login"
    def build(self):
        return MainLayout()
    
    
        
        
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    testComponentApp().run()
    