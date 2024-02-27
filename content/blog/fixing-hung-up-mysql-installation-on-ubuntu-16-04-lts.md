+++
title = "Fixing Hung Up MySQL installation on Ubuntu 16.04 LTS"
description = ""
date = 2016-09-04T13:29:58
updated = 2018-08-22T08:21:16
draft = false
slug = "fixing-hung-up-mysql-installation-on-ubuntu-16-04-lts"
aliases = ['2016/09/04/fixing-hung-up-mysql-installation-on-ubuntu-16-04-lts/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Few days back, I was asked by Tushar Mishra [https://github.com/tmess567] if we
both could host his blog [http://blog.tusharmishra.in/] alongside my blog
[http://omgdebugging.com]. His blog is based on WordPress platform which meant
repeating the whole process (OMGDebugging.com was earlier running on WordPress
as well) of installing WordPress along with it's dependencies like MySQL, PHP
etc.

The installation process was butter smooth and we got the blog up and running
fairly easily. The blog was running perfect but after a reboot, when I ran 
apt-get update , I got the following error -

E: dpkg was interrupted, you must manually run 'sudo dpkg --configure -a' to
correct the problem.

Hmm strange. That was not supposed to happen. On running the above command, I
found that the MySQL server is causing all this trouble. After the above command
went ahead a bit, it got stuck at the following line -

Setting up mysql-server-5.7 (5.7.13-0ubuntu0.16.04.2) ... Renaming removed
key_buffer and myisam-recover options (if present)

As per the above line, the MYSQL Post Installation script replaced the 
key_buffer and myisam-recover keywords in the MYSQL configuration file (my.cnf)
since they are deprecated.

On searching around, I found that this was a known bug since from version 5.7,
several of the deprecated settings (inside my.cnf) have been removed. Also,
there are bugs with the installation script & invoke-rc.d . You can find more
information over here - 
https://bugs.launchpad.net/ubuntu/+source/mysql-5.7/+bug/1571865

But, still the problem was there. One of the person on the above link mentioned
that killing the spawned MYSQL processes would make the install script proceed
ahead. So, I ran ps aux | grep mysql which gave me the following output -

> root 3830 0.0 0.9 20888 4832 pts/0 S+ 09:21 0:00 dpkg --configure
mysql-server-5.7


> root 3831 0.7 3.4 62828 17272 pts/0 S+ 09:21 0:00 /usr/bin/perl -w
/usr/share/debconf/frontend /var/lib/dpkg/info/mysql-server-5.7.postinst
configure


> root 3840 0.0 0.6 12972 3316 pts/0 S+ 09:21 0:00 /bin/bash
/var/lib/dpkg/info/mysql-server-5.7.postinst configure


> mysql 4063 0.6 35.0 1141400 175376 pts/0 Sl+ 09:21 0:00 mysqld --user=mysql
--init-file=/var/lib/mysql-files/tmp.4E2Sdu9DQ3
--socket=/tmp/tmp.CInFSccVPv/mysqld.sock
--pid-file=/tmp/tmp.CInFSccVPv/mysqld.pid


> root 4093 0.0 0.2 14512 1032 pts/2 S+ 09:22 0:00 grep --color=auto mysql


I killed the 2 highlighted MYSQL processes (I killed them randomly and it worked
the first time :0) and the setup proceeded ahead normally and completed
successfully.

==Motto of the story = Always read comments till the end ;) ==