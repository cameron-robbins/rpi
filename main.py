import platform
import socket

def main():
    print("hello from your rpi")
    print(f"running on {platform.node()}")
    print(f"platform: {platform.platform()}")
    print(f"python version: {platform.python_version()}")
    print(f"socket: {socket.gethostname()}")
    print(f"ip address: {socket.gethostbyname(socket.gethostname())}")
    print(f"mac address: {':'.join(hex(ord(c))[2:] for c in uuid.getnode().to_bytes(6, 'little'))}")
    
if __name__ == "__main__":
    main()