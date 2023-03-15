import kivy
#import App Class functionality located in kivy_venv\Lib\site_packages\kivy\app.py
from kivy.app import App 
#import Label Class functionality in kivy_venv\Lib\site_packages\kivy\uix\label.py
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#import os, sys
#from kivy.resources import resource_add_path, resource_find

#def resourcePath():
#    if hasattr(sys, '_MEIPASS'):
#        return os.path.join(sys._MEIPASS)
#    return os.path.join(os.path.abspath("."))


#Builder.load_file('kivyDesign\\loginDesign.kv')
class MainLayout(Widget):
    
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
        
                
        
        
    
    
    
    
class LoginApp(App):
    title="Login"
    def build(self):
        Window.clearcolor = (1,1,1,1)
        Window.size = (600, 800)
        return MainLayout()
    
    
        
        
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    LoginApp().run()
    