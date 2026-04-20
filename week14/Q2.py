def check_headers(url):
    try:
        response = urllib.request.urlopen(url)
        headers = dict(response.headers)
        results = []

        for name in REQUIRED_HEADERS:
            if name in headers:
                results.append({
                    "header": name,
                    "present": True,
                    "value": headers[name]
                })
            else:
                results.append({
                    "header": name,
                    "present": False,
                    "value": "MISSING"
                })

        return results
    except Exception:
        return []


def generate_report(url, results):
    print(f"  URL: {url}")
    missing_count = 0

    for result in results:
        if result["present"]:
            print(f"  ✓ {result['header']}: {result['value']}")
        else:
            print(f"  ✗ {result['header']}: MISSING — {REQUIRED_HEADERS[result['header']]}")
            missing_count += 1

    print(f"  Missing {missing_count} of {len(results)} security headers!")