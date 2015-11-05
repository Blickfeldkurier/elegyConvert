#!/usr/bin/env python

import argparse
import json
import sys

def genMarkdown(lines, yfonts):
    retVal = ""

    obj = json.loads(lines)

    header = "\\documentclass[a4paper,10pt, twocolumn]{article}\n"
    if yfonts:
        header +="\\usepackage{yfonts}\n"

    header +="\\author{" + obj["author"] + "}\n"
    header +="\\title{" + obj["title"] + "}\n"
    header +="\\begin{document}\n"

    if yfonts:
        header +="\\frakfamily\\large\\fraklines\n"

    header +="\\maketitle\n"
    retVal += header

    for elem in obj['text']:
        if yfonts:
            retVal += "\\yinipar{" + elem[0] + "}" + elem[1:] + '\n\n'
        else:
            retVal += elem  + '\n\n'

    retVal += "\\end{document}\n"
    return(retVal)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ex2MD.py')
    parser.add_argument("-i", "--input", dest='inpath', help="Path to input JSON file")
    parser.add_argument("-o", "--output", dest='outpath', help="Path to output file")
    parser.add_argument("-y", "--yfonts", dest='yfonts', action='store_true', default=False, help="Use YFonts")
    args = parser.parse_args()

    if args.inpath:
        with open(args.inpath, 'r') as content:
            retVal = genMarkdown(content.read(),args.yfonts)
    else:
        retVal = genMarkdown(sys.stdin.readline(),args.yfonts)

    if(args.outpath):
        with open(args.outpath, 'w') as file:
            file.write(retVal)
    else:
        print(retVal)