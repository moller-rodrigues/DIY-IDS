# Author: Moller.R 
# Email: greenorange103@gmail.com
# net_scan.py - 

# Import imports file
from blue_sentinel.scripts.global_imports import *
from blue_sentinel.scripts.rules import *
import threading
import socket 
import struct
import textwrap

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

class NetScan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=GGC.APP_BG)
        self.controller = controller
        self.rules = Rules()
        self.ip = '192.168.0.14'

        if self.controller.status_tab.notifications_status == "DISABLED":
            self.NOTIFICATIONS_BUTTON_TEXT = "turn on"
        else:
            self.NOTIFICATIONS_BUTTON_TEXT = "turn off"

        self.create_widgets()

    def create_widgets(self):

        self.netscan_status_frame = tk.Frame(self, relief='groove', borderwidth="2", background="#ffffff")
        self.netscan_status_frame.place(relx=0.263, rely=0.133, relheight=0.192, relwidth=0.72)

        self.netscan_status_label = tk.Label(self.netscan_status_frame, background="#ffffff", text='''Status: ''' + self.controller.status_tab.netscan_status)
        self.netscan_status_label.place(relx=0.035, rely=0.174, height=21, width=87)

        self.notfications_label = tk.Label(self.netscan_status_frame, background="#ffffff", text='''Notifications''')
        self.notfications_label.place(relx=0.035, rely=0.609, height=21, width=71)

        self.report_output_label = tk.Label(self.netscan_status_frame, background="#ffffff", text='''Report output''')
        self.report_output_label.place(relx=0.399, rely=0.113, height=21, width=244)

        self.report_output_browse = ttk.Button(self.netscan_status_frame, text='''browse''')
        self.report_output_browse.place(relx=0.833, rely=0.087, height=25, width=76)

        self.notifactions_toggle_button = ttk.Button(self.netscan_status_frame, text=self.NOTIFICATIONS_BUTTON_TEXT, command = self.toggle_notifications)
        self.notifactions_toggle_button.place(relx=0.193, rely=0.598, height=25, width=76)

        self.rules_frame = tk.Frame(self, relief='groove', borderwidth="2", background="#ffffff")
        self.rules_frame.place(relx=0.263, rely=0.358, relheight=0.308, relwidth=0.72)

        self.rules_listbox_frame = tk.Frame(self.rules_frame, relief='groove', borderwidth="2", background="#d9d9d9")
        self.rules_listbox_frame.place(relx=0.01, rely=0.065, relheight=0.73, relwidth=0.981)

        self.add_rule_button = ttk.Button(self.rules_frame, text='''add''')
        self.add_rule_button.place(relx=0.069, rely=0.811, height=25, width=76)

        self.edit_rule_button = ttk.Button(self.rules_frame, text='''edit''')
        self.edit_rule_button.place(relx=0.434, rely=0.811, height=25, width=76)

        self.delete_rule_button = ttk.Button(self.rules_frame, text='''delete''')
        self.delete_rule_button.place(relx=0.799, rely=0.811, height=25, width=76)

        self.netscan_status_frame_label = tk.Label(self, background="#ffffff", text='''Network scan''')
        self.netscan_status_frame_label.place(relx=0.275, rely=0.117, height=21, width=76)

        self.rules_frame_label = tk.Label(self, background="#ffffff", text='''Rules''')
        self.rules_frame_label.place(relx=0.275, rely=0.343, height=21, width=32)

        self.rules_scrollbar = tk.Scrollbar(self.rules_listbox_frame, orient="vertical", highlightcolor="#d9d9d9", highlightbackground="#d9d9d9")
        self.rules_scrollbar.pack(side='right', fill='y')

        self.rules_listNodes = tk.Listbox(self.rules_listbox_frame, width=100, yscrollcommand=self.rules_scrollbar.set, font=("Helvetica", 12))
        self.rules_listNodes.bind("<Double-Button-1>", self.rules_on_double)
        self.rules_listNodes.pack(expand=True, fill='y')
        self.rules_scrollbar.config(command=self.rules_listNodes.yview)

        self.alerts_frame = tk.Frame(self, relief='groove', borderwidth="2", background="#ffffff")
        self.alerts_frame.place(relx=0.263, rely=0.7, relheight=0.242, relwidth=0.72)

        self.alerts_listbox_frame = tk.Frame(self.alerts_frame, relief='groove', borderwidth="2", background="#d9d9d9")
        self.alerts_listbox_frame.place(relx=0.017, rely=0.103, relheight=0.655, relwidth=0.964)

        self.alerts_scrollbar = tk.Scrollbar(self.rules_listbox_frame, orient="vertical", highlightcolor="#d9d9d9", highlightbackground="#d9d9d9")
        self.alerts_scrollbar.pack(side='right', fill='y')

        self.alerts_listNodes = tk.Listbox(self.alerts_listbox_frame, width=100, yscrollcommand=self.alerts_scrollbar.set, font=("Helvetica", 12))
        self.alerts_listNodes.bind("<Double-Button-1>", self.alerts_on_double)
        self.alerts_listNodes.pack(expand=True, fill='y')
        self.alerts_scrollbar.config(command=self.alerts_listNodes.yview)

        self.clear_alerts_button = ttk.Button(self.alerts_frame, text='''clear''', command=self.clear_alerts)
        self.clear_alerts_button.place(relx=0.434, rely=0.779, height=25, width=76)

        self.alerts_frame_label = tk.Label(self, background="#ffffff", text='''Alerts''')
        self.alerts_frame_label.place(relx=0.275, rely=0.683, height=21, width=36)

        self.scan_button = ttk.Button(self.netscan_status_frame, text='''start''', command = self.toggle_scan)
        self.scan_button.place(relx=0.193, rely=0.161, height=25, width=76)

    def start_scan(self):
        self.controller.status_tab.toggle_status("network")
        self.scan_button.configure(text="stop")

        t1 = threading.Thread(target=self.scan).start()
        return

    def add_alert(self, text):
        self.alerts_listNodes.insert('end', text)

    def scan(self):
        self.conn = socket.socket(socket.AF_INET,socket.SOCK_RAW) 
        self.conn.bind((self.ip, 0))
        self.conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        while self.controller.status_tab.netscan_status == "ACTIVE":
            raw_data, addr = self.conn.recvfrom(65536)
            dest, src, eth_proto, data = self.ethernet_frame(raw_data)
            # print('\nEthernet Frame:')
            #print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(dest, src, eth_proto))

            (version, header_length, ttl, proto, src, target, data) = self.ipv4_packet(raw_data)
            for bad_ip in self.rules.ip_blocklist:
                if src == bad_ip[0] or target == bad_ip[0]:
            #if src in self.rules.ip_blocklist or target in self.rules.ip_blocklist:
                    self.add_alert("ALERT: Flagged IP: " + '{} Alias: {}'.format(bad_ip[0], bad_ip[1]))
                # print("ALERT connection with flagged IP: ") 
                # print(TAB_1 + 'IPv4 Packet:')
                # print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(version, header_length, ttl))
                # print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

            if proto == 1:
                icmp_type, code, checksum, data = self.icmp_packet(data)
                #print(TAB_1 + 'ICMP Packet:')
                #print(TAB_2 + 'Type: {}, Code: {}, Checksum: {},'.format(icmp_type, code, checksum))
                #print(TAB_2 + 'Data:')
                #print(format_multi_line(DATA_TAB_3, data))
            elif proto == 6:
                src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = self.tcp_segment(data)
                
                if src_port == 80 or dest_port == 80:
                    self.add_alert("ALERT: HTTP " + 'Protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

                #print(TAB_1 + 'TCP Segment:')
                #print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(src_port, dest_port))
                #print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(sequence, acknowledgment))
                #print(TAB_2 + 'Flags:')
                #print(TAB_3 + 'URG: {}, ACK: {}, PSH: {}'.format(flag_urg, flag_ack, flag_psh))
                #print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(flag_rst, flag_syn, flag_fin))

                # if len(data) > 0:
                #     # HTTP
                #     if src_port == 80 or dest_port == 80:
                #         print(TAB_2 + 'HTTP Data:')
                #         try:
                #             http_data = data.decode('utf-8')
                #             http_info = str(http_data).split('\n')
                #             for line in http_info:
                #                 print(DATA_TAB_3 + str(line))
                #         except:
                #             print(self.format_multi_line(DATA_TAB_3, data))
                #     else:
                #         print(TAB_2 + 'TCP Data:')
                #         print(self.format_multi_line(DATA_TAB_3, data))
    
    def ethernet_frame(self, data):
        dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
        return self.get_mac_addr(dest_mac), self.get_mac_addr(src_mac), socket.htons(proto), data[14:]
            
    # Returns MAC as string from bytes (ie AA:BB:CC:DD:EE:FF)
    def get_mac_addr(self, mac_raw):
        byte_str = map('{:02x}'.format, mac_raw)
        mac_addr = ':'.join(byte_str).upper()
        return mac_addr


    # Formats multi-line data
    def format_multi_line(self, prefix, string, size=80):
        size -= len(prefix)
        if isinstance(string, bytes):
            string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
            if size % 2:
                size -= 1
        return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])



    def ipv4_packet(self, data):
        version_header_length = data[0]
        version = version_header_length >> 4
        header_length = (version_header_length & 15) * 4
        ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
        return version, header_length, ttl, proto, self.ipv4(src), self.ipv4(target), data[header_length:]

    def ipv4(self, addr):
        return '.'.join(map(str, addr))

    def icmp_packet(self, data):
        icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
        return icmp_type, code, checksum, data[4:]

    def udp_segment(self, data):
        src_port, dest_port, size = struct.unpack('! H H 2x H', data[8:])
        return src_port, dest_port, size, data[8:]

    def tcp_segment(self, data):
        (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        flag_urg = (offset_reserved_flags & 32) >> 5
        flag_ack = (offset_reserved_flags & 16) >> 4
        flag_psh = (offset_reserved_flags & 8) >> 3
        flag_rst = (offset_reserved_flags & 4) >> 2
        flag_syn = (offset_reserved_flags & 2) >> 1
        flag_fin = offset_reserved_flags & 1
        data = data[offset:]
        return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data 

    def stop_scan(self):
        self.controller.status_tab.toggle_status("network")
        self.scan_button.configure(text="start")


    def toggle_notifications(self):
        if self.notifactions_toggle_button["text"] == "turn on":
            self.controller.status_tab.toggle_status("notifications")
            self.notifactions_toggle_button["text"] = "turn off"
        elif self.notifactions_toggle_button["text"] == "turn off":
            self.controller.status_tab.toggle_status("notifications")
            self.notifactions_toggle_button["text"] = "turn on"
        return

    def toggle_scan(self):
        if self.controller.status_tab.netscan_status == "INACTIVE":
            self.start_scan()
        elif self.controller.status_tab.netscan_status == "ACTIVE":
            self.stop_scan()
        return

    def rules_on_double(self, event):
        #TO DO 
        pass

    def alerts_on_double(self, event):
        #TO DO 
        pass

    def clear_alerts(self):
        self.alerts_listNodes.delete(0, 'end')