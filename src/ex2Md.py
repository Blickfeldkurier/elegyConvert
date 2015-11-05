#!/usr/bin/env python

import argparse
import json
import sys

def genMarkdown(lines):
    retVal = ""
    obj = json.loads(lines)
    retVal += "# " + obj["author"] + ": " + obj["title"] +  '\n\n'
    for elem in obj['text']:
        retVal += elem + '\n\n'
    return(retVal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ex2MD.py')
    parser.add_argument("-i", "--input", dest='inpath', help="Path to input JSON file")
    parser.add_argument("-o", "--output", dest='outpath', help="Path to output file")
    args = parser.parse_args()

    retVal = ""
    if args.inpath:
        with open(args.inpath, 'r') as content:
            retVal = genMarkdown(content.read())
    else:
        retVal = genMarkdown(sys.stdin.readline)

    if(args.outpath):
        with open(args.outpath, 'w') as file:
            file.write(retVal)
    else:
        print(retVal)