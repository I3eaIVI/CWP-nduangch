#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) <= 1:
        print("none")
    else:
        text = input("What was the parameter? " )
        if text == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")

main()