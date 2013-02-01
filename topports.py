# List top ten TCP ports

# List is taken from "Nmap - Scanning the Internet", DEFCON 16
# presentation by Fyodor

           # port   # service name
topports = [80,     # http
            23,     # telnet
            22,     # ssh
            443,    # https
            3389,   # ms-term-serv
            445,    # microsoft-ds
            139,    # netbios-ssn
            21,     # ftp
            135,    # msrpc
            25]     # smtp
