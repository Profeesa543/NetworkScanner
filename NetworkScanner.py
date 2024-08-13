import scapy.all as scapy
import optparse

print("""                  __
.--.--.--..-----.|  |.----..-----..--------..-----.
|  |  |  ||  -__||  ||  __||  _  ||        ||  -__|
|________||_____||__||____||_____||__|__|__||_____|




""")

def get_user_input():
    opt_write = optparse.OptionParser()

    
    opt_write.add_option("-i", "--ip", dest="ip", help="ENTER IP ADDRESS")

    
    (options, arguments) = opt_write.parse_args()

    
    

    
    if not options.ip:
        print("The program was closed because you did not enter a valid IP address.")
        exit()

    return options

def send(ip):
    arp = scapy.ARP(pdst=ip)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp  
    (answer, unanswer) = scapy.srp(packet, timeout=1, )
    answer.summary()


user_input = get_user_input()
send(user_input.ip)
