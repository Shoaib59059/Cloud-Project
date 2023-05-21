
from tkinter import *
from database import *
from verification import *
from data import *
from calc import *
from PIL import ImageTk,Image
from functools import partial


# define login function
def login_screen():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="Enter Username or Aadhar number").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
    global aadhar_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
    aadhar_verify = StringVar()
 
   
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="Aadhar number ").pack()
    aadhar_login_entry = Entry(login_screen, textvariable=aadhar_verify)
    aadhar_login_entry.pack()



    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()

    Label(login_screen, text="").pack()
    # Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

def register():
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
 
# Set text variables
    global username
    username = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()



def main_account_screen():
    global main_screen
 
# add command=register in button widget
 
    
    main_screen = Tk()
    main_screen.geometry("800x700")
    main_screen.title("main_screen")
 
    # create a Form label 
    Label(text="Electricity Billing system", bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    # create Login Button 
    Button(text="Login", height="2", width="30", command = login_screen).pack()
    Label(text="").pack() 


    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text = "").pack()
    # Button(text = "Admin Login",height = "2",width = "30",command = admin_login_screen).pack()
    my_canvas = Canvas(main_screen,width = 800 , height = 700)
    my_canvas.pack(fill = "both" , expand= True)
    bg = ImageTk.PhotoImage(file = "elctric.jpg")
    #set image in canvas
    my_canvas.create_image(0,0,image = bg,anchor="nw")
    def resizer(e):
        global bg1,resized_bg,new_bg
        bg1 = Image.open("elctric.jpg")
        resized_bg =bg1.resize((e.width,e.height))
        new_bg = ImageTk.PhotoImage(resized_bg)
        my_canvas.create_image(0,0,image = new_bg,anchor="nw")
    main_screen.mainloop()
 
main_account_screen()