#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 27, 2020 08:32:32 PM CEST  platform: Windows NT

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
    global currentdessertnamevar
    currentdessertnamevar = tk.StringVar()
    currentdessertnamevar.set('')
    global currentdessertlistvar
    currentdessertlistvar = tk.StringVar()
    currentdessertlistvar.set('')
    global dessertstep1var
    dessertstep1var = tk.StringVar()
    dessertstep1var.set('')
    global dessertstep3var
    dessertstep3var = tk.StringVar()
    dessertstep3var.set('')
    global dessertstep5var
    dessertstep5var = tk.StringVar()
    dessertstep5var.set('')
    global dessertstep7var
    dessertstep7var = tk.StringVar()
    dessertstep7var.set('')
    global dessertstep2var
    dessertstep2var = tk.StringVar()
    dessertstep2var.set('')
    global dessertstep4var
    dessertstep4var = tk.StringVar()
    dessertstep4var.set('')
    global dessertstep6var
    dessertstep6var = tk.StringVar()
    dessertstep6var.set('')
    global dessertstep8var
    dessertstep8var = tk.StringVar()
    dessertstep8var.set('')

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
    import CurrentDessert
    CurrentDessert.vp_start_gui()




