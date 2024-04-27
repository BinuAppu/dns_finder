# DNS Finder
import socket


filepath = input("Enter the Input file path : ")
domainname = input("Enter Domain Name : ")

readfile = open(filepath,"r",encoding="utf-8")
for line in readfile:
    dnsval = line.strip() + "." + domainname
    try:
        query = socket.gethostbyname_ex(dnsval)
        extractip = query[-1]
        print(f" [+] ",dnsval," - ",extractip)
    except:
        # print("Error occured")
        pass