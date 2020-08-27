#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 27, 2020 09:14:06 PM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global currentmainnamevar
    currentmainnamevar = tk.StringVar()
    currentmainnamevar.set('')
    global currentmainlistvar
    currentmainlistvar = tk.StringVar()
    currentmainlistvar.set('')
    global mainstep1var
    mainstep1var = tk.StringVar()
    mainstep1var.set('')
    global mainstep3var
    mainstep3var = tk.StringVar()
    mainstep3var.set('')
    global mainstep5var
    mainstep5var = tk.StringVar()
    mainstep5var.set('')
    global mainstep7var
    mainstep7var = tk.StringVar()
    mainstep7var.set('')
    global mainstep2var
    mainstep2var = tk.StringVar()
    mainstep2var.set('')
    global mainstep4var
    mainstep4var = tk.StringVar()
    mainstep4var.set('')
    global mainstep6var
    mainstep6var = tk.StringVar()
    mainstep6var.set('')
    global mainstep8var
    mainstep8var = tk.StringVar()
    mainstep8var.set('')

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import CurrentMain
    CurrentMain.vp_start_gui()




