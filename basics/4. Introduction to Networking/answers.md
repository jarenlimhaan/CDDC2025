# 🌐 Introduction to Networking 

## Challenge 1

* **Flag:** `CDDC2025{w1r3d_0pt1c4l_w1r3l355}`

## Challenge 2

### Steps:

1. Navigate to the URL & Download the PCAP file 

2. Run wireshark on the pcap file 

3. Click on `Edit` -> `Find Packet` -> Change Filter to String -> Enter `CDDC`

4. Inspect the Packet, the flag is found in the URL!
```bash
Frame 2305: 461 bytes on wire (3688 bits), 461 bytes captured (3688 bits) on interface eth0, id 0
Ethernet II, Src: VMware_32:4d:5b (00:0c:29:32:4d:5b), Dst: VMware_eb:59:b2 (00:50:56:eb:59:b2)
Internet Protocol Version 4, Src: 192.168.64.149, Dst: 44.228.249.3
Transmission Control Protocol, Src Port: 37414, Dst Port: 80, Seq: 1998, Ack: 13572, Len: 407
    Source Port: 37414
    Destination Port: 80
    [Stream index: 1]
    [Stream Packet Number: 37]
    [Conversation completeness: Incomplete, DATA (15)]
    [TCP Segment Len: 407]
    Sequence Number: 1998    (relative sequence number)
    Sequence Number (raw): 1529094804
    [Next Sequence Number: 2405    (relative sequence number)]
    Acknowledgment Number: 13572    (relative ack number)
    Acknowledgment number (raw): 1405767478
    0101 .... = Header Length: 20 bytes (5)
    Flags: 0x018 (PSH, ACK)
    Window: 65535
    [Calculated window size: 65535]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0x28d7 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    [Timestamps]
    [SEQ/ACK analysis]
    TCP payload (407 bytes)
Hypertext Transfer Protocol
    GET /CDDC2025%7BSometimes_what_you_see_may_not_be_all_that_you_see%7D.png HTTP/1.1\r\n
    Host: testphp.vulnweb.com\r\n
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
    Accept-Language: en-US,en;q=0.5\r\n
    Accept-Encoding: gzip, deflate\r\n
    Connection: keep-alive\r\n
    Upgrade-Insecure-Requests: 1\r\n
    Priority: u=0, i\r\n
    \r\n
    [Response in frame: 2307]
    [Full request URI: http://testphp.vulnweb.com/CDDC2025%7BSometimes_what_you_see_may_not_be_all_that_you_see%7D.png]

```

* **Flag:** `CDDC2025{Sometimes_what_you_see_may_not_be_all_that_you_see}`

## Challenge 3

### Steps:

1. Navigate to the URL & Download the PCAP file 

2. Run wireshark on the pcap file 

3. Set in the filter `http.request.method == "POST"`

4. If we inspect under `HTML Form URL ENCODED`:
```bash
uname=CDDC2025%7B%7D&
pass=I_use_a_password_of_more_than_10_digits%21
```

* **Flag:** `CDDC2025{I_use_a_password_of_more_than_10_digits!}`

## Challenge 4

### Steps:

1. Navigate to the URL & Download the PCAP file 

2. Run wireshark on the pcap file 

3. Set the filter to `ICMP`

4. Inspect each packet by looking at the `data` section and view each packet -> `show packet bytes`

* **Flag:** `CDDC2025{I_Love_ICMP}`

## Challenge 5

### Steps:

1. Navigate to the URL & Download the PCAP file 

2. Run wireshark on the pcap file 

3. Set the filter to `telnet`

4. Inspect each packet, at packet 64 you will see the flag
```bash
Frame 64: 102 bytes on wire (816 bits), 102 bytes captured (816 bits) on interface lo, id 0
    Section number: 1
    Interface id: 0 (lo)
        Interface name: lo
        Interface description: Loopback
    Encapsulation type: Ethernet (1)
    Arrival Time: Apr  8, 2025 00:39:30.555471059 +08
    UTC Arrival Time: Apr  7, 2025 16:39:30.555471059 UTC
    Epoch Arrival Time: 1744043970.555471059
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.000755908 seconds]
    [Time delta from previous displayed frame: 0.000755908 seconds]
    [Time since reference or first frame: 26.149220274 seconds]
    Frame Number: 64
    Frame Length: 102 bytes (816 bits)
    Capture Length: 102 bytes (816 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp:telnet]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: 00:00:00_00:00:00 (00:00:00:00:00:00), Dst: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Destination: 00:00:00_00:00:00 (00:00:00:00:00:00)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: 00:00:00_00:00:00 (00:00:00:00:00:00)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
    [Stream index: 0]
Internet Protocol Version 4, Src: 192.168.64.149, Dst: 192.168.64.149
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 88
    Identification: 0x7b01 (31489)
    010. .... = Flags: 0x2, Don't fragment
        0... .... = Reserved bit: Not set
        .1.. .... = Don't fragment: Set
        ..0. .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 64
    Protocol: TCP (6)
    Header Checksum: 0xbd23 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 192.168.64.149
    Destination Address: 192.168.64.149
    [Stream index: 0]
Transmission Control Protocol, Src Port: 23, Dst Port: 60504, Seq: 3311, Ack: 37, Len: 36
    Source Port: 23
    Destination Port: 60504
    [Stream index: 0]
    [Stream Packet Number: 64]
    [Conversation completeness: Complete, WITH_DATA (31)]
        ..0. .... = RST: Absent
        ...1 .... = FIN: Present
        .... 1... = Data: Present
        .... .1.. = ACK: Present
        .... ..1. = SYN-ACK: Present
        .... ...1 = SYN: Present
        [Completeness Flags: ·FDASS]
    [TCP Segment Len: 36]
    Sequence Number: 3311    (relative sequence number)
    Sequence Number (raw): 3990035964
    [Next Sequence Number: 3347    (relative sequence number)]
    Acknowledgment Number: 37    (relative ack number)
    Acknowledgment number (raw): 2249578127
    1000 .... = Header Length: 32 bytes (8)
    Flags: 0x018 (PSH, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 1... = Push: Set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······AP···]
    Window: 512
    [Calculated window size: 65536]
    [Window size scaling factor: 128]
    Checksum: 0x02c6 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
        TCP Option - No-Operation (NOP)
            Kind: No-Operation (1)
        TCP Option - No-Operation (NOP)
            Kind: No-Operation (1)
        TCP Option - Timestamps: TSval 1255540897, TSecr 1255540897
            Kind: Time Stamp Option (8)
            Length: 10
            Timestamp value: 1255540897
            Timestamp echo reply: 1255540897
    [Timestamps]
        [Time since first frame in this TCP stream: 26.149220274 seconds]
        [Time since previous frame in this TCP stream: 0.000755908 seconds]
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 63]
        [The RTT to ACK the segment was: 0.000755908 seconds]
        [iRTT: 0.000016575 seconds]
        [Bytes in flight: 36]
        [Bytes sent since last PSH flag: 36]
    TCP payload (36 bytes)
Telnet
    Data: CDDC2025{Use_SSH_Instead_Of_Telnet}\n
```

* **Flag:** `CDDC2025{Use_SSH_Instead_Of_Telnet}`