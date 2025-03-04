# Network Security Toolkit  

A command-line cybersecurity toolkit for scanning networks, detecting nearby devices, and spoofing MAC addresses.  

## 📂 Project Structure  
```
📦 Network Security Toolkit  
 ┣ 📂 scans/              # Stores scan results  
 ┣ 📂 network_tool/       # Main tool scripts  
 ┣ 📜 setup.py            # Installation script  
 ┣ 📜 requirements.txt    # Dependencies  
 ┣ 📜 README.md           # Documentation  
```

## 🔧 Installation  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/your-username/network-security-toolkit.git  
   cd network-security-toolkit  
   ```  
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt  
   ```  
   Or install via `setup.py`:  
   ```sh
   python setup.py install  
   ```

## 🚀 Usage  
Run the main script:  
```sh
python3 network_tool/main.py  
```  

### Features  
- **Port Scan** – Scan a single IP or a list of IPs for open ports. Results are saved in `scans/`.  
- **Device Scanner** – Detect nearby devices, capturing IPs and MAC addresses.  
- **MAC Address Spoofing** – Temporarily change your MAC address for privacy.  

## ⚠️ Disclaimer  
This tool is for **educational purposes only**. Unauthorized use is strictly prohibited. The developer is not responsible for misuse.

