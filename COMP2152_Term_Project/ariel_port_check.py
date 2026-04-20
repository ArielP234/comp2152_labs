"""
Author: Ariel
Vulnerability Name: Insecure Service Port Exposed
Target Subdomain: telnet.0x10.cloud
Description:
This script checks whether a specific insecure service port is reachable.
An exposed insecure service may allow unencrypted communication.
"""

import socket


TARGET_HOST = "telnet.0x10.cloud"
TARGET_PORT = 2323
TIMEOUT_SECONDS = 3


def main() -> None:
    """Attempt a TCP connection to a single target port and report the result."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT_SECONDS)

    try:
        print(f"Host: {TARGET_HOST}")
        print(f"Port: {TARGET_PORT}")

        result = sock.connect_ex((TARGET_HOST, TARGET_PORT))

        if result == 0:
            print(f"VULNERABILITY: Port {TARGET_PORT} is open on {TARGET_HOST}.")
            print("Security Risk: Insecure services may allow cleartext communication.")
        else:
            print(f"No issue detected: port {TARGET_PORT} appears closed or filtered.")

    except socket.gaierror as e:
        print(f"DNS error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    main()