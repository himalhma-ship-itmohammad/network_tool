#!/usr/bin/env python3
"""
Network Information Tool
Author: Your Name
GitHub: himalhma-ship-timohammad
"""

import socket
import platform
import subprocess
import os
from datetime import datetime

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print tool banner"""
    banner = """
    ╔═══════════════════════════════════╗
    ║        NETWORK INFO TOOL          ║
    ║      GitHub Learning Project      ║
    ╚═══════════════════════════════════╝
    """
    print(banner)

def get_system_info():
    """Get basic system information"""
    print("🔧 SYSTEM INFORMATION")
    print("=" * 40)
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Node Name: {platform.node()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")
    print("")

def get_network_info():
    """Get network information"""
    print("🌐 NETWORK INFORMATION")
    print("=" * 40)
    
    try:
        # Get local machine name and IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        print(f"Hostname: {hostname}")
        print(f"Local IP: {local_ip}")
        
        # Get public IP (using external service)
        try:
            import requests
            public_ip = requests.get('https://api.ipify.org', timeout=5).text
            print(f"Public IP: {public_ip}")
        except:
            print("Public IP: Could not fetch")
            
    except Exception as e:
        print(f"Error getting network info: {e}")
    
    print("")

def ping_test():
    """Test connectivity with ping"""
    print("📡 CONNECTIVITY TEST")
    print("=" * 40)
    
    targets = ['8.8.8.8', 'github.com', 'google.com']
    
    for target in targets:
        try:
            # For Windows and Linux/Mac
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            result = subprocess.run(
                ['ping', param, '2', target],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ {target}: Reachable")
            else:
                print(f"❌ {target}: Unreachable")
                
        except Exception as e:
            print(f"❌ {target}: Error - {e}")

def port_scanner_local():
    """Simple local port scanner"""
    print("\n🔍 LOCAL PORT SCANNER")
    print("=" * 40)
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    open_ports = []
    
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            open_ports.append(port)
            print(f"✅ Port {port}: OPEN")
        else:
            print(f"❌ Port {port}: CLOSED")
        sock.close()
    
    return open_ports

def save_report(open_ports):
    """Save results to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""
    Network Scan Report
    Generated: {timestamp}
    
    System Info:
    - OS: {platform.system()} {platform.release()}
    - Hostname: {platform.node()}
    
    Open Ports: {open_ports}
    
    Scan completed successfully.
    """
    
    with open('network_scan_report.txt', 'w') as f:
        f.write(report)
    
    print(f"\n💾 Report saved as: network_scan_report.txt")

def main():
    """Main function"""
    clear_screen()
    print_banner()
    
    get_system_info()
    get_network_info()
    ping_test()
    open_ports = port_scanner_local()
    
    # Save report
    save_report(open_ports)
    
    print("\n" + "=" * 50)
    print("🎉 Scan completed! Check the report file.")
    print("=" * 50)

if __name__ == "__main__":
    main()

