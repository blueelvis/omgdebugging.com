+++
title = "Certbot --dry-run with NGINX fails with Invalid PID"
description = ""
date = 2018-04-30T07:36:34
updated = 2018-08-22T08:21:16
draft = false
slug = "certbot-dry-run-with-nginx-fails-with-invalid-pid"
aliases = ['2018/04/30/certbot-dry-run-with-nginx-fails-with-invalid-pid/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I have been recently trying to figure out why LetsEncyrpt's Certbot was failing
to renew the SSL certificates automatically.

I ran the following command - certbot renew --nginx --dry-run

After running the command, I got the following error at the start of the process
-

> root@blueelvis:/etc/cron.d# certbot renew --nginx --dry-run
Saving debug log to /var/log/letsencrypt/letsencrypt.log


> 
--------------------------------------------------------------------------------


> Processing /etc/letsencrypt/renewal/blueelvis.eastus2.cloudapp.azure.com.conf


> 
--------------------------------------------------------------------------------


> Cert is due for renewal, auto-renewing...


> Plugins selected: Authenticator nginx, Installer nginx


> Running pre-hook command: service nginx stop


> Renewing an existing certificate


> Performing the following challenges:


> tls-sni-01 challenge for blueelvis.eastus2.cloudapp.azure.com


> nginx: [error] invalid PID number "" in "/run/nginx.pid"


> Waiting for verification...


> Cleaning up challenges


> Running post-hook command: service nginx start


> Hook command "service nginx start" returned error code 1


> Error output from service:


> Job for nginx.service failed because the control process exited with error code.
See


> "systemctl status nginx.service" and "journalctl -xe" for details.


The command kept failing and after that, the NGINX process was left in a hung up
state where doing a service nginx restart failed with the following error -

> Apr 30 07:29:30 blueelvis nginx[37808]: nginx: [emerg] bind() to [::]:80 failed
(98: Address already in use)


> Apr 30 07:29:30 blueelvis nginx[37808]: nginx: [emerg] bind() to 0.0.0.0:443
failed (98: Address already in use)


> Apr 30 07:29:30 blueelvis nginx[37808]: nginx: [emerg] bind() to 0.0.0.0:80
failed (98: Address already in use)


> Apr 30 07:29:30 blueelvis nginx[37808]: nginx: [emerg] bind() to [::]:80 failed
(98: Address already in use)


> Apr 30 07:29:30 blueelvis nginx[37808]: nginx: [emerg] bind() to 0.0.0.0:443
failed (98: Address already in use)


> Apr 30 07:29:31 blueelvis nginx[37808]: nginx: [emerg] still could not bind()


> Apr 30 07:29:31 blueelvis systemd[1]: nginx.service: Control process exited,
code=exited status=1


If you do a ps aux | grep nginx, you will notice several NGINX processes still
running. Kill them by running kill Process_ID where Process_ID is the PID's you
get from running ps aux | grep nginx. After killing all these processes, ensure
that you run service nginx start before proceeding ahead.

The problem in this case was that Certbot was running the Pre hook at the start
which for NGINX configurations is generally service nginx stop. Since NGINX was
stopped by Certbot at the start, it was not able to read the file /run/nginx.pid 
which is generated for the master NGINX process while running.

The fix for this was simple after realizing this. Follow the below steps -

 1. cd /etc/letsencrypt/renewal
 2. nano/vim and edit the domain file in there.
 3. Find the line where it is written pre_hook = service nginx stop
 4. Change that line to this #pre_hook = service nginx stop. In other words,
    just comment it out.
 5. Now, again find the line where it is written post_hook = service nginx start
 6. Change that line to this post_hook = service nginx restart

And voila! Till next time...