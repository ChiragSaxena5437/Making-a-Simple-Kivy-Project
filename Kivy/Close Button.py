



from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.logger import Logger

class myapp(BoxLayout):
    def __init__(self,**kwargs):
        super(myapp,self).__init__(**kwargs)
        self.padding = 250

        btn = Button(text='Close Window')
        btn.bind(on_press=self.clkfunc)
        self.add_widget(btn)

    def clkfunc(self , obj):
        App.get_running_app().stop()
        Window.close()


class SimpleKivy(App):
    def on_stop(self):
        Logger.critical('Remember me ')
        
    def build(self):
        return myapp()

if __name__ == '__main__':
    SimpleKivy().run()