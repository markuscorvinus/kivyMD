import os
from kaki.app import App 
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = [600, 800]
        
class MainApp(App,MDApp):    
    DEBUG = True
    
    KV_FILES = {
        os.path.join(os.getcwd(), "kivyDesign/loginDesign.kv")
        #os.path.join('.', 'logic.screen_manager.kv')
    }

    CLASSES = {
        "MainLayout": "login"
    }

    AUTORELOADER_PATHS = [('.', {"recursive": True})]
    
    def build_app(self):
        return Factory.MainLayout()
    
MainApp().run()