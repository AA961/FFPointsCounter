from cProfile import label
from tkinter import*
import tkinter
from tkinter import font
from tkinter import messagebox
from turtle import Screen, color
from unittest import TestCase


def ClearAll():
    pts1.set("")
    pts2.set("")
    pts3.set("")
    pts4.set("")
    pts5.set("")
    pts6.set("")


    kills1.set("")
    kills2.set("")
    kills3.set("")
    kills4.set("")
    kills5.set("")
    kills6.set("")
        
def Calculation():        
    
#POINTS-----------------------------------------------------------------
    try:    
        Pts1 = int(pts1.get())
        Pts2 = int(pts2.get())
        Pts3 = int(pts3.get())
        Pts4 = int(pts4.get())
        Pts5 = int(pts6.get())
        Pts6 = int(pts6.get())
    
        Pts = [12,9,8,7,6,5,4,3,2,1,0,0]

    
        PositionPoints = (Pts[Pts1 - 1] + Pts[Pts2 - 1] + Pts[Pts3 - 1] + Pts[Pts4 - 1] + Pts[Pts5 - 1] + Pts[Pts6 - 1] )
        
        


        
        Positionpts.set(PositionPoints)

    except tkinter.TclError:
        Error1 = "Enter the position of all matches"
        messagebox.showerror("Error" , Error1)
    
    except IndexError:
        Error2 = "Enter Your Correct Position"
        messagebox.showerror("Error" , Error2)
    



    try:
        Kill1 = int(kills1.get())
        Kill2 = int(kills2.get())
        Kill3 = int(kills3.get())
        Kill4 = int(kills4.get())
        Kill5 = int(kills5.get())
        Kill6 = int(kills6.get())

        TotalKills = (Kill1 + Kill2 + Kill3 + Kill4 + Kill5 + Kill6 )

        Killpts.set(TotalKills)
        TotalPoints = (TotalKills + PositionPoints)
        Totalpts.set(TotalPoints)
    
    except tkinter.TclError:
        Error1 = "Enter the Kills of All Games"
        messagebox.showerror("Error" , Error1)

        
        







main = Tk()
main.geometry("500x500")
main.configure(bg='powder blue')
main.title("Ad PTS")

ptslabel = tkinter.Label(main, text="Enter your positions" , font= "Corbel 27 bold " , bd=2)
ptslabel.pack(padx=80  , ipady=10 ,ipadx=10)
ptslabel.place(x=43,y=10)

killlabel = tkinter.Label(main, text="Enter your kills" , font= "lucida 25 bold")
killlabel.pack(padx=15 ,pady=15 , ipady=10 ,ipadx=10)
killlabel.place(x=85,y=200)



Lfor1pts = Label(main, text="1st" ,font=13 , justify=LEFT , anchor="e")
Lfor1pts.pack()
Lfor1pts.place(x=20, y=100)
pts1 = IntVar()
pts1.set("")
ps1 = Entry(main, textvar=pts1 ,font='lucida 10' , bd=4)
ps1.pack()
ps1.place(x=50,y=100)


Lfor2pts = Label(main, text="2nd" ,font=13 , justify=LEFT , anchor="e")
Lfor2pts.pack()
Lfor2pts.place(x=20, y=125)
pts2 = IntVar()
pts2.set("")
ps2 = Entry(main, textvar=pts2 ,font='lucida 10' , bd=4)
ps2.pack()
ps2.place(x=50,y=125)


Lfor3pts = Label(main, text="3rd" ,font=13 , justify=LEFT , anchor="e")
Lfor3pts.pack()
Lfor3pts.place(x=20, y=150)
pts3= IntVar()
pts3.set("")
ps3 = Entry(main, textvar=pts3 ,font='lucida 10', bd=4)
ps3.pack()
ps3.place(x=50,y=150)

Lfor4pts = Label(main, text="4th",font=13 , justify=LEFT , anchor="e")
Lfor4pts.pack()
Lfor4pts.place(x=205,y=101)
pts4 = IntVar()
pts4.set("")
ps4= Entry(main, textvar=pts4 ,font='lucida 10', bd=4)
ps4.pack()
ps4.place(x=235,y=101)


Lfor5pts = Label(main, text="5th" ,font=13 , justify=LEFT , anchor="e")
Lfor5pts.pack()
Lfor5pts.place(x=205,y=126)
pts5 = IntVar()
pts5.set("")
ps5 = Entry(main, textvar=pts5 ,font='lucida 10', bd=4 )
ps5.pack()
ps5.place(x=235,y=126)


