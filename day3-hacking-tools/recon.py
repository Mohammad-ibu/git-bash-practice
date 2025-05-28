import os

def banner():
    print("simple recon tool")
    print("=================")

def ping_target(target):
    print(f"pinging {target}...")
    os.system(f"ping -c 4 {target}")
    
def whois_target(target):
    print(f"whois info for {target}...")
    os.system(f"whois {target}")

def main():
    banner()
    target = input("enter target domain ip: ")
    
    print("\n[1] ping target")
    print("[2] whois lookup")
    choice = input("choose an option: ")
    
    if choice == "1":
       ping_target(target)
    elif choice == "2":
         whois_target(target)
    else:
        print("invalid choice")

if __name__ == "__main__":
    main() 
