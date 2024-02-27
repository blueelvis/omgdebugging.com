+++
title = "How to check if Write Barriers have been enabled/disabled while mounting a disk in Linux"
description = ""
date = 2018-05-06T12:36:43
updated = 2019-01-23T20:57:46
draft = false
slug = "how-to-check-if-write-barriers-have-been-enabled-disabled-while-mounting-a-disk-in-linux"
aliases = ['2018/05/06/how-to-check-if-write-barriers-have-been-enabled-disabled-while-mounting-a-disk-in-linux/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["red hat", "Azure", "linux", "write barrier", "microsoft"]
+++


Some time back, I had to work with Red Hat Enterprise Linux 6.9 and as per 
Microsoft's documents on optimization for Linux Virtual Machines
[https://docs.microsoft.com/en-us/azure/virtual-machines/linux/premium-storage#premium-storage-for-linux-vms]
, I had to ensure that Write Barriers on the disk(s) was disabled.

Red Hat says
[https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-writebarriers] 
that the benefits which are provided by the Write Barriers compensate for the
minor performance degradation but we wanted to ensure that we got all the juice
available from those premium SSDs.

By default, Write Barriers are enabled for all partition mounts in the Red Hat
Enterprise Linux. So, whenever you mount a disk in RHEL, you will see something
like this in /var/log/messages -

==May 6th 08:35:10 BLUEELVIS kernel: EXT4-fs (sdc1): mounted filesystem with ordered data mode. Opts:==


There is just a single line stating that partition was mounted successfully.

If you want to disable Write Barriers, you need to have something like below in
your /etc/fstab --

> UUID=b1119318-0ee8-4f1b-8e57-993832fea324 /home ext4 defaults,barrier=0 0 0


Now, when you run sudo mount -a, you will see the following entry in 
/var/log/messages -

May 6th 08:35:10 BLUEELVIS kernel: EXT4-fs (sdc1): barriers disabled
May 6th 08:35:10 BLUEELVIS kernel: EXT4-fs (sdc1): mounted filesystem with ordered data mode. Opts: