#!/usr/bin/env python3
import sys
import os
import platform
import subprocess
import requests
import base64
import re
import time
import socket
from concurrent.futures import ThreadPoolExecutor

VPN_GATE_CSV_URL = "https://www.vpngate.net/api/iphone/"

def check_and_install_modules():
    """Check for required modules and install them if missing"""
    required_modules = {
        'requests': 'requests',
        'concurrent.futures': 'concurrent'  # Part of standard library but check for completeness
    }
    
    for module_name, pip_name in required_modules.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[!] Installing missing module: {module_name}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
                print(f"[✓] Successfully installed {module_name}")
            except Exception as e:
                print(f"[!] Failed to install {module_name}: {e}")
                print("[!] Please install it manually using: pip install " + pip_name)
                return False
    return True

def fetch_vpngate_list():
    print("[*] Fetching VPN Gate server list... 🌐")
    try:
        response = requests.get(VPN_GATE_CSV_URL, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch VPN server list: {e}")
        sys.exit(1)

def parse_openvpn_configs(csv_data):
    servers = []
    lines = csv_data.splitlines()
    for line in lines:
        if line.startswith("*") or line.startswith("Title") or "," not in line:
            continue
        parts = line.split(",")
        if len(parts) < 15 or not parts[-1].strip():
            continue
        try:
            ovpn_data = base64.b64decode(parts[-1].strip()).decode("utf-8", errors="ignore")
            servers.append({
                "host": parts[1],
                "port": extract_port_from_ovpn(ovpn_data),
                "country": parts[5],
                "score": int(parts[2]),
                "ovpn": ovpn_data
            })
        except Exception as e:
            continue
    return sorted(servers, key=lambda s: s["score"], reverse=True)

def extract_port_from_ovpn(ovpn_data):
    match = re.search(r'^remote\s+([^\s]+)\s+(\d+)', ovpn_data, re.MULTILINE)
    if match:
        return match.group(2)
    return "1194"

def tcping(host, port, timeout=10):
    try:
        start_time = time.time()
        # Create socket with timeout
        with socket.create_connection((host, int(port)), timeout=timeout):
            latency_ms = (time.time() - start_time) * 1000
            return True, latency_ms
    except (socket.timeout, socket.gaierror, OSError):
        return False, None

def print_server_list(servers, count):
    print("\n**SERVER LIST** 📋")
    print("-" * 30)
    for s in servers[:count]:
        host = s["host"]
        port = s["port"]
        print(f"🌐 {host}:{port}")
    print("-" * 30)

def save_ovpn_configs(servers):
    output_dir = "vpngate_configs"
    os.makedirs(output_dir, exist_ok=True)
    
    for server in servers:
        # Sanitize filename for all OS
        safe_host = re.sub(r'[\\/*?:"<>|]', "_", server['host'])
        filename = os.path.join(output_dir, f"{server['country']}_{safe_host}.ovpn")
        
        with open(filename, "w") as f:
            f.write(server["ovpn"])
        print(f"[+] Saved: {filename} ✅")

def test_servers(servers, count):
    print("\n[*] WAIT 10 SECONDS BEFORE STARTING TESTS... ⏳")
    for i in range(10, 0, -1):
        print(f"Testing starts in {i}... ⏲", end="\r")
        time.sleep(1)
    print("[*] Starting connectivity tests... 🚀\n")
    
    connected_servers = []
    
    def check_server(s):
        status, latency = tcping(s["host"], s["port"])
        return s, status, latency
    
    # Adjust thread count based on OS
    max_workers = 100 if platform.system() != "Windows" else 20
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(check_server, servers[:count])
        for s, status, latency in results:
            result = f"✅ OPEN ({latency:.2f} ms)" if status else "❌ CLOSED"
            print(f"{s['host']}:{s['port']} - {result}")
            if status:
                s["latency"] = latency
                connected_servers.append(s)
    
    connected_servers.sort(key=lambda s: s["latency"])
    return connected_servers

def print_connected_servers(connected_servers):
    if connected_servers:
        print("\n**CONNECTED SERVERS (SORTED BY LATENCY)** 🌟")
        print("-" * 30)
        for i, s in enumerate(connected_servers, 1):
            print(f"{i}. {s['host']}:{s['port']} - {s['latency']:.2f} ms ✅")
        print("-" * 30)
    else:
        print("\n[!] No servers were reachable. ❌")

def get_user_input(total_servers):
    while True:
        try:
            user_input = input("Please enter the number of servers to test (press Enter for all servers): ")
            if user_input.strip() == "":
                return total_servers
            num_servers = int(user_input)
            if num_servers > 0:
                return num_servers
            else:
                print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    # Check and install required modules
    if not check_and_install_modules():
        print("[!] Failed to install required modules. Exiting.")
        sys.exit(1)
    
    # Cross-platform compatibility
    if platform.system() == "Windows":
        os.system('color')  # Enable ANSI color support on Windows
    
    try:
        csv_data = fetch_vpngate_list()
        servers = parse_openvpn_configs(csv_data)
        if not servers:
            print("❌ No OpenVPN servers found.")
            return
        
        print(f"[+] Found {len(servers)} OpenVPN servers. ✅")
        
        num_servers = get_user_input(len(servers))
        num_servers = min(num_servers, len(servers))
        
        print_server_list(servers, num_servers)
        connected_servers = test_servers(servers, num_servers)
        
        if connected_servers:
            print("\n[*] Saving configs for connected servers... 💾")
            save_ovpn_configs(connected_servers)
        
        print_connected_servers(connected_servers)
        
        print("\n**CREDENTIALS** 🔑")
        print("-" * 30)
        print("User Name: vpn")
        print("Password: vpn")
        print("-" * 30)
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()