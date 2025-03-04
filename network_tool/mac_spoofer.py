import os

def mac_spoof(interface, new_mac):
    print(f"\n[🔁] Changing MAC address of {interface} to {new_mac}...")

    if os.name == "nt":
        print("[❌] MAC spoofing is not supported on Windows via this method.")
        return

    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
    os.system(f"sudo ifconfig {interface} up")

    print("[✅] MAC address changed!")
