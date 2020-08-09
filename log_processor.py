#!/usr/bin/env python
import os
import requests
import gzip
import shutil

# Download log archive
url = 'http://opensource.indeedeng.io/imhotep/files/nasa_19950630.22-19950728.12.tsv.gz'
base_name = os.path.basename(url)
"""
r = requests.get(url, stream=True)
with open(base_name, 'wb') as f:
    for chunk in r.raw.stream(1024, decode_content=False):
        if chunk:
            f.write(chunk)
"""            

# get filename without extension from the archive file
file_extns = base_name.split(".")
new_filename1 = str(file_extns[-5])
new_filename2 = str(file_extns[-4])
new_filename3 = str(file_extns[-3])
new_filename = (".".join([new_filename1,new_filename2,new_filename3]))

#Extract log archive
with gzip.open(base_name, 'rb') as f_in:
    with open(new_filename+'.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
