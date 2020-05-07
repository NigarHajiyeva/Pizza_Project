from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import time
import pizza_dp

with sqlite3.connect('pizza.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL ,password TEXT NOT NULL);')
c.execute('CREATE TABLE IF NOT EXISTS user_orders (username TEXT NOT NULL, pizza_id  TEXT NOT NULL,price INT);')
db.commit()
db.close()


class main:
    def __init__(self,master):
    	# Window 
        self.master = master
       # IMAGE_PATH= 'a.png'
        #WIDTH, HEIGHT =1000,1000
        #master.geometry('{}x{}'.format(HEIGHT,WIDTH))
        #canvas=Canvas(master,width=WIDTH,height=HEIGHT)
        #canvas.pack()
        #img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        #canvas.background = img  # Keep a reference in case this code is put in a function.
        #bg = canvas.create_image(0, 0, anchor=NW, image=img)
        self.master.configure(bg="orchid")
        
       

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        
        self.widgets()

   
    def login(self):
    	
        with sqlite3.connect('pizza.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM users WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if self.username.get()=="admin" and self.password.get()=="admin":
            self.logf.pack_forget()
            self.admin_b_seeorders.place(x=50,y=150)
            self.admin_b_income.place(x=400,y=150)
        
        elif  result:
            self.logf.pack_forget()
            self.label_main.place(x=20,y=100)
            self.label2_main.place(x=450,y=100)
            self.label3_main.place(x=850,y=100)

            
            self.p1.place(x=70,y=350)
            self.p2.place(x=520,y=350)
            self.p3.place(x=920,y=350)
            self.l1.place(x=10,y=50)
            self.b1.place(x=20,y=500)
            self.b2.place(x=280,y=500)
            self.b3.place(x=540,y=500)
            self.label_extention.place(x=20,y=450)
            self.b_tomato.place(x=20,y=680)
            self.b_cheese.place(x=290,y=680)
            self.b_bbq.place(x=540,y=680)
            self.b4.place(x=540,y=730)
            self.b5.place(x=290,y=730)
            self.b6.place(x=20,y=730)
            self.b_order.place(x=920,y=780)
            self.b_prev.place(x=1250,y=60)
            
            
            
        else:
            ms.showerror('Username Not Found.','Try again or Create ')
    def admin(self):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        result = [x[0] for x in c.execute("SELECT price FROM user_orders")]
        count=0
        for i in result:
            count+=i
        string="Your income is "+str(count) +"$"
        self.admin_l1=Label(self.master,text=string,font=("arial",20))
        self.admin_l1.place(x=225,y=250)
            
    def all(self):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        result1=[x[0] for x in c.execute('SELECT username FROM user_orders')]
        result2=[x[0] for x in c.execute('SELECT pizza_id FROM user_orders')]

     

        for i in range(len(result1)):
            print(result1[i],result2[i])
            
        
        

    def create_pizza(self,a):
        if a=="Margherita":
            self.pizza=pizza_dp.PizzaBuilder(a)
        elif a=="Chicken_BBQ":
            self.pizza=pizza_dp.PizzaBuilder(a)
        elif a=="Pepperoni":
            self.pizza=pizza_dp.PizzaBuilder(a)




    def add_remove(self,ptype,extention,choice):
        if choice=="add":
            self.pizza.add_extension(extention)
        elif choice=="remove":
            self.pizza.remove_extension(extention)

    def order_price(self,pizza):
        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        insert='INSERT INTO user_orders(username,pizza_id,price) VALUES(?,?,?)'
        c.execute(insert,[(self.username.get()),(self.pizza.get_status()),(self.pizza.get_price())])
        db.commit()
        ms.showinfo('Price','Your order is {} dollar'.format(self.pizza.get_price()))
        

    def previous_order(self):
        

        with sqlite3.connect('pizza.db') as db:
            c=db.cursor()
        find_user=('SELECT * FROM user_orders WHERE username=?')
        c.execute(find_user,[(self.username.get())])
        result=c.fetchall()
        print("Username is",result[0][0])
        for i in result:
            print("Order:",i[1],end="\n")
            print("Price:",i[2],"dollar")
        ms.showinfo('Your Order','{}'.format(i[1]))
        
                  

            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('pizza.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM users WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO users(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.reg.pack_forget()
        self.head['text'] = ' PizzaDelivery '
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.reg.pack()

    
        
    def widgets(self):
        self.head = Label(self.master,bg='orchid',text = 'PizzaDelivery ',font = ('Times bold ',36))
        self.head.pack()
        
        self.logf = Frame(self.master,padx =20,pady = 20, bg='orchid')
        Label(self.logf,text = ' Username: ',fg='black', bg='orchid',font = ('Times bold',24)).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bg='violet',bd = 5,font = ('',15)).grid()
        Label(self.logf,text = ' Password: ',bg='orchid',fg='black',font = ('Times bold',24),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,bg='violet',font = ('',15),show = '*').grid()

        Button(self.logf,text = ' Login ',bd = 3 ,bg='cyan',width=15,font = ('',15),padx=5,pady=5,command=self.login).grid(row=6)
        Label(self.logf,text = ' Not have an account? ',fg='black', bg='deep pink',font = ('Italic',12)).grid(row=7)
        Button(self.logf,text = ' Create Account ',bg='cyan',width=15,bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=7,column=7)
        self.logf.pack()
        
        self.reg = Frame(self.master,padx =10,pady = 10, bg='orchid')
        
        Label(self.reg,text = 'Username: ',bg='orchid',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg,textvariable = self.n_username,bg='violet',bd = 5,font = ('',15)).grid()
        Label(self.reg,text = 'Password: ',bg='orchid',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg,textvariable = self.n_password,bg='violet',bd = 5,font = ('',15),show = '*').grid()
        Button(self.reg,text = 'Create Account',bd = 3 ,bg='cyan',font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.reg,text = 'Login>>',bd = 3 ,bg='cyan',font = ('',15),padx=5,pady=5,command=self.log).grid(column=2)

        #main page widgets    
        self.label_main=Label(self.master)
        self.label_main.img=ImageTk.PhotoImage(file="marg.jpg")
        self.label_main.config(image=self.label_main.img)
        self.label_main.pack_forget()

        self.label2_main=Label(self.master)
        self.label2_main.img=ImageTk.PhotoImage(file="chicken_bbq.jpg")
        self.label2_main.config(image=self.label2_main.img)
        self.label2_main.pack_forget()

        self.label3_main=Label(self.master)
        self.label3_main.img=ImageTk.PhotoImage(file="pepperoni.jpg")
        self.label3_main.config(image=self.label3_main.img)
        self.label3_main.pack_forget()

        self.b1=Label(self.master)
        self.b1.img=ImageTk.PhotoImage(file="tomato.png")
        self.b1.config(image=self.b1.img)
        self.b1.pack_forget()

        self.b2=Label(self.master)
        self.b2.img=ImageTk.PhotoImage(file="cheese.png")
        self.b2.config(image=self.b2.img)
        self.b2.pack_forget()

        self.b3=Label(self.master)
        self.b3.img=ImageTk.PhotoImage(file="bbq.png")
        self.b3.config(image=self.b3.img)
        self.b3.pack_forget()
        

       # self.p1=Label(self.master,bg='orchid',text="          Margherita",font=("arial",20))
       # self.p1.pack_forget()
       # self.p2=Label(self.master,bg='orchid',text="          Chicken_BBQ",font=("arial",20))
       # self.p2.pack_forget()
        self.l1=Label(self.master,bg='orchid',text="Pizza Menu",font=("arial",20))
        self.l1.pack_forget()

        self.v=IntVar()

        self.p1=Radiobutton(self.master,variable=self.v,value=1,bg='cyan',width=15,text="Margherita",font=('',15),command=lambda:self.create_pizza("Margherita"))
        self.p1.pack_forget()
        self.p2=Radiobutton(self.master,variable=self.v,value=2,bg='cyan',width=15,text="Chicken_BBQ",font=('',15),command=lambda:self.create_pizza("Chicken_BBQ"))
        self.p2.pack_forget()
        self.p3=Radiobutton(self.master,variable=self.v,value=3,bg='cyan',width=15,text="Pepperoni",font=('',15),command=lambda:self.create_pizza("Pepperoni"))
       # self.b1.pack_forget()
        #self.p2.pack_forget()
        self.p3.pack_forget()
        
        self.label_extention=Label(self.master,bg='orchid',text="Extentions",font=("arial",20))
        self.label_extention.pack_forget()
        self.b_tomato=Button(self.master,text="add",bd=3,bg='cyan',width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"Tomato","add"))
        self.b_tomato.pack_forget()
        self.b_cheese=Button(self.master,text="add",bd=3,bg='cyan',width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"Cheese","add"))
        self.b_cheese.pack_forget()
        self.b_bbq=Button(self.master,text="add",bg='cyan',bd=3,width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"BBQ","add"))
        self.b_bbq.pack_forget()
        self.b4=Button(self.master,text="remove",bg='cyan',bd=3,width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"BBQ","remove"))
        self.b4.pack_forget()
        self.b5=Button(self.master,text="remove",bg='cyan',bd=3,width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"Cheese","remove"))
        self.b5.pack_forget()
        self.b6=Button(self.master,text="remove",bg='cyan',bd=3,width=15,font=('',15),command=lambda:self.add_remove(self.pizza,"Tomato","remove"))
        self.b6.pack_forget()

        

        self.b_order=Button(self.master,text="    Order     ",bd=3,font=('',15),command=lambda:self.order_price(self.pizza))
        self.b_order.pack_forget()

        self.b_prev=Button(self.master,text="See History ",bd=3,font=('',15),command=lambda:self.previous_order())
        self.b_prev.pack_forget()

        self.admin_b_seeorders=Button(self.master,text="See all orders",bd=3,font=('arial',20),bg="yellow",command=lambda:self.all())
        self.admin_b_seeorders.pack_forget()
        self.admin_b_income=Button(self.master,text="Income",bd=3,font=('arial',20),bg="yellow",command=lambda:self.admin())
        self.admin_b_income.pack_forget()

       




    
#create window and application object
root = Tk()
root.geometry("1000x1000")


#root.title("Login Form")
main(root)
root.mainloop()
