# Author: Moller.R 
# Email: greenorange103@gmail.com
# file_analysis.py - 

# Import imports file
from blue_sentinel.scripts.global_imports import *
from blue_sentinel.scripts.strings import strings
from tkinter import filedialog



class FileAnalysis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=GGC.APP_BG)
        self.controller = controller
        self.file_path = None

        self.file_malware_analysis_frame = tk.Frame(self, relief='groove', borderwidth="2", background="#ffffff")
        self.file_malware_analysis_frame.place(relx=0.263, rely=0.121, relheight=0.819, relwidth=0.72)

        self.file_label = tk.Label(self.file_malware_analysis_frame, anchor="w", background="#ffffff", text='''file''')
        self.file_label.place(relx=0.035, rely=0.063, height=21, width=214)

        self.upload_button = ttk.Button(self.file_malware_analysis_frame, text='''upload''', command=self.upload)
        self.upload_button.place(relx=0.417, rely=0.061, height=25, width=76)

        self.begin_analysis_frame = ttk.Button(self.file_malware_analysis_frame, text='''begin analysis''', command=self.start_analysis)
        self.begin_analysis_frame.place(relx=0.035, rely=0.168, height=25, width=84)

        self.analysis_frame = tk.Frame(self.file_malware_analysis_frame, relief='groove', borderwidth="2", background="#ffffff")
        self.analysis_frame.place(relx=0.017, rely=0.253, relheight=0.726, relwidth=0.964)

        self.strings_frame = tk.Frame(self.analysis_frame, borderwidth="2", relief="groove", background="#d9d9d9")
        self.strings_frame.place(relx=0.025, rely=0.087, relheight=0.884, relwidth=0.459)

        self.hex_dump_frame = tk.Frame(self.analysis_frame, relief='groove', borderwidth="2", background="#d9d9d9")
        self.hex_dump_frame.place(relx=0.505, rely=0.087, relheight=0.884, relwidth=0.458)

        self.strings_frame_label = tk.Label(self.analysis_frame, background="#ffffff", text='''strings''')
        self.strings_frame_label.place(relx=0.032, rely=0.026, height=21, width=34)

        self.hex_dump_frame_label = tk.Label(self.analysis_frame, background="#ffffff", text='''hex dump''')
        self.hex_dump_frame_label.place(relx=0.505, rely=0.026, height=21, width=64)

        self.file_malware_analysis_frame_label = tk.Label(self, background="#ffffff", text='''file malware analysis''')
        self.file_malware_analysis_frame_label.place(relx=0.275, rely=0.103, height=21, width=116)

        self.scrollbar = tk.Scrollbar(self.strings_frame, orient="vertical", highlightcolor="#d9d9d9", highlightbackground="#d9d9d9")
        self.scrollbar.pack(side='right', fill='y')

        self.listNodes = tk.Listbox(self.strings_frame, width=100, yscrollcommand=self.scrollbar.set, font=("Helvetica", 12))
        #self.listNodes.bind("<Double-Button-1>", self.on_double)
        self.listNodes.pack(expand=True, fill='y')
        self.scrollbar.config(command=self.listNodes.yview)

    def upload(self):
        self.file_path = filedialog.askopenfilename()
        self.file_label.configure(text="file: " + self.file_path)

    def start_analysis(self):
        if self.file_path == None:
            messagebox.showwarning("Prompt", "Please specify file path!")
            return
        else:
            sl = strings(self.file_path, 4)

            for s in sl:
                self.listNodes.insert('end', s)
        