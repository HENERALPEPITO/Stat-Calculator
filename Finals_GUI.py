
import math
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from statistics import variance
from statistics import stdev
import scipy.stats as stats
import matplotlib.pyplot as plt

# import support module
import Finals_GUI_support

# create object for the UI
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        # configure default size of the window
        top.geometry("568x416+341+124")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Variance and Standard Deviation Calculator")
        top.configure(background="#d9d9d9")

        self.top = top

        #create tkinter frame widget
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.018, rely=0.024, relheight=0.966
                , relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(cursor="fleur")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        # create 15 entry widgets for user input ('o' for observations)
        self.o1 = tk.Entry(self.Frame1)
        self.o1.place(relx=0.016, rely=0.119, height=20, relwidth=0.17)
        self.o1.configure(background="white")
        self.o1.configure(disabledforeground="#a3a3a3")
        self.o1.configure(font="TkFixedFont")
        self.o1.configure(foreground="#000000")
        self.o1.configure(highlightbackground="#d9d9d9")
        self.o1.configure(highlightcolor="black")
        self.o1.configure(insertbackground="black")
        self.o1.configure(selectbackground="blue")
        self.o1.configure(selectforeground="white")
        # shifts focus to next entry widget when pressing Enter button
        self.o1.bind('<Return>', lambda o1: self.o2.focus_set())

        self.o2 = tk.Entry(self.Frame1)
        self.o2.place(relx=0.016, rely=0.169, height=20, relwidth=0.17)
        self.o2.configure(background="white")
        self.o2.configure(disabledforeground="#a3a3a3")
        self.o2.configure(font="TkFixedFont")
        self.o2.configure(foreground="#000000")
        self.o2.configure(highlightbackground="#d9d9d9")
        self.o2.configure(highlightcolor="black")
        self.o2.configure(insertbackground="black")
        self.o2.configure(selectbackground="blue")
        self.o2.configure(selectforeground="white")
        self.o2.bind('<Return>', lambda o2: self.o3.focus_set())

        self.o3 = tk.Entry(self.Frame1)
        self.o3.place(relx=0.016, rely=0.216, height=20, relwidth=0.17)
        self.o3.configure(background="white")
        self.o3.configure(disabledforeground="#a3a3a3")
        self.o3.configure(font="TkFixedFont")
        self.o3.configure(foreground="#000000")
        self.o3.configure(highlightbackground="#d9d9d9")
        self.o3.configure(highlightcolor="black")
        self.o3.configure(insertbackground="black")
        self.o3.configure(selectbackground="blue")
        self.o3.configure(selectforeground="white")
        self.o3.bind('<Return>', lambda o3: self.o4.focus_set())

        self.o4 = tk.Entry(self.Frame1)
        self.o4.place(relx=0.016, rely=0.264, height=20, relwidth=0.17)
        self.o4.configure(background="white")
        self.o4.configure(disabledforeground="#a3a3a3")
        self.o4.configure(font="TkFixedFont")
        self.o4.configure(foreground="#000000")
        self.o4.configure(highlightbackground="#d9d9d9")
        self.o4.configure(highlightcolor="black")
        self.o4.configure(insertbackground="black")
        self.o4.configure(selectbackground="blue")
        self.o4.configure(selectforeground="white")
        self.o4.bind('<Return>', lambda o4: self.o5.focus_set())

        self.o5 = tk.Entry(self.Frame1)
        self.o5.place(relx=0.016, rely=0.313, height=20, relwidth=0.17)
        self.o5.configure(background="white")
        self.o5.configure(disabledforeground="#a3a3a3")
        self.o5.configure(font="TkFixedFont")
        self.o5.configure(foreground="#000000")
        self.o5.configure(highlightbackground="#d9d9d9")
        self.o5.configure(highlightcolor="black")
        self.o5.configure(insertbackground="black")
        self.o5.configure(selectbackground="blue")
        self.o5.configure(selectforeground="white")
        self.o5.bind('<Return>', lambda o5: self.o6.focus_set())

        self.o6 = tk.Entry(self.Frame1)
        self.o6.place(relx=0.016, rely=0.361, height=20, relwidth=0.17)
        self.o6.configure(background="white")
        self.o6.configure(disabledforeground="#a3a3a3")
        self.o6.configure(font="TkFixedFont")
        self.o6.configure(foreground="#000000")
        self.o6.configure(highlightbackground="#d9d9d9")
        self.o6.configure(highlightcolor="black")
        self.o6.configure(insertbackground="black")
        self.o6.configure(selectbackground="blue")
        self.o6.configure(selectforeground="white")
        self.o6.bind('<Return>', lambda o6: self.o7.focus_set())

        self.o7 = tk.Entry(self.Frame1)
        self.o7.place(relx=0.016, rely=0.408, height=20, relwidth=0.17)
        self.o7.configure(background="white")
        self.o7.configure(disabledforeground="#a3a3a3")
        self.o7.configure(font="TkFixedFont")
        self.o7.configure(foreground="#000000")
        self.o7.configure(highlightbackground="#d9d9d9")
        self.o7.configure(highlightcolor="black")
        self.o7.configure(insertbackground="black")
        self.o7.configure(selectbackground="blue")
        self.o7.configure(selectforeground="white")
        self.o7.bind('<Return>', lambda o7: self.o8.focus_set())

        self.o8 = tk.Entry(self.Frame1)
        self.o8.place(relx=0.016, rely=0.458, height=20, relwidth=0.17)
        self.o8.configure(background="white")
        self.o8.configure(disabledforeground="#a3a3a3")
        self.o8.configure(font="TkFixedFont")
        self.o8.configure(foreground="#000000")
        self.o8.configure(highlightbackground="#d9d9d9")
        self.o8.configure(highlightcolor="black")
        self.o8.configure(insertbackground="black")
        self.o8.configure(selectbackground="blue")
        self.o8.configure(selectforeground="white")
        self.o8.bind('<Return>', lambda o8: self.o9.focus_set())

        self.o9 = tk.Entry(self.Frame1)
        self.o9.place(relx=0.016, rely=0.505, height=20, relwidth=0.17)
        self.o9.configure(background="white")
        self.o9.configure(disabledforeground="#a3a3a3")
        self.o9.configure(font="TkFixedFont")
        self.o9.configure(foreground="#000000")
        self.o9.configure(highlightbackground="#d9d9d9")
        self.o9.configure(highlightcolor="black")
        self.o9.configure(insertbackground="black")
        self.o9.configure(selectbackground="blue")
        self.o9.configure(selectforeground="white")
        self.o9.bind('<Return>', lambda o9: self.o10.focus_set())

        self.o10 = tk.Entry(self.Frame1)
        self.o10.place(relx=0.016, rely=0.552, height=20, relwidth=0.17)
        self.o10.configure(background="white")
        self.o10.configure(disabledforeground="#a3a3a3")
        self.o10.configure(font="TkFixedFont")
        self.o10.configure(foreground="#000000")
        self.o10.configure(highlightbackground="#d9d9d9")
        self.o10.configure(highlightcolor="black")
        self.o10.configure(insertbackground="black")
        self.o10.configure(selectbackground="blue")
        self.o10.configure(selectforeground="white")
        self.o10.bind('<Return>', lambda o10: self.o11.focus_set())


        self.o11 = tk.Entry(self.Frame1)
        self.o11.place(relx=0.016, rely=0.602, height=20, relwidth=0.17)
        self.o11.configure(background="white")
        self.o11.configure(disabledforeground="#a3a3a3")
        self.o11.configure(font="TkFixedFont")
        self.o11.configure(foreground="#000000")
        self.o11.configure(highlightbackground="#d9d9d9")
        self.o11.configure(highlightcolor="black")
        self.o11.configure(insertbackground="black")
        self.o11.configure(selectbackground="blue")
        self.o11.configure(selectforeground="white")
        self.o11.bind('<Return>', lambda o11: self.o12.focus_set())


        self.o12 = tk.Entry(self.Frame1)
        self.o12.place(relx=0.016, rely=0.649, height=20, relwidth=0.17)
        self.o12.configure(background="white")
        self.o12.configure(disabledforeground="#a3a3a3")
        self.o12.configure(font="TkFixedFont")
        self.o12.configure(foreground="#000000")
        self.o12.configure(highlightbackground="#d9d9d9")
        self.o12.configure(highlightcolor="black")
        self.o12.configure(insertbackground="black")
        self.o12.configure(selectbackground="blue")
        self.o12.configure(selectforeground="white")
        self.o12.bind('<Return>', lambda o12: self.o13.focus_set())


        self.o14 = tk.Entry(self.Frame1)
        self.o14.place(relx=0.016, rely=0.746, height=20, relwidth=0.17)
        self.o14.configure(background="white")
        self.o14.configure(disabledforeground="#a3a3a3")
        self.o14.configure(font="TkFixedFont")
        self.o14.configure(foreground="#000000")
        self.o14.configure(highlightbackground="#d9d9d9")
        self.o14.configure(highlightcolor="black")
        self.o14.configure(insertbackground="black")
        self.o14.configure(selectbackground="blue")
        self.o14.configure(selectforeground="white")
        self.o14.bind('<Return>', lambda o14: self.o15.focus_set())

        self.o15 = tk.Entry(self.Frame1)
        self.o15.place(relx=0.016, rely=0.794, height=20, relwidth=0.17)
        self.o15.configure(background="white")
        self.o15.configure(disabledforeground="#a3a3a3")
        self.o15.configure(font="TkFixedFont")
        self.o15.configure(foreground="#000000")
        self.o15.configure(highlightbackground="#d9d9d9")
        self.o15.configure(highlightcolor="black")
        self.o15.configure(insertbackground="black")
        self.o15.configure(selectbackground="blue")
        self.o15.configure(selectforeground="white")

        self.o13 = tk.Entry(self.Frame1)
        self.o13.place(relx=0.016, rely=0.697, height=20, relwidth=0.17)
        self.o13.configure(background="white")
        self.o13.configure(disabledforeground="#a3a3a3")
        self.o13.configure(font="TkFixedFont")
        self.o13.configure(foreground="#000000")
        self.o13.configure(highlightbackground="#d9d9d9")
        self.o13.configure(highlightcolor="black")
        self.o13.configure(insertbackground="black")
        self.o13.configure(selectbackground="blue")
        self.o13.configure(selectforeground="white")
        self.o13.bind('<Return>', lambda o13: self.o14.focus_set())

        # create frame for label "Observations", will contain the label
        self.observationframe = tk.LabelFrame(self.Frame1)
        self.observationframe.place(relx=0.009, rely=0.005, relheight=0.102
                , relwidth=0.179)
        self.observationframe.configure(relief='groove')
        self.observationframe.configure(foreground="black")
        self.observationframe.configure(text='''Observations''')
        self.observationframe.configure(background="#d9d9d9")
        self.observationframe.configure(highlightbackground="#d9d9d9")
        self.observationframe.configure(highlightcolor="black")

        # create label
        self.Observation = tk.Label(self.observationframe)
        self.Observation.place(relx=0.061, rely=0.366, height=17, width=170
                , bordermode='ignore')
        self.Observation.configure(activebackground="#f9f9f9")
        self.Observation.configure(activeforeground="black")
        self.Observation.configure(anchor='w')
        self.Observation.configure(background="#d9d9d9")
        self.Observation.configure(compound='left')
        self.Observation.configure(disabledforeground="#a3a3a3")
        self.Observation.configure(foreground="#000000")
        self.Observation.configure(highlightbackground="#d9d9d9")
        self.Observation.configure(highlightcolor="black")
        self.Observation.configure(text='''x''')

        # create frame for label mean
        self.meanframe = tk.LabelFrame(self.Frame1)
        self.meanframe.place(relx=0.206, rely=0.0, relheight=0.107
                , relwidth=0.17)
        self.meanframe.configure(relief='groove')
        self.meanframe.configure(foreground="black")
        self.meanframe.configure(text='''Mean''')
        self.meanframe.configure(background="#d9d9d9")
        self.meanframe.configure(highlightbackground="#d9d9d9")
        self.meanframe.configure(highlightcolor="black")

        # create label for mean
        self.meanLabel = tk.Label(self.meanframe)
        self.meanLabel.place(relx=0.426, rely=0.349, height=20, width=34
                , bordermode='ignore')
        self.meanLabel.configure(activebackground="#f9f9f9")
        self.meanLabel.configure(activeforeground="black")
        self.meanLabel.configure(anchor='w')
        self.meanLabel.configure(background="#d9d9d9")
        self.meanLabel.configure(compound='left')
        self.meanLabel.configure(disabledforeground="#a3a3a3")
        self.meanLabel.configure(foreground="#000000")
        self.meanLabel.configure(highlightbackground="#d9d9d9")
        self.meanLabel.configure(highlightcolor="black")
        self.meanLabel.configure(text='''x̄''')

        # create entry widgets for mean column, 15 total. 'm' for mean
        self.m1 = tk.Entry(self.Frame1)
        self.m1.place(relx=0.222, rely=0.119, height=20, relwidth=0.152)
        self.m1.configure(background="white")
        self.m1.configure(disabledforeground="#a3a3a3")
        self.m1.configure(font="TkFixedFont")
        self.m1.configure(foreground="#000000")
        self.m1.configure(highlightbackground="#d9d9d9")
        self.m1.configure(highlightcolor="black")
        self.m1.configure(insertbackground="black")
        self.m1.configure(selectbackground="blue")
        self.m1.configure(selectforeground="white")

        self.m2 = tk.Entry(self.Frame1)
        self.m2.place(relx=0.222, rely=0.169, height=20, relwidth=0.152)
        self.m2.configure(background="white")
        self.m2.configure(disabledforeground="#a3a3a3")
        self.m2.configure(font="TkFixedFont")
        self.m2.configure(foreground="#000000")
        self.m2.configure(highlightbackground="#d9d9d9")
        self.m2.configure(highlightcolor="black")
        self.m2.configure(insertbackground="black")
        self.m2.configure(selectbackground="blue")
        self.m2.configure(selectforeground="white")

        self.m3 = tk.Entry(self.Frame1)
        self.m3.place(relx=0.222, rely=0.216, height=20, relwidth=0.152)
        self.m3.configure(background="white")
        self.m3.configure(disabledforeground="#a3a3a3")
        self.m3.configure(font="TkFixedFont")
        self.m3.configure(foreground="#000000")
        self.m3.configure(highlightbackground="#d9d9d9")
        self.m3.configure(highlightcolor="black")
        self.m3.configure(insertbackground="black")
        self.m3.configure(selectbackground="blue")
        self.m3.configure(selectforeground="white")

        self.m4 = tk.Entry(self.Frame1)
        self.m4.place(relx=0.222, rely=0.264, height=20, relwidth=0.152)
        self.m4.configure(background="white")
        self.m4.configure(disabledforeground="#a3a3a3")
        self.m4.configure(font="TkFixedFont")
        self.m4.configure(foreground="#000000")
        self.m4.configure(highlightbackground="#d9d9d9")
        self.m4.configure(highlightcolor="black")
        self.m4.configure(insertbackground="black")
        self.m4.configure(selectbackground="blue")
        self.m4.configure(selectforeground="white")

        self.m5 = tk.Entry(self.Frame1)
        self.m5.place(relx=0.222, rely=0.313, height=20, relwidth=0.152)
        self.m5.configure(background="white")
        self.m5.configure(disabledforeground="#a3a3a3")
        self.m5.configure(font="TkFixedFont")
        self.m5.configure(foreground="#000000")
        self.m5.configure(highlightbackground="#d9d9d9")
        self.m5.configure(highlightcolor="black")
        self.m5.configure(insertbackground="black")
        self.m5.configure(selectbackground="blue")
        self.m5.configure(selectforeground="white")

        self.m6 = tk.Entry(self.Frame1)
        self.m6.place(relx=0.222, rely=0.361, height=20, relwidth=0.152)
        self.m6.configure(background="white")
        self.m6.configure(disabledforeground="#a3a3a3")
        self.m6.configure(font="TkFixedFont")
        self.m6.configure(foreground="#000000")
        self.m6.configure(highlightbackground="#d9d9d9")
        self.m6.configure(highlightcolor="black")
        self.m6.configure(insertbackground="black")
        self.m6.configure(selectbackground="blue")
        self.m6.configure(selectforeground="white")

        self.m7 = tk.Entry(self.Frame1)
        self.m7.place(relx=0.222, rely=0.408, height=20, relwidth=0.152)
        self.m7.configure(background="white")
        self.m7.configure(disabledforeground="#a3a3a3")
        self.m7.configure(font="TkFixedFont")
        self.m7.configure(foreground="#000000")
        self.m7.configure(highlightbackground="#d9d9d9")
        self.m7.configure(highlightcolor="black")
        self.m7.configure(insertbackground="black")
        self.m7.configure(selectbackground="blue")
        self.m7.configure(selectforeground="white")

        self.m8 = tk.Entry(self.Frame1)
        self.m8.place(relx=0.222, rely=0.458, height=20, relwidth=0.152)
        self.m8.configure(background="white")
        self.m8.configure(disabledforeground="#a3a3a3")
        self.m8.configure(font="TkFixedFont")
        self.m8.configure(foreground="#000000")
        self.m8.configure(highlightbackground="#d9d9d9")
        self.m8.configure(highlightcolor="black")
        self.m8.configure(insertbackground="black")
        self.m8.configure(selectbackground="blue")
        self.m8.configure(selectforeground="white")

        self.m9 = tk.Entry(self.Frame1)
        self.m9.place(relx=0.222, rely=0.505, height=20, relwidth=0.152)
        self.m9.configure(background="white")
        self.m9.configure(disabledforeground="#a3a3a3")
        self.m9.configure(font="TkFixedFont")
        self.m9.configure(foreground="#000000")
        self.m9.configure(highlightbackground="#d9d9d9")
        self.m9.configure(highlightcolor="black")
        self.m9.configure(insertbackground="black")
        self.m9.configure(selectbackground="blue")
        self.m9.configure(selectforeground="white")

        self.m10 = tk.Entry(self.Frame1)
        self.m10.place(relx=0.222, rely=0.552, height=20, relwidth=0.152)
        self.m10.configure(background="white")
        self.m10.configure(disabledforeground="#a3a3a3")
        self.m10.configure(font="TkFixedFont")
        self.m10.configure(foreground="#000000")
        self.m10.configure(highlightbackground="#d9d9d9")
        self.m10.configure(highlightcolor="black")
        self.m10.configure(insertbackground="black")
        self.m10.configure(selectbackground="blue")
        self.m10.configure(selectforeground="white")

        self.m11 = tk.Entry(self.Frame1)
        self.m11.place(relx=0.222, rely=0.602, height=20, relwidth=0.152)
        self.m11.configure(background="white")
        self.m11.configure(disabledforeground="#a3a3a3")
        self.m11.configure(font="TkFixedFont")
        self.m11.configure(foreground="#000000")
        self.m11.configure(highlightbackground="#d9d9d9")
        self.m11.configure(highlightcolor="black")
        self.m11.configure(insertbackground="black")
        self.m11.configure(selectbackground="blue")
        self.m11.configure(selectforeground="white")

        self.m12 = tk.Entry(self.Frame1)
        self.m12.place(relx=0.222, rely=0.649, height=20, relwidth=0.152)
        self.m12.configure(background="white")
        self.m12.configure(disabledforeground="#a3a3a3")
        self.m12.configure(font="TkFixedFont")
        self.m12.configure(foreground="#000000")
        self.m12.configure(highlightbackground="#d9d9d9")
        self.m12.configure(highlightcolor="black")
        self.m12.configure(insertbackground="black")
        self.m12.configure(selectbackground="blue")
        self.m12.configure(selectforeground="white")

        self.m13 = tk.Entry(self.Frame1)
        self.m13.place(relx=0.222, rely=0.697, height=20, relwidth=0.152)
        self.m13.configure(background="white")
        self.m13.configure(disabledforeground="#a3a3a3")
        self.m13.configure(font="TkFixedFont")
        self.m13.configure(foreground="#000000")
        self.m13.configure(highlightbackground="#d9d9d9")
        self.m13.configure(highlightcolor="black")
        self.m13.configure(insertbackground="black")
        self.m13.configure(selectbackground="blue")
        self.m13.configure(selectforeground="white")

        self.m14 = tk.Entry(self.Frame1)
        self.m14.place(relx=0.222, rely=0.744, height=20, relwidth=0.152)
        self.m14.configure(background="white")
        self.m14.configure(disabledforeground="#a3a3a3")
        self.m14.configure(font="TkFixedFont")
        self.m14.configure(foreground="#000000")
        self.m14.configure(highlightbackground="#d9d9d9")
        self.m14.configure(highlightcolor="black")
        self.m14.configure(insertbackground="black")
        self.m14.configure(selectbackground="blue")
        self.m14.configure(selectforeground="white")

        self.m15 = tk.Entry(self.Frame1)
        self.m15.place(relx=0.222, rely=0.794, height=20, relwidth=0.152)
        self.m15.configure(background="white")
        self.m15.configure(disabledforeground="#a3a3a3")
        self.m15.configure(font="TkFixedFont")
        self.m15.configure(foreground="#000000")
        self.m15.configure(highlightbackground="#d9d9d9")
        self.m15.configure(highlightcolor="black")
        self.m15.configure(insertbackground="black")
        self.m15.configure(selectbackground="blue")
        self.m15.configure(selectforeground="white")

        # create frame that will contain the observation - mean label
        self.obs_meanFrame = tk.LabelFrame(self.Frame1)
        self.obs_meanFrame.place(relx=0.41, rely=0.0, relheight=0.107
                , relwidth=0.222)
        self.obs_meanFrame.configure(relief='groove')
        self.obs_meanFrame.configure(foreground="black")
        self.obs_meanFrame.configure(text='''Observation - Mean''')
        self.obs_meanFrame.configure(background="#d9d9d9")
        self.obs_meanFrame.configure(highlightbackground="#d9d9d9")
        self.obs_meanFrame.configure(highlightcolor="black")

        # create label for the observation - mean column
        self.Label1_1 = tk.Label(self.obs_meanFrame)
        self.Label1_1.place(relx=0.325, rely=0.349, height=20, width=39
                , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''x - x̄''')

        # create label widget for observation - mean column
        self.obs_mean1 = tk.Entry(self.Frame1)
        self.obs_mean1.place(relx=0.444, rely=0.119, height=20, relwidth=0.152)
        self.obs_mean1.configure(background="white")
        self.obs_mean1.configure(disabledforeground="#a3a3a3")
        self.obs_mean1.configure(font="TkFixedFont")
        self.obs_mean1.configure(foreground="#000000")
        self.obs_mean1.configure(highlightbackground="#d9d9d9")
        self.obs_mean1.configure(highlightcolor="black")
        self.obs_mean1.configure(insertbackground="black")
        self.obs_mean1.configure(selectbackground="blue")
        self.obs_mean1.configure(selectforeground="white")

        self.obs_mean2 = tk.Entry(self.Frame1)
        self.obs_mean2.place(relx=0.444, rely=0.169, height=20, relwidth=0.152)
        self.obs_mean2.configure(background="white")
        self.obs_mean2.configure(disabledforeground="#a3a3a3")
        self.obs_mean2.configure(font="TkFixedFont")
        self.obs_mean2.configure(foreground="#000000")
        self.obs_mean2.configure(highlightbackground="#d9d9d9")
        self.obs_mean2.configure(highlightcolor="black")
        self.obs_mean2.configure(insertbackground="black")
        self.obs_mean2.configure(selectbackground="blue")
        self.obs_mean2.configure(selectforeground="white")

        self.obs_mean3 = tk.Entry(self.Frame1)
        self.obs_mean3.place(relx=0.444, rely=0.216, height=20, relwidth=0.152)
        self.obs_mean3.configure(background="white")
        self.obs_mean3.configure(disabledforeground="#a3a3a3")
        self.obs_mean3.configure(font="TkFixedFont")
        self.obs_mean3.configure(foreground="#000000")
        self.obs_mean3.configure(highlightbackground="#d9d9d9")
        self.obs_mean3.configure(highlightcolor="black")
        self.obs_mean3.configure(insertbackground="black")
        self.obs_mean3.configure(selectbackground="blue")
        self.obs_mean3.configure(selectforeground="white")

        self.obs_mean4 = tk.Entry(self.Frame1)
        self.obs_mean4.place(relx=0.444, rely=0.264, height=20, relwidth=0.152)
        self.obs_mean4.configure(background="white")
        self.obs_mean4.configure(disabledforeground="#a3a3a3")
        self.obs_mean4.configure(font="TkFixedFont")
        self.obs_mean4.configure(foreground="#000000")
        self.obs_mean4.configure(highlightbackground="#d9d9d9")
        self.obs_mean4.configure(highlightcolor="black")
        self.obs_mean4.configure(insertbackground="black")
        self.obs_mean4.configure(selectbackground="blue")
        self.obs_mean4.configure(selectforeground="white")

        self.obs_mean5 = tk.Entry(self.Frame1)
        self.obs_mean5.place(relx=0.444, rely=0.313, height=20, relwidth=0.152)
        self.obs_mean5.configure(background="white")
        self.obs_mean5.configure(disabledforeground="#a3a3a3")
        self.obs_mean5.configure(font="TkFixedFont")
        self.obs_mean5.configure(foreground="#000000")
        self.obs_mean5.configure(highlightbackground="#d9d9d9")
        self.obs_mean5.configure(highlightcolor="black")
        self.obs_mean5.configure(insertbackground="black")
        self.obs_mean5.configure(selectbackground="blue")
        self.obs_mean5.configure(selectforeground="white")

        self.obs_mean6 = tk.Entry(self.Frame1)
        self.obs_mean6.place(relx=0.444, rely=0.361, height=20, relwidth=0.152)
        self.obs_mean6.configure(background="white")
        self.obs_mean6.configure(disabledforeground="#a3a3a3")
        self.obs_mean6.configure(font="TkFixedFont")
        self.obs_mean6.configure(foreground="#000000")
        self.obs_mean6.configure(highlightbackground="#d9d9d9")
        self.obs_mean6.configure(highlightcolor="black")
        self.obs_mean6.configure(insertbackground="black")
        self.obs_mean6.configure(selectbackground="blue")
        self.obs_mean6.configure(selectforeground="white")

        self.obs_mean7 = tk.Entry(self.Frame1)
        self.obs_mean7.place(relx=0.444, rely=0.408, height=20, relwidth=0.152)
        self.obs_mean7.configure(background="white")
        self.obs_mean7.configure(disabledforeground="#a3a3a3")
        self.obs_mean7.configure(font="TkFixedFont")
        self.obs_mean7.configure(foreground="#000000")
        self.obs_mean7.configure(highlightbackground="#d9d9d9")
        self.obs_mean7.configure(highlightcolor="black")
        self.obs_mean7.configure(insertbackground="black")
        self.obs_mean7.configure(selectbackground="blue")
        self.obs_mean7.configure(selectforeground="white")

        self.obs_mean8 = tk.Entry(self.Frame1)
        self.obs_mean8.place(relx=0.444, rely=0.458, height=20, relwidth=0.152)
        self.obs_mean8.configure(background="white")
        self.obs_mean8.configure(disabledforeground="#a3a3a3")
        self.obs_mean8.configure(font="TkFixedFont")
        self.obs_mean8.configure(foreground="#000000")
        self.obs_mean8.configure(highlightbackground="#d9d9d9")
        self.obs_mean8.configure(highlightcolor="black")
        self.obs_mean8.configure(insertbackground="black")
        self.obs_mean8.configure(selectbackground="blue")
        self.obs_mean8.configure(selectforeground="white")

        self.obs_mean9 = tk.Entry(self.Frame1)
        self.obs_mean9.place(relx=0.444, rely=0.505, height=20, relwidth=0.152)
        self.obs_mean9.configure(background="white")
        self.obs_mean9.configure(disabledforeground="#a3a3a3")
        self.obs_mean9.configure(font="TkFixedFont")
        self.obs_mean9.configure(foreground="#000000")
        self.obs_mean9.configure(highlightbackground="#d9d9d9")
        self.obs_mean9.configure(highlightcolor="black")
        self.obs_mean9.configure(insertbackground="black")
        self.obs_mean9.configure(selectbackground="blue")
        self.obs_mean9.configure(selectforeground="white")

        self.obs_mean10 = tk.Entry(self.Frame1)
        self.obs_mean10.place(relx=0.444, rely=0.552, height=20, relwidth=0.152)
        self.obs_mean10.configure(background="white")
        self.obs_mean10.configure(disabledforeground="#a3a3a3")
        self.obs_mean10.configure(font="TkFixedFont")
        self.obs_mean10.configure(foreground="#000000")
        self.obs_mean10.configure(highlightbackground="#d9d9d9")
        self.obs_mean10.configure(highlightcolor="black")
        self.obs_mean10.configure(insertbackground="black")
        self.obs_mean10.configure(selectbackground="blue")
        self.obs_mean10.configure(selectforeground="white")

        self.obs_mean11 = tk.Entry(self.Frame1)
        self.obs_mean11.place(relx=0.444, rely=0.602, height=20, relwidth=0.152)
        self.obs_mean11.configure(background="white")
        self.obs_mean11.configure(disabledforeground="#a3a3a3")
        self.obs_mean11.configure(font="TkFixedFont")
        self.obs_mean11.configure(foreground="#000000")
        self.obs_mean11.configure(highlightbackground="#d9d9d9")
        self.obs_mean11.configure(highlightcolor="black")
        self.obs_mean11.configure(insertbackground="black")
        self.obs_mean11.configure(selectbackground="blue")
        self.obs_mean11.configure(selectforeground="white")

        self.obs_mean12 = tk.Entry(self.Frame1)
        self.obs_mean12.place(relx=0.444, rely=0.649, height=20, relwidth=0.152)
        self.obs_mean12.configure(background="white")
        self.obs_mean12.configure(disabledforeground="#a3a3a3")
        self.obs_mean12.configure(font="TkFixedFont")
        self.obs_mean12.configure(foreground="#000000")
        self.obs_mean12.configure(highlightbackground="#d9d9d9")
        self.obs_mean12.configure(highlightcolor="black")
        self.obs_mean12.configure(insertbackground="black")
        self.obs_mean12.configure(selectbackground="blue")
        self.obs_mean12.configure(selectforeground="white")

        self.obs_mean13 = tk.Entry(self.Frame1)
        self.obs_mean13.place(relx=0.444, rely=0.697, height=20, relwidth=0.152)
        self.obs_mean13.configure(background="white")
        self.obs_mean13.configure(disabledforeground="#a3a3a3")
        self.obs_mean13.configure(font="TkFixedFont")
        self.obs_mean13.configure(foreground="#000000")
        self.obs_mean13.configure(highlightbackground="#d9d9d9")
        self.obs_mean13.configure(highlightcolor="black")
        self.obs_mean13.configure(insertbackground="black")
        self.obs_mean13.configure(selectbackground="blue")
        self.obs_mean13.configure(selectforeground="white")

        self.obs_mean14 = tk.Entry(self.Frame1)
        self.obs_mean14.place(relx=0.444, rely=0.744, height=20, relwidth=0.152)
        self.obs_mean14.configure(background="white")
        self.obs_mean14.configure(disabledforeground="#a3a3a3")
        self.obs_mean14.configure(font="TkFixedFont")
        self.obs_mean14.configure(foreground="#000000")
        self.obs_mean14.configure(highlightbackground="#d9d9d9")
        self.obs_mean14.configure(highlightcolor="black")
        self.obs_mean14.configure(insertbackground="black")
        self.obs_mean14.configure(selectbackground="blue")
        self.obs_mean14.configure(selectforeground="white")

        self.obs_mean15 = tk.Entry(self.Frame1)
        self.obs_mean15.place(relx=0.444, rely=0.794, height=20, relwidth=0.152)
        self.obs_mean15.configure(background="white")
        self.obs_mean15.configure(disabledforeground="#a3a3a3")
        self.obs_mean15.configure(font="TkFixedFont")
        self.obs_mean15.configure(foreground="#000000")
        self.obs_mean15.configure(highlightbackground="#d9d9d9")
        self.obs_mean15.configure(highlightcolor="black")
        self.obs_mean15.configure(insertbackground="black")
        self.obs_mean15.configure(selectbackground="blue")
        self.obs_mean15.configure(selectforeground="white")

        # create frame for the squared version of observation - mean
        self.obs_meanFrame_sqrd = tk.LabelFrame(self.Frame1)
        self.obs_meanFrame_sqrd.place(relx=0.668, rely=0.0, relheight=0.107
                , relwidth=0.273)
        self.obs_meanFrame_sqrd.configure(relief='groove')
        self.obs_meanFrame_sqrd.configure(foreground="black")
        self.obs_meanFrame_sqrd.configure(text='''(Observation - Mean)²''')
        self.obs_meanFrame_sqrd.configure(background="#d9d9d9")
        self.obs_meanFrame_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_meanFrame_sqrd.configure(highlightcolor="black")

        # create label for the squared version of observation - mean
        self.Label1_1_1 = tk.Label(self.obs_meanFrame_sqrd)
        self.Label1_1_1.place(relx=0.265, rely=0.349, height=20, width=43
                , bordermode='ignore')
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#d9d9d9")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''(x - x̄)²''')

        # create entry widgets for sqrd of observation-mean
        self.obs_mean1_sqrd = tk.Entry(self.Frame1)
        self.obs_mean1_sqrd.place(relx=0.724, rely=0.119, height=20
                , relwidth=0.152)
        self.obs_mean1_sqrd.configure(background="white")
        self.obs_mean1_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean1_sqrd.configure(font="TkFixedFont")
        self.obs_mean1_sqrd.configure(foreground="#000000")
        self.obs_mean1_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean1_sqrd.configure(highlightcolor="black")
        self.obs_mean1_sqrd.configure(insertbackground="black")
        self.obs_mean1_sqrd.configure(selectbackground="blue")
        self.obs_mean1_sqrd.configure(selectforeground="white")

        self.obs_mean2_sqrd = tk.Entry(self.Frame1)
        self.obs_mean2_sqrd.place(relx=0.724, rely=0.169, height=20
                , relwidth=0.152)
        self.obs_mean2_sqrd.configure(background="white")
        self.obs_mean2_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean2_sqrd.configure(font="TkFixedFont")
        self.obs_mean2_sqrd.configure(foreground="#000000")
        self.obs_mean2_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean2_sqrd.configure(highlightcolor="black")
        self.obs_mean2_sqrd.configure(insertbackground="black")
        self.obs_mean2_sqrd.configure(selectbackground="blue")
        self.obs_mean2_sqrd.configure(selectforeground="white")

        self.obs_mean3_sqrd = tk.Entry(self.Frame1)
        self.obs_mean3_sqrd.place(relx=0.724, rely=0.216, height=20
                , relwidth=0.152)
        self.obs_mean3_sqrd.configure(background="white")
        self.obs_mean3_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean3_sqrd.configure(font="TkFixedFont")
        self.obs_mean3_sqrd.configure(foreground="#000000")
        self.obs_mean3_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean3_sqrd.configure(highlightcolor="black")
        self.obs_mean3_sqrd.configure(insertbackground="black")
        self.obs_mean3_sqrd.configure(selectbackground="blue")
        self.obs_mean3_sqrd.configure(selectforeground="white")

        self.obs_mean4_sqrd = tk.Entry(self.Frame1)
        self.obs_mean4_sqrd.place(relx=0.724, rely=0.264, height=20
                , relwidth=0.152)
        self.obs_mean4_sqrd.configure(background="white")
        self.obs_mean4_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean4_sqrd.configure(font="TkFixedFont")
        self.obs_mean4_sqrd.configure(foreground="#000000")
        self.obs_mean4_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean4_sqrd.configure(highlightcolor="black")
        self.obs_mean4_sqrd.configure(insertbackground="black")
        self.obs_mean4_sqrd.configure(selectbackground="blue")
        self.obs_mean4_sqrd.configure(selectforeground="white")

        self.obs_mean5_sqrd = tk.Entry(self.Frame1)
        self.obs_mean5_sqrd.place(relx=0.724, rely=0.313, height=20
                , relwidth=0.152)
        self.obs_mean5_sqrd.configure(background="white")
        self.obs_mean5_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean5_sqrd.configure(font="TkFixedFont")
        self.obs_mean5_sqrd.configure(foreground="#000000")
        self.obs_mean5_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean5_sqrd.configure(highlightcolor="black")
        self.obs_mean5_sqrd.configure(insertbackground="black")
        self.obs_mean5_sqrd.configure(selectbackground="blue")
        self.obs_mean5_sqrd.configure(selectforeground="white")

        self.obs_mean6_sqrd = tk.Entry(self.Frame1)
        self.obs_mean6_sqrd.place(relx=0.724, rely=0.361, height=20
                , relwidth=0.152)
        self.obs_mean6_sqrd.configure(background="white")
        self.obs_mean6_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean6_sqrd.configure(font="TkFixedFont")
        self.obs_mean6_sqrd.configure(foreground="#000000")
        self.obs_mean6_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean6_sqrd.configure(highlightcolor="black")
        self.obs_mean6_sqrd.configure(insertbackground="black")
        self.obs_mean6_sqrd.configure(selectbackground="blue")
        self.obs_mean6_sqrd.configure(selectforeground="white")

        self.obs_mean7_sqrd = tk.Entry(self.Frame1)
        self.obs_mean7_sqrd.place(relx=0.724, rely=0.408, height=20
                , relwidth=0.152)
        self.obs_mean7_sqrd.configure(background="white")
        self.obs_mean7_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean7_sqrd.configure(font="TkFixedFont")
        self.obs_mean7_sqrd.configure(foreground="#000000")
        self.obs_mean7_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean7_sqrd.configure(highlightcolor="black")
        self.obs_mean7_sqrd.configure(insertbackground="black")
        self.obs_mean7_sqrd.configure(selectbackground="blue")
        self.obs_mean7_sqrd.configure(selectforeground="white")

        self.obs_mean8_sqrd = tk.Entry(self.Frame1)
        self.obs_mean8_sqrd.place(relx=0.724, rely=0.458, height=20
                , relwidth=0.152)
        self.obs_mean8_sqrd.configure(background="white")
        self.obs_mean8_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean8_sqrd.configure(font="TkFixedFont")
        self.obs_mean8_sqrd.configure(foreground="#000000")
        self.obs_mean8_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean8_sqrd.configure(highlightcolor="black")
        self.obs_mean8_sqrd.configure(insertbackground="black")
        self.obs_mean8_sqrd.configure(selectbackground="blue")
        self.obs_mean8_sqrd.configure(selectforeground="white")

        self.obs_mean9_sqrd = tk.Entry(self.Frame1)
        self.obs_mean9_sqrd.place(relx=0.724, rely=0.505, height=20
                , relwidth=0.152)
        self.obs_mean9_sqrd.configure(background="white")
        self.obs_mean9_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean9_sqrd.configure(font="TkFixedFont")
        self.obs_mean9_sqrd.configure(foreground="#000000")
        self.obs_mean9_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean9_sqrd.configure(highlightcolor="black")
        self.obs_mean9_sqrd.configure(insertbackground="black")
        self.obs_mean9_sqrd.configure(selectbackground="blue")
        self.obs_mean9_sqrd.configure(selectforeground="white")

        self.obs_mean10_sqrd = tk.Entry(self.Frame1)
        self.obs_mean10_sqrd.place(relx=0.724, rely=0.552, height=20
                , relwidth=0.152)
        self.obs_mean10_sqrd.configure(background="white")
        self.obs_mean10_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean10_sqrd.configure(font="TkFixedFont")
        self.obs_mean10_sqrd.configure(foreground="#000000")
        self.obs_mean10_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean10_sqrd.configure(highlightcolor="black")
        self.obs_mean10_sqrd.configure(insertbackground="black")
        self.obs_mean10_sqrd.configure(selectbackground="blue")
        self.obs_mean10_sqrd.configure(selectforeground="white")

        self.obs_mean11_sqrd = tk.Entry(self.Frame1)
        self.obs_mean11_sqrd.place(relx=0.724, rely=0.602, height=20
                , relwidth=0.152)
        self.obs_mean11_sqrd.configure(background="white")
        self.obs_mean11_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean11_sqrd.configure(font="TkFixedFont")
        self.obs_mean11_sqrd.configure(foreground="#000000")
        self.obs_mean11_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean11_sqrd.configure(highlightcolor="black")
        self.obs_mean11_sqrd.configure(insertbackground="black")
        self.obs_mean11_sqrd.configure(selectbackground="blue")
        self.obs_mean11_sqrd.configure(selectforeground="white")

        self.obs_mean12_sqrd = tk.Entry(self.Frame1)
        self.obs_mean12_sqrd.place(relx=0.724, rely=0.649, height=20
                , relwidth=0.152)
        self.obs_mean12_sqrd.configure(background="white")
        self.obs_mean12_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean12_sqrd.configure(font="TkFixedFont")
        self.obs_mean12_sqrd.configure(foreground="#000000")
        self.obs_mean12_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean12_sqrd.configure(highlightcolor="black")
        self.obs_mean12_sqrd.configure(insertbackground="black")
        self.obs_mean12_sqrd.configure(selectbackground="blue")
        self.obs_mean12_sqrd.configure(selectforeground="white")

        self.obs_mean13_sqrd = tk.Entry(self.Frame1)
        self.obs_mean13_sqrd.place(relx=0.724, rely=0.697, height=20
                , relwidth=0.152)
        self.obs_mean13_sqrd.configure(background="white")
        self.obs_mean13_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean13_sqrd.configure(font="TkFixedFont")
        self.obs_mean13_sqrd.configure(foreground="#000000")
        self.obs_mean13_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean13_sqrd.configure(highlightcolor="black")
        self.obs_mean13_sqrd.configure(insertbackground="black")
        self.obs_mean13_sqrd.configure(selectbackground="blue")
        self.obs_mean13_sqrd.configure(selectforeground="white")

        self.obs_mean14_sqrd = tk.Entry(self.Frame1)
        self.obs_mean14_sqrd.place(relx=0.724, rely=0.744, height=20
                , relwidth=0.152)
        self.obs_mean14_sqrd.configure(background="white")
        self.obs_mean14_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean14_sqrd.configure(font="TkFixedFont")
        self.obs_mean14_sqrd.configure(foreground="#000000")
        self.obs_mean14_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean14_sqrd.configure(highlightcolor="black")
        self.obs_mean14_sqrd.configure(insertbackground="black")
        self.obs_mean14_sqrd.configure(selectbackground="blue")
        self.obs_mean14_sqrd.configure(selectforeground="white")

        self.obs_mean15_sqrd = tk.Entry(self.Frame1)
        self.obs_mean15_sqrd.place(relx=0.724, rely=0.794, height=20
                , relwidth=0.152)
        self.obs_mean15_sqrd.configure(background="white")
        self.obs_mean15_sqrd.configure(disabledforeground="#a3a3a3")
        self.obs_mean15_sqrd.configure(font="TkFixedFont")
        self.obs_mean15_sqrd.configure(foreground="#000000")
        self.obs_mean15_sqrd.configure(highlightbackground="#d9d9d9")
        self.obs_mean15_sqrd.configure(highlightcolor="black")
        self.obs_mean15_sqrd.configure(insertbackground="black")
        self.obs_mean15_sqrd.configure(selectbackground="blue")
        self.obs_mean15_sqrd.configure(selectforeground="white")

        # create button for clearing all entries except the user inputs(observation column)
        self.clearBtn = tk.Button(self.Frame1)
        self.clearBtn.place(relx=0.054, rely=0.871, height=24, width=47)
        self.clearBtn.configure(activebackground="#ececec")
        self.clearBtn.configure(activeforeground="#000000")
        self.clearBtn.configure(background="#d9d9d9")
        # call the clear() func when pressing the button
        self.clearBtn.configure(command=lambda :clear())
        self.clearBtn.configure(compound='left')
        self.clearBtn.configure(disabledforeground="#a3a3a3")
        self.clearBtn.configure(foreground="#000000")
        self.clearBtn.configure(highlightbackground="#d9d9d9")
        self.clearBtn.configure(highlightcolor="black")
        self.clearBtn.configure(pady="0")
        self.clearBtn.configure(text='''Clear''')

        # create button for calculating the entries
        self.calculateBtn = tk.Button(self.Frame1)
        self.calculateBtn.place(relx=0.253, rely=0.871, height=24, width=60)
        self.calculateBtn.configure(activebackground="#ececec")
        self.calculateBtn.configure(activeforeground="#000000")
        self.calculateBtn.configure(background="#d9d9d9")
        self.calculateBtn.configure(compound='left')
        # call the calculate() func when pressing the button
        self.calculateBtn.configure(command=lambda :calculate())
        self.calculateBtn.configure(disabledforeground="#a3a3a3")
        self.calculateBtn.configure(foreground="#000000")
        self.calculateBtn.configure(highlightbackground="#d9d9d9")
        self.calculateBtn.configure(highlightcolor="black")
        self.calculateBtn.configure(pady="0")
        self.calculateBtn.configure(text='''Calculate''')

        # create entry widget for the variance result
        self.varianceResult = tk.Entry(self.Frame1)
        self.varianceResult.place(relx=0.451, rely=0.92, height=20
                , relwidth=0.152)
        self.varianceResult.configure(background="white")
        self.varianceResult.configure(disabledforeground="#a3a3a3")
        self.varianceResult.configure(font="TkFixedFont")
        self.varianceResult.configure(foreground="#000000")
        self.varianceResult.configure(highlightbackground="#d9d9d9")
        self.varianceResult.configure(highlightcolor="black")
        self.varianceResult.configure(insertbackground="black")
        self.varianceResult.configure(selectbackground="blue")
        self.varianceResult.configure(selectforeground="white")

        # create entry widget for standard deviation result
        self.varianceLabel = tk.Label(self.Frame1)
        self.varianceLabel.place(relx=0.478, rely=0.858, height=21, width=74)
        self.varianceLabel.configure(activebackground="#f9f9f9")
        self.varianceLabel.configure(activeforeground="black")
        self.varianceLabel.configure(anchor='w')
        self.varianceLabel.configure(background="#d9d9d9")
        self.varianceLabel.configure(compound='left')
        self.varianceLabel.configure(disabledforeground="#a3a3a3")
        self.varianceLabel.configure(foreground="#000000")
        self.varianceLabel.configure(highlightbackground="#d9d9d9")
        self.varianceLabel.configure(highlightcolor="black")
        self.varianceLabel.configure(text='''Variance:''')

        self.stanDevLabel = tk.Label(self.Frame1)
        self.stanDevLabel.place(relx=0.704, rely=0.858, height=21, width=114)
        self.stanDevLabel.configure(anchor='w')
        self.stanDevLabel.configure(background="#d9d9d9")
        self.stanDevLabel.configure(compound='left')
        self.stanDevLabel.configure(disabledforeground="#a3a3a3")
        self.stanDevLabel.configure(foreground="#000000")
        self.stanDevLabel.configure(text='''Standard Deviation:''')

        self.stanDevResult = tk.Entry(self.Frame1)
        self.stanDevResult.place(relx=0.722, rely=0.92, height=20, relwidth=0.17)

        self.stanDevResult.configure(background="white")
        self.stanDevResult.configure(disabledforeground="#a3a3a3")
        self.stanDevResult.configure(font="TkFixedFont")
        self.stanDevResult.configure(foreground="#000000")
        self.stanDevResult.configure(insertbackground="black")

        # clears all entry widgets except the observation column
        def clear():
            for i in [
                      self.m1, self.m2, self.m3, self.m4, self.m5,
                      self.m6, self.m7, self.m8, self.m9, self.m10,
                      self.m11, self.m12, self.m13, self.m14, self.m15,

                      self.obs_mean1, self.obs_mean2, self.obs_mean3, self.obs_mean4, self.obs_mean5,
                      self.obs_mean6, self.obs_mean7, self.obs_mean8, self.obs_mean9, self.obs_mean10,
                      self.obs_mean11, self.obs_mean12, self.obs_mean13, self.obs_mean14, self.obs_mean15,

                      self.obs_mean1_sqrd, self.obs_mean2_sqrd, self.obs_mean3_sqrd, self.obs_mean4_sqrd,
                      self.obs_mean5_sqrd, self.obs_mean5_sqrd, self.obs_mean6_sqrd, self.obs_mean7_sqrd,
                      self.obs_mean8_sqrd, self.obs_mean9_sqrd, self.obs_mean10_sqrd, self.obs_mean11_sqrd,
                      self.obs_mean12_sqrd, self.obs_mean13_sqrd, self.obs_mean14_sqrd, self.obs_mean15_sqrd,

                      self.stanDevResult, self.varianceResult]:
                i.delete(0, 'end')
        # the main function of the program, calls various functions
        def calculate():
            total = 0
            # create global variable that are used outside the function
            global observations
            global observation_column
            observations = 15
            observation_column = [self.o1, self.o2,self.o3,self.o4,self.o5,self.o6,self.o7,self.o8,self.o9,self.o10,
                                  self.o11,self.o12,self.o13,self.o14,self.o15]
            # counts the number of observations and their total
            for i in observation_column:
                if len(i.get()) == 0:
                    observations -= 1
                else:
                    total += float(i.get())
            # calculate the mean
            global mean
            mean = total / observations
            # call other functions
            insert_mean()
            insert_obs_minus_mean()
            variance_()
            standard_deviation()
            plot()
        # inserts the mean to all entries under mean column
        def insert_mean():
            global mean_column
            mean_column = [self.m1, self.m2, self.m3, self.m4, self.m5,
                           self.m6, self.m7, self.m8, self.m9, self.m10,
                           self.m11, self.m12, self.m13, self.m14, self.m15]
            for i in range(observations):
                mean_column[i].insert(0, float(round(mean, 2)))  # round off to 2 digits from the decimal point

        #  inserts corresponding values to the 3rd column
        def insert_obs_minus_mean():
            observation_minus_mean_column = [self.obs_mean1, self.obs_mean2, self.obs_mean3, self.obs_mean4,
                                             self.obs_mean5,
                                             self.obs_mean6, self.obs_mean7, self.obs_mean8, self.obs_mean9,
                                             self.obs_mean10,
                                             self.obs_mean11, self.obs_mean12, self.obs_mean13, self.obs_mean14,
                                             self.obs_mean15]
            difference_list = []
            # subtracts the mean from the observation, then insert them in the same row, then store them in a list
            for i in range(observations):
                difference = float(observation_column[i].get()) - float(mean_column[i].get())
                observation_minus_mean_column[i].insert(0, round(difference, 4))
                difference_list.append(float(round(difference, 4)))
            # every entry in the list is squared and inserted to the same row, next column
            observation_minus_mean_column_sqrd = [self.obs_mean1_sqrd,
                                                  self.obs_mean2_sqrd,
                                                  self.obs_mean3_sqrd,
                                                  self.obs_mean4_sqrd,
                                                  self.obs_mean5_sqrd,
                                                  self.obs_mean6_sqrd,
                                                  self.obs_mean7_sqrd,
                                                  self.obs_mean8_sqrd,
                                                  self.obs_mean9_sqrd,
                                                  self.obs_mean10_sqrd,
                                                  self.obs_mean11_sqrd,
                                                  self.obs_mean12_sqrd,
                                                  self.obs_mean13_sqrd,
                                                  self.obs_mean14_sqrd,
                                                  self.obs_mean15_sqrd]
            for i in range(observations):
                observation_minus_mean_column_sqrd[i].insert(0, round((difference_list[i] ** 2), 4))

        # calculates the standard deviation and inserts it to the entry widget
        def standard_deviation():
            temp_list = []
            global stanDev
            for i in range(observations):
                temp_list.append(float(observation_column[i].get()))
            stanDev = round(stdev(temp_list), 4)
            self.stanDevResult.insert(0, stanDev)
        # calculates the variance and inserts it to the entry widget
        def variance_():
            temp_list = []
            for i in range(observations):
                temp_list.append(float(observation_column[i].get()))
            mu = round(variance(temp_list), 4)
            self.varianceResult.insert(0, mu)
        # plots the histogram and distribution graph on different windows
        # makes use of pyplot from the matplotlib
        def plot():
            temp_list = []
            for i in range(observations):
                temp_list.append(float(observation_column[i].get()))
            plt.style.use('ggplot')
            plt.figure(1)
            plt.plot(sorted(temp_list), stats.norm.pdf(sorted(temp_list), mean, stanDev))
            plt.figure(2)
            plt.hist(sorted(temp_list))
            plt.show()

# starts the program thru the support module
def start_up():
    Finals_GUI_support.main()

if __name__ == '__main__':
    Finals_GUI_support.main()




