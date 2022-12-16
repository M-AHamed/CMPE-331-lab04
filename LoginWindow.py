"""
    Stage: Development-01
    @author: Mohammad Hamed
    @author: Huseyin can Ulkebay
    github: https://github.com/M-AHamed/CMPE-331-lab04
    Stage: Development-02
    @author: Abdel Rahman Abdin, 120200128
    @author: Çağatay Yaman 120200029

"""

import tkinter as tk

class newWindow:
    def __init__(self):
        self.userInfo = []
        self.window = tk.Tk()
        self._initializeGUI()
        self._addGUIElementsToFrame()

    def _initializeGUI(self):
        self.welcome = tk.Label(text="WELCOME")
        self.adress = tk.Label(text="adress")
        self.phone = tk.Label(text="phone number")
        self.email = tk.Label(text="e-mail")
        self.creditCard= tk.Label(text="credit card")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()
        self.txt03 = tk.Entry()
        self.txt04 = tk.Entry()
        

        self.btn01 = tk.Button(text="enter")
        self.btn02 = tk.Button(text="clear")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)



    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.adress.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.phone.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.email.grid(row=2, column=0, padx=10, pady=5)
        self.txt03.grid(row=2, column=1, padx=10, pady=5)

        self.creditCard.grid(row=3, column=0, padx=10, pady=5)
        self.txt04.grid(row=3, column=1, padx=10, pady=5)
        
        self.btn01.grid(row=4, column=0, padx=10, pady=5)
        self.btn02.grid(row=4, column=1, padx=10, pady=5)

    def handle_click(self, event):
        if(event.widget == self.btn02):
            print("Text fields cleared")
            self.clearTextFields()

        if(event.widget == self.btn01):
            print("Data saved")
            self.saveUserData()
            print(self.userInfo)
        pass


    def saveUserData(self):
        self.userInfo = []
        self.userInfo.append(self.txt01.get())
        self.userInfo.append(self.txt02.get())
        self.userInfo.append(self.txt03.get())
        self.userInfo.append(self.txt04.get())

    def clearTextFields(self):
        self.txt01.delete(0, 'end')
        self.txt02.delete(0, 'end')
        self.txt03.delete(0, 'end')
        self.txt04.delete(0, 'end')
        
        
class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.savedUsername="admin"
        self.savedPassword="admin"
        # start the GUI frame
        self.window.mainloop()
    


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.username = tk.Label(text="Username")
        self.password = tk.Label(text="Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="login")
        self.btn02 = tk.Button(text="Exit")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.username.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.password.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        if(self.btn02 == event.widget):
            self.window.destroy()
            print("bye")
            

        if(self.btn01 == event.widget):
            if(self.verifyUser() == True):
                print("welocme")
                self.createNewPage()
        pass

    def verifyUser(self):
        #login_password = username
        #login_password = password
        savedUsername="admin"
        savedPassword="admin"
        if((self.txt01.get() == self.savedPassword) and (self.txt02.get() == self.savedUsername)):
            return True
        else:
            return False

    def createNewPage(self):
        self.window.destroy()
        newWindow()
        



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
