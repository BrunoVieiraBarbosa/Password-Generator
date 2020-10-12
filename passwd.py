from tkinter import END
import random

class Password():
    def __init__(self):
        self.values = ['abcdefgijklmnopqrstuvwxyzç'.upper(),
                        'abcdefgijklmnopqrstuvwxyzç',
                        '0123456789',
                        '!@#$%&*()-+*_={}[]~^\/,.;:']
    

    def generate(self, itens, listbox):
        def make_body():
            body = [random.choice(checkbox) for x in range(0, entry)]
            for x in checkbox:
                if x not in body:
                    return make_body()
            body = ''.join([random.choice(self.values[x]) for x in body])
            return body

        checkbox, entry = itens
        entry = entry.get()
        if entry.strip() == "":
            entry = 8
        else:
            try:
                entry = int(entry)
                if entry <= 0:
                    return
            except Exception:
                return
        checkbox = [x.get() for x in checkbox]
        if 1 in checkbox:
            checkbox = [x for x in range(0, len(checkbox)) if checkbox[x] == 1]
            listbox.insert(END, make_body())