import tkinter as tk

# Importing config modules
from blue_sentinel.configs import global_gui_config as GGC

class StatusTab(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, relief='groove', borderwidth=GGC.DEFAULT_BORDERWIDTH, background=GGC.DEFAULT_WIN_BG)
        self.controller = controller

        self.file_scan_status = "INACTIVE"
        self.netscan_status = "INACTIVE"
        self.notifications_status = "DISABLED"

        self.status_frame_label = tk.Label(self, background="#c0c0c0", borderwidth="0", relief="groove", text='''status''')
        self.status_frame_label.place(relx=0.0, rely=0.0, height=20, width=164)

        self.file_scan_status_light = tk.Label(self, background=GGC.INACTIVE_BG)
        self.file_scan_status_light.place(relx=0.061, rely=0.25, height=20, width=20)

        self.file_scan_status_label = tk.Label(self, background=GGC.DEFAULT_WIN_BG, font=GGC.STATUS_FONT, text='''file scan: ''' + self.file_scan_status)
        self.file_scan_status_label.place(relx=0.194, rely=0.25, height=21, width=104)

        self.netscan_status_light = tk.Label(self, background=GGC.INACTIVE_BG)
        self.netscan_status_light.place(relx=0.061, rely=0.438, height=20, width=20)

        self.netscan_status_label = tk.Label(self, background=GGC.DEFAULT_WIN_BG, font=GGC.STATUS_FONT, text='''network scan: ''' + self.netscan_status)
        self.netscan_status_label.place(relx=0.194, rely=0.438, height=21, width=124)

        self.notifications_status_light = tk.Label(self, background=GGC.INACTIVE_BG)
        self.notifications_status_light.place(relx=0.061, rely=0.626, height=20, width=20)

        self.notifications_status_label = tk.Label(self, background=GGC.DEFAULT_WIN_BG, font=GGC.STATUS_FONT, text='''notifications: ''' + self.notifications_status)
        self.notifications_status_label.place(relx=0.194, rely=0.626, height=21, width=124)


    def toggle_status(self, status_type):
        if status_type == "file":
            if self.file_scan_status == "INACTIVE":
                self.file_scan_status = "ACTIVE"
                self.file_scan_status_label.configure(text='''file scan: ''' + self.file_scan_status)
                self.file_scan_status_light.configure(background=GGC.ACTIVE_BG)
            else:
                self.file_scan_status = "INACTIVE"
                self.file_scan_status_label.configure(text='''file scan: ''' + self.file_scan_status)
                self.file_scan_status_light.configure(background=GGC.INACTIVE_BG)
        if status_type == "network":
            if self.netscan_status == "INACTIVE":
                self.netscan_status = "ACTIVE"
                self.netscan_status_label.configure(text='''network scan: ''' + self.netscan_status)
                self.netscan_status_light.configure(background=GGC.ACTIVE_BG)
            else:
                self.netscan_status = "INACTIVE"
                self.netscan_status_label.configure(text='''network scan: ''' + self.netscan_status)
                self.netscan_status_light.configure(background=GGC.INACTIVE_BG)
        if status_type == "notifications":
            if self.notifications_status == "ENABLED":
                self.notifications_status = "DISABLED"
                self.notifications_status_label.configure(text='''notifications: ''' + self.notifications_status)
                self.notifications_status_light.configure(background=GGC.INACTIVE_BG)
            else:
                self.notifications_status = "ENABLED"
                self.notifications_status_label.configure(text='''notifications: ''' + self.notifications_status)
                self.notifications_status_light.configure(background=GGC.ACTIVE_BG)
        return 