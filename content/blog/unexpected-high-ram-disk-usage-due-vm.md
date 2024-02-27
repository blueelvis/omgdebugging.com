+++
title = "The Unexpected High RAM & Disk Usage Due To VM"
description = ""
date = 2014-09-07T00:38:02
updated = 2018-08-22T08:21:16
draft = false
slug = "unexpected-high-ram-disk-usage-due-vm"
aliases = ['2014/09/07/unexpected-high-ram-disk-usage-due-vm/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Disk", "Hyper-V", "RAM", "Resource Monitor", "Task Manager", "Virtual Machine"]
+++


Recently, before joining the college, I started up my laptop and started playing
DOTA 2. The game started fine but to my horror, the loading of the maps and all
the elements took around a minute and when I joined the actual game had already
started. I thought that this was just a chance so I simply restarted my laptop
but the issue was still there. For a few days, I started thinking that my ISP is
having issues.

So one fine day, I opened the Task Manager while running Chrome & Spotify and I
saw the following :-



[![Loading](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/High-RAM.png?resize=665%2C607)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/High-RAM.png)See
how there is 100% Disk Usage by the System and RAM is above 72%Now, a question
might arise here that why is the Disk Usage so high and the RAM is above 70%?
This happens due to a mechanism of the Windows Operating System known as Paging.
I won’t go too much deep what is Paging but to explain and understand it better,
the mechanism allows the Windows Operating System to utilize the Hard Disk as
the Memory for operations (RAM). This mechanism is automatically triggered which
in my case is when the RAM Usage goes above 70%. Now, since the Hard Disk is
very slow as compared to the RAM, the computer starts behaving slow and feels
sluggish.So, I finally sat down and thought of seeing what is causing this much
high usage of Memory and Disk as my laptop is having 8GB of RAM which is more
than enough for normal operations. I first checked for Malware using Windows
Defender to make sure that this was not caused by some Malware. Once it was
clear, I started looking at the Resource Monitor which is the next step of
troubleshooting problems after Task Manager for Intermediate Users. On
re-arranging the Disk activity according in Descending Order, I found the below
entry :-

[![Loading...](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Resource-Monitor-1024x505.png?resize=730%2C360)](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Resource-Monitor.png)Notice
how there is Disk Activity on the Virtual Hard Disks Folder which is selected?
Hmm, the Disk is serving to the Virtual Hard Disk for a Virtual Machine in Hyper
V. That was strange as I did not start any Virtual Machine on booting into
Windows. So, I fired up Hyper-V Manager and to my surprise a Virtual Machine was
running and utilizing 3GB of RAM as you can see in the below screenshot :-

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Hyper-V-VM-Running-1024x545.png?resize=730%2C388)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Hyper-V-VM-Running.png):O
So this was eating up my RAM I Turned Off the Virtual Machine and the RAM Usage
came back to 25% and the constant Disk Activity fell to 1%. Now, the question
was How come the Virtual Machine started running automatically on Windows
Startup? I opened the Settings for the Virtual Machine (Right Click on the VM in
Hyper V Manager –> Settings) and I reached to the Automatic Start Action Tab
which could be seen below and it was set to Start the VM if the Hyper V Service
was stopped which happens during Shut Down and the VM was running at that time.
[![Loading...](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/VM-Settings.png?resize=730%2C696)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/VM-Settings.png)Really
Hyper V?So, I selected the Nothing radio button, clicked on Apply and hoped that
the issue would not come back on reboot. So, I rebooted the machine and to my
joy the problem was gone. The RAM & Disk Usage were at 20% and 1% respectively
and DOTA 2 started loading maps within 5 seconds. The option for Automatic
Startup should be enabled only in Enterprise Environments as I do not see any
practical usage in the Home environment.

In case of any questions, feel free to post in the comments section ^_^.