import socket
import scapy.all as scapy
import os

def save_results(filename, data):
    if not os.path.exists("scans"):
        os.makedirs("scans")
    with open(f"scans/{filename}", "w") as file:
        file.write(data)
    print(f"[✅] Results saved in scans/{filename}")

# 1️⃣ Port Scanner
def port_scan(target):
    open_ports = []
    print(f"\n[🔍] Scanning {target} for open ports...\n")

    for port in range(1, 65537):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[✔] Port {port} is open.")
            open_ports.append(port)
        sock.close()

    if open_ports:
        save_choice = input("Do you want to save the results? (y/n): ")
        if save_choice.lower() == "y":
            save_results(f"port_scan_{target}.txt", "\n".join(map(str, open_ports)))

# 2️⃣ Network Scanner
def scan_network(ip_range):
    print(f"\n[🔍] Scanning network: {ip_range}...\n")

    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    results = "IP Address\t\tMAC Address\n" + "-" * 40 + "\n"
    for sent, received in answered_list:
        results += f"{received.psrc}\t{received.hwsrc}\n"
        print(f"[✔] {received.psrc} - {received.hwsrc}")

    save_choice = input("\nDo you want to save the results? (y/n): ")
    if save_choice.lower() == "y":
        save_results("network_scan.txt", results)
