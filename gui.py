# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import *
from tkinter.ttk import *
from VisualizeResults import *

# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfilenames 

root = Tk() 
root.geometry('200x100') 

# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(): 
     file = askopenfilenames(filetypes =[('zip files','*.gz')])
     four = root.tk.splitlist(file)
     if(len(four)==4):
                op_img(four)
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10)

mainloop() 
