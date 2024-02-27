+++
title = "Fix Random (Seemingly) Port Blocks on Localhost Loopback Interface"
description = ""
date = 2021-06-03T11:48:07
updated = 2021-06-04T09:52:56
draft = false
slug = "fix-random-seemingly-port-blocks-on-localhost-loopback-interface"
aliases = ['2021/06/03/fix-random-seemingly-port-blocks-on-localhost-loopback-interface/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Windows", "port", "azure storage emulator", "loopback"]
+++


It has been a really, really long time since I have written a blog post. This
blog post talks about a recent problem which I encountered, forgot to write
about on how I solved it and it bit me back again after some time! Reminder to
all of you who are able to solve issues but don't document them!

The Problem
One fine day, I start debugging an Azure Functions project by starting the Azure
Storage Emulator and I am greeted with this -

PS C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator> .\AzureStorageEmulator.exe start -inprocess
Windows Azure Storage Emulator 5.10.0.0 command line tool
Service Status: Blob http://127.0.0.1:10000/ False
Access is denied
Error: Unable to start the storage emulator.
PS C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator>


This was pretty strange as I checked which process was trying to use this port
using netstat and I didn't see any entries -

I then went ahead and tried starting the Azure Functions project and it also
threw the same error that Port 7071 is blocked and access was denied to it. This
was very weird because I didn't have any applications running on that port & I
also tried running the application with Administrator privileges. I tried
running the Azure Functions project using a different port as well but it was
also blocked. I also tried running Apache using XAMPP on various ports. It
worked on some and it failed with the same port access blocked message on the
others.

The Troubleshooting
After running the usual netstat commands, I thought that maybe it could be the
Windows Firewall which might have some issue and it decided to block those
ports. I turned on Windows Firewall logging
[https://www.howtogeek.com/220204/how-to-track-firewall-activity-with-the-windows-firewall-log/] 
and I didn't see any blockings over there as well. I then turned towards Event
Viewer to see if there is any exception which is being generated in the 
Administrative Logs.

To my surprise, I found the port blocking event being generated i.e. Event 15005
HttpEvent with the following message -

Unable to bind to the underlying transport for 127.0.0.1:10000. The IP Listen-Only list may contain a reference to an interface which may not exist on this machine.  The data field contains the error number.


After searching around for quite a bit, I came across this Github link
[https://github.com/docker/for-win/issues/3171]. This talks about the Dynamic
Port range reservations which can be used by other services to block ports. I
ran netsh int ipv4 show dynamicport tcp and the following list popped -

PS D:\> netsh interface ipv4 show excludedportrange protocol=tcp

Protocol tcp Port Exclusion Ranges

Start Port    End Port
----------    --------
      1542        1641
      1742        1841
      1842        1941
      2280        2379
      2557        2656
      2682        2781
      2782        2881
      2882        2981
      2982        3081
      3082        3181
      3182        3281
      3282        3381
      3390        3489
      3490        3589
      3590        3689
      3690        3789
      3790        3889
      3990        4089
      4090        4189
      4243        4342
      4343        4442
      4443        4542
      4843        4942
      5043        5142
      5143        5242
      5243        5342
      5443        5542
      5943        6042
      6143        6242
      6243        6342
      6343        6442
      6543        6642
      7143        7242
      7343        7442
      7443        7542
      7543        7642
      7743        7842
      8443        8542
      8643        8742
      8743        8842
      8843        8942
      9043        9142
      9143        9242
      9243        9342
      9343        9442
      9443        9542
      9543        9642
      9643        9742
      9743        9842
      9848        9947
      9948       10047
     10048       10147
     10148       10247
     10248       10347
     10348       10447
     10448       10547
     50000       50059     *

* - Administered port exclusions.


As you can see, the port 10000 was in the range of ports blocked. I confirmed
this theory by running Apache on the various ports. As expected, it turned out
that if I tried running Apache on the ports which are in the list (& range)
above, it failed. On ports other than that, it worked without any issue.

The Solution
The solution which worked for me was to remove Hyper-V, reserve the port for
Hyper-V and then re-enable it.

 1. Disable hyper-v (which will required a couple of restarts).
    Do note that disabling and removing Hyper-V will mean that all your Virtual
    Machines & other objects part of Hyper-V will be removed.
    dism.exe /Online /Disable-Feature:Microsoft-Hyper-V
    
    
 2. When you finish all the required restarts, reserve the port you want so
    hyper-v doesn't reserve it back
    netsh int ipv4 add excludedportrange protocol=tcp startport=50051
    numberofports=1
    
    
 3. Re-Enable hyper-V (which will require a couple of restart)
    dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
    
    

Credit - https://github.com/docker/for-win/issues/3171#issuecomment-459205576

After rebooting after the 3rd step, my system was back to normal and the above
problems were resolved.