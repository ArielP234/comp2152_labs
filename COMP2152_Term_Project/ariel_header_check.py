"""
Author: Ariel
Vulnerability Name: Information Disclosure in HTTP Headers
Target Subdomain: api.0x10.cloud
Description:
This script inspects response headers for exposed technology information.
Revealing server or backend details can help attackers identify likely weaknesses.
"""

import urllib.request
import urllib.error


TARGET_URL = "http://api.0x10.cloud"


def main() -> None:
    """Read HTTP headers and report obvious information disclosure."""
    try:
        response = urllib.request.urlopen(TARGET_URL, timeout=5)
        headers = dict(response.headers)

        server = headers.get("Server", "Not disclosed")
        powered_by = headers.get("X-Powered-By", "Not disclosed")

        print(f"Requested URL: {TARGET_URL}")
        print(f"HTTP Status: {response.status}")
        print(f"Server: {server}")
        print(f"X-Powered-By: {powered_by}")

        found_issue = False

        if server != "Not disclosed":
            found_issue = True
            print("VULNERABILITY: Server header exposes implementation details.")
            print("Security Risk: Exposed version or server details can help targeted attacks.")

        if powered_by != "Not disclosed":
            found_issue = True
            print("VULNERABILITY: X-Powered-By header exposes backend technology.")
            print("Security Risk: Attackers can use this to profile the application stack.")

        if not found_issue:
            print("No obvious header disclosure detected.")

    except urllib.error.URLError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()