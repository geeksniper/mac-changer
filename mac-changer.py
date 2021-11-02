import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", dest="interface", help="name of interface")
parser.add_option("-m", dest="new_mac", help="new mac address")

(options, arguments) = parser.parse_args()

if not options.interface:
    parser.error("please specify interface, use --help for more information")
elif not options.new_mac:
    parser.error("please specify mac-address, use --help for more information")

def func(interface, new_mac):

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("your current mac is: " + new_mac)
    
func(options.interface, options.new_mac)
