# 🕵 Introduction to Cryptography 

## Challenge 1

* **Flag:** `CDDC2025{1nf0rm4t10n_s3cv12ity_foundation}`

## Challenge 2

### Steps:

1. We are given a ciphertext: `lxxtw://tewxifmr.gsq/ZyLJTmIy` and this is just caesar cypher
2. Shift the characters by 4 using this site: https://cryptii.com/pipes/caesar-cipher
3. And we are presented with a link: https://pastebin.com/VuHFPiEu, the link contains the flag

* **Flag:** `CDDC2025{cl4ssic_ciph3rs_n3ver_g3t_0ld}`

## Challenge 3

### Steps:

1. We are given a ciphertext in `message.txt` 
2. Based on the context, we can denote it is likely `substitution cipher`
3. We brute force using this site: https://www.guballa.de/substitution-solver, which gives us the flag

* **Flag:** `CDDC2025{frequency_analysis_attack_on_substitution_cipher}`

## Challenge 4

### Steps:

1. We are a given RSA problem
2. Just edit the chall.py with `output.txt` values 
3. Run `chall.py`

* **Flag:** `CDDC2025{g00d_j0b_0n_5olv1ng_RSA}`

## Challenge 5

### Steps:

1. We are a given RSA problem
2. Just edit the chall.py with `message.txt` values 
3. Run `chall2.py`

* **Flag:** `CDDC2025{it5_0nly_m3_wh0_kn0w_my_priv4te_k3y_ther3fore_1ts_m3}`