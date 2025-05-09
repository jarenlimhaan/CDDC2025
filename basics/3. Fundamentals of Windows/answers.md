# 🖥️ Fundamentals of Windows

## Challenge 1

* **Flag:** `CDDC2025{w1nd0ws_m3_m1st4ke}`

## Challenge 2

### Steps:

1. Unzip first then Run wine and pipe the output to a text file 
    ```bash
    wine fast_console_flag.exe > output.txt 2>&1
    ```
2. Read the output file with `cat`
    ```bash
    cat output.txt
    ```

* **Flag:** `CDDC2025{pR1nt_4nD_g0}`

## Challenge 3

### Steps:

1. Unzip first then Run wine and pipe the output to a text file 
    ```bash
    wine hidden_reg_flag/hidden_reg_flag.exe > output2.txt 2>&1
    ```
2. Read the output file with `cat`
    ```bash
    cat output2.txt
    ```

* **Flag:** `CDDC2025{ReG_hAcK}`

## Challenge 4

### Steps:

1. The brackets are known as js code obfuscation (jsfuck)

2. Copy the bracket expressions and decode on this site: https://www.dcode.fr/jsfuck-language

* **Flag:** `CDDC2025{YES_1t_1S_JAVA2CR1pt!}`

## Challenge 5

### Steps:

1. Just do ctrl-f `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

2. Extract the part before `.exe`

* **Flag:** `CDDC2025{W3ll_d0n3_Y0u_F0un[)_17}`

## Challenge 6 

### Steps:

1. Firstly lets run `file` on my directory 
```bash
file *
```
>> we notice that only Tiger.png is the only png file and the rest are webp images

2. Lets examine tiger.png by running `xxd`
```bash
xxd Tiger.png
```

3. We notice at the last few bytes, the flag is there!
```bash
0008e640: 4344 4400 0000 0000 0000 0000 0000 0000  CDD.............
0008e650: 4332 3000 0000 0000 0000 0000 0000 0000  C20.............
0008e660: 3235 7b00 0000 0000 0000 0000 0000 0000  25{.............
0008e670: 614e 6900 0000 0000 0000 0000 0000 0000  aNi.............
0008e680: 4d61 3100 0000 0000 0000 0000 0000 0000  Ma1.............
0008e690: 5f46 6100 0000 0000 0000 0000 0000 0000  _Fa.............
0008e6a0: 526d 5f00 0000 0000 0000 0000 0000 0000  Rm_.............
0008e6b0: 5332 4300 0000 0000 0000 0000 0000 0000  S2C.............
0008e6c0: 7245 7400 0000 0000 0000 0000 0000 0000  rEt.............
0008e6d0: 7d                                       }

```

* **Flag:** `CDDC2025{aNiMa1_FaRm_S2CrEt}`

## Challenge 7 

### Steps:

* **Flag:**

## Challenge 8 

### Steps:

* **Flag:**

## Challenge 9 

### Steps:

* **Flag:**