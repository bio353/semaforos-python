import tkinter as tk
from src.model import Model
from src.view import View
from src.controller import Controller
from src.utils import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Timer Simulator')
        model = Model()
        view = View(self)
        controller = Controller(model, view)
        self.geometry('400x400')
        view.set_controller(controller)
        view.mainloop()


if __name__ == '__main__':
    cli_clear()
    app = App()
