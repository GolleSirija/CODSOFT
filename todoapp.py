#CREATING A "TO-DO LIST APPLICATION" USING PYTHON BY "GUI"
#Generally we require modules to create any gui application,so,python provides "tkinter" module to create those gui models
#step1:import module
#step2:create a main window(parent window)
#step3:create a frame
#we require some of the components like listbox,entry box,scroll bars,buttons to run our app,so,we add those components to the frame
#step4:add components to the frame
#step5:create funtions to "ADD" & "DELETE" the tasks


#importing the modules
from tkinter import *
from tkinter import messagebox

#defining newTask and deleteTask functions
def newTask():
    task = e.get()
    if task != "":
        lb.insert(END, task)
        e.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteTask():
    lb.delete(ANCHOR)

#creating & configuring the window
mw = Tk()
mw.geometry('500x450+500+200')
mw.title('TO-DO LIST')
mw.config(bg='black')
mw.resizable(width=False, height=False)

#creating frame
fr = Frame(mw)
fr.pack(pady=10)

#adding components to the frame
#1.Listbox
lb = Listbox(fr,width=25,height=8,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='grey',
    activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

#add some duplicate(dummy) data
dummy_list = [
    'wake up at 5:00 am',
    'drink water',
    'do exercise',
    'fresh up',
    'have breakfast',
    'prepare projects',
    'have lunch',
    'do chores',
    'take nap',
    'learn courses'
    ]
for item in dummy_list:
    lb.insert(END, item)

#2.scrollbars
sb = Scrollbar(fr)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#3.Entry box
e = Entry(mw,font=('times', 24))
e.pack(pady=20)

#creating button frames
b_f = Frame(mw)
b_f.pack(pady=20)

#4.adding buttons to the b_f
addTask_btn = Button(b_f,text='Add Task',font=('times 14'),bg='#c5f776',padx=20,pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(b_f,text='Delete Task',font=('times 14'),bg='#ff8b61',padx=20,pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

mw.mainloop()