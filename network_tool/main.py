import os
from scanner import port_scan, scan_network
from mac_spoofer import mac_spoof

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_terminal()
    print("=== Network Security Tool ===")
    print("1️⃣ Port Scan")
    print("2️⃣ Scan Nearby Devices (With MAC Spoofer)")
    
    choice = input("\nSelect an option: ")
    
    if choice == "1":
        target = input("\nEnter IP address to scan: ")
        port_scan(target)

    elif choice == "2":
        network = input("\nEnter network range (e.g., 192.168.1.1/24): ")
        scan_network(network)

        mac_choice = input("\nDo you want to spoof your MAC address? (y/n): ")
        if mac_choice.lower() == "y":
            interface = input("Enter your network interface (e.g., eth0 or wlan0): ")
            new_mac = input("Enter new MAC address (e.g., 00:11:22:33:44:55): ")
            mac_spoof(interface, new_mac)

if __name__ == "__main__":
    main()
