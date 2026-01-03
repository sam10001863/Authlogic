from core.logger import info, warn
from engine.auth_tester import test_authorization

def run():
    base = input("Target base URL (https://example.com): ").strip()
    token = input("User access token (JWT/session): ").strip()

    if not base or not token:
        warn("Missing required input")
        return

    findings = test_authorization(base, token)

    if not findings:
        info("No obvious authorization flaws detected")
    else:
        info("Critical authorization issues detected")
