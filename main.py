import platform
import socket

def main():
    print("hello from your rpi")
    print(f"running on {platform.node()}")
    print(f"platform: {platform.platform()}")
    print(f"python version: {platform.python_version()}")
    print(f"socket: {socket.gethostname()}")
    
if __name__ == "__main__":
    main()