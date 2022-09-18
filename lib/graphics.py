'''
    Author: Luke Broadfoot (lucasxavier@email.arizona.edu)
    File: graphics.py
    Purpose: a wrapper around tkinter    
'''
import time
import tkinter as tk

class Gui:
    '''
        a wrapper class around tkinter to make it easier to work with
    '''
    def __init__(self, fullscreen: bool | tuple[int, int] = (700, 500), ontop=True, bg='#555555'):
        x_offset, y_offset = 0, 0
        self._root = tk.Tk()
        self._background = ()
        if fullscreen == True:
            w = self._width = self._root.winfo_screenwidth()
            h = self._height = self._root.winfo_screenheight()
            self._root.attributes('-fullscreen', fullscreen)
        else:
            w = self._width = fullscreen[0]
            h = self._height = fullscreen[1]
            x_offset, y_offset = self._root.winfo_screenwidth() - 50 - w, 50
        self._root.attributes("-topmost", 1 if ontop else 0)
        self._root.geometry(f"{w}x{h}+{x_offset}+{y_offset}")
        self._canvas = tk.Canvas(self._root, width=w, height=h, highlightthickness=0)
        self.set_background(bg)
        self._canvas.focus_set()
        self._canvas.pack()
        self._setup_exit_handler()

    def rgb(self, r: int, g: int, b: int) -> str:
        '''
            converts 3 integers into their hex values.
            assumes that r, g, and b are all within [0,255] inclusive
        '''
        return f'#{r:02x}{g:02x}{b:02x}'

    def get_width(self) -> int: return self._width
    def get_height(self) -> int: return self._height

    def _setup_exit_handler(self):
        '''
            binds keyboard input to an exit event handler
        '''
        for key in ['<Escape>', '<q>', '<Q>']:
            self._canvas.bind(key, lambda _: exit(0))
        self._canvas.focus_force()
        self._root.update()

    def line(self, top_left: tuple[int, int], bottom_right: tuple[int, int], fill='black', width=3):
        '''
            creates a line from top_left to bottom_right
        '''
        return self._canvas.create_line(top_left[0], top_left[1], bottom_right[0], bottom_right[1], fill=fill, width=width)

    def text(self, pos: tuple[int, int], text: str, fill='black', size=17):
        '''
            draws text at pos
        '''
        return self._canvas.create_text(pos[0], pos[1], text=text, fill=fill, font=('Arial', size), anchor='nw')

    def ellipse(self, pos: tuple[int, int], width: int, height: int, fill='black'):
        '''
            draws an ellipse around pos of width and height
        '''
        x1, x2, y1, y2 = pos[0]-(width/2), pos[0]+(width/2), pos[1]-(height/2), pos[1]+(height/2)
        return self._canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=fill)
    
    def rectangle(self, pos: tuple[int, int], width: int, height: int, fill='black', outline=''):
        '''
            draws a rectangle with pos being the top left mosts point
        '''
        return self._canvas.create_rectangle(pos[0], pos[1], pos[0]+width, pos[1]+height, fill=fill, outline=outline)

    def set_background(self, color: str) -> None:
        '''
            binds a color as the background color
        '''
        if self._background != ():
            self._background = (self._background[0], color)
            self._canvas.itemconfig(self._background[0], fill=color)
        else:
            self._background = (self._canvas.create_rectangle(-1, -1, self._width+1, self._height+1, fill=color), color)
    
    def set_text(self, ref: int, text: str) -> None:
        '''
            takes a tk._CanvasItemId and updates the text that is displayed in it
        '''
        self._canvas.itemconfigure(ref, text=text)

    def move(self, ref: int, x0: int, y0: int, x1: int, y1: int) -> None:
        '''
            translates a tk._CanvasItemId item to the next coordinates
        '''
        self._canvas.coords(ref, x0, y0, x1, y1)

    def bind(self, input_: str, callable_) -> None:
        '''
            adds an event binding
        '''
        self._canvas.bind(input_, callable_)
        self._canvas.focus_force()
        self._root.update()

    def mainloop(self) -> None:
        '''
            enters the program into a gui mainloop
        '''
        self._root.mainloop()

    def update(self, frame_rate: float = 60.0) -> None:
        '''
            WIP: could be implemented for better frame timings
            not the most consistent frame timings but gets the job done
        '''
        self._root.update_idletasks()
        self._root.update()
        time.sleep(1.0 / float(frame_rate))

    def clear(self) -> None:
        '''
            deletes all canvas items that aren't being references elsewhere
        '''
        self._canvas.delete('all')
        color = self._background[1]
        self._background = ()
        self.set_background(color)
