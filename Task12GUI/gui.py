#Require: pip install gobject cairo
import numpy as np
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from cairo import *
import matplotlib.pyplot as plt

cell_size = 5
field_size = 100
cell_color = [0.0, 0.0, 0.0]
background_color = [1.0, 1.0, 0.6]
button_width = 40
button_height = 20

#2D array contains filled cells by x, y
field = np.zeros(field_size**2)
density = np.random.random()

right_answers = []
your_answers = []

def fillField():
	for n in range(field_size**2):
		field[n] = 1 if np.random.random() < density else 0

fillField()

def drawField(da:'Gtk.DrawingArea', context:'Context'):\
	#Background
	context.set_source_rgb(background_color[0], background_color[1], background_color[2])
	context.rectangle(0, 0, field_size*cell_size, field_size*cell_size)
	context.fill()
	
	context.set_source_rgb(cell_color[0], cell_color[1], cell_color[2])
	n = 0
	y = 0
	for j in range(field_size):
		x = 0
		for i in range(field_size):
			if field[n] != 0:
				context.rectangle(x, y, cell_size, cell_size)
			x += cell_size
			n += 1
		y += cell_size
	context.fill()

def newDensity():
	global density
	density = np.random.random()
	fillField()
	da.queue_draw()

def enter(button:'Gtk.Button'):
	answer = entry.get_text()
	try:
		ans = int(answer)
		your_answers.append(ans)
		right_answers.append(round(density*100))
		right_answer.set_markup('Right answer was: '+ str(round(density*100))+ '%')
		your_answer.set_markup('Your answer was: '+ entry.get_text() + '%')
		newDensity()
		entry.set_text('')
	except:
		right_answer.set_markup('Incorrect answer!')
		your_answer.set_markup('')

def statPrint(button:'Gtk.Button'):
	print('Your answers	Right answers')
	for i in range(len(right_answers)):
		print(str(your_answers[i]) + '		' + str(right_answers[i]))

def statDraw(button:'Gtk.Button'):
	fig, ax = plt.subplots()
	ax.plot(right_answers, your_answers, 'p')
	ax.set_xlabel('right answer')
	ax.set_ylabel('your answer')
	plt.show()

def newGame(button:'gtk.Button'):
	your_answers.clear()
	right_answers.clear()
	right_answer.set_markup('')
	your_answer.set_markup('')
	newDensity()
	entry.set_text('')


prompt = Gtk.Label('Input density (in %) of black cells in this field:')

entry = Gtk.Entry()

enter_button = Gtk.Button(label = 'Enter')
enter_button.set_size_request(button_width, button_height)
enter_button.connect('clicked', enter)

hbox_enter_button = Gtk.HBox()
hbox_enter_button.pack_end(enter_button, expand=False, fill=False, padding=0)

right_answer = Gtk.Label('')
your_answer = Gtk.Label('')

stat_button = Gtk.Button(label = 'Print statistics')
stat_button.set_size_request(2*button_width, button_height)
stat_button.connect('clicked', statPrint)

graph_button = Gtk.Button(label = 'Graphic')
graph_button.set_size_request(button_width, button_height)
graph_button.connect('clicked', statDraw)

hbox_stat_buttons = Gtk.HBox()
hbox_stat_buttons.pack_start(stat_button, expand=False, fill=False, padding=5)
hbox_stat_buttons.pack_start(graph_button, expand=False, fill=False, padding=5)

vbox_left = Gtk.VBox()
vbox_left.pack_start(prompt, expand=False, fill=False, padding=5)
vbox_left.pack_start(entry, expand=False, fill=False, padding=5)
vbox_left.pack_start(hbox_enter_button, expand=False, fill=False, padding=5)
vbox_left.pack_start(right_answer, expand=False, fill=False, padding=5)
vbox_left.pack_start(your_answer, expand=False, fill=False, padding=5)
vbox_left.pack_end(hbox_stat_buttons, expand=False, fill=False, padding=5)

da = Gtk.DrawingArea()
da.set_size_request(field_size*cell_size, field_size*cell_size)
da.connect('draw', drawField)

quit_button = Gtk.Button(label='Quit')
quit_button.set_size_request(button_width, button_height)
quit_button.connect('clicked', Gtk.main_quit)

newgame_button = Gtk.Button(label='New game')
newgame_button.set_size_request(button_width, button_height)
newgame_button.connect('clicked', newGame)

hbox_quit_button = Gtk.HBox()
hbox_quit_button.pack_end(quit_button, expand=False, fill=False, padding=0)
hbox_quit_button.pack_start(newgame_button, expand=False, fill=False, padding=0)
vbox_right = Gtk.VBox()
vbox_right.pack_start(da, expand=True, fill=True, padding=5)
vbox_right.pack_end(hbox_quit_button, expand=False, fill=False, padding=5)

hbox = Gtk.HBox(spacing=10)
hbox.set_border_width(10)
hbox.pack_start(vbox_left, expand=True, fill=False, padding=0)
hbox.pack_start(vbox_right, expand=True, fill=False, padding=0)

if __name__=='__main__':
	win = Gtk.Window(title='Field')
	win.set_default_size(750, 750)
	win.add(hbox)
	win.connect('destroy', Gtk.main_quit)
	win.show_all()
	Gtk.main()
