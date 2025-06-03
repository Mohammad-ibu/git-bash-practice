#!/usr/bin/env bash

# extract IPs from file

grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$1"
