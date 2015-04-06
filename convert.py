# coding=utf-8

import os
import codecs
import sys

def repl(data):
    REPL = '{{replace}}'
    svg_file = open('template.svg', 'r')
    svg_data = svg_file.read()
    svg_file.close()

    total = len(data)
    i = 0
    while svg_data.find(REPL) > 0:
        print svg_data.find(REPL)
        print total, i
        i += 1
        if i <= total:
            svg_data = svg_data.replace(REPL, data[i-1], 1)
            print svg_data.find(REPL)
    return svg_data

def get_ink_path():
    USAGE = """
Usage:\n
\tpython [Inkscape executable path]
"""
    if len(sys.argv) != 2:
        print USAGE
        exit(1)
    else:
        return sys.argv[1]


if __name__ == '__main__':
    ink_path = get_ink_path()

    characters = codecs.open('characters.txt', 'r', encoding='utf-16')

    c = 0
    counter = 0

    labels = ['character', 'pinyin', 'meaning']
    data = {}

    for line in characters:
        data[labels[c]] = line.strip()
        c +=1 

        if c == 3: 
            counter +=1

            svg_code = repl([data['character'], data['character'], data['pinyin'], data['meaning']])

            out = codecs.open('out.svg', 'w', encoding='utf-16')
            out.write(svg_code)
            out.close()

            command = '%s -z -f out.svg -w 1600 -j -e images\%s' % (ink_path, str(counter) )
            command = command + '.png'

            print command

            os.system(command)        

            c = 0






