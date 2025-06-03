import socket

def grab_banner(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2) as s:
            banner = s.recv(1024).decode(errors="ignore").strip()
            return banner
    except Exception as e:
        return f"Error: {e}"

with open("targets.txt") as file:
    for line in file:
        target = line.strip()
        if ':' in target:
            ip, port = target.split(":")
            port = int(port)
            print(f"[*] Connecting to {ip}:{port}")
            banner = grab_banner(ip, port)
            print(f"[+] Banner: {banner}\n")
