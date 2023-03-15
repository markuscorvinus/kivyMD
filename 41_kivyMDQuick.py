import kivy
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
 
Builder.load_file('41_kivyMDQuick.kv')

class MyLayout(Widget):
    pass


class AwesomeApp(MDApp):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()

