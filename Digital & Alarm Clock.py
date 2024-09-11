import sys
from tkinter import *
from tkinter import messagebox
import time
import datetime
from playsound import playsound
from PIL import ImageTk, Image

def tick(val):
    global clock
    window=Toplevel()
    window.geometry("300x130")
    clock=Label(window, font=("Arial", 30, "bold"), fg="white", bg="black", bd=16, relief=SUNKEN) 
    clock.place(x=18, y=30)
    if val=='btn_24':
        time_24()
    elif val=='btn_12':
        time_12()
    else:
        alarm()
        
def time_24():
    global clock
    ts=time.strftime("%H:%M:%S")
    clock["text"]=ts
    clock.after(1000, time_24) #look at this if its supposed to be time24?
    
    
def time_12():
    global clock
    ts=time.strftime("%I:%M:%S %p")
    clock["text"]=ts
    clock.after(1000, time_12) #also have a look here if it fails to work
    
    
def alarm():
    global e1, e2
    window=Toplevel()
    window.geometry("350x200")
    hours=Label(window, text="Select Hour:", font=("Arial", 30, "bold"), fg="white", bg="dark")
    hours.place(x=18, y=30)
    e1=Entry(window, relief=GROOVE)
    e1.place(x=18, y=30)
    minutes=Label(window, text="Select Minute:", font=("Arial", 30, "bold"), fg="white", bg="dark")
    minutes.place(x=18, y=30)
    e2=Entry(window, relief=GROOVE)
    e2.place(x=30, y=130)
    begin=Button(window, text="Start", relief=GROOVE)
    begin.place(x=200, y=150)
    begin.bind("<Button-1", alarm_begin)
    
    
def alarm_begin(event):
    global e1, e2
    h=e1.get()
    m=e2.get()
    while(1):
        if(int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            playsound("one.mp3")
            messagebox.showinfo("It's Time")
            break

root=Tk()

root.geometry("550x400")
img1=PhotoImage(file="12.jpg")
img2=PhotoImage(file="24.jpg")
img3=PhotoImage(file="alarm.jpg")
text=Label(root, text="Which clock d'you want to try?", font=("Arial", 30, "bold"), fg="white", bg="dark")
text.place(x=80, y=20)

btn1=Button(root, image=img1, borderwidth=0, command=lambda: tick("btn_12")).place(anchor=SW, x=0, y=200)
btn2=Button(root, image=img2, borderwidth=0, command=lambda: tick("btn_24)")).place(anchor=SW, x=0, y=300)
btn3=Button(root, image=img3, borderwidth=0, command=alarm).place(anchor=SW, x=0, y=400) 

photo=ImageTk.PhotoImage(Image.open("clock.jpg"))

img_label=Label(root, image=photo)
img_label.place(x=230, y=150)

root.mainloop()

#install playsound module to work
#And where tf is break statement even supposed to be in py!!!!