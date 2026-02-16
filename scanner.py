import socket

target = "8.8.8.8"
ports = [21, 22, 80, 443]

print(f"Scanning & Grabbing Banners on {target}...")

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        
        # Banner ကို လှမ်းတောင်းကြည့်မယ်
        s.send(b'Hello\r\n')
        banner = s.recv(1024).decode().strip()
        
        print(f"Port {port}: OPEN ✅ | Banner: {banner}")
    except:
        print(f"Port {port}: OPEN ✅ | Banner: No info (Firewalled?)")
    finally:
        s.close()

print("Mission Finished!")

