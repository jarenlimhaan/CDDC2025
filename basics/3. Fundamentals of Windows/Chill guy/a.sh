#!/bin/bash

# File and wordlist
FILE="Chill.jpg"
WORDLIST=("philb" "Philb" "PHILB" "ph1lb" "Ph1lb" "philb123" "philb!" "philB" "PhilB" "ph!lb" "Chill" "chill" "cool" "cold" "relax" "password" "letmein" "admin" "dex" "dexphilb" "name" "Start")

for PASS in "${WORDLIST[@]}"; do
    echo "[*] Trying password: $PASS"
    steghide extract -sf "$FILE" -p "$PASS" -f > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "[+] Success! Password: $PASS"
        exit 0
    fi
done

echo "[-] No password worked from list."
