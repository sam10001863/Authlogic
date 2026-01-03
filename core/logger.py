GREEN="\033[92m"
RED="\033[91m"
YELLOW="\033[93m"
RESET="\033[0m"

def info(msg): print(f"{GREEN}[+] {msg}{RESET}")
def warn(msg): print(f"{YELLOW}[!] {msg}{RESET}")
def fail(msg): print(f"{RED}[-] {msg}{RESET}")
