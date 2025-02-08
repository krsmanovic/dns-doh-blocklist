# DNS block list for well known DNS over HTTPS domains

![Weekly update](https://github.com/krsmanovic/dns-doh-blocklist/actions/workflows/sched-scrape-publish.yml/badge.svg)

This repository is hosting compiled list of well known DoH services which can be used with DNS sinkhole servers.

Scrape souce is cURL wiki located at https://github.com/curl/curl/wiki/DNS-over-HTTPS. Check for updates is automatic on weekly basis.

> [!IMPORTANT]  
> You would want this list in case you are hosting your own network-wide blocker. This list will help prevent clients in your local network from overriding your local DNS.  
> Use this in combination with other DOh and DoT block lists, because my aim is not to cover ALL servers publicly available on the Internet.
