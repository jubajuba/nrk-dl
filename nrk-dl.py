#!/usr/bin/env python3

import re
import urllib.request
import urllib.error

url = 'https://tv.nrk.no/serie/thunderbirds'
outputfile = 'outfile.txt'

with urllib.request.urlopen(url) as response:
    with open(outputfile, 'w') as output:
            output.write(str(response.read()))
