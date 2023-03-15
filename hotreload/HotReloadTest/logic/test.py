from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

class Test(MDBoxLayout):
    pass
    
    
class TestMe(MDApp):
	def build(self):
		return Test()

if __name__ == '__main__':
	TestMe().run()