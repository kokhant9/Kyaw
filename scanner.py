import socket
import threading

target = "8.8.8.8"

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN ✅")
    s.close()

print(f"Starting Multi-threaded Scan on {target}...")

# Port 1 ကနေ 500 အထိ တစ်ပြိုင်တည်း စစ်မယ်
for port in range(1, 501):
    thread = threading.Thread(target=port_scan, args=(port,))
    thread.start()

