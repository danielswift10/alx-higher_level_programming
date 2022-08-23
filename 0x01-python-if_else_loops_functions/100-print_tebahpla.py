#!/usr/bin/python3
for alphabet in reversed(range(97, 123)):
    print(f"{(alphabet if (alphabet % 2 == 0) else (alphabet - 32)):c}", end='')
