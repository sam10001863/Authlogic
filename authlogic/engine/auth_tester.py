from core.logger import info, warn
from utils.http import send

COMMON_TESTS = [
    ("GET",  "/api/admin"),
    ("GET",  "/api/users"),
    ("GET",  "/api/me"),
    ("POST", "/api/admin"),
]

def test_authorization(base, token):
    headers = {"Authorization": f"Bearer {token}"}
    findings = []

    info("Testing authorization logic")

    for method, path in COMMON_TESTS:
        url = base + path
        try:
            r = send(method, url, headers=headers)
            if r.status_code == 200:
                findings.append((method, path, "Accessible"))
                warn(f"Possible broken access control → {method} {path}")
        except:
            pass

    return findings
