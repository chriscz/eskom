#!/usr/bin/env python2
from Tkinter import Tk, Label
import urllib

def create_label_window():
    """
        Creates a label displaying window.
        returns (root_window, tinker StringVar).
    """
    root = Tk()
    root.minsize(width=300, height=50)
    root.maxsize(width=300, height=50)
    label = Label(root, text='Waiting...', fg='red', font=('Arial', 24))
    label.pack()
    return root, label

def read_status():
    string = "Stage: {}"
    try:

        url = 'http://loadshedding.eskom.co.za/LoadShedding/GetStatus'
        content = urllib.urlopen(url).read(-1)
        status = int(content)
        if status == 1:
            return 'No loadshedding'
        elif status == 2:
            return string.format(1)
        elif status == 3:
            return string.format(2)
        elif status == 4:
            return string.format(3)
        else:
            return 'Unknown loadshedding stage'
    except Exception as e:
        print e
        return "Connection error occured"

def main(poll_seconds):
    win, label = create_label_window()
    def refresher():
        status = read_status()
        old_text = label['text']
        label.configure(text=status)
        label.pack()
        if old_text != status:
            win.deiconify()
            win.lift()
            win.wm_attributes("-topmost", 1)
        win.after(poll_seconds*1000, refresher)
    win.after(0, refresher)
    win.mainloop()
if __name__ == "__main__":
    # Update every minute
    main(60)
