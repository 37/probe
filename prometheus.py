import kivy
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.core.window import Window

class MainScreen (Widget):
    f = open("sourcefile.txt", 'r')
    lines = f.readlines()
    f.close
    i = 0	

    def ChangeBtn(self, **kwargs):
    	current_label = self.lines[self.i]
    	label = self.ids['label_display']
    	label.text = current_label
        self.i += 1

class PrometheusApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    PrometheusApp().run()
