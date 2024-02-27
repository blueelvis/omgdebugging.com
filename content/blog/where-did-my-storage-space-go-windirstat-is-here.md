+++
title = "Where Did My Storage Space Go? WinDirStat is here!"
description = ""
date = 2015-02-22T22:43:09
updated = 2018-08-22T08:21:16
draft = false
slug = "where-did-my-storage-space-go-windirstat-is-here"
aliases = ['2015/02/22/where-did-my-storage-space-go-windirstat-is-here/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "WinDirStat", "Windows"]
+++


Often, I am asked the question “Where Did My Storage Space Go?”. In this post, I
would try to solve that problem. Let me begin this blog post with a recent
experience I faced due to the use of Download Managers. Day before yesterday, I
shut down my laptop and it did so peacefully. On starting the laptop again, I
got a message from Windows that there is not enough space in the C: drive and it
could cause performance slowdown. I was like, are you kidding me? I had around
150GB free last night so what caused Windows to pop up that message? I
immediately opened up Explorer and found that C: drive was completely filled
with 0 Bytes free. After some initial diagnostics of Malware Scans, I came to
the conclusion that the system was malware free. So, I started out checking the
folders one by one and after an hour or so, I found that the Download Manager
(Internet Download Manager) was trying to download a partially complete file
despite no internet connection and it filled up it’s Temporary Folder. I cleaned
the Temporary Folder and I got my space back. It seems that the Download Manager
I was using does not work well with Proxifier causing it to keep on garbage
files (Logs) even if there is no internet.

So, I was baffled by the fact that it took me around an hour to find the
location which was taking up most of the space even though I keep my C: drive
organized and clean it from time to time. I tried searching for an online
utility which could tell me the space occupied by a file/folder in a nice way
and I won’t have to check the properties of each file/folder manually.

I came across WinDirStat.

[![WinDirStat](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/WinDirStat-1024x547.png?resize=730%2C390)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/WinDirStat.png)Well
that Pac Man animation is nice!I ran WinDirStat and after some minutes, I had a
complete report of which file/folder is taking up the most space. Using it, I
was able to clean up an additional of 10GB which I had just copied and forgot.
This is especially useful when the data on the Hard Disk contains copied data,
music, movies, games which might not show up in the Add/Remove of Control Panel.
While the program is running, there is a nice Pac Man animation and the best
feature of this program is that it is able to show the information for Network
Shares as well provided that the Network Shares are mounted.You can download
WinDirStat from the below link –
https://windirstat.info/download.html