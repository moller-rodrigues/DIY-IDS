# Author: Moller.R 
# Email: greenorange103@gmail.com
# file_scan.py - file scan page for app, allows user to scan for malicous files

# Import imports file
from blue_sentinel.scripts.global_imports import *

# Externel imports
from tkinter import filedialog
import threading

# Local imports
from blue_sentinel.scripts.os_funcs import *
from blue_sentinel.scripts.hash_funcs import md5
from blue_sentinel.scripts.manage_dbs import *
import os

hashes = ["54b0c58c7ce9f2a8b551351102ee0938"]

# FONTS
OPTIONS_CHECKBUTTONS_FONT = "-family {Segoe UI} -size 11 -weight normal -slant roman -underline 0 -overstrike 0"
FRAME_LABEL_FONT = "-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0"
SELECT_SCAN_TYPE_FONT = "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

class FileScan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=GGC.APP_BG)
        self.controller = controller

        # ATTRIBUTES
        self.scan_type = tk.IntVar()
        self.scan_path = None
        self.folder_path = None
        self.file_path = None


        self.create_widgets()

    def create_widgets(self):
        self.file_scan_frame = tk.Frame(self, relief='groove', borderwidth="2", background=GGC.APP_BG)
        self.file_scan_frame.place(relx=0.25, rely=0.138, relheight=0.806, relwidth=0.424)

        # all widgets within file scan frame
        self.select_scan_type_label = tk.Label(self.file_scan_frame, background=GGC.APP_BG, font=SELECT_SCAN_TYPE_FONT, text='''select type''')
        self.select_scan_type_label.place(relx=0.059, rely=0.047, height=19, width=76)

        self.complete_scan_check = tk.Checkbutton(self.file_scan_frame, background=GGC.APP_BG, font=OPTIONS_CHECKBUTTONS_FONT, text='''complete scan''', variable=self.scan_type, onvalue=1)
        self.complete_scan_check.place(relx=0.118, rely=0.092, relheight=0.057, relwidth=0.357)

        self.folder_scan_check = tk.Checkbutton(self.file_scan_frame, background=GGC.APP_BG, font=OPTIONS_CHECKBUTTONS_FONT, text='''folder scan''', variable=self.scan_type, onvalue=2)
        self.folder_scan_check.place(relx=0.083, rely=0.161, relheight=0.057, relwidth=0.36)

        self.folder_path_label = tk.Label(self.file_scan_frame, background=GGC.APP_BG, text='''path: not set''', anchor="w")
        self.folder_path_label.place(relx=0.177, rely=0.221, height=19, width=240)

        self.browse_folder_path_button = ttk.Button(self.file_scan_frame, text='''browse''', command=lambda:self.browse("dir"))
        self.browse_folder_path_button.place(relx=0.195, rely=0.275, height=25, width=56)

        self.file_scan_check = tk.Checkbutton(self.file_scan_frame, background=GGC.APP_BG, font=OPTIONS_CHECKBUTTONS_FONT, text='''file scan''', variable=self.scan_type, onvalue=3)
        self.file_scan_check.place(relx=0.059, rely=0.345, relheight=0.057, relwidth=0.357)

        self.file_path_label = tk.Label(self.file_scan_frame, background=GGC.APP_BG, text='''path: not set''', anchor="w")
        self.file_path_label.place(relx=0.177, rely=0.4, height=20, width=240)

        self.browse_file_path_button = ttk.Button(self.file_scan_frame, text='''browse''', command=lambda:self.browse("file"))
        self.browse_file_path_button.place(relx=0.192, rely=0.449, height=25, width=56)

        self.toggle_scan_button = ttk.Button(self.file_scan_frame, text='''start''', command=self.toggle_scan)
        self.toggle_scan_button.place(relx=0.404, rely=0.548, height=25, width=76)

        # file scan frame label parent is self
        self.file_scan_frame_label = tk.Label(self, font=FRAME_LABEL_FONT, text='''file scan''', background=GGC.APP_BG)
        self.file_scan_frame_label.place(relx=0.263, rely=0.118, height=19, width=56)

        # results frame parent is self
        self.results_frame = tk.Frame(self, relief='groove', borderwidth="2", background=GGC.APP_BG)
        self.results_frame.place(relx=0.683, rely=0.138, relheight=0.806, relwidth=0.31)

        # all wdgets in results frame
        self.clear_results_button = ttk.Button(self.results_frame, text='''clear''', command=self.clear_results)
        self.clear_results_button.place(relx=0.04, rely=0.893, height=25, width=74)

        self.export_results_button = ttk.Button(self.results_frame, text='''export''', command=self.export_results)
        self.export_results_button.place(relx=0.351, rely=0.893, height=25, width=74)

        self.help_results_button = ttk.Button(self.results_frame, text='''help''', command=self.help_results)
        self.help_results_button.place(relx=0.661, rely=0.893, height=25, width=74)

        self.results_listbox_frame = tk.Frame(self.results_frame, relief='groove', borderwidth="2", background=GGC.DEFAULT_WIN_BG)
        self.results_listbox_frame.place(relx=0.028, rely=0.035, relheight=0.831, relwidth=0.948)

        self.scrollbar = tk.Scrollbar(self.results_listbox_frame, orient="vertical", highlightcolor="#d9d9d9", highlightbackground="#d9d9d9")
        self.scrollbar.pack(side='right', fill='y')

        self.listNodes = tk.Listbox(self.results_listbox_frame, width=100, yscrollcommand=self.scrollbar.set, font=("Helvetica", 12))
        self.listNodes.bind("<Double-Button-1>", self.on_double)
        self.listNodes.pack(expand=True, fill='y')
        self.scrollbar.config(command=self.listNodes.yview)

        self.results_frame_label = tk.Label(self, background=GGC.APP_BG, font=FRAME_LABEL_FONT, text='''results''')
        self.results_frame_label.place(relx=0.701, rely=0.116, height=19, width=47)

    def create_active_scan_widgets(self):
        self.scan_progress_frame = tk.Frame(self.file_scan_frame, borderwidth="2", relief="groove", background=GGC.DEFAULT_WIN_BG)
        self.scan_progress_frame.place(relx=0.021, rely=0.638, relheight=0.335, relwidth=0.959)

        self.scan_progress_label = tk.Label(self.scan_progress_frame, background=GGC.DEFAULT_WIN_BG, text='''scan progress''')
        self.scan_progress_label.place(relx=0.031, rely=0.074, height=21, width=78)

        self.item_being_scanned_label = tk.Label(self.scan_progress_frame, anchor='w', background=GGC.DEFAULT_WIN_BG, text='''item being scanned:''')
        self.item_being_scanned_label.place(relx=0.062, rely=0.296, height=21, width=296)

        self.items_detected_label = tk.Label(self.scan_progress_frame, anchor='w', background=GGC.DEFAULT_WIN_BG, text='''0 items detected''')
        self.items_detected_label.place(relx=0.062, rely=0.496, height=21, width=163)

    def toggle_scan(self):
        if self.controller.status_tab.file_scan_status == "INACTIVE":
            self.start_scan()
        elif self.controller.status_tab.file_scan_status == "ACTIVE":
            self.stop_scan()
        return

    def on_double(self, event):
        self.results_options = tk.Tk()
        self.results_options.wm_title("Actions needed")
        
        widget = event.widget
        selection=widget.curselection()
        path = widget.get(selection[0])

        file_label = tk.Label(self.results_options, text = "FILE: " + path, pady=2)
        file_label.grid(row=0)

        options_label = tk.Label(self.results_options, text = "OPTIONS:", anchor = "w", pady=2)
        options_label.grid(row=1, sticky = "w")

        delete_file_button = ttk.Button(self.results_options, text="delete", command=lambda: self.delete_file(path))
        delete_file_button.grid(row=2, sticky="nw", columnspan=1)

        ignore_file_button = ttk.Button(self.results_options, text="ignore", command=self.clear_results)
        ignore_file_button.grid(row=2, column=1,columnspan=1)


        width_of_window = 320
        height_of_window = 120
        screen_width = self.results_options.winfo_screenwidth()
        screen_height = self.results_options.winfo_screenheight()
        x_coordinate = (screen_width//2) - (width_of_window//2)
        y_coordinate = (screen_height//2) - (height_of_window//2)
        self.results_options.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.results_options.resizable(False, False)
        self.results_options.mainloop()

    def start_scan(self):
        if not self.option_and_path_check():
            return

        self.controller.status_tab.toggle_status("file")
        self.create_active_scan_widgets()
        self.toggle_scan_button.configure(text="stop")


        t1 = threading.Thread(target=self.scan).start()

        return

    def scan(self):
        count = 0
        if self.controller.status_tab.file_scan_status == "INACTIVE":
            return
        if self.scan_type.get() == 3:
            if md5(self.scan_path) in hash_database:
                count += 1
                self.listNodes.insert('end', self.scan_path)
                text = str(count) + " items detected"
                self.items_detected_label.configure(text= text)

        else:
            for path, subdirs, files in path_walker(self.scan_path):
                if self.controller.status_tab.file_scan_status == "INACTIVE":
                    return
                for name in files:
                    if self.controller.status_tab.file_scan_status == "INACTIVE":
                        return
                    self.item_being_scanned_label.configure(text=add_name_to_path(path, name))
                    if str(md5(add_name_to_path(path, name))) in hashes:
                        count += 1
                        self.listNodes.insert('end', add_name_to_path(path, name))
                        text = str(count) + " items detected"
                        self.items_detected_label.configure(text= text)
        messagebox.showinfo("Scan complete", "Scan complete, please view results tab")
        self.stop_scan()
        return

    def browse(self, browse_type):
        if browse_type == "dir":
            self.folder_path = filedialog.askdirectory()
            self.folder_path_label.configure(text=self.folder_path)
        elif browse_type == "file":
            self.file_path = filedialog.askopenfilename()
            self.file_path_label.configure(text=self.file_path)
        return

    def option_and_path_check(self):
        scan_type = self.scan_type.get()
        if  scan_type == 0:
            messagebox.showwarning("Prompt", "Please select a scan type!")
            return False
        # complete scan
        if scan_type == 1:
            self.scan_path = "C:\\"
        #folder scan
        elif scan_type == 2:
            if self.folder_path == None or self.folder_path == "":
                messagebox.showwarning("Prompt", "Please specify directory path!")
                return False
            self.scan_path = self.folder_path
        elif scan_type == 3:
            if self.file_path == None or self.file_path == "":
                messagebox.showwarning("Prompt", "Please specify file path!")
                return False
            self.scan_path = self.file_path
        return True
        
    def stop_scan(self):
        self.controller.status_tab.toggle_status("file")
        self.toggle_scan_button.configure(text="start")
        self.scan_path = None
        self.folder_path = None
        self.file_path = None
        self.scan_type.set(0)
        self.folder_path_label.configure(text="Path not set")
        self.file_path_label.configure(text="Path not set")
        self.scan_progress_frame.destroy()
        self.scan_progress_label.destroy()
        self.item_being_scanned_label.destroy()
        self.items_detected_label.destroy()
        return

    def delete_file(self,path):
        if self.results_options:
            self.results_options.destroy()
        remove_file(path)

    def clear_results(self):
        try:
            self.results_options.destroy()
        except:
            pass
        self.listNodes.delete(0, 'end')

    def export_results(self):
        print("TODO Exporting results ")

    def help_results(self):
        print("TODO help results ")