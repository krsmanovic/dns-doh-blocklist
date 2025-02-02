#!/usr/bin/env python

import requests
from requests.adapters import HTTPAdapter, Retry
from bs4 import BeautifulSoup
from urllib.parse import urlparse

curl_wiki_url = 'https://github.com/curl/curl/wiki/DNS-over-HTTPS'
output_tmp = 'doh_tmp.txt'
doh_blocklist = []

# Requesting the HTML file
session = requests.Session()
retry_strategy = Retry(
    total=5,
    backoff_factor=2,
)
session.mount('http://', HTTPAdapter(max_retries=retry_strategy))
response = session.get(curl_wiki_url)

# Parsing the HTML file
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.select_one('h1:-soup-contains("Publicly available servers")').find_next('table')
if table in (None, ""):
    sys.exit('Error: table is empty.')
for dns_data in table.find_all('tbody'):
    rows = dns_data.find_all('tr')
for row in rows:
    base_url_column = row.find_all('td')[1].text.replace(' ', '\n')
    if 'https' in base_url_column:
        who_runs_it_column = row.find_all('td')[0].text.strip()
        doh_blocklist.append('\n# ' + who_runs_it_column + '\n')
    links = [elem['href'] for elem in row.find_all('td')[1].select('a')]
    old_key = ''
    for link in links:
        fqdn = urlparse(link).netloc.strip()
        if fqdn != old_key:
            doh_blocklist.append(fqdn + '\n')
            old_key = fqdn

# Writing temporary file
with open(output_tmp, 'w') as f:
    f.writelines(doh_blocklist)
