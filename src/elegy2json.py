#!/usr/bin/env python
import argparse
import json
from bs4 import BeautifulSoup

def parseElegy(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
        soup = BeautifulSoup(content)
        fulltext = soup.find("div", {"id": "fulltext"})
        story = dict()
        story['title'] = fulltext.find("span", {"id": "fulltextTitle"}).string
        story['author'] = fulltext.find("span", {"id": "fulltextAuthor"}).string.split(' ')[1]
        textdiv = fulltext.find("div")
        textelem = []
        for elem in textdiv.find_all('p'):
            textelem.append(elem.string)
        story['text'] = textelem
        return(json.dumps(story))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='elegy2json.py')
    parser.add_argument('filepath', help='Path to a elegy html file')
    args = parser.parse_args()
    print(parseElegy(args.filepath))
