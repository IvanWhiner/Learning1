from tkinter import *
from tkinter import  ttk

class FeetToMeters:

    def __init__(self, root):

        root.title('Футы в метры')

        s1 = ttk.Style()
        s1.configure('Danger.TFrame',  background='red', relief='sunken')

        # mainframe = ttk.Frame(root, padding= (5, 10), style='Danger.TFrame')
        mainframe = ttk.Frame(root, padding=(5, 10))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe['relief'] = 'groove'

        frame2 = ttk.Frame(root, padding=(5, 10))
        frame2.grid(column=1, row=0, sticky=(S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #Здесь буду пытаться все ломать

        ttk.Label(frame2, text='Halk lomat'
                               '\ni krushit').grid(column=1, row=0, sticky = W)


        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text='Вычислить', command=self.calculate).grid(column=3, row=3, sticky=(W))

        ttk.Label(mainframe, text='Фут').grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text='равны').grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text='метров').grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass

def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)


root = Tk()
# text = ttk.Label(root, text="Hello World!")
# text.grid()
# l =ttk.Label(root, text="Starting...")
# l.grid()
# l.bind('<1>', lambda e: l.configure(text='B1 нажато'))
# l.bind_all('<Shift_L><A>', lambda e: l.configure(text='Левый шифт нажат'))

FeetToMeters(root)
# print_hierarchy(root)
root.mainloop()

