# Compiled list of DNS over HTTPS server domains published on cURL wiki

![Weekly update](https://github.com/krsmanovic/dns-doh-blocklist/actions/workflows/sched-scrape-publish.yml/badge.svg)

This repository is hosting compiled list of DoH server domains published on cURL wiki which can be used by DNS sinkhole servers.

Scrape souce is cURL wiki located at https://github.com/curl/curl/wiki/DNS-over-HTTPS.

Check for updates is performed weekly.

> [!IMPORTANT]  
> You would want this list in case you are hosting your own network-wide blocker. This list will help prevent clients in your local network from overriding your local "clear" DNS.  
>
> Use this in combination with other DoH and DoT block lists. My aim is not to cover all publicly available DoH/DoT servers on the Internet, just the ones covered in the scrape source.  
