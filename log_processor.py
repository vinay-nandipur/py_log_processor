#!/usr/bin/env python
import os
import requests


url = 'http://opensource.indeedeng.io/imhotep/files/nasa_19950630.22-19950728.12.tsv.gz'
base_name = os.path.basename(url)
r = requests.get(url, stream=True)
with open(base_name, 'wb') as f:
    for chunk in r.raw.stream(1024, decode_content=False):
        if chunk:
            f.write(chunk)
