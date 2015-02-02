import kivy
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation

class MainScreen (BoxLayout):
    active_label = ObjectProperty(None)
    f = open("sourcefile.txt", 'r')
    lines = f.readlines()
    f.close
    i = 0	

    def Animate(self):
        right = Animation(x=self.active_label.parent.width, color= [0,0,0,0])
        fade = Animation(color= [0,0,0,0], duration=0.5)
        fade.bind(on_complete=self.ChangeBtn) 
        snap = Animation(x=0, duration=0.01)
        wait = Animation(duration = 5)
        left = Animation(center_x=self.active_label.parent.width/2, color= [1,1,1,1])
        anim = fade + snap + left + wait + right
        anim.start(self.active_label)

    def ChangeBtn(self, instance, value):
    	current_label = self.lines[self.i]
    	label = self.ids['label_display']
        label.text = current_label
        self.i += 1

class PrometheusApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PrometheusApp().run()
