#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        if len(re.findall("z",sys.argv[1])) == 0:
            print("none")
        else:
            print(len(re.findall("z",sys.argv[1])) * "z")
main()