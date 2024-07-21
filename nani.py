import requests
import time
import sys

class VulnerabilityScanner:
    def __init__(self, base_url, wordlist):
        self.base_url = base_url.rstrip('/')
        self.lfi_payloads = self.load_wordlist(wordlist)

    def load_wordlist(self, wordlist):
        try:
            with open(wordlist, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except IOError:
            print(f"Error: Unable to open wordlist file: {wordlist}")
            sys.exit(1)

    def print_banner(self):
        banner = r"""

  ______            _____       _    ____       _    _   _______          _ 
 |  ____|          / ____|     | |  / __ \     | |  | | |__   __|        | |
 | |____   _____  | (___   __ _| |_| |  | |_ __| |  | |    | | ___   ___ | |
 |  __\ \ / / _ \  \___ \ / _` | __| |  | | '__| |  | |    | |/ _ \ / _ \| |
 | |___\ V /  __/  ____) | (_| | |_| |__| | |  | |__| |    | | (_) | (_) | |
 |______\_/ \___| |_____/ \__,_|\__|\____/|_|   \____/     |_|\___/ \___/|_|
                                                                            
                                                                            

"""
        print(banner)

    def scan_lfi(self):
        print("[*] Scanning for Local File Inclusion (LFI) vulnerabilities...\n")
        time.sleep(2)  
        for payload in self.lfi_payloads:
            url = f"{self.base_url}{payload}"
            try:
                response = requests.get(url, headers={'User-Agent': 'VulnerabilityScanner/1.0'})
                if response.status_code == 200:
                    if "root:" in response.text:
                        print(f"[+] LFI vulnerability found: {url} ")
                    elif "[fonts]" in response.text or "for 16-bit app support" in response.text:
                        print(f"[+] LFI vulnerability found: {url} ")
                    elif "[boot loader]" in response.text:
                        print(f"[+] LFI vulnerability found: {url} ")
                    elif "localhost" in response.text:
                        print(f"[+] LFI vulnerability found: {url} ")
                    else:
                        print(f"[-] No LFI vulnerability found for payload: {payload}")
                else:
                    print(f"[-] Non-200 HTTP response for payload {payload}: {response.status_code}")
                time.sleep(1)  
            except requests.RequestException as e:
                print(f"[!] Error connecting to {url}: {e}")

    def run(self):
        self.print_banner()
        self.scan_lfi()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")
    parser.add_argument("url", help="Base URL of the web application to scan")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    args = parser.parse_args()

    scanner = VulnerabilityScanner(args.url, args.wordlist)
    scanner.run()