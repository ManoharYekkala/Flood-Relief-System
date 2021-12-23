from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk, filedialog
import webbrowser
import DB_connect

#screen info--


w=Tk()
w.geometry('925x500')
w.title('Flood Relief Manager')
w.configure(bg='#ff4f5a')
w.minsize(925,500)

#welcome screen--

def welcome():
    welcome_win=Frame(w,width=925,height=500,bg='white')
    welcome_win.place(x=0,y=0)
    f1=Frame(welcome_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Flood.jpg"))
    Label(welcome_win,image=img1,border=0,bg='white').place(x=0,y=0)

    l2=Label(welcome_win,text="WELCOME",fg='#655ada',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=545,y=0)



    #-mech------------------------------------------------


    #------------------------------------------------------
    Button(f1,width=39,pady=7,text='PROCEED',bg='#675bdb',fg='white',border=0,command=mangport).place(x=35,y=204)
    l1=Label(f1,text="Flood Relief Management\nSoftware By\nGroup 21",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=35,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#welcome screen end--

#management portal--

def mangport():
    mangport_win=Frame(w,width=925,height=500,bg='white')
    mangport_win.place(x=0,y=0)
    f1=Frame(mangport_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Nav.jpg"))
    Label(mangport_win,image=img1,border=0,bg='white').place(x=20,y=10)

    l2=Label(mangport_win,text="MANAGEMENT",fg='#fdb047',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=510,y=0)

    l3=Label(mangport_win,text="PORTAL",fg='#fdb047',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=570,y=60)


    #-mech-------------------------------------------------

    #------------------------------------------------------
    Button(f1,width=39,pady=7,text='AFFECTED AREA',bg='#fd8596',fg='white',border=0,command=affnav).place(x=35,y=130)
    
    Button(f1,width=39,pady=7,text='MANAGE INVENTORY',bg='#fd8596',fg='white',border=0,command=invnav).place(x=35,y=175)
        
    Button(f1,width=39,pady=7,text='RESCUED PEOPLE',bg='#fd8596',fg='white',border=0,command=resnav).place(x=35,y=220)
    
    Button(f1,width=30,pady=7,text='DONATE',bg='#655ada',fg='white',border=0,command=donate).place(x=70,y=265)
    
    l1=Label(f1,text="Choose an option:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=75,y=60)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#management portal end--

#affected area nav--

def affnav():
    affnav_win=Frame(w,width=925,height=500,bg='white')
    affnav_win.place(x=0,y=0)
    f1=Frame(affnav_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Nav.jpg"))
    Label(affnav_win,image=img1,border=0,bg='white').place(x=20,y=10)

    l2=Label(affnav_win,text="AFFECTED",fg='#fdb047',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=550,y=0)

    l3=Label(affnav_win,text="AREA",fg='#fdb047',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=590,y=60)


    #-mech-------------------------------------------------

    #------------------------------------------------------
    
    Button(f1,width=30,pady=7,text='CREATE AN ENTRY',bg='#fd8596',fg='white',border=0,command=affrec).place(x=70,y=140)
        
    Button(f1,width=30,pady=7,text='VIEW RECORDS',bg='#fd8596',fg='white',border=0,command=affdis).place(x=70,y=190)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#fd8596',fg='white',border=0,command=mangport)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Choose an option:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=75,y=60)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#affected area nav end--

#affected area record--

def affrec():
    affrec_win=Frame(w,width=925,height=500,bg='white')
    affrec_win.place(x=0,y=0)
    f1=Frame(affrec_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records.jpg"))
    Label(affrec_win,image=img1,border=0,bg='white').place(x=0,y=100)

    l2=Label(affrec_win,text="ENTRY",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=600,y=0)

    l3=Label(affrec_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=587,y=60)


    #-mech------------------------------------------------
    def addrec():
        insertsql = "INSERT INTO affected_areas VALUES (%s,%s,%s)"
        if pincode1.get()==0:
            L=Label(f1,text="PINCODE CANNOT BE 0")
            L.place(x=150,y=290)
        record = (pincode1.get(), location.get(), population.get())
        DB_connect.insert_into_table(insertsql, record)
        L=Label(f1,text="ENTRY ADDED")
        L.place(x=150,y=290)


    xpos = 70
    ypos = 80
    pincode1 = IntVar()
    lbl_pincode = Label(f1, text="Pincode:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=xpos, y=ypos)
    E_pincode = Entry(f1, font=('ariel', 15),textvariable=pincode1)
    E_pincode.place(x=xpos + 150, y=ypos)

    location = StringVar()
    lbl_Location = Label(f1, text="Location:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_Location.place(x=xpos, y=ypos + 50)
    E_Location = Entry(f1, font=('ariel', 15),textvariable=location)
    E_Location.place(x=xpos + 150, y=ypos + 50)

    population = IntVar()
    lbl_population = Label(f1, text="Population:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_population.place(x=xpos, y=ypos + 100)
    E_population = Entry(f1, font=('ariel', 15),textvariable=population)
    E_population.place(x=xpos + 150, y=ypos + 100)




    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='ADD',bg='#b53bc2',fg='white',border=0,command=addrec)
    button_add1.place(x=35,y=250)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=affnav)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Fill the fields to create an entry:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=10,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)
    
    

#affected area record end--

#affected area display --

def affdis():
    affdis_win=Frame(w,width=925,height=500,bg='white')
    affdis_win.place(x=0,y=0)
    f1=Frame(affdis_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records2.jpg"))
    Label(affdis_win,image=img1,border=0,bg='white').place(x=0,y=50)

    l2=Label(affdis_win,text="RECORDS",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=560,y=0)

    l3=Label(affdis_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=577,y=60)


    #-mech------------------------------------------------
    def displayrec():
        disp_sql=f"SELECT * FROM affected_areas where pincode={pincode.get()}"
        row=DB_connect.search_in_table(disp_sql)
        if row==False:
            lbl = Label(f1, text='NO DATA FOUND!')
            lbl.place(x=150, y=290)
        else:
            lbl1 = Label(f1,text=f"Pincode: {row[0]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl1.place(x=90, y=120)
            lbl2 = Label(f1,text=f"Location: {row[1]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl2.place(x=90, y=150)
            lbl3 = Label(f1,text=f"Population: {row[2]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl3.place(x=90, y=180)

    lbl_pincode = Label(f1, text="Pincode:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=90, y=80)
    pincode=IntVar()
    E1_pincode = Entry(f1, font=('Axiforma-Bold', 15),textvariable=pincode)
    E1_pincode.place(x=240, y=80)





    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='SUBMIT',bg='#b53bc2',fg='white',border=0,command=displayrec)
    button_add1.place(x=35,y=250)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=affnav)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Fill the entry to view records:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=35,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#affected area display end--

#inventory nav--

def invnav():
    invnav_win=Frame(w,width=925,height=500,bg='white')
    invnav_win.place(x=0,y=0)
    f1=Frame(invnav_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Nav.jpg"))
    Label(invnav_win,image=img1,border=0,bg='white').place(x=20,y=10)

    l2=Label(invnav_win,text="MANAGE",fg='#fdb047',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=555,y=0)

    l3=Label(invnav_win,text="INVENTORY",fg='#fdb047',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=525,y=60)


    #-mech-------------------------------------------------

    #------------------------------------------------------
    
    Button(f1,width=30,pady=7,text='CREATE AN ENTRY',bg='#fd8596',fg='white',border=0,command=invrec).place(x=70,y=140)
        
    Button(f1,width=30,pady=7,text='VIEW RECORDS',bg='#fd8596',fg='white',border=0,command=invdis).place(x=70,y=190)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#fd8596',fg='white',border=0,command=mangport)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Choose an option:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=75,y=60)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#inventory nav end--

#inventory record--

def invrec():
    invrec_win=Frame(w,width=925,height=500,bg='white')
    invrec_win.place(x=0,y=0)
    f1=Frame(invrec_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records.jpg"))
    Label(invrec_win,image=img1,border=0,bg='white').place(x=0,y=100)

    l2=Label(invrec_win,text="ENTRY",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=600,y=0)

    l3=Label(invrec_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=587,y=60)


    #-mech------------------------------------------------
    def addrec2():
        insertsql = "INSERT INTO inventory VALUES (%s,%s,%s)"
        record = (Itemid.get(), Item_Name.get(), quantity.get())
        DB_connect.insert_into_table(insertsql, record)
        L=Label(f1,text="ENTRY ADDED")
        L.place(x=150,y=290)


    xpos = 70
    ypos = 80
    Itemid = IntVar()
    lbl_pincode = Label(f1, text="Item ID:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=xpos, y=ypos)
    E_pincode = Entry(f1, font=('ariel', 15),textvariable=Itemid)
    E_pincode.place(x=xpos + 150, y=ypos)

    Item_Name = StringVar()
    lbl_Location = Label(f1, text="Item Name:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_Location.place(x=xpos, y=ypos + 50)
    E_Location = Entry(f1, font=('ariel', 15),textvariable=Item_Name)
    E_Location.place(x=xpos + 150, y=ypos + 50)

    quantity = IntVar()
    lbl_population = Label(f1, text="Quantity:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_population.place(x=xpos, y=ypos + 100)
    E_population = Entry(f1, font=('ariel', 15),textvariable=quantity)
    E_population.place(x=xpos + 150, y=ypos + 100)




    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='ADD',bg='#b53bc2',fg='white',border=0,command=addrec2)
    button_add1.place(x=35,y=250)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=invnav)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Fill the fields to create an entry:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=10,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)
    
    

#inventory record end--

#inventory display --

def invdis():
    invdis_win=Frame(w,width=925,height=500,bg='white')
    invdis_win.place(x=0,y=0)
    f1=Frame(invdis_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records2.jpg"))
    Label(invdis_win,image=img1,border=0,bg='white').place(x=0,y=50)

    l2=Label(invdis_win,text="RECORDS",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=560,y=0)

    l3=Label(invdis_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=577,y=60)


    #-mech------------------------------------------------
    def displayrec2():
        disp_sql = f"SELECT * FROM inventory where Item_ID={Itemid1.get()}"
        row=DB_connect.search_in_table(disp_sql)
        if row==False:
            lbl = Label(f1, text='NO DATA FOUND!')
            lbl.place(x=150, y=290)
        else:
            lbl1 = Label(f1,text=f"Item ID: {row[0]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl1.place(x=90, y=120)
            lbl2 = Label(f1,text=f"Item Name: {row[1]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl2.place(x=90, y=150)
            lbl3 = Label(f1,text=f"Quantity: {row[2]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl3.place(x=90, y=180)

    lbl_pincode = Label(f1, text="Item ID:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=90, y=80)
    Itemid1=IntVar()
    E1_pincode = Entry(f1, font=('Axiforma-Bold', 15),textvariable=Itemid1)
    E1_pincode.place(x=240, y=80)





    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='SUBMIT',bg='#b53bc2',fg='white',border=0,command=displayrec2)
    button_add1.place(x=35,y=250)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=invnav)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Fill the entry to view records:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=35,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#inventory display end--

#rescue nav--

def resnav():
    resnav_win=Frame(w,width=925,height=500,bg='white')
    resnav_win.place(x=0,y=0)
    f1=Frame(resnav_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Nav.jpg"))
    Label(resnav_win,image=img1,border=0,bg='white').place(x=20,y=10)

    l2=Label(resnav_win,text="RESCUED",fg='#fdb047',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=560,y=0)

    l3=Label(resnav_win,text="PEOPLE",fg='#fdb047',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=570,y=60)


    #-mech-------------------------------------------------

    #------------------------------------------------------
    
    Button(f1,width=30,pady=7,text='CREATE AN ENTRY',bg='#fd8596',fg='white',border=0,command=resrec).place(x=70,y=140)
        
    Button(f1,width=30,pady=7,text='VIEW RECORDS',bg='#fd8596',fg='white',border=0,command=resdis).place(x=70,y=190)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#fd8596',fg='white',border=0,command=mangport)
    button_back1.place(x=190,y=250)
    
    l1=Label(f1,text="Choose an option:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=75,y=60)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=310)

#rescue nav end--

#rescue record--

def resrec():
    resrec_win=Frame(w,width=925,height=500,bg='white')
    resrec_win.place(x=0,y=0)
    f1=Frame(resrec_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records.jpg"))
    Label(resrec_win,image=img1,border=0,bg='white').place(x=0,y=100)

    l2=Label(resrec_win,text="ENTRY",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=600,y=0)

    l3=Label(resrec_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=587,y=60)


    #-mech------------------------------------------------
    def addrec3():
        insertsql = "INSERT INTO rescued_people VALUES (%s,%s,%s,%s)"
        record = (Rid.get(), Name.get(), Age.get(), address.get())
        DB_connect.insert_into_table(insertsql, record)
        L=Label(f1,text="ENTRY ADDED")
        L.place(x=150,y=290)


    xpos = 70
    ypos = 80
    Rid = IntVar()
    lbl_pincode = Label(f1, text="Rescue ID:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=xpos, y=ypos)
    E_pincode = Entry(f1, font=('ariel', 15),textvariable=Rid)
    E_pincode.place(x=xpos + 150, y=ypos)

    Name = StringVar()
    lbl_Location = Label(f1, text="Name:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_Location.place(x=xpos, y=ypos + 50)
    E_Location = Entry(f1, font=('ariel', 15),textvariable=Name)
    E_Location.place(x=xpos + 150, y=ypos + 50)

    Age = IntVar()
    lbl_population = Label(f1, text="Age:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_population.place(x=xpos, y=ypos + 100)
    E_population = Entry(f1, font=('ariel', 15),textvariable=Age)
    E_population.place(x=xpos + 150, y=ypos + 100)

    address = StringVar()
    lbl_address = Label(f1, text="Address:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_address.place(x=xpos, y=ypos + 150)
    E_address = Entry(f1, font=('ariel', 15),textvariable=address)
    E_address.place(x=xpos + 150, y=ypos + 150)




    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='ADD',bg='#b53bc2',fg='white',border=0,command=addrec3)
    button_add1.place(x=35,y=290)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=resnav)
    button_back1.place(x=190,y=290)
    
    l1=Label(f1,text="Fill the fields to create an entry:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=10,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=330)
    
    

#rescue record end--

#rescue display --

def resdis():
    resdis_win=Frame(w,width=925,height=500,bg='white')
    resdis_win.place(x=0,y=0)
    f1=Frame(resdis_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("Records2.jpg"))
    Label(resdis_win,image=img1,border=0,bg='white').place(x=0,y=50)

    l2=Label(resdis_win,text="RECORDS",fg='#406ff9',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=560,y=0)

    l3=Label(resdis_win,text="PORTAL",fg='#406ff9',bg='white')
    l3.config(font=('Axiforma-Bold',30, 'bold'))
    l3.place(x=577,y=60)


    #-mech------------------------------------------------
    def displayrec3():
        disp_sql = f"SELECT * FROM rescued_people where R_id={Rid1.get()}"
        row=DB_connect.search_in_table(disp_sql)
        if row==False:
            lbl = Label(f1, text='NO DATA FOUND!')
            lbl.place(x=150, y=290)
        else:
            lbl1 = Label(f1,text=f"Rescue ID: {row[0]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl1.place(x=90, y=120)
            lbl2 = Label(f1,text=f"Name: {row[1]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl2.place(x=90, y=150)
            lbl3 = Label(f1,text=f"Age: {row[2]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl3.place(x=90, y=180)
            lbl4 = Label(f1,text=f"Address: {row[2]}", font=('Axiforma-Bold', 15),fg="#ef497b",bg='white')
            lbl4.place(x=90, y=215)

    lbl_pincode = Label(f1, text="Rescue ID:", font=('Axiforma-Bold', 15), bg='white', fg='black')
    lbl_pincode.place(x=90, y=80)
    Rid1=IntVar()
    E1_pincode = Entry(f1, font=('Axiforma-Bold', 15),textvariable=Rid1)
    E1_pincode.place(x=240, y=80)





    #------------------------------------------------------

    
    button_add1=Button(f1,width=20,pady=7,text='SUBMIT',bg='#b53bc2',fg='white',border=0,command=displayrec3)
    button_add1.place(x=35,y=290)
    
    button_back1=Button(f1,width=20,pady=7,text='BACK',bg='#b53bc2',fg='white',border=0,command=resnav)
    button_back1.place(x=190,y=290)
    
    l1=Label(f1,text="Fill the entry to view records:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=35,y=30)

    b2=Button(f1,width=10,text='ABOUT US',border=0,bg='white',fg='#ff4f5a',command=abbus)
    b2.place(x=285,y=330)

#rescue display end--

#donate--
url = "https://www.globalgiving.org/kerala-flood-relief/"
def donate():
    webbrowser.open(url,new=1) #new=1 opens in new window new=2 opens new tab
    
#donate end--

#about us--

def abbus():
    abbus_win=Frame(w,width=925,height=500,bg='white')
    abbus_win.place(x=0,y=0)
    f1=Frame(abbus_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("About.jpg"))
    Label(abbus_win,image=img1,border=0,bg='white').place(x=0,y=0)

    l2=Label(abbus_win,text="ABOUT US",fg='#655ada',bg='white')
    l2.config(font=('Axiforma-Bold',30, 'bold'))
    l2.place(x=565,y=0)



    #-mech------------------------------------------------


    #------------------------------------------------------
    b2=Button(f1,width=10,text='HOME',border=0,bg='white',fg='#ff4f5a',command=welcome)
    b2.place(x=285,y=330)
    
    l1=Label(f1,text="Software Made By:",fg="black",bg='white')
    l1.config(font=('Axiforma-Bold',15, ))
    l1.place(x=85,y=0)
    
    l3=Label(f1,text="Mohammad Haider\n(12018707)\n\nKota Manohar Babu Yekkela\n(12018548)\n\nAbhitesh Bharadwaj\n(12018557)",fg="#4693fb",bg='white')
    l3.config(font=('Axiforma-Bold',15, ))
    l3.place(x=35,y=40)

#about us end--

welcome() #default screen initiator

w.mainloop()