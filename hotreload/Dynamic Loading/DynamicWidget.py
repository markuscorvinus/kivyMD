import os, sys


import sqlite3
#import mysql.connector #FOR mysql connection
from datetime import datetime
import base64
import io


from kivy.config            import Config
#Config.set('graphics', 'width', '730')
#Config.set('graphics', 'height', '980')
#Config.set("kivy", "log_level", "error")
#Config.write()
from kivymd.app             import MDApp

from kivy.uix.widget        import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout   import FloatLayout
from kivy.uix.image         import Image
from kivy.properties        import ObjectProperty,StringProperty,NumericProperty
from kivy.resources         import resource_add_path, resource_find
from kivy.metrics           import dp
from kivy.core.window       import Window
from kivy.core.image        import Image as ImageConvert
from kivy.lang              import Builder
from kivy.clock             import mainthread


from kivymd.uix.snackbar    import BaseSnackbar
from kivymd.uix.snackbar    import Snackbar
from kivymd.uix.card        import MDCard

#Builder.load_file('test.kv')``
#Define our different screens
class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
    
class MainLayout(FloatLayout):
    screen_mngr = ObjectProperty(None)
    dbconn      = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.load_cards()
    
    @mainthread
    def on_kv_post(self, base_widget):
        self.load_cards()
        #return super().on_kv_post(base_widget)    
    
    def load_cards(self):
        self.dbconn = sqlite3.connect('kivysql.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        # self.dbconn = mysql.connector.connect(
		# 	host ="database-1.csfcckck2rja.us-east-1.rds.amazonaws.com", 
		# 	user = "admin",
		# 	passwd = "DENe6Yhqny5SLxS7zc1h",
		# 	database = "ITPE02",
		# 	)
        
        dbcursor = self.dbconn.cursor()
        
        sql_query = """SELECT * FROM mstimages ORDER BY mstimages.code """
        #sql_query = """SELECT * FROM Movies ORDER BY Movies.year """
        dbcursor.execute(sql_query)
        
        records = dbcursor.fetchall()
        if not records: #if no record exist
            print("No record created")
        else:
            self.ids.scrn_grid.clear_widgets()
            for img_rec in records:
                # convert blob from database to texture
                data = io.BytesIO(img_rec[3])
                #data = io.BytesIO(img_rec[1])
                #data = io.BytesIO(base64.b64decode(img_rec[3]))
                dbImage = ImageConvert(data, ext="webp",filename=f'{img_rec[1]}.webp').texture 
                hexColor = "DCA454" if img_rec[4] == 5 else "9174A9"
                # create CustomCard
                mdCard = CustomCard(id=str(img_rec[0]),
                                    title=img_rec[1].title(),
                                    source=f"",
                                    group=img_rec[2].title()
                                    )
                mdCard.md_bg_color=hexColor
                mdCard.assign_texture_from_database(dbImage)
                #mdCard.assign_texture_from_database("D:\Dir\python\Codemy\KivyMD-Sandberg\hotreload\Dynamic Loading\_Images\Avengers_EndGame.png")
                self.ids.scrn_grid.add_widget(mdCard)
                
                
        self.dbconn.commit()
        self.dbconn.close()
        
       
        
    def open_custom_snackbar(self):
        #Snackbar - create popup message after successful posting
        snackbar = Snackbar(
            text="[color=#ffffff]Yo! this is a custom snackbar![/color]",
            font_size="16dp",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,
            bg_color="#FF9800"
        )
        snackbar.open()

        
    
    def open_icon_snackbar(self):
        snackbar = CustomSnackbar(
            text="This is a sample snackbar error!",
            icon= "close-circle",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,
            bg_color="#B71C1C"
            #buttons=[MDFlatButton(text="ACTION", text_color=(1, 1, 1, 1))]
        )
        snackbar.open()
        
        
    def insert_image(self):
        self.dbconn = sqlite3.connect('kivysql.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        # self.dbconn = mysql.connector.connect(
		# 	host ="database-1.csfcckck2rja.us-east-1.rds.amazonaws.com", 
		# 	user = "admin",
		# 	passwd = "DENe6Yhqny5SLxS7zc1h",
		# 	database = "ITPE02",
		# 	)
         
        dbcursor = self.dbconn.cursor()
        
        # database_params = {
		# 		'var_name'        : 'Avengers-EndGame',
        #         'var_group_type'  : 'pyro',
        #         'var_image_data'  : self.imageToBlob('D:\Dir\python\Codemy\KivyMD-Sandberg\hotreload\Dynamic Loading\_Images\Avengers_EndGame.png'),
        #         'var_created_by'  : "mbabiano",'var_updated_by'  : "mbabiano",
        #         'var_created_at'  : datetime.now(),'var_updated_at'  : datetime.now(),
		# 	}
        database_params = ('Avengers-InfinityWar','pyro',self.imageToB64('D:\Dir\python\Codemy\KivyMD-Sandberg\hotreload\Dynamic Loading\_Images\\avengers-infinity.jpeg'),"mbabiano","mbabiano",datetime.now(),datetime.now())
        #query_string = "INSERT INTO mstimages (name,group_type,image_data,created_by,updated_by,created_at,updated_at) VALUES (:var_name,:var_group_type,:var_image_data,:var_created_by,:var_updated_by,:var_created_at,:var_updated_at)"
        query_string = "INSERT INTO mstimages (name,group_type,image_data,created_by,updated_by,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        dbcursor.execute(query_string,database_params)
        
        #check if NO RECORD is created, return False(ERROR)
        if(dbcursor.rowcount < 1):
            print("No record created")
        else:
            print("Image Uplodded ")
            self.dbconn.commit()
            self.dbconn.close()
               
    
    def imageToBlob(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def imageToB64(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
            b64_string = base64.b64encode(binaryData).decode("utf-8")
            
        return b64_string
    
    def blobToImage(self,blobdata):
        with open(blobdata, 'wb') as file:
            file.write(data)
        
class CustomCard(MDCard):
    id      = StringProperty(None)
    title   = StringProperty(None)
    source  = StringProperty(None)
    group   = StringProperty(None)
        
    def assign_texture_from_database(self,dbTexture):
        self.ids.display_image.source = dbTexture
    
class DynamicWidgetApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"    
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Teal"
        return MainLayout()  

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    DynamicWidgetApp().run()
