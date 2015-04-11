import kivy
import time
import urllib2
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation


class MainScreen (BoxLayout):
	
	REMOTE_SERVER = "http://8.8.8.8"

	def is_connected():
		try:
			# see if we can resolve the host name -- tells us if there is
			# a DNS listening
			host = socket.gethostbyname(REMOTE_SERVER)
			# connect to the host -- tells us if the host is actually
			# reachable
			s = socket.create_connection((host, 80), 2)
			return True
		except:
			pass
		return False

	def CallApi():
		url = "https://prometheus-cube.herokuapp.com/api/keaton.okkonen@gmail.com"
		response = urlopen(url).read()
		data = json.loads(response.decode('utf-8'))
		return data
		
	def WriteList(num, cont):
		corenum = num
		corenum += ".txt"
		corefile = open(corenum, 'w')
		for line in cont:
			corefile.write("%s\n" % line)
		corefile.close
		keyfile = open("key.txt", 'w')
		keyfile.write("%s" % num)
		keyfile.close

	def ReadList(num):
		corenum = num
		corenum += ".txt"
		openfile = open(corenum, 'r')
		lines = openfile.readlines()
		openfile.close
		if lines:
			return lines
		else:
			return "null"

	def CoreLine(num):
		statnum = num
		statnum += "s.txt"
		statfile = open(statnum, 'r')
		lines = statfile.readlines()
		statfile.close
		current = lines[0]
		if current:
			return current
		else:
			return 0

	def CoreList():
		statfile = open("key.txt", 'r')
		lines = statfile.readlines()
		prime = lines[0]
		if prime:
			return prime
		else:
			return 0

	if is_connected():
		data = CallApi()
		listnum = data["pid"]
		listcont = data["listcont"]
		corenum = listnum
		corenum += ".txt"

		if os.path.isfile(corenum):
			print ('list previously loaded.')
			WriteList(listnum, listcont)

		else:
			print ('list does not exist.')
			WriteList(listnum, listcont)

	currentlist = CoreList()
	currentline = CoreLine(currentlist)
	activefile = ReadList(currentlist)
	print ('current line is :', currentline)
	print ('current list is :', currentlist)
    print ('current list content is :', activefile)

	# This is the old code, to be properly integrated with data extraction mechanism.
	
	active_label = ObjectProperty(None)

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
		current_label = self.activefile[self.currentline]
		label = self.ids['label_display']
		label.text = current_label
		self.currentline += 1

class PrometheusApp(App):
	def build(self):
		return MainScreen()

if __name__ == '__main__':
	PrometheusApp().run()
