# Author: Moller.R 
# Email: greenorange103@gmail.com
# main.py - interface for the views acts as a controller

# Import imports file
from blue_sentinel.scripts.global_imports import *
from blue_sentinel.scripts.os_funcs import get_dir

# Importing views (screens/pages)
from blue_sentinel.views.home import Home
from blue_sentinel.views.file_scan import FileScan
from blue_sentinel.views.net_scan import NetScan
from blue_sentinel.views.file_analysis import FileAnalysis

# Importing widgets
from blue_sentinel.widgets.navbar import Navbar
from blue_sentinel.widgets.sidebar import Sidebar
from blue_sentinel.widgets.taskbar import Taskbar
from blue_sentinel.widgets.status_tab import StatusTab


class BlueSentinel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, GGC.APP_TITLE)

        self.project_dir = get_dir()
        self.data_dir = self.project_dir + "/data"


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.create_widgets()

        self.frames = {}
        for F in (Home, FileScan, NetScan, FileAnalysis):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Log out")
        filemenu.add_separator()
        filemenu.add_command(label="Menu")
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self, menu=menubar)

        

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_widgets(self):
    	self.navbar = Navbar(parent=self, controller = self)
    	self.navbar.place(relx=0.001, rely=0.0, relheight=0.095, relwidth=0.999)

    	self.sidebar = Sidebar(parent=self, controller = self)
    	self.sidebar.place(relx=0.001, rely=0.093, relheight=0.871, relwidth=0.244)

    	self.status_tab = StatusTab(parent = self.sidebar, controller = self)
    	self.status_tab.place(relx=0.077, rely=0.041, relheight=0.328, relwidth=0.846)

    	self.taskbar = Taskbar(parent=self, controller = self)
    	self.taskbar.place(relx=0.001, rely=0.957, relheight=0.043, relwidth=0.999)

if __name__ == "__main__":
    app = BlueSentinel()
    width_of_window = 800
    height_of_window = 600
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_coordinate = (screen_width//2) - (width_of_window//2)
    y_coordinate = (screen_height//2) - (height_of_window//2)
    app.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    app.resizable(False, False)
    app.iconbitmap('data/blue_sentinel_img_icon.ico')
    app.mainloop()