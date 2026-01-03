def report(findings):
    print("\nFindings:")
    for f in findings:
        print(f" - {f[0]} {f[1]} → {f[2]}")
