#!/usr/bin/env python

#Import Python Libraries
import os
import requests
import gzip
import shutil
import sys


# Download log archive
url = 'http://opensource.indeedeng.io/imhotep/files/nasa_19950630.22-19950728.12.tsv.gz'
base_name = os.path.basename(url)
r = requests.get(url, stream=True)
with open(base_name, 'wb') as f:
    for chunk in r.raw.stream(1024, decode_content=False):
        if chunk:
            f.write(chunk)


# get filename without extension from the archive file
file_extns = base_name.split(".")
new_filename1 = str(file_extns[-5])
new_filename2 = str(file_extns[-4])
new_filename3 = str(file_extns[-3])
new_filename4 = (".".join([new_filename1,new_filename2,new_filename3]))
new_filename = new_filename4 + '.txt'


#Extract log archive
with gzip.open(base_name, 'rb') as f_in:
    with open(new_filename, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


#Define functions

def formated_data(line):
    split_line = line.split()
    return {'remote_host': split_line[0],
            'method': split_line[3],
            'bytes': split_line[6],
    }

def final_report(logfile):
    for line in logfile:
        line_dict = formated_data(line)
        print(line_dict)

if __name__ == "__main__":
    try:
        infile = open(new_filename, 'r', encoding='utf-8', errors='ignore')
    except IOError:
        print ("You must specify a valid file to parse")
        sys.exit(1)
    log_report = final_report(infile)
    print (log_report)
    infile.close()
