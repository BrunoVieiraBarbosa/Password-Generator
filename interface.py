import tkinter, passwd, _thread

class Interface():
    def __init__(self, name, size):
        self.Generator = passwd.Password()
        self.size = size
        self.root = tkinter.Tk()
        self.root.title(name)
        self.winfo_screen = [self.root.winfo_screenwidth()//2, self.root.winfo_screenheight()//2]
        self.root.geometry(f'{size[0]}x{size[1]}+{self.winfo_screen[0]-size[0]//2}+{self.winfo_screen[1]-size[1]//2}')
        self.root.minsize(size[0], size[1])
        self.root.maxsize(size[0], size[1])
        self.layout()


    def generate(self, values):
        _thread.start_new_thread(self.Generator.generate, (values, self.listbox))


    def layout(self):
        #Espace
        tkinter.Frame(self.root, height=10).pack()

        #Frame options
        self.frame_options = tkinter.Frame(self.root, width=self.size[0]-100, height=100, relief=tkinter.SUNKEN, bd=1)
        self.frame_options.pack()

        #Itens Frame Options
        self.var_checkbox = [tkinter.IntVar() for _ in range(0, 4)]
        text = ('Capital letters', 'Small letters', 'Numbers', 'Symbols')
        self.checkbox = [tkinter.Checkbutton(self.frame_options, text=x, variable=self.var_checkbox[text.index(x)]) for x in text]
        [x.select() for x in self.checkbox]
        self.checkbox[0].place(x=5, y=10)
        self.checkbox[1].place(x=150, y=10)
        self.checkbox[2].place(x=5, y=40)
        self.checkbox[3].place(x=150, y=40)

        tkinter.Label(self.frame_options, text='Digits:').place(x=10, y=70)
        self.entry_digits = tkinter.Entry(self.frame_options, width=5)
        self.entry_digits.place(x=65, y=70)

        self.button_generate = tkinter.Button(self.frame_options, text="Generate", command=lambda *args: self.generate((self.var_checkbox, self.entry_digits)))
        self.button_clean = tkinter.Button(self.frame_options, text="Clean", command=lambda *args: self.listbox.delete(0, tkinter.END))
        self.button_generate.place(x=140, y=65)
        self.button_clean.place(x=230, y=65)

        #Bind
        self.entry_digits.bind("<Return>", lambda *args: self.generate((self.var_checkbox, self.entry_digits)))

        self.button_generate.bind("<Return>", lambda *args: self.generate((self.var_checkbox, self.entry_digits)))
        self.button_generate.bind("<Enter>", lambda *args: self.button_generate.focus_force())
        self.button_generate.bind_all("<Alt-KeyPress-g>", lambda *args: self.generate((self.var_checkbox, self.entry_digits)))

        self.button_clean.bind("<Return>", lambda *args: self.listbox.delete(0, tkinter.END))
        self.button_clean.bind_all("<Alt-KeyPress-c>", lambda *args: self.listbox.delete(0, tkinter.END))

        #Espace
        tkinter.Frame(self.root, height=10).pack()

        #Frame ListBox
        self.frame_listbox = tkinter.Frame(self.root, relief=tkinter.SUNKEN, bd=1)
        self.frame_listbox.pack()
        scrollbar = [tkinter.Scrollbar(self.frame_listbox, orient=x) for x in ('vertical', 'horizontal')]
        self.listbox = tkinter.Listbox(self.frame_listbox, width=37, height=20, selectmode=tkinter.EXTENDED, yscrollcommand=scrollbar[0].set, xscrollcommand=scrollbar[1].set)
        scrollbar[0].config(command=self.listbox.yview)
        scrollbar[1].config(command=self.listbox.xview)
        scrollbar[0].pack(side="right", fill="y")
        scrollbar[1].pack(side="bottom", fill="x")
        self.listbox.pack()


    def run(self):
        self.root.mainloop()