#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 27, 2020 08:25:34 PM CEST  platform: Windows NT

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

import CurrentDessert_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    CurrentDessert_support.set_Tk_var()
    top = CurrentDessert (root)
    CurrentDessert_support.init(root, top)
    root.mainloop()

w = None
def create_CurrentDessert(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_CurrentDessert(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    CurrentDessert_support.set_Tk_var()
    top = CurrentDessert (w)
    CurrentDessert_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CurrentDessert():
    global w
    w.destroy()
    w = None

class CurrentDessert:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x400+920+270")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("CurrentDessert")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.CurrentDessertTopPic = tk.Button(top)
        self.CurrentDessertTopPic.place(relx=0.0, rely=0.0, height=100
                , width=200)
        self.CurrentDessertTopPic.configure(activebackground="#ececec")
        self.CurrentDessertTopPic.configure(activeforeground="#000000")
        self.CurrentDessertTopPic.configure(background="#d9d9d9")
        self.CurrentDessertTopPic.configure(disabledforeground="#a3a3a3")
        self.CurrentDessertTopPic.configure(foreground="#000000")
        self.CurrentDessertTopPic.configure(highlightbackground="#d9d9d9")
        self.CurrentDessertTopPic.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"Example.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.CurrentDessertTopPic.configure(image=_img0)
        self.CurrentDessertTopPic.configure(overrelief="raised")
        self.CurrentDessertTopPic.configure(pady="0")
        self.CurrentDessertTopPic.configure(text='''CurrentDessertTopPic''')

        self.CurrentDessertName = tk.Label(top)
        self.CurrentDessertName.place(relx=0.0, rely=0.25, height=25, width=200)
        self.CurrentDessertName.configure(activebackground="#f9f9f9")
        self.CurrentDessertName.configure(activeforeground="black")
        self.CurrentDessertName.configure(background="#eacf15")
        self.CurrentDessertName.configure(disabledforeground="#a3a3a3")
        self.CurrentDessertName.configure(foreground="#000000")
        self.CurrentDessertName.configure(highlightbackground="#d9d9d9")
        self.CurrentDessertName.configure(highlightcolor="black")
        self.CurrentDessertName.configure(relief="raised")
        self.CurrentDessertName.configure(textvariable=CurrentDessert_support.currentdessertnamevar)

        self.CurrentDessertList = tk.Label(top)
        self.CurrentDessertList.place(relx=0.0, rely=0.313, height=275
                , width=200)
        self.CurrentDessertList.configure(activebackground="#f9f9f9")
        self.CurrentDessertList.configure(activeforeground="black")
        self.CurrentDessertList.configure(background="#fcf2ad")
        self.CurrentDessertList.configure(disabledforeground="#a3a3a3")
        self.CurrentDessertList.configure(foreground="#000000")
        self.CurrentDessertList.configure(highlightbackground="#d9d9d9")
        self.CurrentDessertList.configure(highlightcolor="black")
        self.CurrentDessertList.configure(relief="raised")
        self.CurrentDessertList.configure(textvariable=CurrentDessert_support.currentdessertlistvar)

        self.StepCount1 = tk.Label(top)
        self.StepCount1.place(relx=0.333, rely=0.0, height=50, width=50)
        self.StepCount1.configure(activebackground="#f9f9f9")
        self.StepCount1.configure(activeforeground="black")
        self.StepCount1.configure(background="#808080")
        self.StepCount1.configure(disabledforeground="#a3a3a3")
        self.StepCount1.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount1.configure(foreground="#000000")
        self.StepCount1.configure(highlightbackground="#d9d9d9")
        self.StepCount1.configure(highlightcolor="black")
        self.StepCount1.configure(relief="raised")
        self.StepCount1.configure(text='''1''')

        self.StepCount2 = tk.Label(top)
        self.StepCount2.place(relx=0.333, rely=0.125, height=50, width=50)
        self.StepCount2.configure(activebackground="#f9f9f9")
        self.StepCount2.configure(activeforeground="black")
        self.StepCount2.configure(background="#949494")
        self.StepCount2.configure(disabledforeground="#a3a3a3")
        self.StepCount2.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount2.configure(foreground="#000000")
        self.StepCount2.configure(highlightbackground="#d9d9d9")
        self.StepCount2.configure(highlightcolor="black")
        self.StepCount2.configure(relief="raised")
        self.StepCount2.configure(text='''2''')

        self.StepCount3 = tk.Label(top)
        self.StepCount3.place(relx=0.333, rely=0.25, height=50, width=50)
        self.StepCount3.configure(activebackground="#f9f9f9")
        self.StepCount3.configure(activeforeground="black")
        self.StepCount3.configure(background="#808080")
        self.StepCount3.configure(disabledforeground="#a3a3a3")
        self.StepCount3.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount3.configure(foreground="#000000")
        self.StepCount3.configure(highlightbackground="#d9d9d9")
        self.StepCount3.configure(highlightcolor="black")
        self.StepCount3.configure(relief="raised")
        self.StepCount3.configure(text='''3''')

        self.StepCount4 = tk.Label(top)
        self.StepCount4.place(relx=0.333, rely=0.375, height=50, width=50)
        self.StepCount4.configure(activebackground="#f9f9f9")
        self.StepCount4.configure(activeforeground="black")
        self.StepCount4.configure(background="#949494")
        self.StepCount4.configure(disabledforeground="#a3a3a3")
        self.StepCount4.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount4.configure(foreground="#000000")
        self.StepCount4.configure(highlightbackground="#d9d9d9")
        self.StepCount4.configure(highlightcolor="black")
        self.StepCount4.configure(relief="raised")
        self.StepCount4.configure(text='''4''')

        self.StepCount5 = tk.Label(top)
        self.StepCount5.place(relx=0.333, rely=0.5, height=50, width=50)
        self.StepCount5.configure(activebackground="#f9f9f9")
        self.StepCount5.configure(activeforeground="black")
        self.StepCount5.configure(background="#808080")
        self.StepCount5.configure(disabledforeground="#a3a3a3")
        self.StepCount5.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount5.configure(foreground="#000000")
        self.StepCount5.configure(highlightbackground="#d9d9d9")
        self.StepCount5.configure(highlightcolor="black")
        self.StepCount5.configure(relief="raised")
        self.StepCount5.configure(text='''5''')

        self.StepCount6 = tk.Label(top)
        self.StepCount6.place(relx=0.333, rely=0.625, height=50, width=50)
        self.StepCount6.configure(activebackground="#f9f9f9")
        self.StepCount6.configure(activeforeground="black")
        self.StepCount6.configure(background="#949494")
        self.StepCount6.configure(disabledforeground="#a3a3a3")
        self.StepCount6.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount6.configure(foreground="#000000")
        self.StepCount6.configure(highlightbackground="#d9d9d9")
        self.StepCount6.configure(highlightcolor="black")
        self.StepCount6.configure(relief="raised")
        self.StepCount6.configure(text='''6''')

        self.StepCount7 = tk.Label(top)
        self.StepCount7.place(relx=0.333, rely=0.75, height=50, width=50)
        self.StepCount7.configure(activebackground="#f9f9f9")
        self.StepCount7.configure(activeforeground="black")
        self.StepCount7.configure(background="#808080")
        self.StepCount7.configure(disabledforeground="#a3a3a3")
        self.StepCount7.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount7.configure(foreground="#000000")
        self.StepCount7.configure(highlightbackground="#d9d9d9")
        self.StepCount7.configure(highlightcolor="black")
        self.StepCount7.configure(relief="raised")
        self.StepCount7.configure(text='''7''')

        self.StepCount8 = tk.Label(top)
        self.StepCount8.place(relx=0.333, rely=0.875, height=50, width=50)
        self.StepCount8.configure(activebackground="#f9f9f9")
        self.StepCount8.configure(activeforeground="black")
        self.StepCount8.configure(background="#949494")
        self.StepCount8.configure(disabledforeground="#a3a3a3")
        self.StepCount8.configure(font="-family ModMatrix -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        self.StepCount8.configure(foreground="#000000")
        self.StepCount8.configure(highlightbackground="#d9d9d9")
        self.StepCount8.configure(highlightcolor="black")
        self.StepCount8.configure(relief="raised")
        self.StepCount8.configure(text='''8''')

        self.DessertStep1 = tk.Label(top)
        self.DessertStep1.place(relx=0.417, rely=0.0, height=50, width=350)
        self.DessertStep1.configure(activebackground="#f9f9f9")
        self.DessertStep1.configure(activeforeground="black")
        self.DessertStep1.configure(background="#c0c0c0")
        self.DessertStep1.configure(disabledforeground="#a3a3a3")
        self.DessertStep1.configure(foreground="#000000")
        self.DessertStep1.configure(highlightbackground="#d9d9d9")
        self.DessertStep1.configure(highlightcolor="black")
        self.DessertStep1.configure(relief="raised")
        self.DessertStep1.configure(textvariable=CurrentDessert_support.dessertstep1var)

        self.DessertStep3 = tk.Label(top)
        self.DessertStep3.place(relx=0.417, rely=0.25, height=50, width=350)
        self.DessertStep3.configure(activebackground="#f9f9f9")
        self.DessertStep3.configure(activeforeground="black")
        self.DessertStep3.configure(background="#c0c0c0")
        self.DessertStep3.configure(disabledforeground="#a3a3a3")
        self.DessertStep3.configure(foreground="#000000")
        self.DessertStep3.configure(highlightbackground="#d9d9d9")
        self.DessertStep3.configure(highlightcolor="black")
        self.DessertStep3.configure(relief="raised")
        self.DessertStep3.configure(textvariable=CurrentDessert_support.dessertstep3var)

        self.DessertStep5 = tk.Label(top)
        self.DessertStep5.place(relx=0.417, rely=0.5, height=50, width=350)
        self.DessertStep5.configure(activebackground="#f9f9f9")
        self.DessertStep5.configure(activeforeground="black")
        self.DessertStep5.configure(background="#c0c0c0")
        self.DessertStep5.configure(disabledforeground="#a3a3a3")
        self.DessertStep5.configure(foreground="#000000")
        self.DessertStep5.configure(highlightbackground="#d9d9d9")
        self.DessertStep5.configure(highlightcolor="black")
        self.DessertStep5.configure(relief="raised")
        self.DessertStep5.configure(textvariable=CurrentDessert_support.dessertstep5var)

        self.DessertStep7 = tk.Label(top)
        self.DessertStep7.place(relx=0.417, rely=0.75, height=50, width=350)
        self.DessertStep7.configure(activebackground="#f9f9f9")
        self.DessertStep7.configure(activeforeground="black")
        self.DessertStep7.configure(background="#c0c0c0")
        self.DessertStep7.configure(disabledforeground="#a3a3a3")
        self.DessertStep7.configure(foreground="#000000")
        self.DessertStep7.configure(highlightbackground="#d9d9d9")
        self.DessertStep7.configure(highlightcolor="black")
        self.DessertStep7.configure(relief="raised")
        self.DessertStep7.configure(textvariable=CurrentDessert_support.dessertstep7var)

        self.DessertStep2 = tk.Label(top)
        self.DessertStep2.place(relx=0.417, rely=0.125, height=50, width=350)
        self.DessertStep2.configure(activebackground="#f9f9f9")
        self.DessertStep2.configure(activeforeground="black")
        self.DessertStep2.configure(background="#d9d9d9")
        self.DessertStep2.configure(disabledforeground="#a3a3a3")
        self.DessertStep2.configure(foreground="#000000")
        self.DessertStep2.configure(highlightbackground="#d9d9d9")
        self.DessertStep2.configure(highlightcolor="black")
        self.DessertStep2.configure(relief="raised")
        self.DessertStep2.configure(textvariable=CurrentDessert_support.dessertstep2var)

        self.DessertStep4 = tk.Label(top)
        self.DessertStep4.place(relx=0.417, rely=0.375, height=50, width=350)
        self.DessertStep4.configure(activebackground="#f9f9f9")
        self.DessertStep4.configure(activeforeground="black")
        self.DessertStep4.configure(background="#d9d9d9")
        self.DessertStep4.configure(disabledforeground="#a3a3a3")
        self.DessertStep4.configure(foreground="#000000")
        self.DessertStep4.configure(highlightbackground="#d9d9d9")
        self.DessertStep4.configure(highlightcolor="black")
        self.DessertStep4.configure(relief="raised")
        self.DessertStep4.configure(textvariable=CurrentDessert_support.dessertstep4var)

        self.DessertStep6 = tk.Label(top)
        self.DessertStep6.place(relx=0.417, rely=0.625, height=50, width=350)
        self.DessertStep6.configure(activebackground="#f9f9f9")
        self.DessertStep6.configure(activeforeground="black")
        self.DessertStep6.configure(background="#d9d9d9")
        self.DessertStep6.configure(disabledforeground="#a3a3a3")
        self.DessertStep6.configure(foreground="#000000")
        self.DessertStep6.configure(highlightbackground="#d9d9d9")
        self.DessertStep6.configure(highlightcolor="black")
        self.DessertStep6.configure(relief="raised")
        self.DessertStep6.configure(textvariable=CurrentDessert_support.dessertstep6var)

        self.DessertStep8 = tk.Label(top)
        self.DessertStep8.place(relx=0.417, rely=0.875, height=50, width=350)
        self.DessertStep8.configure(activebackground="#f9f9f9")
        self.DessertStep8.configure(activeforeground="black")
        self.DessertStep8.configure(background="#d9d9d9")
        self.DessertStep8.configure(disabledforeground="#a3a3a3")
        self.DessertStep8.configure(foreground="#000000")
        self.DessertStep8.configure(highlightbackground="#d9d9d9")
        self.DessertStep8.configure(highlightcolor="black")
        self.DessertStep8.configure(relief="raised")
        self.DessertStep8.configure(textvariable=CurrentDessert_support.dessertstep8var)

if __name__ == '__main__':
    vp_start_gui()




