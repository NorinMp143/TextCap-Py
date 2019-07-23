from tkinter import *
import random
class cap:
    lists=['bJ6xFh','6sxFcv','k7Ge3x','o1v3Xe','n0xg2X']
    Capch=random.choice(lists)
Fix=cap()
window = Tk()

def Refresh():
    Fix.Capch=random.choice(Fix.lists)
    x=Label(window,text=Fix.Capch,fg="white",width=15,height=2,font="None 15 bold",bg="black")
    x.grid(row=10,column=1,columnspan=2)

def check():
    A=N1.get()
    B=N2.get()
    C=N3.get()
    D=N4.get()
    E=N5.get()
    F=N6.get()
    G=C1.get()
    if True:
        if A=="":
            mp=Message(window,text="Please Enter Name.")
            mp.config(width=350,fg="red",font=('times', 10, 'bold'))
            mp.grid(row=0,column=1,columnspan=2)
        else:
            mp=Message(window,text="                                      ")
            mp.config(width=350)
            mp.grid(row=0,column=1,columnspan=2)
            if True:
                if B=="":
                    mp=Message(window,text="Please Enter MobileNo.")
                    mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                    mp.grid(row=0,column=1,columnspan=2)
                else:
                    mp=Message(window,text="                                    ")
                    mp.config(width=350)
                    mp.grid(row=0,column=1,columnspan=2)
                    if True:
                        if C=="":
                            mp=Message(window,text="Please Enter Email.")
                            mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                            mp.grid(row=0,column=1,columnspan=2)
                        else:
                            mp=Message(window,text="                                       ")
                            mp.config(width=350)
                            mp.grid(row=0,column=1,columnspan=2)
                            if True:
                                if D=="":
                                    mp=Message(window,text="Please Enter Dateofbirth.")
                                    mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                                    mp.grid(row=0,column=1,columnspan=2)
                                else:
                                    mp=Message(window,text="                                              ")
                                    mp.config(width=350)
                                    mp.grid(row=0,column=1,columnspan=2)
                                    if True:
                                        if E=="":
                                            mp=Message(window,text="Please Enter City.")
                                            mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                                            mp.grid(row=0,column=1,columnspan=2)
                                        else:
                                            mp=Message(window,text="                                     ")
                                            mp.config(width=350)
                                            mp.grid(row=0,column=1,columnspan=2)
                                            if True:
                                                if F=="":
                                                    mp=Message(window,text="Please Enter State.")
                                                    mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                                                    mp.grid(row=0,column=1,columnspan=2)
                                                else:
                                                    mp=Message(window,text="                                   ")
                                                    mp.config(width=350)
                                                    mp.grid(row=0,column=1,columnspan=2)
                                                    if True:
                                                        if G=="":
                                                            mp=Message(window,text="Please Enter Captcha.")
                                                            mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                                                            mp.grid(row=0,column=1,columnspan=2)
                                                        else:
                                                            mp=Message(window,text="                                   ")
                                                            mp.config(width=350)
                                                            mp.grid(row=0,column=1,columnspan=2)
                                                            if G!=Fix.Capch:
                                                                mp=Message(window,text="Enter Right Captcha.")
                                                                mp.config(width=350,fg="red",font=('times', 10, 'bold'))
                                                                mp.grid(row=0,column=1,columnspan=2)
                                                            else:
                                                                window.destroy()
                                                                newWin=Tk()
                                                                newWin.title("Successful")
                                                                Label(newWin,text="  ",width=5).grid(row=0,column=1)
                                                                Label(newWin,text="  ",width=5).grid(row=1,column=1)
                                                                Label(newWin,text="  ",width=5).grid(row=3,column=3)
                                                                Label(newWin,text="  ",width=5).grid(row=4,column=3)
                                                                Label(newWin,text="  You Registered Successful.  ",bg="pink",fg="violet",height=2,font="none 12 bold").grid(row=2,column=2)
                                                                newWin.mainloop()
        
Label(window).grid(row=0,column=1)
Label(window,text="\t   Personal Details\t\t",bg="Violet",fg="Yellow",height=2,font="None 20 bold").grid(row=1,column=1,columnspan=2)
canvas = Canvas(window, width = 50, height = 50,bg="pink")      
canvas.grid(row=1,column=1)      
img = PhotoImage(file="avatar.gif")      
canvas.create_image(0,0,anchor=NW, image=img)
Label(window).grid(row=2,column=1)
Label(window,text="\tName :",fg="Blue",font="None 12 bold").grid(row=3,column=1)
N1=Entry(window,width=30)
N1.grid(row=3,column=2,sticky=W)
Label(window,text="\tMobile No. :",fg="Blue",font="None 12 bold").grid(row=4,column=1)
N2=Entry(window,width=30)
N2.grid(row=4,column=2,sticky=W)
Label(window,text="\tE-mail :",fg="Blue",font="None 12 bold").grid(row=5,column=1)
N3=Entry(window,width=30)
N3.grid(row=5,column=2,sticky=W)
Label(window,text="\tDOB :",fg="Blue",font="None 12 bold").grid(row=6,column=1)
N4=Entry(window,width=30)
N4.grid(row=6,column=2,sticky=W)
Label(window,text="\tCity :",fg="Blue",font="None 12 bold").grid(row=7,column=1)
N5=Entry(window,width=30)
N5.grid(row=7,column=2,sticky=W)
Label(window,text="\tState :",fg="Blue",font="None 12 bold").grid(row=8,column=1)
N6=Entry(window,width=30)
N6.grid(row=8,column=2,sticky=W)
Label(window).grid(row=9,column=1)
Label(window,text=Fix.Capch,fg="white",width=15,height=2,font="None 15 bold",bg="black").grid(row=10,column=1,columnspan=2)
Label(window,text="Type the code you see above",fg="green",font="None 12 bold").grid(row=11,column=1,columnspan=2)
C1=Entry(window,width=15)
C1.grid(row=12,column=1,columnspan=2)
Button(window,text="Refresh",bg="pink",fg="blue",command=Refresh).grid(row=12,column=2)
Label(window).grid(row=13,column=1)
Button(window,text="Submit",bg="lightgreen",width=20,activeforeground="lightgreen",fg="white",font="none 10 bold",command=check).grid(row=14,column=1,columnspan=2)
window.mainloop()