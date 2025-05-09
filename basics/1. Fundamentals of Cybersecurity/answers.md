# 🛡️ Fundamentals of Cybersecurity

## Challenge 1

* **Flag:** `CDDC2025{reaper_ch4se_creeper}`

---

## Challenge 2

### Steps:

1. Check if TCP port is open:

   ```bash
   nc -vz 52.76.13.43 8085
   ```
2. Connect via Netcat:

   ```bash
   nc 52.76.13.43 8085
   ```

   * Inputs: `22`, `25`, `443`

* **Flag:** `CDDC2025{netcat_challenge_success}`

---

## Challenge 3

### Steps:

1. Copy binaries from `this_is_yours.txt`
2. Convert the binary to ASCII (text)

* **Flag:** `CDDC2025{hidden_in_binary}`

---

## Challenge 4

### Steps:

1. Use Steghide to extract hidden data:

   ```bash
   steghide extract -sf kapow.jpg
   ```
2. Password: ``
3. Read extracted text file

* **Flag:** `CDDC2025{Kap00vv_congratulations}`

---

## Challenge 5

### Steps:

1. Download `fcrackzip` and `rockyou.txt` wordlist
2. Crack the zip file:

   ```bash
   fcrackzip -u -D -p rockyou.txt yourfile.zip
   ```
3. Returns back hmm.txt

* **Flag:** `CDDC2025{cr4ck3d_m3_fast}`

---

## Challenge 6

### Steps:

1. Write an automated arithmetic script `arith.py`
2. Flag is returned on terminal

* **Flag:** `CDDC2025{5uP3r_p0W3r3d_c4lCuL4t0r}`
