def make_request(url):
    try:
        response = urllib.request.urlopen(url)
        body = response.read().decode()
        return {
            "status": response.status,
            "headers": dict(response.headers),
            "body": body
        }
    except Exception as e:
        return {
            "status": 0,
            "headers": {},
            "body": "",
            "error": str(e)
        }


def parse_json(body):
    try:
        return json.loads(body)
    except ValueError:
        return None


def check_api_info(response):
    findings = []
    headers = response.get("headers", {})

    if "Server" in headers:
        findings.append(f"Server version exposed: {headers['Server']}")

    if "X-Powered-By" in headers:
        findings.append(f"Technology exposed: {headers['X-Powered-By']}")

    if headers.get("Access-Control-Allow-Origin") == "*":
        findings.append("CORS: open to all origins")

    return findings