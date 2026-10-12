"""Extract FRED's error explanation without logging request URLs.
Use with an existing requests.Response; this module makes no network calls.
Inspect results privately before sharing. Redaction is not a universal secret detector.
"""
import json
import re
import xml.etree.ElementTree as ET
from urllib.parse import quote

def safe_fred_error(response, api_key=""):
    try:
        data = response.json()
        message = data.get("error_message", "") if isinstance(data, dict) else ""
    except ValueError:
        try:
            message = ET.fromstring(response.text).attrib.get("message", "")
        except ET.ParseError:
            message = ""
    message = str(message or "No FRED error message; inspect response privately.")
    if api_key:
        for secret in (api_key, quote(api_key, safe="")):
            message = message.replace(secret, "[redacted]")
    return re.sub(r"\b[a-zA-Z0-9]{32}\b", "[redacted]", message)[:500]

# Example inside the existing worker, after its existing request and before
# raise_for_status(). Rename r to the existing response variable:
# import os
# print("FRED status:", r.status_code)
# print("FRED error:", safe_fred_error(r, os.getenv("FRED_API_KEY", "").strip()))

def self_test():
    class Response:
        def __init__(self, text):
            self.text = text
        def json(self):
            return json.loads(self.text)
    key = "FAKE-KEY/with space"
    cases = [
        ("json", '{"error_message":"Invalid series_id"}', "Invalid series_id"),
        ("xml", '<error code="400" message="Invalid api_key"/>', "Invalid api_key"),
        ("html", "<html>bad gateway</html>", "No FRED error message; inspect response privately."),
        ("malformed", "not json or XML", "No FRED error message; inspect response privately."),
        ("raw key", json.dumps({"error_message": "Rejected " + key}), "Rejected [redacted]"),
        ("encoded key", json.dumps({"error_message": "Rejected " + quote(key, safe="")}), "Rejected [redacted]"),
        ("fred key", json.dumps({"error_message": "Rejected " + "a"*32}), "Rejected [redacted]"),
        ("json list", "[]", "No FRED error message; inspect response privately."),
    ]
    for name, body, expected in cases:
        assert safe_fred_error(Response(body), key) == expected, name
        print(name + ": PASS")
    print("8 synthetic response cases passed; no external API calls.")

if __name__ == "__main__":
    self_test()
