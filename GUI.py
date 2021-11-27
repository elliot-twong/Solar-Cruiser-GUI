import matplotlib.pyplot as plt
import numpy as np
import time

from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image

# GUI look
# Tkdocs - https://tkdocs.com/shipman/index-2.html

# GUI start
root = Tk()
root.title("solar cruiser camera")

# GUI variables
frate = IntVar()
acqmode = StringVar()
trigger = StringVar()
exttrigger_list = ('Software', 'Hardware', 'Counter', 'Activation Control', 'Ang')
exttrigger = StringVar()
burstcnt = IntVar()
trigdelayrange = StringVar()
trigdelayrange_list = ('nanoseconds', 'microseconds', 'milliseconds', 'seconds', 'minutes')
trigdelay = DoubleVar()
trigcache = StringVar()

# GUI commands
# GUI event handlers
def frate_command(frate_string):
    frate.set(int(frate_string))
    print("FPS: ", frate.get())

def acqmode_command():
    print("acqmode: ", acqmode.get())

def trigger_command():
    print("trigger: ", trigger.get())

def exttrigger_command(trigger_string):
    print("exttrigger: ", trigger_string)

def burstcnt_command(burstcnt_string):
    burstcnt.set(int(burstcnt_string))
    print("burstcnt: ", burstcnt.get())

def trigdelay_command(trigdelay_string):
    multiplier = {
        'nanoseconds' :   0.000000001,
        'microseconds' :  0.000001,
        'milliseconds' :  0.001,
        'seconds' :       1.0,
        'minutes' :      60.0}
    trigdelay.set(int(trigdelay_string) * multiplier.get(trigdelayrange.get(), 0))
    print("trigdelay: ", trigdelay.get())

def trigcache_command():
    print("trigcache: ", trigcache.get())

# GUI widgets
bold_font = font.Font(weight='bold')
top_labelframe = LabelFrame(root, text = 'HIKROBOT MV-CA013-20GM')
top_labelframe.grid()

image_labelframe = LabelFrame(top_labelframe, text = 'image')
image_labelframe.grid(column = 0, row = 0)

canvas = Canvas(image_labelframe,bg='white', width = 500,height = 500, scrollregion=(0,0,1024,1024))

image1 = ImageTk.PhotoImage(Image.open("C:/Users/Elliot/Downloads/NASA.png"))
#image1 = PhotoImage("../../Downloads/NASA.png")
test_image = canvas.create_image(100, 100, anchor = NW, image = image1)
#oval = canvas.create_oval(0, 0, 50, 50)

hbar = ttk.Scrollbar(image_labelframe, orient = HORIZONTAL)
hbar.grid(row = 1,column = 0, sticky=E+W)
hbar.config(command = canvas.xview)

vbar = ttk.Scrollbar(image_labelframe,orient = VERTICAL)
vbar.grid(row = 0,column = 1, sticky=N+S)
vbar.config(command = canvas.yview)

