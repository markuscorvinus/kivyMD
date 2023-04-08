import os, sys
from kivy.lang import Builder
from kivy.config import Config
#Config.set('graphics', 'width', '730')
#Config.set('graphics', 'height', '980')
#Config.set('graphics','resizable',0)

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.snackbar import BaseSnackbar
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty,NumericProperty
from kivy.resources import resource_add_path, resource_find

class CustomPasswordField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = "15sp"
    
class MainLayout(MDBoxLayout):
    dialog = None
    snackbar = None
    notif_count = 0
    
    def callback(self,app):
        print(app.theme_cls.theme_style)
        
   
    def theme_change(self,app):
        if app.theme_cls.theme_style == "Dark":
            app.theme_cls.theme_style = "Light"
            app.theme_cls.primary_palette = "Teal"
            app.theme_cls.accent_palette = "Blue"
            self.ids.mdflatbutton.text = "[color=#009688]Click Me[/color]"
            self.ids.mdrectbutton.text_color = "teal"
            self.ids.mdrecticonbutton.text_color = "teal"
            self.ids.mdrecticonbutton.icon_color = "teal"
            self.ids.mdcflatbutton.text_color = "teal"
            self.ids.mdcircleiconbutton.text_color = "teal"
            self.ids.mdcircleiconbutton.icon_color = "teal"
            if self.dialog is not None:
                self.dialog.title="[color=#008080]Exit?[/color]"
                
        else:
            app.theme_cls.theme_style = "Dark"
            app.theme_cls.primary_palette = "Blue"
            app.theme_cls.accent_palette = "Teal"
            self.ids.mdflatbutton.text = "[color=#e8eaf6]Click Me[/color]"
            self.ids.mdrectbutton.text_color = "white"
            self.ids.mdrecticonbutton.text_color = "white"
            self.ids.mdrecticonbutton.icon_color = "white"
            self.ids.mdcflatbutton.text_color = "white"
            self.ids.mdcircleiconbutton.text_color = "white"
            self.ids.mdcircleiconbutton.icon_color = "white"
            if self.dialog is not None:
                self.dialog.title="[color=#FFFFFF]Exit?[/color]"
            
    
    
    def click_me(self):
            print("Button is click")
    
            
    def open_button_dialog(self,app):
        if not self.dialog:
            self.dialog = MDDialog(
                title="[color=#FFFFFF]Exit?[/color]",
                text="[size=18sp]Confirm Logout?[/size]",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        font_size='18sp',
                        theme_text_color="Custom",
                        #text_color=app.theme_cls.primary_color,
                        on_press=self.dismiss_dialog
                    ),
                    MDRaisedButton(
                        text="LOGOUT",
                        text_color="white",
                        font_size='18sp',
                        theme_text_color="Custom",
                        #text_color=app.theme_cls.primary_color,
                        on_release=self.dismiss_dialog
                    ),
                ],
            )
        self.dialog.open()
    
    
    def dismiss_dialog(self, *args):
        self.dialog.dismiss()
    
    # def check_text_length(self,*args):
    #     if len(self.ids.pin_field.text) < 6:
    #         self.ids.pin_field.error = True
    #     elif len(self.ids.pin_field.text) > 6:
    #         self.ids.pin_field.error = True
    #     else:
    #         self.ids.pin_field.error = False
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
    def add_notification(self):
        self.notif_count+=1
        if self.notif_count<=9:
            self.ids.screen5.badge_icon = f"numeric-{self.notif_count}" 
        else:  
            self.ids.screen5.badge_icon = f"numeric-{self.notif_count}+" 
        
        #if not self.snackbar:
        self.snackbar = CustomSnackbar(
            text="You have a notification!",
            icon="information",
            snackbar_x="10dp",
            snackbar_y="10dp",
            buttons=[MDIconButton(icon="close",icon_color=(0, 0, 0, 1), on_press = self.close_snackbar)]
        )
        self.snackbar.size_hint_x = (
            Window.width - (self.snackbar.snackbar_x * 20)
        ) / Window.width
        self.snackbar.snackbar_x = Window.width
        self.snackbar.snackbar_y = "30dp"
        self.snackbar.open()
    
    def clear_notification(self):
        self.notif_count=0
        self.ids.screen5.badge_icon = "" 

    def close_snackbar(self,*args):
        self.snackbar.dismiss()
        
class mdAppComponents(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    mdAppComponents().run()