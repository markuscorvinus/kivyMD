import os, sys
import sqlite3      #FOR sqlite3 connection
import datetime     #FOR date saving of current date
import base64       #FOR password encoding

from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
Config.set('graphics','resizable',0)
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton,MDFillRoundFlatButton
from kivymd.uix.screenmanager import MDScreenManager
from kivy.metrics import dp
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from kivy.resources import resource_add_path, resource_find
from kivymd.uix.dialog import MDDialog

#Builder.load_file('./mdAppComponents.kv')    
class MainLayout(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    screen_manager = ObjectProperty(None)
    dbconn = None
    dialogbox = None
    
    def login_account(self): #Validate user input if it is in the database
        input_username = self.ids.log_username.text.strip()
        input_password = self.ids.log_password.pass_text.text.strip()
        login_complete = self.check_user(input_username,input_password) #select record in database
        if login_complete: 
            self.display_dialog("Login Success!")
        else:
            self.display_dialog("Username & password not found")
    
        
    def register_account(self,app): #Validate user input if a field is empty
        if self.input_validate():
            reg_complete = self.add_user() #insert record to database
            if reg_complete: 
                self.display_dialog("", True)
            else:
                self.display_dialog("Error inserting records")
           
            
            
    
    #display_dialog - Display dialog for success or error in registration form
    def display_dialog(self, text_msg,is_success=False):
        #text_msg = text message
        #is_success = if TRUE return to login screen else dismiss dialog
        if is_success :
            self.dialogbox = None
            if not self.dialogbox:
                self.clear_registration()
                self.dialogbox = MDDialog(
                    type="custom",
                    content_cls=RegDialogContent(),
                    buttons = [MDFillRoundFlatButton(
                                    text='Return to Login',  #pad blank spaces left and right
                                    font_size="20sp",
                                    md_bg_color="orange",
                                    pos_hint={'center_x': 0.5},
                                    on_release=self.reg_success_button
                                )],
                )
            self.dialogbox.open()  
        else:
            self.dialogbox = None
            if not self.dialogbox:
                self.dialogbox = MDDialog(
                    text=f"[color=#263238]{text_msg}[/color]",
                    buttons = [MDRaisedButton(
                            text="Ok",
                            md_bg_color="orange",
                            pos_hint={'center_x': 0.5},
                            on_press=self.dismiss_dialog)],
                )
            self.dialogbox.open()  
        
        
    #dismiss_dialog - Hide dialog box
    def dismiss_dialog(self,*args):
        if self.dialogbox:
            self.dialogbox.dismiss()
    
    
    #reg_success_button - Custom function for registration success dialog box
    def reg_success_button(self,*args):
        print("pasok")
        self.dismiss_dialog()
        self.screen_manager.current = "login_screen" 
        self.screen_manager.transition.direction = "right"     
        
           
    #input_verify - validate all input to check if there are empty records. Returns
    #               True if the all fields are NOT EMPTY, false if otherwise      
    def input_validate(self):
        username = self.ids.username.text.strip()  #strip removes any extra spaces
        firstname = self.ids.firstname.text.strip()  
        lastname = self.ids.lastname.text.strip()  
        email = self.ids.email.text.strip()  
        password = self.ids.password.pass_text.text.strip()
        cbTerms = self.ids.checkBox.active
        
        if not username or not firstname or not lastname or not email or not password:
            self.display_dialog("Please fill up all required fields") 
            return False       
        elif not cbTerms:
            self.display_dialog("You must agree to terms and condition")
            return False
        else:
            return True   
            
            

            
    
    #add_user - add user data from registration form to database    
    def add_user(self):
        self.dbconn = sqlite3.connect('kivysql.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        dbcursor = self.dbconn.cursor()
        
        database_params = {
				'var_username': self.ids.username.text.strip(),
                'var_firstname': self.ids.firstname.text.strip(),
                'var_lastname': self.ids.lastname.text.strip(),
                'var_email': self.ids.email.text.strip(),
                'var_password': self.password_encode(self.ids.password.pass_text.text.strip()),
                'var_created_at': datetime.datetime.now(),
                'var_updated_at': datetime.datetime.now(),
			}
         
        dbcursor.execute("INSERT INTO mstuser (username,first_name,last_name,email,password,created_at,updated_at) VALUES (:var_username,:var_firstname,:var_lastname,:var_email,:var_password,:var_created_at,:var_updated_at)",database_params)
        
        # 'var_username': self.ids.username.text.strip(),
        # 'var_firstname': self.ids.firstname.text.strip(),
        # 'var_lastname': self.ids.lastname.text.strip(),
        # 'var_email': self.ids.email.text.strip(),
        # 'var_password': self.password_encode(self.ids.password.pass_text.text.strip()),
        # 'var_created_at': datetime.datetime.now(),
        # 'var_updated_at': datetime.datetime.now(),
        #dbcursor.execute("INSERT INTO mstuser (username,first_name,last_name,email,password,created_at,updated_at) VALUES ('sample2','test34','test34','test@test.com34','manual34','2023-03-17 21:35:06.268893','2023-03-17 21:35:06.268893')")
        
        #check if NO RECORD is created, return False(ERROR)
        if(dbcursor.rowcount < 1):
            print("No record created")
            return False
        else:
            #print("Commit " + dbcursor.rowcount )
            self.dbconn.commit()
            self.dbconn.close()
            return True
    
    
    
    def check_user(self,input_username,input_password):
        self.dbconn = sqlite3.connect('kivysql.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        dbcursor = self.dbconn.cursor()
        
        sql_query = """SELECT * FROM mstuser WHERE username = :var_username AND password = :var_password"""
        parameter = {'var_username': input_username,'var_password':self.password_encode(input_password)}
        dbcursor.execute(sql_query,parameter)
        
        records = dbcursor.fetchall()
        #check if NO RECORD is created, return False(ERROR)
        
        if not records: #if no record exist
            print("No record created")
            return False
        else:
            for user in records:
                print(f"Username:{user[1]}\nFirstName:{user[2]}\nLastName:{user[3]}")
            self.dbconn.commit()
            self.dbconn.close()
            return True
    
    #password_encode - encode password into b64 encryption for database storage
    def password_encode(self,password_string):
        ascii_pass = password_string.encode("ascii")
        b64_pass = base64.b64encode(ascii_pass)
        return b64_pass.decode("ascii")
    
    
    #password_decode - decode password into b64 encryption for database checking
    def password_decode(self,password_string):
        ascii_pass = password_string.encode("ascii")
        b64_pass = base64.b64decode(ascii_pass)
        return b64_pass.decode("ascii")
    
    
    def clear_registration(self):
        self.ids.username.text = ''
        self.ids.firstname.text = ''
        self.ids.lastname.text = ''
        self.ids.email.text = ''
        self.ids.password.pass_text.text = ''
        self.ids.checkBox.active = False
        
class CustomPasswordField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    pass_text = ObjectProperty(None)

class CustomPasswordRegField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()      
    pass_text = ObjectProperty(None)

class RegDialogContent(MDBoxLayout):
    pass      

class mdAppComponentsApp(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    mdAppComponentsApp().run()