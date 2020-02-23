import os, pickle
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def read_index():
    root_path = en.get()
    #get file index from path
    file_index = [(path, files) for path, _, files in os.walk(root_path)]

    #save files index to file_index.pkl
    with open("file_index.pkl", 'wb') as f:
        pickle.dump(file_index, f)

def search():
    #get info
    key = en2.get() 
    search_type = search_type_cb.get()
    f_ex = check1.get()

    #load file_index.pkl
    with open("file_index.pkl", 'rb') as f:
        file_index = pickle.load(f)
    
    ##clear listbox
    lb.delete(0,'end')

    #search
    for path, files in file_index:
        for f in files:
            #remove file extension from name
            if f_ex == False:
                f2 = os.path.splitext(f)[0]
            else:
                f2 = f
            #search by search_type
            if key == f2: #it the same
                    lb.insert(END, path+"/"+f)
            elif (search_type == "contain" or search_type == None): #contain keyword  
                if (key in f2) == True:
                    lb.insert(END, path+"/"+f)
            elif (search_type == "startwith"): #start with keyword
                if f2.find(key) == 0: 
                    lb.insert(END, path+"/"+f)
            elif (search_type == "endwith"): #end with keyword
                f_len = len(f2)
                key_len = len(key)
                key_start_index = f2.find(key, f_len-key_len-1, f_len)
                if (key_start_index != -1): 
                    lb.insert(END, path+"/"+f)
    
#read_index("C:/CODE/file_search_engine")
#search("ol", "endwith", False)
def sel_direc():
    direc = filedialog.askdirectory()
    en.delete(0, END)
    en.insert(0, direc)

win = Tk()
win.title("FSG")

#entry+button 1 
en = Entry(win, width=60)
en.grid(row=0, column=0)
Button(win, text="Select Folder", command=sel_direc).grid(row=0, column=1)
Button(win, text="Indexing", command=read_index).grid(row=0, column=2)

#entry+button 2
en2 = Entry(win, width=60)
en2.grid(row=1, column=0)
Button(win, text="Search", command=search).grid(row=1, column=4)
search_type_cb = StringVar()
combobox = ttk.Combobox(win, width = 15 , textvariable = search_type_cb)
combobox['values'] = ("contain","startwith","endwith")
combobox.grid(column = 0, row = 2)

check1 = BooleanVar()
c1 = Checkbutton(win, text="file_ex", variable = check1, onvalue = True, offvalue = False)
c1.grid(row=2, column=1)

lb = Listbox(win, width=82)
lb.grid(row=3, column=0, columnspan=3)
win.mainloop()



