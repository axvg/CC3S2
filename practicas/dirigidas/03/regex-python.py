#!/usr/bin/env python3
import re
import sys

texto = sys.stdin.read()
pat = re.compile(r'([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+)')
for email in set(pat.findall(texto)):
    print(email)
