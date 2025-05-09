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
1. First run `start.exe`
```bash
For linux:
wine start.exe
```
2. Since, bruteforcing different combinations of `philb` doesn't work for `steghide`, we try to grep through the registries
```bash
grep -i -E 'password|philb|chill' ~/.wine/*.reg
```
3. We notice the flag after we do a grep on the registry files 
```bash
/home/topiko/.wine/system.reg:@="ChillGuy File"
/home/topiko/.wine/system.reg:@="C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\powershell.exe -ExecutionPolicy Bypass -Command \"Add-Type -AssemblyName 'System.Windows.Forms'; [System.Windows.Forms.MessageBox]::Show('CDDC2025{Chill111111111111111_9uy}', 'Notification')\""
/home/topiko/.wine/system.reg:[Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE] 1746780347
/home/topiko/.wine/system.reg:[Software\\Wow6432Node\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_HTTP_USERNAME_PASSWORD_DISABLE] 1746780363
```

* **Flag:** `CDDC2025{Chill111111111111111_9uy}`

## Challenge 8 

### Steps:
1. We are given a Hisotry file which is usually a sqlite3 db
2. Write a bash script to grep all related `cddc` row data fetched from all tables - `find_history_flag.sh`
3. We notice a particular suspicious url with `flag` url params
```bash
403|http://cddc.dstabrainhack.com/?id=12345&user=johndoe&email=johndoe%40email.com&age=25&gender=male&country=US&city=NewYork&zip=10001&phone=123-456-7890&dob=1995-08-15&status=active&balance=1520.75&points=2500&membership=premium&last_login=2025-03-30T14%3A30%3A00Z&referrer=google.com&session_id=abcde12345&cart_id=xyz67890&

fl4g=d08df2b8de382d42c60e116368c3ee799e00f286&device=mobile&ip=192.168.1.1&browser=chrome&os=windows&app_version=1.2.3&subscription=true&newsletter=false&timezone=UTC-5&language=en&theme=dark&tracking_id=trk_98765&discount_code=SPRING50||1|1|13380368653775195|0
```
4. By plugging it into the flag format, we get the flag!

* **Flag:** `CDDC2025{d08df2b8de382d42c60e116368c3ee799e00f286}`

## Challenge 9 

### Steps:

1. Based on the clues, we must convert the excel to zip file, as  they are actually ZIP archives under the hood, structured according to the Office Open XML standard.
```bash
mv excel_hidden_flag.xlsx yourfile.zip
```
2. Unzip the converted zip file
```bash
unzip yourfile.zip -d extracted_excel 
```
3. grep the flag pattern within the extracted diretcory 
```bash
 grep -r "CDDC2025{" extracted_excel/
```

* **Flag:** `CDDC2025{3xcEl_H1dden_fl4g}`