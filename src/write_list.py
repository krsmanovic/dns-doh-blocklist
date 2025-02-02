#!/usr/bin/env python

import os
from string import Template
from datetime import datetime

header_file = './header.tpl'
output_file = '../doh_blocklist.txt'
path_tmp = './doh_tmp.txt'
path_hash = '../hash'

# Templating header
header_values = {
    'time': datetime.utcnow().isoformat()[:-3]+'Z',
    'version': datetime.now().strftime("%Y-%m-%d"),
}
with open(header_file, 'r') as f:
    src = Template(f.read())
    header = src.substitute(header_values)

# Writing to a file
with open(output_file, 'w') as f:
    f.writelines(header)
with open(output_file, 'a') as f:
    with open(path_tmp) as innerfile:
        for line in innerfile:
            f.write(line)

# Write hash
with open(path_hash, 'w') as f:
    f.write(os.getenv('HASH_TEMP', ''))
