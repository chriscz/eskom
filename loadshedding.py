from Tkinter import Tk, Label, StringVar
import subprocess
from multiprocessing import Pool, Process
import time
from lxml import etree
import re

def create_label_window():
	"""
		Creates a label displaying window.
		returns (root_window, tinker StringVar).
	"""
	root = Tk()
	data_var = StringVar("")
	
	label = Label(root, textvariable=data_var, fg='red', font=('Arial', 32))
	label.pack()
	
	return  root, data_var

def read_status():
	string = "Stage: {}"
	try:
		import urllib
		from lxml.html import fromstring
		url = 'http://loadshedding.eskom.co.za/LoadShedding/GetStatus'
		content = urllib.urlopen(url).read(-1)
		status = int(content)
		if status == 1:
			return string.format('None')
		elif status == 2:
			return string.format(1)
		elif status == 3:
			return string.format(2)
		elif status == 4:
			return string.format(3)
	except Exception as e:
		print e
		return "Connection error occured"

def main(poll_seconds):
	win, msg = create_label_window()
	while True:
		status = read_status()
		msg.set(status)
		win.update()
		time.sleep(poll_seconds)
if __name__ == "__main__":
	main(2)
