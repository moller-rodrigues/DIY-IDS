# Author: Moller.R 
# Email: greenorange103@gmail.com
# home.py - home page/screen for app

# Import imports file
from blue_sentinel.scripts.global_imports import *

# DEFAULT TEXT FOR HOME SCREEN
SCAN_COMPUTER_BUTTON_TEXT = "scan computer"
FILE_ANALYSIS_BUTTON_TEXT = "file analysis"
SCAN_NETWORK_BUTTON_TEXT = "scan network"
HOST_FRAME_LABEL_TEXT = "Host"
NETWROK_FRAME_LABEL_TEXT = "Network"

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=GGC.APP_BG)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):

        # Host features
        self.host_frame = tk.Frame(self, relief='groove', borderwidth=GGC.DEFAULT_BORDERWIDTH, background=GGC.APP_BG)
        self.host_frame.place(relx=0.275, rely=0.171, relheight=0.336, relwidth=0.694)

        self.file_scan_img = tk.PhotoImage(file=self.controller.data_dir+"/file_scan_img.png")
        self.scan_computer_icon = tk.Label(self.host_frame, background=GGC.APP_BG, image = self.file_scan_img)
        self.scan_computer_icon.place(relx=0.018, rely=0.106, height=40, width=40)
        self.scan_computer_button = tk.Button(self.host_frame, background=GGC.APP_BG, borderwidth="0", text=SCAN_COMPUTER_BUTTON_TEXT, command=lambda:self.controller.show_frame("FileScan"))
        self.scan_computer_button.place(relx=0.099, rely=0.16, height=20, width=86)

        self.file_analysis_img = tk.PhotoImage(file=self.controller.data_dir+"/file_analysis_img.png")
        self.file_analysis_icon = tk.Label(self.host_frame, background=GGC.APP_BG, image = self.file_analysis_img)
        self.file_analysis_icon.place(relx=0.018, rely=0.4, height=40, width=40)
        self.file_analysis_button = tk.Button(self.host_frame, background=GGC.APP_BG, borderwidth="0", text=FILE_ANALYSIS_BUTTON_TEXT, command=lambda:self.controller.show_frame("FileAnalysis"), anchor="w")
        self.file_analysis_button.place(relx=0.099, rely=0.45, height=20, width=86)

        # Network features
        self.network_frame = tk.Frame(self, relief='groove', borderwidth=GGC.DEFAULT_BORDERWIDTH, background=GGC.APP_BG)
        self.network_frame.place(relx=0.275, rely=0.586, relheight=0.336, relwidth=0.695)

        self.netscan_img = tk.PhotoImage(file=self.controller.data_dir+"/netscan_img.png")
        self.scan_network_icon = tk.Label(self.network_frame, background=GGC.APP_BG, image = self.netscan_img )
        self.scan_network_icon.place(relx=0.018, rely=0.106, height=40, width=40)

        self.scan_network_button = tk.Button(self.network_frame, background=GGC.APP_BG, borderwidth="0", text=SCAN_NETWORK_BUTTON_TEXT, command=lambda:self.controller.show_frame("NetScan"))
        self.scan_network_button.place(relx=0.097, rely=0.154, height=24, width=77)

        # Labels for host frame and network frame
        self.host_frame_label = tk.Label(self, background=GGC.APP_BG, font="-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0", text=HOST_FRAME_LABEL_TEXT)
        self.host_frame_label.place(relx=0.293, rely=0.155, height=20, width=40)

        self.netwrok_frame_label = tk.Label(self, background=GGC.APP_BG, font="-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0", text=NETWROK_FRAME_LABEL_TEXT)
        self.netwrok_frame_label.place(relx=0.291, rely=0.57, height=20, width=57)