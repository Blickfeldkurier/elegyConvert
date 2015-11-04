# Elegy for a Dead World - Export Tools

Tools to generate various text formats from the Elegy for a dead worlds export.
Currently I just try to get the Title, Author and the fulltext.

## Requirements
  
  * Python 
  * Beautiful Soup

## Export
    
The export tool works in two parts. First there is the eledgy2json.py.
This Program takes an exported index.html file and dumps a JSON onbject to SDTOUT.
The second Part are the ex2Something.py scripts. Those read JSON from STDIN and save 
a File to a given location.

### Examples

Export to latex.
    
    ./elegy2json.py ~/Elegy/TheRaven/index.html | ./ex2Tex.py raven.tex 

## Development
Currently the elegy2json script returns a simple json object with the following structure

    { title: <Title>,
        author: <Author>,
        text: {
            part: <Text>
            ...
        }
    }