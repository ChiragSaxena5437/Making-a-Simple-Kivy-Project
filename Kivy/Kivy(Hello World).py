from kivy.app import App
 
from kivy.uix.label import Label
 # lets start with hello world as usual
class FirstKivy(App):
 
    def build(self):
# kivy will use its default label size
#Main part of kivy is in open gl  and hence in glew if u have read open gll this is for you
        return Label(text="Hello World ")
 
FirstKivy().run()