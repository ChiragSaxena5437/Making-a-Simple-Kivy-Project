##this is the final result we gwt using Screen Manager and Various Screens
##Please in all the codes match your verionj of kivy libriary with the one use din the code 
##Also Please report Any error you find in teh codes also if you are using jupyter notebook remember to 
##clear you kernls after using them for kivy there is some error you incour that i m also not clear about 
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
 
import time
import random
 
class FirstScreen(Screen):
    pass
 
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass
class FourthScreen(Screen):
    pass
class SixthScreen(Screen):
    pass

 
class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])
 
class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

    def clkfunc(self , obj):
        App.get_running_app().stop()
        Window.close()

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ' '
            font_size: 30
            
        Label:
            text: 'First Screen!'
            font_size: 30
        Label:
            text: ' '
            font_size: 30
        


        BoxLayout:
            Button:
                text: 'Add text'
                font_size: 30
                on_release: app.root.current = 'second'

<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ' '
            font_size: 30
        Label:
            text: 'Second Screen'
            font_size: 30
        TextInput:
        
        Label:
            text: ' '
            font_size: 30

        BoxLayout:
            Button:
                text: ' Next Screen'
                font_size: 30
                on_release: app.root.current = 'Third'
<ThirdScreen>
    name: 'Third'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ' Third Screen'
            font_size: 30
        Label:
            text: ' '
            font_size: 30


        BoxLayout:
            Button:
                text: 'Navigation button'
                font_size: 30
                on_release: app.root.current = 'Fourth'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ' '
            font_size: 30
        Label:
            text: ''
            font_size: 30


        
<FourthScreen>
    name: 'Fourth'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ' Your Text '
            font_size: 30
        Label:
            text: 'Your Text '
            font_size: 30
        Label:
            text: 'Your Text '
            font_size: 30
        Label:
            text: 'Your Text'
            font_size: 30
        Label:
            text: 'Your Text'
            font_size: 30

        Label:
            text: 'Your Text'
            font_size: 30
        Label:
            text: 'Your Text'
            font_size: 30
        


        BoxLayout:
            Button:
                text: 'end'
                font_size: 30
                on_release: app.root.current = 'Third'




''')
 
class ScreenManagerApp(App):
    def build(self):
        return root_widget
 
ScreenManagerApp().run()
