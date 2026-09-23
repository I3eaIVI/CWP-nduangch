#!/usr/bin/env python3
import sys

def main():
    x = []
    if len(sys.argv) <= 1:
        print("none")
    else:
        num = range(int(sys.argv[1]),int(sys.argv[2]) + 1)
        for i in num:
            x.append(i)
        print(x)
main()