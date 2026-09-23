#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        print(sys.argv[1].lower())
main()