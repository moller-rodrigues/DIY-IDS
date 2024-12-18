import tkinter as tk

# Importing config modules
from blue_sentinel.configs import global_gui_config as GGC

class Navbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth=GGC.DEFAULT_BORDERWIDTH, relief="groove", background=GGC.APP_BG)
        self.controller = controller


        self.home_img = tk.PhotoImage(file=self.controller.data_dir+"/home_img.png")
        self.home_button_nav_button = tk.Button(self, background=GGC.DEFAULT_WIN_BG, text = "Home", command=lambda:self.controller.show_frame("Home"))
        self.home_button_nav_button.place(relx=0.0, rely=0.0, height=54, width=97)

        self.about_img = tk.PhotoImage(file=self.controller.data_dir+"/about_img.png")
        self.about_button = tk.Button(self, background=GGC.DEFAULT_WIN_BG, text = "About")
        self.about_button.place(relx=0.121, rely=0.0, height=54, width=97)

        self.help_img = tk.PhotoImage(file=self.controller.data_dir+"/help_img.png")
        self.help_button = tk.Button(self,background=GGC.DEFAULT_WIN_BG,text="Help")
        self.help_button.place(relx=0.242, rely=0.0, height=54, width=97)
