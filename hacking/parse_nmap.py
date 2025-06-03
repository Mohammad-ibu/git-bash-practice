# parse_nmap.py

live_host = []

with open("scan.txt") as file:
    for line in file:
        if "ports" in line and "open" in line:
                                          parts = line.split()
                                          ip = parts[1]
                                          live_hosts.append(ip)


print("[*] live host with open ports:")
for host in live_host:
    print(f" - {host}")
