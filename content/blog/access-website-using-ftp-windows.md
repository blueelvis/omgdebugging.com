+++
title = "How to access Website using FTP in Windows"
description = ""
date = 2015-01-13T00:23:06
updated = 2018-08-22T08:21:16
draft = false
slug = "access-website-using-ftp-windows"
aliases = ['2015/01/13/access-website-using-ftp-windows/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Azure", "Easy", "FTP", "Website", "Windows"]
+++


In this post, I would be showing how to connect to a website using FTP (File
Transfer Protocol) to access/modify the files without using any kind of software
on Windows Operating System(Tested this on Windows 8.1).

For demonstration, I have quickly created a Website on Microsoft Azure and the
URL to access the website’s file system using FTP can be found under
Website->Dashboard. You can use any other host as well to create a website.
Generally for other hosts, you would get the FTP URL on the Email ID with which
you have registered with the host.

[![How to access Website using FTP in
Windows](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Azure-FTP-Details-1024x449.png?resize=730%2C320)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Azure-FTP-Details.png)FTP
Details in Microsoft AzureNow, once you get a hold of the FTP URL, open up
Windows Explorer by pressing (Windows Button + E) combination on the keyboard. A
window similar to the below window would open up –[![How to access Website using
FTP in
Windows](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Windows-Explorer-1024x545.png?resize=730%2C389)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Windows-Explorer.png)Windows
Explorer opened by pressing (Windows+E) or typing in Explorer in Start MenuNow,
on the Address Bar (Highlighted in RED) either click on the empty space or Right
Click on Address Bar and then click on Edit Address – 
[http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Address-Bar.png]

[![How to access Website using FTP in
Windows](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Login-Screen-1024x544.png?resize=730%2C388)](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/01/Login-Screen.png)The
Login Screen :OAfter clicking the Edit Address, the Address Bar will turn into
editable text. Paste your FTP URL here and press Enter. If the URL is working,
you will get the login screen like below (If Authentication is Enabled) –Once
you enter the correct credentials, you will be able to access the website’s file
system and modify the files as per your wish. You won’t be able to edit the
files directly from here but you can always copy/paste from other directories
here.

In case of any doubts, feel free to comment below or contact me via Twitter – 
https://twitter.com/Blueelvis_RoXXX