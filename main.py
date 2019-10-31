from tkinter import *
from tkinter import colorchooser

class Paint(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
            self.root = Tk()
            self.root.geometry("850x500")
            self.root.title('Paint')
            self.c = Canvas(self.root, bg='white', width=1920, height=1080)
            self.c.grid(row=1, columnspan=5)
            self.old_x = None
            self.old_y = None
            self.line_width = self.DEFAULT_PEN_SIZE
            self.eraser_on = False
            self.linenow = False
            self.color = self.DEFAULT_COLOR
            self.c.bind("<B1-Motion>", self.draw)
            self.c.bind("<Button-1>", self.draw_figure)
            self.createmenu()
            self.createbuttons()
            self.root.mainloop()

    def createmenu(self):
        self.mainmenu = Menu(self.root, bg="snow")
        self.root.config(menu=self.mainmenu)

    def createbuttons(self):
        self.choose_size_button = Scale(self.root, from_= 5, to=150, orient=HORIZONTAL, bg="snow",
                                        activebackground="MediumPurple1", font=("Helvetica", 10))
        self.choose_size_button.place(x=0, y=0, width=120,  height=40)
        self.color_button = Button(self.root, text='color', font=("Helvetica", 10),  bg="snow",
                                   activebackground="MediumPurple1", command=self.choose_color)
        self.color_button.place(x=0, y=40, width=60,  height=25)
        self.eraser_button = Button(self.root, text='eraser', font=("Helvetica", 10), bg="snow",
                                    activebackground="MediumPurple1", command=self.use_eraser)
        self.eraser_button.place(x=60, y=40, width=60,  height=25)
        self.delete_button = Button(self.root, text='delete', font=("Helvetica", 10), bg="snow",
                                    activebackground="MediumPurple1", command=lambda: self.c.delete("all"))
        self.delete_button.place(x=0, y=65, width=60,  height=25)
        self.pen_button = Button(self.root, text='pen', font=("Helvetica", 10),
                                 activebackground="MediumPurple1", bg="snow")
        self.pen_button.place(x=60, y=65, width=60,  height=25)

    def draw(self, event):
        self.line_width = self.choose_size_button.get()
        self.color = 'white' if self.eraser_on else self.color
        self.c.create_oval(event.x - 1, event.y - 1, event.x + 1, event.y + 1, fill=self.color, outline=self.color,
                           width=self.line_width)

    def choose_color(self):
        self.eraser_on = False
        self.color = colorchooser.askcolor(color=self.color)[1]

    def line(self):
        self.linenow = True

    def draw_figure(self, event):
        self.line_width = self.choose_size_button.get()
        if self.linenow:
            self.c.create_line(0, 0, event.x, event.y, fill=self.color)

    def use_eraser(self):
        self.eraser_on = True

if __name__ == '__main__':
    Paint()
