import os, sys
import kivy
import csv

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from kivy.app import App 
from kivy.uix.gridlayout import GridLayout


  
class MainLayout(GridLayout):
    reference = None
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MainLayout, self).__init__(**kwargs)
        self.match_names()

    def match_names(self):
        with open("./csv/reference.csv", 'r') as ref_file:
            self.reference = csv.reader(ref_file)
            
        with open("./csv/mortgagee-list.csv", 'r') as file:
            csvreader = csv.reader(file)
            self.processCSV(csvreader)
            
            
    
    def processCSV(self,csvrecords):
        match_records = []  
        for row in csvrecords:
            clearname = row[0].replace(",","")
            splitname = clearname.split(" ",-1)
            
            for refname in self.reference:
                ratio = 0
                stringmatch = refname[3] if refname[3].find(splitname[0]) > 0 else None
                
                if not stringmatch:
                    ratio = fuzz.token_sort_ratio(clearname, stringmatch)
                if ratio >= 80:
                    match_records.append((ratio,refname[3],refname[2],refname[1]))
                            
            
class NameSearchApp(App):
    def build(self):
        return MainLayout()  

if hasattr(sys, '_MEIPASS'):
    resource_add_path(os.path.join(sys._MEIPASS))
NameSearchApp().run()