import tkinter as tk

window = tk.Tk()
menufrm = tk.Frame()
menufrm.grid(row = 0)
logobtn = tk.Button(master=menufrm, text = "click to add logo")
logobtn.pack(side = tk.LEFT)

class section(tk.Frame):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        header = tk.Label(text= label, master=self)
        self.grid(row=1)
        header.pack()
        
sections: list[section] = []
visible = 0
def addSection():
    global visible
    frame = section(f"section {len(sections)+1}")
    
    sections.append(frame)
    visible += 1
addSectionBtn = tk.Button(text="add section", command=addSection)
def nextPage():
    global visible
    visible += 1
    if visible > len(sections):
        visible -= 1
        return
    section[visible-1]
    sections[visible].tkraise()
def prevPage():
    global visible
    visible -= 1
    if visible < len(sections):
        visible += 1
        return
    sections[visible].tkraise()
tk.Button(text=">", command=nextPage).grid(row=2, column=2)
tk.Button(text="<", command=prevPage).grid(row=2, column=0)
addSectionBtn.grid(row = 2, column=1)
class menuButton(tk.Button):
    def __init__(self, **kwargs):
        super().__init__(command = self.gotoFrame, **kwargs)
        self.linkedFrame: tk.Frame = None
    def gotoFrame(self):
        print("Called!")
        if self.linkedFrame == None:
            return
        self.linkedFrame.tkraise()
menubuttons: set[menuButton] = set()

    

def addButton():
    x = menuButton(master=menufrm, text=input())
    menubuttons.add(x)
    x.pack(side=tk.RIGHT, anchor=tk.N, after=removebtn)
def removeButton(btn: tk.Button):
    menubuttons.remove(btn)
    btn.destroy()
    for button in menubuttons:
        button.config(command=button.gotoFrame)
def clickRemove():
    for button in menubuttons:
        button.config(command=lambda: removeButton(button))
addbtn = tk.Button(master = menufrm, text="+", command=addButton)
addbtn.pack(side=tk.RIGHT, anchor = tk.N)
removebtn = tk.Button(master = menufrm, text = "-", command=clickRemove)
removebtn.pack(side=tk.RIGHT, anchor = tk.N)


# def raise_frame(frame):
#    frame.tkraise()



# f1 = tk.Frame(master=window)
# f2 = tk.Frame(master=window)
# f3 = tk.Frame(master=window)
# f4 = tk.Frame(master=window)



# for frame in (f1, f2, f3, f4):
#     frame.grid(row=1, column=0, sticky='news')

# tk.Button(master =f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# tk.Label(master =f1, text='FRAME 1').pack()

# tk.Label(master =f2, text='FRAME 2').pack()
# tk.Button(master =f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

# tk.Label(master =f3, text='FRAME 3').pack(side='left')
# tk.Button(master =f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

# tk.Label(master =f4, text='FRAME 4').pack()
# tk.Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

# raise_frame(f1)
window.mainloop()