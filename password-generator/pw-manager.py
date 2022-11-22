from tkinter import *
from tkinter import messagebox
import random
import numpy as np
from PIL import Image, ImageTk

#classes contain information about all the pages

class LoginForm:
    def __init__(self, window):
        self.window = window
        window.title('PWLibrary Login')
        self.window.geometry('750x500') 

        #self.window.state('zoomed')
        #zoomed could be used for future GUI problems, right now all text is placed based on coordinates

        #the window is not resizable, it stays at 750 x 500
        self.window.resizable(0, 0)

        #background color
        window.configure(bg='#393E41')

        #white background frame
        self.login_frame = Frame(self.window, bg='#F6F7EB', width=690, height=400)
        self.login_frame.place(x=30, y=70)

        #text
        self.heading = Label(self.window, text='PWL Login', font=('yu gothic ui', 25, 'bold'), bg='#393E41', fg='#F6F7EB')
        self.heading.place(x=215, y=10, width='350', height='50')

        self.welcometxt = Label(window, text='Welcome!', font=('yu gothic ui', 20, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.welcometxt.place(x=325, y=75)

        self.usernametxt = Label(window, text='Username', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.usernametxt.place(x=160, y=175)

        self.passwordtxt = Label(window, text='Password', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.passwordtxt.place(x=160, y=255)

        #global
        global unentry
        global pwentry

        #username and password entry
        self.unentry = Entry(window, bd=5)
        self.unentry.place(x=515, y=183)  

        self.pwentry = Entry(window, bd=5)
        self.pwentry.place(x=515, y=263)

        #button commands
        def forgotpw():
            messagebox.showinfo("Forgot Password", "unfortunately, peanut butter")

        #when both entries match the username and password, it opens the menu page
        def login():
            username = self.unentry.get()
            password = self.pwentry.get()

            if (username=="" and password=="") or (username=="") or (password==""):
                messagebox.showerror("Error", "Blank Not Allowed")
            
            elif (username=="TESTUSER" and password=="TESTPASS"):
                messagebox.showinfo("Log In", "You are now logged in succesfully")
                window.destroy()
                menupage()

            else:
                messagebox.showinfo("Log In", "Incorrect username and password")

        #buttons
        self.loginbutton = Button(window, text='Login', command=login, height='1', width='13', bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#44BBA4')
        self.loginbutton.place(x=325, y=330)

        self.forgotpwbutton = Button(window, text='Forgot Password', command=forgotpw, height='1', width='13', bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#44BBA4')
        self.forgotpwbutton.place(x=325, y=400)

        self.quitbutton = Button(window, text='QUIT', command=window.destroy, height=1, bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#E94F37')
        self.quitbutton.place(x=15, y=15)

        #images
        #resizes the image using PIL
        #a small border is left around the image, it seems like this is caused by the image itself
        image = Image.open('security.png')
        img = image.resize((187, 98))
        self.my_img = ImageTk.PhotoImage(img)
        self.security_label = Label(image=self.my_img)
        self.security_label.place(x=75, y=320)

class MainMenu:
    def __init__(self, window):
        #going to a different page creates a new window

        #default window settings
        self.window = window
        window.title("PWLibrary Menu")
        self.window.geometry('750x500')
        self.window.resizable(0, 0)

        #background color
        window.configure(bg='#393E41')

        #white frame
        self.menu_frame = Frame(self.window, bg='#F6F7EB', width=690, height=400)
        self.menu_frame.place(x=30, y=70)

        #text
        self.heading1 = Label(self.window, text='Main Menu', font=('yu gothic ui', 25, 'bold'), bg='#393E41', fg='#F6F7EB')
        self.heading1.place(x=215, y=10, width='350', height='50')

        self.option1txt = Label(window, text='Find passwords', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.option1txt.place(x=95, y=150)

        self.option2txt = Label(window, text='Add Passwords', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.option2txt.place(x=310, y=150)

        self.option3txt = Label(window, text='Generate Passwords', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.option3txt.place(x=500, y=150)

        self.option4txt = Label(window, text='Delete Saved Passwords', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.option4txt.place(x=95, y=280)

        # password
        self.password = ""

        #buttons and the button commands
        def logoutbuttoncommand():
            window.destroy()
            loginpage()

        def findpassword():
            #currently works with a msgbox, therefore it doesn't need a new page
            #if its empty, it doesn't print anything

            file1 = open("entry_list.txt")
            file_contents = file1.read()

            if file_contents == "":
                messagebox.showinfo("Password List", "No Passwords In Library")
                file1.close

            else:
                messagebox.showinfo("Password List", file_contents)
                file1.close()
        
        def addpassword():
            window.destroy()
            addpwpage()

        def generatepassword():
            window.destroy()
            pwgenpage()

        def deletepasswords():
            #"r+" for reading and writing
            #truncate changes the size to 0, erasing everything

            file1 = open("entry_list.txt", "r+")
            file1.truncate(0)
            file1.close()

        self.logoutbutton = Button(window, text='LOG OUT', command=logoutbuttoncommand, height=1, bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#E94F37')
        self.logoutbutton.place(x=15, y=15)
        
        self.opt1button = Button(window, text='Find Passwords', command=findpassword, height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.opt1button.place(x=105, y=200)

        self.opt2button = Button(window, text='Add Passwords', command=addpassword, height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.opt2button.place(x=322, y=200)

        self.opt3button = Button(window, text='Generate Passwords', command=generatepassword, height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.opt3button.place(x=520, y=200)

        self.opt4button = Button(window, text='Delete', command=deletepasswords, height=1, bd=6, font=('yu gothic ui', 10, 'bold'), background='#E94F37', foreground='#F6F7EB', activebackground='#E94F37', activeforeground='#F6F7EB')
        self.opt4button.place(x=105, y=330)

class PWGen:
    def __init__(self, window):
        #default settings for the window
        self.window = window
        window.title("PWLibrary Password Generator")
        self.window.geometry('750x500')
        self.window.resizable(0, 0)

        #background color
        window.configure(bg='#393E41')

        #white frame
        self.menu_frame = Frame(self.window, bg='#F6F7EB', width=690, height=400)
        self.menu_frame.place(x=30, y=70)

        #text
        self.heading2 = Label(self.window, text='Generate Passwords', font=('yu gothic ui', 25, 'bold'), bg='#393E41', fg='#F6F7EB')
        self.heading2.place(x=215, y=10, width='350', height='50')

        self.pwlengthtxt = Label(self.window, text='Password Length', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.pwlengthtxt.place(x=75, y=410, width='250', height='50')

        #places the frame before generatepw is used
        #relief (flat, raised, sunken, groove, ridge)
        self.removeoldpwtxt = Frame(self.window, bg='#F6F7EB', width=670, height=50, borderwidth=2, relief="groove")
        self.removeoldpwtxt.place(x=40, y=80)

        #toggle buttons labels (text)
        self.smallletterstoggle = Label(self.window, text='Small', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.smallletterstoggle.place(x=120, y=180, height='50')

        self.capsletterstoggle = Label(self.window, text='Caps', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.capsletterstoggle.place(x=290, y=180, height='50')

        self.numbersletterstoggle = Label(self.window, text='Numbers', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.numbersletterstoggle.place(x=440, y=180, height='50')

        self.specialletterstoggle = Label(self.window, text='Special', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
        self.specialletterstoggle.place(x=613, y=180, height='50')

        #buttons
        def logoutbuttoncommand():
            window.destroy()
            loginpage()

        def mainmenucommand():
            window.destroy()
            menupage()

        #the toggle buttons are all selected in the beginning
        #outside of generatepw because it would keep changing when trying to generate a password
        self.Q=True
        self.R=True
        self.S=True
        self.T=True

        #generates a new password using numpy
        #n is the number from the sliderbar, it is the length of the password
        def generatepw(self):
            empty = list("")
            small = list("abcdefghijklmnopqrstuvwxyz")#codeletter Q
            caps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#codeletter R
            number = list("1234567890")#codeletter S
            special = list("!@$%^&*()?#,.")#codeletter T
            n = self.sliderbar.get()
            a = empty

            allow_gen = True

            #a is the list used for the password
            #it adds the character lists to a if one of the toggle buttons is on
            if self.Q == True:
                a = a + small
            if self.R == True:
                a = a + caps
            if self.S == True:
                a = a + number
            if self.T == True:
                a = a + special

            #returns an error if the list is empty
            #only generates a password if the list contains 1 set of characters
            if a == empty:
                #print("error, select what characters you want in your password")
                messagebox.showinfo("Error", "Error, select at least one set of characters")
                allow_gen = False

            #replace = True allows characters to be used twice
            if allow_gen == True:
                choices = np.random.choice(a, size=n, replace=True)
                password = ''.join(choices)

                print(password)

                self.password = password

            #places a white rectangle over the old password
            self.removeoldpwtxt = Frame(self.window, bg='#F6F7EB', width=670, height=50, borderwidth=2, relief="groove")
            self.removeoldpwtxt.place(x=40, y=80)

            #shows the password on the screen
            generatedpassword = Label(self.window, text=password, font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41', anchor="center")
            generatedpassword.place(x=375, y=100, height='30', anchor='center')

            #password strength label
            #password strength is decided by the length of the password, since no one knows which characters are in use

            #creates a bar that increases in length and changes colour
            
            self.eraserframe = Frame(self.window, bg='#F6F7EB', width=455, height=10, borderwidth=2)
            self.eraserframe.place(x=70, y=150)

            self.strengthframe = Frame(self.window, bg='#f2d816', width=15, height=10, borderwidth=2)
            self.strengthframe.place(x=70, y=150)

            self.textremoverstrengthframe = Frame(self.window, bg='#F6F7EB', width=130, height=20, borderwidth=2)
            self.textremoverstrengthframe.place(x=600, y=152, anchor='center')

            strengthtext = ''

            if n >= 0 and n <= 5:
                self.strengthframe.config(bg='#f21616')
                self.strengthframe.config(width=15)
                strengthtext = 'Weak'

            if n >= 6 and n <= 10:
                self.strengthframe.config(bg='#f23b16')
                self.strengthframe.config(width=55)
                strengthtext = 'Weak'

            if n >= 11 and n <= 15:
                self.strengthframe.config(bg='#f25f16')
                self.strengthframe.config(width=105)
                strengthtext = 'Mediocre'

            if n >= 16 and n <= 20:
                self.strengthframe.config(bg='#f28f16')
                self.strengthframe.config(width=155)
                strengthtext = 'Mediocre'

            if n >= 21 and n <= 25:
                self.strengthframe.config(bg='#f2c616')
                self.strengthframe.config(width=205)
                strengthtext = 'Good'

            if n >= 26 and n <= 30:
                self.strengthframe.config(bg='#e7f216')
                self.strengthframe.config(width=255)
                strengthtext = 'Good'

            if n >= 31 and n <= 35:
                self.strengthframe.config(bg='#bbf216')
                self.strengthframe.config(width=305)
                strengthtext = 'Strong'

            if n >= 36 and n <= 40:
                self.strengthframe.config(bg='#8ff216')
                self.strengthframe.config(width=355)
                strengthtext = 'Strong'

            if n >= 41 and n <= 45:
                self.strengthframe.config(bg='#63f216')
                self.strengthframe.config(width=405)
                strengthtext = 'Unbreakable'

            if n >= 46 and n <= 50:
                self.strengthframe.config(bg='#2cf216')
                self.strengthframe.config(width=455)
                strengthtext = 'Unbreakable'

            strengthtext = Label(self.window, text=strengthtext, font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41', anchor='center')
            strengthtext.place(x=600, y=152, height='30', anchor='center')

        #command for the copybutton
        #clears the clipboard, then adds the password
        #updates the window so that it stays on the clipboard
        
        def copyclipboard(self):
            window.clipboard_clear()
            window.clipboard_append(self.password)
            window.update()

        #toggle button commands
        def SimpletoggleSmall():
            if toggle_button_small.config('bg')[-1] == '#F6F7EB':
                toggle_button_small.config(bg='#E94F37')
                self.Q = True
            else:
                toggle_button_small.config(bg='#F6F7EB')
                toggle_button_small.config(activebackground='#E94F37')
                self.Q = False
        
        def SimpletoggleCaps():
            if toggle_button_caps.config('bg')[-1] == '#F6F7EB':
                toggle_button_caps.config(bg='#E94F37')
                self.R = True
            else:
                toggle_button_caps.config(bg='#F6F7EB')
                toggle_button_caps.config(activebackground='#E94F37')
                self.R = False

        def SimpletoggleNumbers():
            if toggle_button_numbers.config('bg')[-1] == '#F6F7EB':
                toggle_button_numbers.config(bg='#E94F37')
                self.S = True
            else:
                toggle_button_numbers.config(bg='#F6F7EB')
                toggle_button_numbers.config(activebackground='#E94F37')
                self.S = False

        def SimpletoggleSpecial():
            if toggle_button_special.config('bg')[-1] == '#F6F7EB':
                toggle_button_special.config(bg='#E94F37')
                self.T = True

            else:
                toggle_button_special.config(bg='#F6F7EB')
                toggle_button_special.config(activebackground='#E94F37')
                self.T = False

        #buttons
        self.logout_button = Button(window, text='LOG OUT', command=logoutbuttoncommand, height=1, bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#E94F37')
        self.logout_button.place(x=15, y=15)

        self.main_menu_button = Button(window, text='MAIN MENU', command=mainmenucommand, height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.main_menu_button.place(x=110, y=15)

        self.generate_button = Button(window, text='Generate', command=lambda: generatepw(self), height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.generate_button.place(x=350, y=350)

        self.copy_button = Button(window, text='Copy to clipboard', command=lambda: copyclipboard(self), height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
        self.copy_button.place(x=325, y=300)

        #toggle buttons
        toggle_button_small = Button(width=3, command=SimpletoggleSmall, font=('yu gothic ui', 10, 'bold'), bg='#E94F37', activebackground='#F6F7EB')
        toggle_button_small.place(x=120, y=230)

        toggle_button_caps = Button(width=3, command=SimpletoggleCaps, font=('yu gothic ui', 10, 'bold'), bg='#E94F37', activebackground='#F6F7EB')
        toggle_button_caps.place(x=290, y=230)

        toggle_button_numbers = Button(width=3, command=SimpletoggleNumbers, font=('yu gothic ui', 10, 'bold'), bg='#E94F37', activebackground='#F6F7EB')
        toggle_button_numbers.place(x=450, y=230)

        toggle_button_special = Button(width=3, command=SimpletoggleSpecial, font=('yu gothic ui', 10, 'bold'), bg='#E94F37', activebackground='#F6F7EB')
        toggle_button_special.place(x=620, y=230)

        #password length slider bar
        #troughcolor='' changes the color of the inside of the bar
        #the border can be changed with bd=''
        self.sliderbar = Scale(
            window,
            from_=1,
            to=50,
            orient='horizontal',
            bg='#F6F7EB',
            highlightthickness=0,
            troughcolor='#393E41'
        )
        self.sliderbar.place(x=395, y=410, width='300')

class AddPW:
        def __init__(self, window):
        #default settings for the window
            self.window = window
            window.title("PWLibrary Password Generator")
            self.window.geometry('750x500')
            self.window.resizable(0, 0)

            #background color
            window.configure(bg='#393E41')

            #white frame
            self.menu_frame = Frame(self.window, bg='#F6F7EB', width=690, height=400)
            self.menu_frame.place(x=30, y=70)

            #text (heading)
            self.heading3 = Label(self.window, text='Add Passwords', font=('yu gothic ui', 25, 'bold'), bg='#393E41', fg='#F6F7EB')
            self.heading3.place(x=215, y=10, width='350', height='50')

            #text (entry labels)
            self.apptxt1 = Label(window, text='App/Website/Device', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
            self.apptxt1.place(x=140, y=150)

            self.usernametxt1 = Label(window, text='Username', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
            self.usernametxt1.place(x=140, y=225)

            self.passwordtxt1 = Label(window, text='Password', font=('yu gothic ui', 15, 'bold'), bg='#F6F7EB', fg='#393E41')
            self.passwordtxt1.place(x=140, y=300)

            #other
            self.FirstLine = True

            #button commands
            def logoutbuttoncommand():
                window.destroy()
                loginpage()

            def mainmenucommand():
                window.destroy()
                menupage()

            def addbuttoncommand():
                #"a" is for append, this causes the new info to be added, not overwritten
                #to overwrite, use "w"
                #"\n" starts the next on a new line

                app_info = self.app_add_entry.get()
                username_info = self.username_add_entry.get()
                password_info = self.password_add_entry.get()

                #does not add passwords to the library if a field is empty
                if app_info == "" or username_info == "" or password_info == "":
                    #messagebox.showinfo("Error", "Empty fields are not allowed")
                    #print("Please enter all info")

                    self.addpw_frame = Frame(self.window, bg='#F6F7EB', width=300, height=30)
                    self.addpw_frame.place(x=295, y=435)

                    self.addedtxt = Label(window, text='Empty fields are not allowed', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
                    self.addedtxt.place(x=310, y=438)

                else:
                    #appends the text to the .txt file
                    #FirstLine decides whether it should use a "\n" at the start or not
                    if self.FirstLine == True:
                        file = open("entry_list.txt", "a")
                        file.write("App: " + app_info + "\n")
                        file.write("Username: " + username_info + "\n")
                        file.write("Password: " + password_info + "\n")
                        file.close()

                        self.FirstLine = False

                        #messagebox.showinfo("Success", "Password Added to the Library")
                        #print("Added to library")

                        self.addpw_frame = Frame(self.window, bg='#F6F7EB', width=300, height=30)
                        self.addpw_frame.place(x=295, y=435)

                        self.addedtxt = Label(window, text='Password Added to the Library!', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
                        self.addedtxt.place(x=300, y=438)

                    #puts an empty space between different apps and login information
                    else:
                        file = open("entry_list.txt", "a")
                        file.write("\n" + "App: " + app_info + "\n")
                        file.write("Username: " + username_info + "\n")
                        file.write("Password: " + password_info + "\n")
                        file.close()

                        #messagebox.showinfo("Success", "Password Added to the Library")
                        #print("Added to library")

                        self.addpw_frame = Frame(self.window, bg='#F6F7EB', width=300, height=30)
                        self.addpw_frame.place(x=295, y=435)

                        self.addedtxt = Label(window, text='Password Added to the Library!', font=('yu gothic ui', 10, 'bold'), bg='#F6F7EB', fg='#393E41')
                        self.addedtxt.place(x=300, y=438)

            #buttons
            self.logout_button = Button(window, text='LOG OUT', command=logoutbuttoncommand, height=1, bd=6, font=('yu gothic ui', 10, 'bold'), activeforeground='#F6F7EB', activebackground='#E94F37')
            self.logout_button.place(x=15, y=15)

            self.main_menu_button = Button(window, text='MAIN MENU', command=mainmenucommand, height=1, bd=6, font=('yu gothic ui', 10, 'bold'))
            self.main_menu_button.place(x=110, y=15)

            self.add_button = Button(window, text='ADD', command=addbuttoncommand, height=2, width=10, bd=6, font=('yu gothic ui', 10, 'bold'))
            self.add_button.place(x=350, y=380)

            #app, user and password entry

            #app_entry = StringVar()
            #username_entry = StringVar()
            #password_entry = StringVar()

            self.app_add_entry = Entry(window, bd=5)
            self.app_add_entry.place(x=515, y=157)  

            self.username_add_entry = Entry(window, bd=5)
            self.username_add_entry.place(x=515, y=232)

            self.password_add_entry = Entry(window, bd=5)
            self.password_add_entry.place(x=515, y=307)

#commands for new windows
def menupage():
    window = Tk()
    MainMenu(window)
    window.mainloop()

def loginpage():
    window = Tk()
    LoginForm(window)
    window.mainloop()

def pwgenpage():
    window = Tk()
    PWGen(window)
    window.mainloop()

def addpwpage():
    window = Tk()
    AddPW(window)
    window.mainloop()

#starts out with the login page
if __name__ == '__main__':
    loginpage()

    #yaml json sqlite
    #encryptie
    # try catch achtige check
