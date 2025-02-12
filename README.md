# Compiled list of DNS over HTTPS server domains published on curl wiki

![Weekly update](https://github.com/krsmanovic/dns-doh-blocklist/actions/workflows/sched-scrape-publish.yml/badge.svg)

This repository is hosting compiled list of DoH server domains published on curl wiki which can be used by DNS sinkhole servers.

Scrape source is curl wiki document located at https://github.com/curl/curl/wiki/DNS-over-HTTPS.

Check for updates is performed weekly.

> [!IMPORTANT]  
> You would want this list in case you are hosting your own network-wide blocker. This list will help prevent clients in your local network from overriding your local "clear" DNS.  
>
> Malware and botnets can exploit DoH to receive commands or funnel data out, bypassing the traditional DNS-based detection mechanisms. This freedom to communicate via DoH allows malware to evolve in response to defensive measures, download updates, or propagate across the network, thereby extending its presence and amplifying its effects.  
