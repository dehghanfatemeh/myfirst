from ctypes.wintypes import PINT
import serial
from tkinter import Variable, messagebox
import tkinter as tk
from tkinter import Entry, Label, StringVar, ttk
import tkinter
from tkinter import *
from tkinter.constants import COMMAND, LEFT, W
from tkinter.font import BOLD
from typing import Sized, Text
from PIL import Image, ImageTk
from typing import Text
import threading

from serial.serialutil import Timeout
window = tk.Tk()
window.title('iotive')

window.geometry('900x500')

window.iconbitmap('C:/Users/Pishgam System/Desktop/iotive.ico')
ser=serial.Serial()
c=d=0
divCeckOk = 0
a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=a13=a14=a15=a16=a17=a18=a19=a20=a21=a22=0
a44=a45=a46=0
a23=a24=a25=a26=a27=a28=a29=a30=a31=a32=a33=a34=a35=a36=a37=a38=a39=a40=a41=a42=a43=0

# عکس
load = Image.open("iotive.png")
render = ImageTk.PhotoImage(load)
# 
img = Label(image=render)
img.image = render 
img.place(x=16, y=15)
# 
load1 = Image.open("line 1.png")
render = ImageTk.PhotoImage(load1)
img = Label(image=render)
img.image = render 
img.place(x=315, y=0)
# 
load = Image.open("line 2.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render 
img.place(x=60, y=147)

load = Image.open("line 2.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render 
img.place(x=60, y=280)

load = Image.open("line 2.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render 
img.place(x=60, y=368)

load = Image.open("line 4.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render 
img.place(x=325, y=280)

load1 = Image.open("line 1.png")
render = ImageTk.PhotoImage(load1)
img = Label(image=render)
img.image = render 
img.place(x=615, y=0)

load = Image.open("line 2.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render 
img.place(x=640, y=366)
#11111111111111111111111111111111111111111111111111111111111111111111111111111 ستون اول
label=Label(text='Step1:')
label.place(x=10,y=132)
label.config(font=BOLD ,fg='#413380')

a8=tk.Label(text='BAUDART:')
a8.place(x=10,y=165)
n = tk.StringVar()
speed = ttk.Combobox( width =19, textvariable = n)
speed['values'] = (110,300 , 1200 ,2400 , 4800 , 9600 , 19200 , 38400, 57600)
speed.place(x=90,y=165)
#===============================================
a9=tk.Label(text='COM PORT:')
a9.place(x=10,y=195)
m = tk.StringVar()
com_port = ttk.Combobox( width =19, textvariable = m)
com_port['values'] = ('COM1','COM2' , 'COM3' ,'COM4' , 'COM5' , 'COM6' , 'COM7' , 'COM8', 'COM9',
'COM10','COM11','COM12','COM13','COM14','COM15')
com_port.place(x=90,y=195)

def CONNECT():
    global ser
    global c
    c=1
   
    if str(m.get())!=None and str(n.get())!=None:
        try:
              ser.baudrate = n.get()
              ser.port = m.get()
              ser.open()
              if ser.is_open:
                print('yes open ..')
                myvar = StringVar()
                Label1 =Label(textvariable=myvar,fg="red")
                Label1.place(x=125,y=250)
                myvar.set("connected !")

        except:
             messagebox.showinfo('information', 'field COM PORT or BAUDART is empty !')
             print('not open !!')
             pass

button1 = tk.Button(
    text="CONNECT",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = CONNECT,
)
button1.place(x=125,y=225)
# ==================================================
myvar2 = StringVar()

label=Label(text='Step2:')
label.place(x=10,y=265)
label.config(font=BOLD ,fg='#413380')

def DIV_check():
    global ser
    # myvar2.set("click DIV check !")
    if c!=1:
         messagebox.showinfo('information', 'First Connect !')
    if ser.is_open :
        try:
            ser.write("HELLO")
        except:
            pass

Label1 =Label(textvariable=myvar2,fg="red")
Label1.place(x=125,y=320)
# Label1.update()

button2 = tk.Button(
    text="DIVcheck",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    # relief=tk.GROOVE,
    command = DIV_check,
    # fg="GREEN",
)
button2.place(x=125,y=295)
# ==================================================
label=Label(text='Step3:')
label.place(x=10,y=355)
label.config(font=BOLD ,fg='#413380')

def READ_DATA(): 
    global ser 

    if c!=1:
         messagebox.showinfo('information', 'First Connect !')

    if ser.is_open :
        try:
            ser.write(READ_DATA )
        except:
            pass

button3 = tk.Button(
    text="READ DATA",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = READ_DATA,
)
button3.place(x=125,y=382)

# 22222222222222222222222222222222222222222222222222222222222222222222222222222222ستون دوم 
a1 = tk.Label(text="IP:")
a1.place(x=340,y=20)
def limitSize(*args):
    value = dayValue1.get()
    if len(value) > 3: dayValue1.set(value[:3])

dayValue1 = tk.StringVar()
dayValue1.trace('w', limitSize)
entry1 = Entry(width=5,textvariable=dayValue1)
entry1.place(x=410,y=20)
#================================================
b=tk.Label(text='.')
b.place(x=442,y=20)
#================================================
def limitSize(*args):
    value = dayValue2.get()
    if len(value) > 3: dayValue2.set(value[:3])
dayValue2 = tk.StringVar()
dayValue2.trace('w', limitSize)
entry2 =Entry(width=5,textvariable=dayValue2)
entry2.place(x=452,y=20)
#================================================
b=tk.Label(text='.')
b.place(x=485,y=20)
#================================================
def limitSize(*args):
    value = dayValue3.get()
    if len(value) > 3: dayValue3.set(value[:3])
dayValue3 = tk.StringVar()
dayValue3.trace('w', limitSize)
entry3 = Entry(width=5,textvariable=dayValue3)
entry3.place(x=495,y=20)
#=================================================
b=tk.Label(text='.')
b.place(x=530,y=20)
#=================================================
def limitSize(*args):
    value = dayValue4.get()
    if len(value) > 3: dayValue4.set(value[:3])
dayValue4 = tk.StringVar()
dayValue4.trace('w', limitSize)
entry4 =Entry(width=5,textvariable=dayValue4)
entry4.place(x=540,y=20)
#=================================================
a2 = tk.Label(text="PORT:")
a2.place(x=340,y=50)
dayValue5= tk.StringVar()
entry5 =Entry(width=27,textvariable=dayValue5)
entry5.place(x=410,y=50)
#================================================= 
a3 = tk.Label(text="GATEWAY:")
a3.place(x=340,y=80)
def limitSize(*args):
    value = dayValue6.get()
    if len(value) > 3: dayValue6.set(value[:3])
dayValue6 = tk.StringVar()
dayValue6.trace('w', limitSize)
entry6 =Entry(width=5,textvariable=dayValue6)
entry6.place(x=410,y=80)

b=tk.Label(text='.')
b.place(x=442,y=80)

def limitSize(*args):
    value = dayValue7.get()
    if len(value) > 3: dayValue7.set(value[:3])
dayValue7 = tk.StringVar()
dayValue7.trace('w', limitSize)
entry7 =Entry(width=5,textvariable=dayValue7)
entry7.place(x=452,y=80)

b=tk.Label(text='.')
b.place(x=485,y=80)

def limitSize(*args):
    value = dayValue8.get()
    if len(value) > 3: dayValue8.set(value[:3])
dayValue8 = tk.StringVar()
dayValue8.trace('w', limitSize)
entry8 = Entry(width=5,textvariable=dayValue8)
entry8.place(x=495,y=80)

b=tk.Label(text='.')
b.place(x=530,y=80)

def limitSize(*args):
    value = dayValue9.get()
    if len(value) > 3: dayValue9.set(value[:3])
dayValue9 = tk.StringVar()
dayValue9.trace('w', limitSize)
entry9 =Entry(width=5,textvariable=dayValue9)
entry9.place(x=540,y=80)
#===============================================
a4 = tk.Label(text="SUBNET:")
a4.place(x=340,y=110)
def limitSize(*args):
    value = dayValue10.get()
    if len(value) > 3: dayValue10.set(value[:3])
dayValue10 = tk.StringVar()
dayValue10.trace('w', limitSize)
entry10=Entry(width=5,textvariable=dayValue10)
entry10.place(x=410,y=110)

b=tk.Label(text='.')
b.place(x=442,y=110)

def limitSize(*args):
    value = dayValue11.get()
    if len(value) > 3: dayValue11.set(value[:3])
dayValue11 = tk.StringVar()
dayValue11.trace('w', limitSize)
entry11 =Entry(width=5,textvariable=dayValue11)
entry11.place(x=452,y=110)

b=tk.Label(text='.')
b.place(x=485,y=110)

def limitSize(*args):
    value = dayValue12.get()
    if len(value) > 3: dayValue12.set(value[:3])
dayValue12 = tk.StringVar()
dayValue12.trace('w', limitSize)
entry12 = Entry(width=5,textvariable=dayValue12)
entry12.place(x=495,y=110)

b=tk.Label(text='.')
b.place(x=530,y=110)

def limitSize(*args):
    value = dayValue13.get()
    if len(value) > 3: dayValue13.set(value[:3])
dayValue13 = tk.StringVar()
dayValue13.trace('w', limitSize)
entry13 =Entry(width=5,textvariable=dayValue13)
entry13.place(x=540,y=110)
#===============================================
a5 = tk.Label(text="DNS1:")
a5.place(x=340,y=140)
def limitSize(*args):
    value = dayValue14.get()
    if len(value) > 3: dayValue14.set(value[:3])
dayValue14 = tk.StringVar()
dayValue14.trace('w', limitSize)
entry14=Entry(width=5,textvariable=dayValue14)
entry14.place(x=410,y=140)

b=tk.Label(text='.')
b.place(x=442,y=140)

def limitSize(*args):
    value = dayValue15.get()
    if len(value) > 3: dayValue15.set(value[:3])
dayValue15 = tk.StringVar()
dayValue15.trace('w', limitSize)
entry15 =Entry(width=5,textvariable=dayValue15)
entry15.place(x=452,y=140)

b=tk.Label(text='.')
b.place(x=485,y=140)

def limitSize(*args):
    value = dayValue16.get()
    if len(value) > 3: dayValue16.set(value[:3])
dayValue16 = tk.StringVar()
dayValue16.trace('w', limitSize)
entry16 = Entry(width=5,textvariable=dayValue16)
entry16.place(x=495,y=140)

b=tk.Label(text='.')
b.place(x=530,y=140)

def limitSize(*args):
    value = dayValue17.get()
    if len(value) > 3: dayValue17.set(value[:3])
dayValue17= tk.StringVar()
dayValue17.trace('w', limitSize)
entry17 =Entry(width=5,textvariable=dayValue17)
entry17.place(x=540,y=140)
#===============================================
a6 = tk.Label(text="DNS2:")
a6.place(x=340,y=170)
def limitSize(*args):
    value = dayValue18.get()
    if len(value) > 3: dayValue18.set(value[:3])
dayValue18= tk.StringVar()
dayValue18.trace('w', limitSize)
entry18=Entry(width=5,textvariable=dayValue18)
entry18.place(x=410,y=170)

b=tk.Label(text='.')
b.place(x=442,y=170)

def limitSize(*args):
    value = dayValue19.get()
    if len(value) > 3: dayValue19.set(value[:3])
dayValue19= tk.StringVar()
dayValue19.trace('w', limitSize)
entry19 =Entry(width=5,textvariable=dayValue19)
entry19.place(x=452,y=170)

b=tk.Label(text='.')
b.place(x=485,y=170)

def limitSize(*args):
    value = dayValue20.get()
    if len(value) > 3: dayValue20.set(value[:3])
dayValue20= tk.StringVar()
dayValue20.trace('w', limitSize)
entry20 = Entry(width=5,textvariable=dayValue20)
entry20.place(x=495,y=170)

b=tk.Label(text='.')
b.place(x=530,y=170)

def limitSize(*args):
    value = dayValue21.get()
    if len(value) > 3: dayValue21.set(value[:3])
dayValue21= tk.StringVar()
dayValue21.trace('w', limitSize)
entry21 =Entry(width=5,textvariable=dayValue21)
entry21.place(x=540,y=170)
#===============================================
a7= tk.Label(text='URL:')
a7.place(x=340,y=200)
dayValue22= tk.StringVar()
entry22=Entry(width=27,textvariable=dayValue22)
entry22.place(x=410,y=200)

def SUBMIT1():
    global ser

    if c!=1:
         messagebox.showinfo('information', 'First Connect !')

    s=""
    s=s+entry1.get()
    s=s+"#"
    s=s+entry2.get()
    s=s+"#"
    s=s+entry3.get()
    s=s+"#"
    s=s+entry4.get()
    s=s+"#"
    s=s+entry5.get()
    s=s+"#"
    s=s+entry6.get()
    s=s+"#"
    s=s+entry7.get()
    s=s+"#"
    s=s+entry8.get()
    s=s+"#"
    s=s+entry9.get()
    s=s+"#"
    s=s+entry10.get()
    s=s+"#"
    s=s+entry11.get()
    s=s+"#"
    s=s+entry12.get()
    s=s+"#"
    s=s+entry13.get()
    s=s+"#"
    s=s+entry14.get()
    s=s+"#"
    s=s+entry15.get()
    s=s+"#"
    s=s+entry16.get()
    s=s+"#"
    s=s+entry17.get()
    s=s+"#"
    s=s+entry18.get()
    s=s+"#"
    s=s+entry19.get()
    s=s+"#"
    s=s+entry20.get()
    s=s+"#"
    s=s+entry21.get()
    s=s+"#"
    s=s+entry22.get()
    s=s + "\r\n"

    ser.write(s.encode())
    print(s)


button4= tk.Button(
    text=" SUBMIT1",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = SUBMIT1,
)
button4.place(x=405,y=240)
#======================================
myvar4 = StringVar()

def READ_DATA1():
    global ser 

    if c!=1:
         messagebox.showinfo('information', 'First Connect !')
    
    if ser.is_open :
        try:
            ser.write(READ_DATA1 )
        except:
            pass

button5 = tk.Button(
    text="READ DATA1",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = READ_DATA1,
)
button5.place(x=490,y=240)
#===============================================
a=Label(text='ID:')
a.place(x=340,y=300)

dayValue44=StringVar()
entry44=Entry(textvariable=dayValue44)
entry44.place(x=410,y=300)

a=Label(text='VC:')
a.place(x=340,y=330)

dayValue45=StringVar()
entry45=Entry(textvariable=dayValue45)
entry45.place(x=410,y=330)

a=Label(text='PASSWORD:')
a.place(x=340,y=360)

dayValue46=StringVar()
entry46=Entry(textvariable=dayValue46)
entry46.place(x=410,y=360) 

myvar7  = StringVar()
def SUBMIT2():
    global ser
    myvar7.set("click SUBMIT2 !")
    if c!=1:
         messagebox.showinfo('information', 'First Connect !')

    s2=""
    s2=s2+entry44.get()
    s2=s2+"#"
    s2=s2+entry45.get()
    s2=s2+"#"
    s2=s2+entry46.get()
    s2=s2+"#"
    s2=s2 + "\r\n"
    ser.write(s2.encode())
    print(s2)

button6= tk.Button(
    text=" SUBMIT2",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = SUBMIT2,
)
button6.place(x=405,y=392)

def READ_DATA2():
    global ser 

    if c!=1:
        messagebox.showinfo('information', 'First Connect !')


    if ser.is_open :
        try:
            ser.write(READ_DATA2 )
        except:
            pass

button7 = tk.Button(
    text="READ DATA2",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = READ_DATA2,
    # fg="yellow",
)
button7.place(x=490,y=392)

# 33333333333333333333333333333333333333333333333333333333333333333333ستون سوم 
dayValue23=StringVar()
entry23=Entry(width=23,textvariable=dayValue23)
entry23.place(x=640,y=20)

a=Label(text='ns')
a.place(x=790,y=20)
# ========
dayValue24=StringVar()
entry24=Entry(width=7,textvariable=dayValue24)
entry24.place(x=640,y=50)

dayValue25=StringVar()
entry25=Entry(width=7,textvariable=dayValue25)
entry25.place(x=687,y=50)

dayValue26=StringVar()
entry26=Entry(width=7,textvariable=dayValue26)
entry26.place(x=734,y=50)

a=Label(text='V/D1m')
a.place(x=790,y=50)
# =========
dayValue27=StringVar()
entry27=Entry(width=7,textvariable=dayValue27)
entry27.place(x=640,y=80)

dayValue28=StringVar()
entry28=Entry(width=7,textvariable=dayValue28)
entry28.place(x=687,y=80)

dayValue29=StringVar()
entry29=Entry(width=7,textvariable=dayValue29)
entry29.place(x=734,y=80)

a=Label(text='V/D2m')
a.place(x=790,y=80)
#=========
dayValue30=StringVar()
entry30=Entry(width=7,textvariable=dayValue30)
entry30.place(x=640,y=110)

dayValue31=StringVar()
entry31=Entry(width=7,textvariable=dayValue31)
entry31.place(x=687,y=110)

dayValue32=StringVar()
entry32=Entry(width=7,textvariable=dayValue32)
entry32.place(x=734,y=110)

a=Label(text='V/D3m')
a.place(x=790,y=110)
#=========
dayValue33=StringVar()
entry33=Entry(width=7,textvariable=dayValue33)
entry33.place(x=640,y=140)

dayValue34=StringVar()
entry34=Entry(width=7,textvariable=dayValue34)
entry34.place(x=687,y=140)

dayValue35=StringVar()
entry35=Entry(width=7,textvariable=dayValue35)
entry35.place(x=734,y=140)

a=Label(text='V/D4m')
a.place(x=790,y=140)
#=========
dayValue36=StringVar()
entry36=Entry(width=7,textvariable=dayValue36)
entry36.place(x=640,y=170)

dayValue37=StringVar()
entry37=Entry(width=7,textvariable=dayValue37)
entry37.place(x=687,y=170)

dayValue38=StringVar()
entry38=Entry(width=7,textvariable=dayValue38)
entry38.place(x=734,y=170)

a=Label(text='V/D5m')
a.place(x=790,y=170)
#=========
dayValue39=StringVar()
entry39=Entry(width=7,textvariable=dayValue39)
entry39.place(x=640,y=200)

dayValue40=StringVar()
entry40=Entry(width=7,textvariable=dayValue40)
entry40.place(x=687,y=200)

dayValue41=StringVar()
entry41=Entry(width=7,textvariable=dayValue41)
entry41.place(x=734,y=200)

a=Label(text='V/D6m')
a.place(x=790,y=200)
#==========
dayValue42=StringVar()
entry42=Entry(width=23,textvariable=dayValue42)
entry42.place(x=640,y=230)

a=Label(text='interval 1')
a.place(x=790,y=230)
#==========
dayValue43=StringVar()
entry43=Entry(width=23,textvariable=dayValue43)
entry43.place(x=640,y=260)

a=Label(text='interval 2')
a.place(x=790,y=260)
#==========
myvar8 = StringVar()

def SUBMIT3():
    global ser
    myvar8.set("click SUBMIT3 !")
    if c!=1:
         messagebox.showinfo('information', 'First Connect !')

    s3=""
    s3=s3+entry23.get()
    s3=s3+"#"
    s3=s3+entry24.get()
    s3=s3+"#"
    s3=s3+entry25.get()
    s3=s3+"#"
    s3=s3+entry26.get()
    s3=s3+"#"
    s3=s3+entry27.get()
    s3=s3+"#"
    s3=s3+entry28.get()
    s3=s3+"#"
    s3=s3+entry29.get()
    s3=s3+"#"
    s3=s3+entry30.get()
    s3=s3+"#"
    s3=s3+entry31.get()
    s3=s3+"#"
    s3=s3+entry32.get()
    s3=s3+"#"
    s3=s3+entry33.get()
    s3=s3+"#"
    s3=s3+entry34.get()
    s3=s3+"#"
    s3=s3+entry35.get()
    s3=s3+"#"
    s3=s3+entry36.get()
    s3=s3+"#"
    s3=s3+entry37.get()
    s3=s3+"#"
    s3=s3+entry38.get()
    s3=s3+"#"
    s3=s3+entry39.get()
    s3=s3+"#"
    s3=s3+entry40.get()
    s3=s3+"#"
    s3=s3+entry41.get()
    s3=s3+"#"
    s3=s3+entry42.get()
    s3=s3+"#"
    s3=s3 + "\r\n"

    ser.write(s3.encode())
    print(s3)

myvar9 = StringVar()
 
def READ_DATA3():
    global ser 
    myvar9.set("click READ DATA3 !")
    if c!=1:
         messagebox.showinfo('information', 'First Connect !')   

    
    if ser.is_open :
        try:
            ser.write(READ_DATA3 )
        except:
            pass

button8 = tk.Button(
    text="SUBMIT3",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
  command = SUBMIT3
)
button8.place(x=640,y=290)

button9 = tk.Button(
    text="READ DATA3",
    width=9,
    height=1,
    bg= '#413380' ,
    fg="white",
    command = READ_DATA3,
    # fg="yellow",
)
button9.place(x=723,y=290)
# =================================================
label=Label(text='Process:')
label.place(x=620,y=352)
label.config(font=BOLD ,fg='#413380')

label=Label(text='1 : وارد کردن مقدار BUADRATE ..مطابق ')
label.place(x=620,y=380)

label=Label(text='2 : وارد کردن مقدار  COMPORT ..مطابق')
label.place(x=620,y=400)

label=Label(text='3 : فشردن connect و اطمینان از اتصال')
label.place(x=620,y=420)
#====================================================
def serial_readtheard ():
    global divCeckOk
    global ser 
    global d
   
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22
    global a23,a24,a25
    global a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46
    while True:
        if ser.is_open:
            try:
                x=ser.readline()
                # print(x)
                # print(type(x))
                dataStr = str(x)
                # print(type(dataStr))
                dataStr = dataStr[2:]
                dataStr = dataStr[:-5]
                print("str is:",dataStr)

                dict1= dataStr.split("#")
                # print(dict1[1])
                # print(dict1)
                if str(dict1[1]) == "hi" :
                    divCeckOk = 1 
                    
                if dict1[1]=="1":  
                    d=1   
                    a1=dict1[2]
                    a2=dict1[3]
                    a3=dict1[4]
                    a4=dict1[5]
                    a5=dict1[6]
                    a6=dict1[7]
                    a7=dict1[8]
                    a8=dict1[9]
                    a9=dict1[10]
                    a10=dict1[11]
                    a11=dict1[12]
                    a12=dict1[13]
                    a13=dict1[14]
                    a14=dict1[15]
                    a15=dict1[16]
                    a16=dict1[17]
                    a17=dict1[18]
                    a18=dict1[19]
                    a19=dict1[20]
                    a20=dict1[21]
                    a21=dict1[22]
                    a22=dict1[23]
              

                if dict1[1]=="2":
                    d=2
                    a44=dict1[2]
                    a45=dict1[3]
                    a46=dict1[4]


                if dict1[1]=="3":
                    d=3
                    a23=dict1[2]
                    a24=dict1[3]     
                    a25=dict1[4]     
                    a26=dict1[5]     
                    a27=dict1[6]     
                    a28=dict1[7]     
                    a29=dict1[8]     
                    a30=dict1[9]     
                    a31=dict1[10]     
                    a32=dict1[11]     
                    a33=dict1[12]     
                    a34=dict1[13]     
                    a35=dict1[14]     
                    a36=dict1[15]     
                    a37=dict1[16]     
                    a38=dict1[17]     
                    a39=dict1[18]     
                    a40=dict1[19]     
                    a41=dict1[20]     
                    a42=dict1[21]
                    a43=dict1[22]

                if dict1[1]=="4":   
                    d=4 
                    a1=dict1[2]
                    a2=dict1[3]
                    a3=dict1[4]
                    a4=dict1[5]
                    a5=dict1[6]
                    a6=dict1[7]
                    a7=dict1[8]
                    a8=dict1[9]
                    a9=dict1[10]
                    a10=dict1[11]
                    a11=dict1[12]
                    a12=dict1[13]
                    a13=dict1[14]
                    a14=dict1[15]
                    a15=dict1[16]
                    a16=dict1[17]
                    a17=dict1[18]
                    a18=dict1[19]
                    a19=dict1[20]
                    a20=dict1[21]
                    a21=dict1[22]
                    a22=dict1[23]
                    
                    a23=dict1[24]
                    a24=dict1[25]     
                    a25=dict1[26]     
                    a26=dict1[27]     
                    a27=dict1[28]     
                    a28=dict1[29]     
                    a29=dict1[30]     
                    a30=dict1[31]     
                    a31=dict1[32]     
                    a32=dict1[33]     
                    a33=dict1[34]     
                    a34=dict1[35]     
                    a35=dict1[36]     
                    a36=dict1[37]     
                    a37=dict1[38]     
                    a38=dict1[39]     
                    a39=dict1[40]     
                    a40=dict1[41]     
                    a41=dict1[42]     
                    a42=dict1[43]
                    a43=dict1[44]
                 
                    a44=dict1[45]
                    a45=dict1[46]
                    a46=dict1[47]

            except:
                pass


t1 = threading.Thread(target=serial_readtheard)
# t1.setDaemon(True)
t1.start()
# t1.join()

while True:

    if divCeckOk == 1 :
             myvar2.set("Device is Connected !")
    
    if d==1:
        dayValue1.set(a1)
        dayValue2.set(a2)
        dayValue3.set(a3)
        dayValue4.set(a4)
        dayValue5.set(a5)
        dayValue6.set(a6)
        dayValue7.set(a7)
        dayValue8.set(a8)
        dayValue9.set(a9)
        dayValue10.set(a10)
        dayValue11.set(a11)
        dayValue12.set(a12)
        dayValue13.set(a13)
        dayValue14.set(a14)
        dayValue15.set(a15)
        dayValue16.set(a16)
        dayValue17.set(a17)
        dayValue18.set(a18)
        dayValue19.set(a19)
        dayValue20.set(a20)
        dayValue21.set(a21)
        dayValue22.set(a22)
    if d==2:
        dayValue44.set(a44)
        dayValue45.set(a45)
        dayValue46.set(a46)
    
    if d==3:
        dayValue23.set(a23)
        dayValue24.set(a24)
        dayValue25.set(a25)
        dayValue26.set(a26)
        dayValue27.set(a27)
        dayValue28.set(a28)
        dayValue29.set(a29)
        dayValue30.set(a30)
        dayValue31.set(a31)
        dayValue32.set(a32)
        dayValue33.set(a33)
        dayValue34.set(a34)
        dayValue35.set(a35)
        dayValue36.set(a36)
        dayValue37.set(a37)
        dayValue38.set(a38)
        dayValue39.set(a39)
        dayValue40.set(a40)
        dayValue41.set(a41)
        dayValue42.set(a42)
        dayValue43.set(a43)

    if d==4:
        dayValue1.set(a1)
        dayValue2.set(a2)
        dayValue3.set(a3)
        dayValue4.set(a4)
        dayValue5.set(a5)
        dayValue6.set(a6)
        dayValue7.set(a7)
        dayValue8.set(a8)
        dayValue9.set(a9)
        dayValue10.set(a10)
        dayValue11.set(a11)
        dayValue12.set(a12)
        dayValue13.set(a13)
        dayValue14.set(a14)
        dayValue15.set(a15)
        dayValue16.set(a16)
        dayValue17.set(a17)
        dayValue18.set(a18)
        dayValue19.set(a19)
        dayValue20.set(a20)
        dayValue21.set(a21)
        dayValue22.set(a22)

        dayValue23.set(a23)
        dayValue24.set(a24)
        dayValue25.set(a25)
        dayValue26.set(a26)
        dayValue27.set(a27)
        dayValue28.set(a28)
        dayValue29.set(a29)
        dayValue30.set(a30)
        dayValue31.set(a31)
        dayValue32.set(a32)
        dayValue33.set(a33)
        dayValue34.set(a34)
        dayValue35.set(a35)
        dayValue36.set(a36)
        dayValue37.set(a37)
        dayValue38.set(a38)
        dayValue39.set(a39)
        dayValue40.set(a40)
        dayValue41.set(a41)
        dayValue42.set(a42)
        dayValue43.set(a43)

        dayValue44.set(a44)
        dayValue45.set(a45)
        dayValue46.set(a46)

    window.update()
# window.mainloop()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
