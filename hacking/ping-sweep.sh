#!/bin/bash

# usage: ./ping-sweep.sh 192.168.1

subnet="$1"

if [ -z "$subnet" ]; then
  echo "usage; $0 <subnet-prefix>"
  echo "example; $0 192.168.1"
  exit 1
fi

for i in {1..254}; do
  ip="$subnet.$i"
  ping -c 1 -w 1 $ip &> /dev/null
  if [ $? -eq 0 ]; then
    echo "[+] host $ip is up"
  else
    echo "[-] host $ip is down"
fi
done   
