---
title: "Uninstalling Pi-Hole on Ubuntu 16.04 with OpenVPN"
date: 2018-07-17T11:51:41+00:00
lastmod: 2018-08-22T08:21:16+00:00
---

You might be aware of Pi-Hole to be a advertisement blocking software which works at the DNS level. The way it works is that, it runs its own DNS server and blocking services. When you configure Pihole during installation, it will setup `dnsmasq` and configure it so that all DNS queries go through it instead of directly going to the nameservers. It uses blocklists to block the DNS queries so whenever a DNS query comes, Pihole will check its blocklists and if it finds an entry, it will reply back with the address of your choice (In my case, 10.8.0.1). So, 10.8.0.1 was the DNS server when the machine was connected with OpenVPN. This VPN server was also hosting a website with NGINX.

I had followed a guide from [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-block-advertisements-at-the-dns-level-using-pi-hole-and-openvpn-on-ubuntu-16-04#step-4-%E2%80%94-testing-dns-filtering) to setup Pihole and redirect all of my VPN traffic through it.

After some time of using Pihole (After some time, I totally forgot that this was setup as well), I noticed few issues -

- HTTPS warnings regarding certificate mismatch were given to several websites. For example, if I tried browsing a website like `stats.wp.com`, I would get a certificate for `abc.com` (Just an example)
- Websites did not work properly like below and Chrome Dev Tools showed several errors -

![](/content/images/2018/07/Buggy-Website.PNG)

After doing some initial searching, performing `nslookup`(s) on both the client and server, I established that this issue was not because of OpenVPN but something concerned with DNS. Eventually, I found that Pihole is the one responsible for all this mess.

![](/content/images/2018/07/dnsmasq.gif)

Follow the below procedure to uninstall Pi-hole properly -

- Make a backup of the file located at `/etc/dhcpcd.conf`
- Now, edit the file and locate the section as below

> > interface tun0

static ip_address=10.8.0.1/24

static routers=128.199.192.1

static `domain_name_servers=127.0.0.1`

- Replace the highlighted portion with `domain_name_servers=1.1.1.1 1.0.0.1`. This line contains the IP addresses of the DNS servers (I am using Cloudflare's DNS) which would be used to lookup domains for that interface.
- Now, we need to remove the entries from the firewall `ufw`. To get a list of all the rules present, run `ufw status numbered`. In my case, I got the following list -

![](/content/images/2018/07/ufw-list.PNG)

Ports `80` & `1234` were for the Pihole Admin interface.
- Remove the rules by typing in `ufw delete [RULE_NUMBER]` where [RULE_NUMBER] is the number of the rule as shown above.
- Now, type in `pihole uninstall`. Press `y` at the prompt to start uninstallation.
- It will ask you to uninstall the packages which were installed by Pihole. I recommend pressing `N` at this prompt to keep all the packages if you don't know.
- Now, remove `dnsmasq` by typing in `apt-get remove dnsmasq`
- Edit the file at `/etc/openvpn/server.conf` and locate the entry like `push "dhcp-option DNS 10.8.0.1"`. You need to replace the DNS server in this line with an actual DNS server like `1.1.1.1` or `8.8.8.8`
- Reboot the system by typing in `reboot`

This should resolve the DNS issues and restore back OpenVPN connectivity. But, yes cheers to Pihole team for building out this product!