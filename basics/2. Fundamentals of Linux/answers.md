# 🐧 Fundamentals of Linux

## Challenge 1

* **Flag:** `CDDC2025{pers0nal_pr0j3ct_nin3tie5}`

---

## Challenge 2

### Steps:

1. Connect via Netcat:

   ```bash
   nc 52.76.13.43 8086
   ```

2. Check files:

   ```bash
   ls -l
   cat flag_2.txt
   ```

   * Flag Component: `_t1{5202CDDC`

3. Follow symlink in `flag_3.txt` to `/opt/file_storage`

4. Read hidden file:

   ```bash
   cd /opt/file_storage
   ls -l
   cat .flag_3.txt
   ```

   * Flag Component: `}n3dd1h_t5uj_54W`

* **Flag:** `CDDC2025{1t_W45_ju5t_h1dd3n}`

---

## Challenge 3

### Steps:

1. Connect:

   ```bash
   nc 52.76.13.43 8087
   ```
2. View file:

   ```bash
   cat fruits
   ```

* **Flag:** `CDDC2025{this_is_Random_fruits}`

---

## Challenge 4

### Steps:

1. Connect:

   ```bash
   nc 52.76.13.43 8088
   ```
2. Navigate and find file type:

   ```bash
   cd desktop
   find . -type f -exec file {} \;
   ```

* **Flag:** `CDDC2025{Y0u_F1nd_Me56}`

---

## Challenge 5

### Steps:

1. Connect:

   ```bash
   nc 52.76.13.43 8089
   ```
2. Search for "password":

   ```bash
   grep -r "password" /
   ```
3. Check the noted readme:

   ```bash
   cat /var/identify_file/Readme.md
   ```

* **Flag:** `CDDC2025{W0w_Y0U_F0UnD_1T!}`

---


