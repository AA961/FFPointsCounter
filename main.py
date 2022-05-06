from tkinter import*
import tkinter

def Calculation(event):
    pass




main = Tk()
main.geometry("480x500")
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
kill1 = IntVar()
kill1.set("")
ks1 = Entry(main, textvar=kill1 ,font='lucida 10', bd=4)
ks1.pack()
ks1.place(x=50,y=270)

Lfor2kill = Label(main, text="2nd" ,font=13 , justify=LEFT , anchor="e")
Lfor2kill.pack()
Lfor2kill.place(x=20, y=295)
kill2 = IntVar()
kill2.set("")
ks2 = Entry(main, textvar=kill2 ,font='lucida 10', bd=4)
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

#Result Screen


Rs = IntVar()
Rs.set("")
Rs1= Entry(main, textvar=Rs ,font='lucida 15' , bd=10)
Rs1.pack()
Rs1.place(x=160,y=375)

print='CalculationButton'
Calb = Button(main,  text= "Calculte" , font='Script 23 bold',bg='Gray' ,fg='black' ,bd=10 )
Calb.bind("<Button-1>" , Calculation)
Calb.pack()
Calb.place(x=50 , y=360)



main.mainloop()