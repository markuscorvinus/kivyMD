import os
from kaki.app import App 
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window


Window.size = [350, 560]
        
class MainApp(App,MDApp):    
    DEBUG = True
    
    KV_FILES = {
        os.path.join(os.getcwd(), "logic/test.kv")
        #os.path.join('.', 'logic.screen_manager.kv')
    }

    CLASSES = {
        "Test": "logic.test"
    }

    AUTORELOADER_PATHS = [('.', {"recursive": True})]
    
    def build_app(self):
        return Factory.Test()
    
MainApp().run()