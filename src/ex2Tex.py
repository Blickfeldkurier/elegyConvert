#!/usr/bin/env python

import argparse
import json
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ex2Tex.py')
    parser.add_argument("-o", "--output", dest='outpath', help="Path to output file")
    args = parser.parse_args()
    print("foo")