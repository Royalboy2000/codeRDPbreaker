
![Logo](https://www.vhv.rs/dpng/f/415-4157779_anonymous-png.png)


# RDP Breaker Tool


## Authors

- [@samir](https://github.com/Royalboy2000/)


## Features

Key Features

- Fetch RDP Hosts: The tool allows users to specify the number of RDP hosts they want to fetch for further assessment.

- Masscan Integration: Users can choose to use masscan, a fast port scanning tool, to identify hosts with open RDP ports.

- Metasploit Integration: Users can choose to use Metasploit, a popular penetration testing framework, to perform security assessments on the fetched RDP hosts.

- Interactive Menu: The tool presents an interactive menu that displays choices in a user-friendly manner, making it easy for users to navigate.

  ## UPDATE V2

- Improved Readability: Python code is structured and easier to read.
- Better User Interaction: Python script provides a user-friendly interface with input validation.
- Color and ASCII Art: Python adds color and ASCII art for a visually appealing display.
- Secure Command Execution: Python uses subprocess for safer command execution.
- String Manipulation: Python uses regular expressions for sophisticated text processing.
- Enhanced Error Handling: Python displays informative error messages in red for better troubleshooting.
- Code Reusability: Python's functions enable easier code reuse and maintainability.
- Expanded Features: Python adds options to run multiple Metasploit exploits.
- Flexibility: Python handles various scenarios and exceptions for a smoother user experience.

### New Exploit 1

- **Exploit Name:** CVE-2019-0708 BlueKeep
- **Description:** Exploit for Microsoft Remote Desktop Protocol (RDP) vulnerability (CVE-2019-0708), also known as BlueKeep.
- **Added in Python Script:** The Python script now supports running the CVE-2019-0708 BlueKeep exploit in Metasploit.
- **Usage:** To run the CVE-2019-0708 BlueKeep exploit, choose option '1' when prompted for the exploit in the script. Then, provide the required inputs such as the number of RDP hosts and the file containing the list of RDP hosts.
- **Note:** Make sure to have the latest version of Metasploit installed and up-to-date exploit modules for CVE-2019-0708 BlueKeep.

### New Exploit 2

- **Exploit Name:** CVE-2021-34527 PrintNightmare
- **Description:** Exploit for Windows Print Spooler Remote Code Execution vulnerability (CVE-2021-34527), also known as PrintNightmare.
- **Added in Python Script:** The Python script now supports running the CVE-2021-34527 PrintNightmare exploit in Metasploit.
- **Usage:** To run the CVE-2021-34527 PrintNightmare exploit, choose option '2' when prompted for the exploit in the script. Then, provide the required inputs such as the number of RDP hosts and the file containing the list of RDP hosts.
- **Note:** Make sure to have the latest version of Metasploit installed and up-to-date exploit modules for CVE-2021-34527 PrintNightmare.

### New Exploit 3

- **Exploit Name:** CVE-2021-36942 MS-RDP Licensing
- **Description:** Exploit for Microsoft Remote Desktop Protocol (RDP) Licensing service vulnerability (CVE-2021-36942).
- **Added in Python Script:** The Python script now supports running the CVE-2021-36942 MS-RDP Licensing exploit in Metasploit.
- **Usage:** To run the CVE-2021-36942 MS-RDP Licensing exploit, choose option '3' when prompted for the exploit in the script. Then, provide the required inputs such as the number of RDP hosts and the file containing the list of RDP hosts.
- **Note:** Make sure to have the latest version of Metasploit installed and up-to-date exploit modules for CVE-2021-36942 MS-RDP Licensing.


## Deployment

To deploy this project run

```bash
  sudo apt-get update -y
```
```bash
  sudo apt-get upgrade y
```
```bash
  git clone https://github.com/Royalboy2000/codeRDPbreaker
```

```bash
  cd codeRDPbreaker
```
```bash
  pip install pyfiglet colorama
```

```bash
  sudo python3 main.py
```


## Contributing


Please adhere to this project's `code of conduct`.


## Feedback

If you have any feedback, please reach out to us at https://www.instagram.com/s.a.m.i.r_012/


