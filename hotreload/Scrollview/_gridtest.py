from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    pass

class MyApp(App):

    def build(self):
        # Create a grid layout with 2 columns and 2 rows
        grid = MyGridLayout(cols=2, rows=2)

        # Create some buttons and add them to the grid layout
        button1 = Button(text='Button 1', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button2 = Button(text='Button 2', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button3 = Button(text='Button 3', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button4 = Button(text='Button 4', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        grid.add_widget(button1)
        grid.add_widget(button2)
        grid.add_widget(button3)
        grid.add_widget(button4)

        return grid

if __name__ == '__main__':
    MyApp().run()