canvas.config(width=700,height=700,xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.grid(row = 0, column = 0, sticky = N)

controls_labelframe = LabelFrame(top_labelframe, text = 'controls')
controls_labelframe.grid(column = 1, row = 0, sticky = N)

frate_labelframe = LabelFrame(controls_labelframe, text = 'Frame Rate')
frate_labelframe.grid(column = 0, row = 0, columnspan = 20, sticky = W)
frate_scale = Scale(frate_labelframe, length = 300, orient = HORIZONTAL,
    bg='#0b3d91', fg='#ffffff', font=bold_font,
    from_ = 1, to = 1023,
    command = frate_command)
frate_scale.grid(column = 0, row = 0, columnspan = 20, sticky = W)

acqmode_labelframe = LabelFrame(controls_labelframe, text = 'Acquisition')
acqmode_labelframe.grid(column = 0, row = 1, sticky = W)
acqmode_cont = Radiobutton(acqmode_labelframe, indicatoron = 0, borderwidth = 4, width = 11,
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    text='Continuous', variable = acqmode, value = 'Continuous', command = acqmode_command)
acqmode_one = Radiobutton(acqmode_labelframe, indicatoron = 0, borderwidth = 4, width = 11,
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    text='Single', variable = acqmode, value = 'Single', command = acqmode_command)
acqmode_cont.grid(column = 0, row = 0, sticky = W)
acqmode_one.grid(column = 1, row = 0, sticky = W)

trigger_labelframe = LabelFrame(controls_labelframe, text = 'Trigger')
trigger_labelframe.grid(column = 0, row = 2, sticky = W)
trigger_on = Radiobutton(trigger_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='ON',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
   variable = trigger, value = 'ON', command = trigger_command)
trigger_off = Radiobutton(trigger_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='OFF',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    variable = trigger, value = 'OFF', command = trigger_command)
trigger_on.grid(column = 0, row = 0, sticky = W)
trigger_off.grid(column = 1, row = 0, sticky = W)

exttrigger_labelframe = LabelFrame(controls_labelframe, text = 'External Trigger Source')
exttrigger_labelframe.grid(column = 0, row = 3, sticky = W)
exttrigger_option = OptionMenu(exttrigger_labelframe, exttrigger, *exttrigger_list,
    command = exttrigger_command)
exttrigger_option.grid(column = 0, row = 0, sticky = W)

burstcnt_labelframe = LabelFrame(controls_labelframe, text = 'Burst Frame Count')
burstcnt_labelframe.grid(column = 0, row = 4, sticky = W)
burstcnt_scale = Scale(burstcnt_labelframe, orient = HORIZONTAL, length = 300,
    bg='#0b3d91', fg='#ffffff', font=bold_font,
    from_ = 1, to = 1023,
    command = burstcnt_command)
burstcnt_scale.grid(column = 0, row = 0, sticky = W)

trigdelay_labelframe = LabelFrame(controls_labelframe, text = 'Trigger Delay')
trigdelay_labelframe.grid(column = 0, row = 5, sticky = W)
trigdelayrange_option = OptionMenu(trigdelay_labelframe, trigdelayrange, *trigdelayrange_list)
trigdelayrange_option.grid(column = 0, row = 0, sticky = W)
trigdelay_scale = Scale(trigdelay_labelframe, orient = HORIZONTAL, length = 300,
    bg='#0b3d91', fg='#ffffff', font=bold_font,
    from_ = 0, to = 10000,
    command = trigdelay_command)
trigdelay_scale.grid(column = 0, row = 1, sticky = W)

trigcache_labelframe = LabelFrame(controls_labelframe, text = 'Trigger Cache Enable')
trigcache_labelframe.grid(column = 0, row = 6, sticky = W)
trigcache_on = Radiobutton(trigcache_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='ON',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    variable = trigcache, value = 'ON', command = trigcache_command)
trigcache_off = Radiobutton(trigcache_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='OFF',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    variable = trigcache, value = 'OFF', command = trigcache_command)
trigcache_on.grid(column = 0, row = 0, sticky = W)
trigcache_off.grid(column = 1, row = 0, sticky = W)

exttrigger_labelframe = LabelFrame(controls_labelframe, text = 'Trigger Activation')
exttrigger_labelframe.grid(column = 0, row = 7, sticky = W)
exttrigger_option = OptionMenu(exttrigger_labelframe, exttrigger, *exttrigger_list,
    command = exttrigger_command)
exttrigger_option.grid(column = 0, row = 0, sticky = W)

frate_labelframe = LabelFrame(controls_labelframe, text = 'Trigger Debouncer')
frate_labelframe.grid(column = 0, row = 8, columnspan = 20, sticky = W)
frate_scale = Scale(frate_labelframe, length = 300, orient = HORIZONTAL,
    bg='#0b3d91', fg='#ffffff', font=bold_font,
    from_ = 1, to = 1000000,
    command = frate_command)
frate_scale.grid(column = 0, row = 0, columnspan = 20, sticky = W)

trigger_labelframe = LabelFrame(controls_labelframe, text = 'Event Control')
trigger_labelframe.grid(column = 0, row = 9, sticky = W)
trigger_on = Radiobutton(trigger_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='Option 1',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
   variable = trigger, value = 'Option 1', command = trigger_command)
trigger_off = Radiobutton(trigger_labelframe, indicatoron = 0, borderwidth = 4, width = 11, text='Option 2',
    selectcolor='#0b3d91', bg='grey', fg='#ffffff', font=bold_font,
    variable = trigger, value = 'Option 2', command = trigger_command)
trigger_on.grid(column = 0, row = 0, sticky = W)
trigger_off.grid(column = 1, row = 0, sticky = W)

# GUI initialiation
frate_scale.set(45)
acqmode_one.select()
trigger_on.select()
exttrigger.set(exttrigger_list[0])
burstcnt_scale.set(0)
trigdelayrange.set(trigdelayrange_list[0])
trigdelay_scale.set(0)
trigcache_on.select()

# GUI
root.mainloop()