Lfor6pts = Label(main, text="6th" ,font=13 , justify=LEFT , anchor="e")
Lfor6pts.pack()
Lfor6pts.place(x=205,y=151)
pts6 = IntVar()
pts6.set("")
ps6= Entry(main, textvar=pts6 ,font='lucida 10' , bd=4)
ps6.pack()
ps6.place(x=235,y=151)

#kills

Lfor1kill = Label(main, text="1st" ,font=13 , justify=LEFT , anchor="e")
Lfor1kill.pack()
Lfor1kill.place(x=20, y=270)
kills1 = IntVar()
kills1.set("")
ks1 = Entry(main, textvar=kills1 ,font='lucida 10', bd=4)
ks1.pack()
ks1.place(x=50,y=270)

Lfor2kill = Label(main, text="2nd" ,font=13 , justify=LEFT , anchor="e")
Lfor2kill.pack()
Lfor2kill.place(x=20, y=295)
kills2 = IntVar()
kills2.set("")
ks2 = Entry(main, textvar=kills2 ,font='lucida 10', bd=4)
ks2.pack()
ks2.place(x=50,y=295)

Lfor3kills = Label(main, text="3rd" ,font=13 , justify=LEFT , anchor="e")
Lfor3kills.pack()
Lfor3kills.place(x=20, y=320)
kills3 = IntVar()
kills3.set("")
ks3 = Entry(main, textvar=kills3 ,font='lucida 10', bd=4)
ks3.pack()
ks3.place(x=50,y=320)

Lfor4kills = Label(main, text="4th" ,font=13 , justify=LEFT , anchor="e")
Lfor4kills.pack()
Lfor4kills.place(x=205, y=270)
kills4 = IntVar()
kills4.set("")
ks4 = Entry(main, textvar=kills4 ,font='lucida 10', bd=4)
ks4.pack()
ks4.place(x=235,y=270)

Lfor5kills = Label(main, text="5th" ,font=13 , justify=LEFT , anchor="e")
Lfor5kills.pack()
Lfor5kills.place(x=205, y=295)
kills5= IntVar()
kills5.set("")
ks5 = Entry(main, textvar=kills5 ,font='lucida 10', bd=4)
ks5.pack()
ks5.place(x=235,y=295)

Lfor6forkills= Label(main, text="6th" ,font=13 , justify=LEFT , anchor="e" , )
Lfor6forkills.pack()
Lfor6forkills.place(x=205, y=320)
kills6 = IntVar()
kills6.set("")
ks6 = Entry(main, textvar=kills6 ,font='lucida 10', bd=4)
ks6.pack()
ks6.place(x=235,y=320)

#Result Screen-----------------------------------------------------------------

#Killspointsoutput--------------------------------------------------------
labelforKill = Label(main,text="Kills Points:" , font= 13 , bd=4, bg="Pink" , border= 4)
labelforKill.place(x=50,y=385)


Killpts = IntVar()
Killpts.set("")
Killpts1= Entry(main, textvar=Killpts ,font='lucida 11' , bd=7 )
Killpts1.pack()
Killpts1.place(x=180,y=385)

#Positionpintsoutput------------------------------------------------------
labelforPosition = Label(main,text="Poistion Points:" , font=13, bd=4 ,  bg="Pink", border=4)
labelforPosition.place(x=50,y=415)


Positionpts = IntVar()
Positionpts.set("")
Positionpts1= Entry(main, textvar=Positionpts ,font='lucida 11' , bd=7)
Positionpts1.pack()
Positionpts1.place(x=180,y=415)

#TotalPointsOutput-------------------------------------------------------------
labelfortotalPoints = Label(main, text="Total Points:" , font= 13 ,bd=4 , bg="Pink", border= 4)
labelfortotalPoints.place(x=50,y=445)

Totalpts = IntVar()
Totalpts.set("")
Totalpts1= Entry(main, textvar=Totalpts ,font='lucida 11' , bd=7)
Totalpts1.pack()
Totalpts1.place(x=180,y=445)


#Calculation Button
Calb = Button(main,  text= "Calculte" , font='Script 10 bold',bg='Gray' ,fg='black' ,bd=3 , command=Calculation)

Calb.pack()
Calb.place(x=50 , y=345)

#Clear Button--------------
ClearButton = Button(main, text="Clear" , font="Script 10 bold", bg="Gray" ,bd="3" , command= ClearAll)
ClearButton.place(x=334,y=345)

#Uid Lebel-------------
Uid = Label(main,text="UID:1086532491" , font="Vani 5",bg="Red" , bd="2" ,)
Uid.place(x=110,y=102)
Uid.pack()

main.mainloop()