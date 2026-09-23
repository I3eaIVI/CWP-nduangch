#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) <= 2:
        print("none")
    else:
        print(len(re.findall(sys.argv[1],sys.argv[2])))
main()