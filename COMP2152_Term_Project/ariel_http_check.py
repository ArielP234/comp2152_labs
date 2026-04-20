Author: Ariel
Vulnerability Name: Missing HTTPS Enforcement
Target Subdomain: blog.0x10.cloud
Description:
This script checks whether the target stays on HTTP instead of redirecting to HTTPS.
If it remains on HTTP, traffic may be sent without encryption.
"""

import urllib.request
import urllib.error


TARGET_URL = "http://blog.0x10.cloud"


def main() -> None:
    """Request the target URL and report whether HTTPS is enforced."""
    try:
        response = urllib.request.urlopen(TARGET_URL, timeout=5)
        final_url = response.geturl()

        print(f"Requested URL: {TARGET_URL}")
        print(f"Final URL: {final_url}")
        print(f"HTTP Status: {response.status}")

        if final_url.startswith("http://"):
            print("VULNERABILITY: HTTPS is not enforced.")
            print("Security Risk: Traffic may be transmitted in cleartext.")
        else:
            print("No issue detected: request ended on HTTPS.")

    except urllib.error.URLError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()