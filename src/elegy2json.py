#!/usr/bin/env python
import argparse

def parseElegy(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
        print content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='elegy2json.py')
    parser.add_argument('filepath', help='Path to a elegy html file')
    args = parser.parse_args()
    parseElegy(args.filepath)
