#running app


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
 
#a somewhat advanced with different colours
class SimpleApp(App):
    def build(self):
        layout = PageLayout()
        layout.add_widget(Button(text='1st',background_color=(1,0,0,1)))
        layout.add_widget(Button(text='2nd',background_color=(0,1,0,1)))
        layout.add_widget(Button(text='3rd',background_color=(1,1,1,1)))
        layout.add_widget(Button(text='4th',background_color=(0,1,1,1)))
        return layout
 
 
if __name__ == "__main__":
    SimpleApp().run()
