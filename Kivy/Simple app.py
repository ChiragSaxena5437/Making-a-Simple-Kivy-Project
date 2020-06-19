from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#this app is not very useful well it does nothing but good for a start
 
 
class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Enter the text for first button ')
        btn1 = Button(text="Similiarly the text for second button  ")
        layout.add_widget(btn)
        layout.add_widget((btn1))
        return layout
 
 
if __name__ == "__main__":
    SimpleApp().run()