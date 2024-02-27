+++
title = "Enable/Disable Watermark on Desktop Of Windows"
description = ""
date = 2014-10-13T00:10:59
updated = 2018-08-22T08:21:16
draft = false
slug = "enabledisable-watermark-desktop-windows"
aliases = ['2014/10/13/enabledisable-watermark-desktop-windows/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Watermark"]
+++


In this tutorial, I would outline the steps so that you could also have a
Desktop in which Windows displays the Operating System installed and it’s Build
Number like below –

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Desktop-Screenshot-1024x575.png?resize=730%2C409)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Desktop-Screenshot.png)Notice
the White Text Watermark in the Bottom-Right just above the Time.Windows uses a
Registry Key to determine whether it needs to display the watermark or not. The
registry key we are talking about is “[**PaintDesktopVersion**
](http://technet.microsoft.com/en-us/library/cc782257(v=ws.10).aspx)“.So, to
enable/disable the Watermark follow the below steps :-

 1. Open the Registry Editor by typing in “regedit” in the Run Prompt (Windows
    Key + R).
 2. Once the Registry Editor is opened, navigate to the path (refer the
    screenshot below)  “HKEY_CURRENT_USER\ControlPanel\Desktop” 
    [http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Registry-Location.png]
    How To Find the Registry Key PaintDesktopVersion

3. Search for the Registry Key named “PaintDesktopVersion” and then double-click
on it to change it’s value.
4. If you want to ENABLE the Watermark, set the value to “1” and if you would
like to disable the Watermark, set it’s value to “0“.
5. Restart the System and you would see the Watermark once you are on the
Desktop.

In case of any problem, do not hesitate to post back in the Comments Section or
Contact Me!