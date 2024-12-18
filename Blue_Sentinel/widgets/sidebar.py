import tkinter as tk

# Importing config modules
from blue_sentinel.configs import global_gui_config as GGC

class Sidebar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, relief='groove', borderwidth=GGC.DEFAULT_BORDERWIDTH, background= GGC.SIDEBAR_BG)
        self.controller = controller
        