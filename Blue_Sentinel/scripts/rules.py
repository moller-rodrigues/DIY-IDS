class Rules():
    def __init__(self):

        self.mac_blocklist = []
        self.ip_blocklist = [["23.207.176.133", "ebuyer.com"]]
        self.protocol_blocklist = ['http']
        self.keyword_blocklist = []

    def add_mac_blocklist(self, mac):
        self.mac_blocklist.append(mac)

    def add_ip_blocklist(self, ip, alias = None):
        self.ip_blocklist.append([ip, alias])

    def add_protocol_blocklist(self, proto):
        self.protocol_blocklist.append(proto)

    def add_keyword_blocklist(self, keyword):
        self.keyword_blocklist.append(keyword)

    def rm_mac_blocklist(self, mac):
        self.mac_blocklist.remove(mac)

    def rm_ip_blocklist(self, ip):
        self.ip_blocklist.remove(ip)

    def rm_protocol_blocklist(self, proto):
        self.protocol_blocklist.remove(proto)

    def rm_keyword_blocklist(self, keyword):
        self.keyword_blocklist.remove(keyword)