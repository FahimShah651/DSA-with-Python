import os
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime


class window_screen(Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{1100}x{700}")
        self.resizable(0, 0)
        self.title("Namal Library")
        self.config(bg="grey")

        self.img =  Image.open("OIP.jpg")
        self.img = self.img.resize((100,80))
        self.img = ImageTk.PhotoImage(self.img)
        self.wm_iconbitmap("2.ico")
        
        # welcome frame
        self.frame1 = Frame(self, bg="red",width=screen_width,height=150,relief="groove",borderwidth=9)
        self.frame1.pack_propagate(False)  # Disable automatic size adjustment
        self.frame1.grid(row=0, column=0,padx=220)
        
        Label(self.frame1,text='WELCOME  TO  NAMAL  LIBRARY' ,font="Algerian 20 italic",padx=10,pady=10).grid(row=0,column=1,pady=10,padx=12)
        Label(self.frame1, image=self.img).grid(row=0,column=0,pady=10,padx=10)
        
        # operation frame :
        self.frame2 = Frame(self, bg="yellow",width=700,relief="groove",borderwidth=9)
        self.frame2.pack_propagate(False)  # Disable automatic size adjustment
        self.frame2.grid(row=1, column=0,sticky="w")
       
        Label(self.frame2,text='O',font="Algerian 20 italic",padx=10).grid(sticky="w",row=0,column=2,pady=10,padx=12)
        Button(self.frame2, text="ADD BOOK",height=2, command=self.add_book).grid(sticky="w",row=1,column=0,pady=10,padx=5)
        Label(self.frame2, text="Book Name" ,font="calibri 12 italic",padx=10).grid(sticky="w",row=1,column=1,padx=5)
        Label(self.frame2, text="Author" ,font="calibri 12 italic",padx=10).grid(sticky="w",row=1,column=2,padx=5)
        Label(self.frame2, text="Subject" ,font="calibri 12 italic",padx=10).grid(sticky="w",row=1,column=3,padx=5)

        Button(self.frame2, text="SEARCH BOOK", command=self.add_book).grid(sticky="w",row=2,column=0,pady=10,padx=5)
        Button(self.frame2, text="REMOVE BOOK", command=self.add_book).grid(sticky="w",row=3,column=0,pady=10,padx=5)
        Button(self.frame2, text="MODIFY BOOK", command=self.add_book).grid(sticky="w",row=4,column=0,pady=10,padx=5)
        Button(self.frame2, text="ADD BOOK", command=self.add_book).grid(sticky="w",row=5,column=0,pady=10,padx=5)
        Button(self.frame2, text="SORT BOOK", command=self.add_book).grid(sticky="w",row=6,column=0,pady=10,padx=5)

    
    def add_book(self):
        pass
        
        
wn_sc = window_screen()
wn_sc.mainloop()


