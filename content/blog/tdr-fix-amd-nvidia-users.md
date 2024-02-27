+++
title = "TDR Fix (For AMD & NVIDIA Users)"
description = ""
date = 2014-09-27T22:52:51
updated = 2018-08-22T08:21:16
draft = false
slug = "tdr-fix-amd-nvidia-users"
aliases = ['2014/09/27/tdr-fix-amd-nvidia-users/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Fix", "Registry", "Registry Fix", "TDR", "Timeout"]
+++


In case you are having Timeout Detection & Recovery problems in Windows or you
are getting constant popups like the Display Driver has stopped responding and
has successfully recovered. If the operating system detects that six or more GPU
hangs and subsequent recoveries occur within 1 minute, the operating system
bug-checks (Blue Screens) the computer on the next GPU hang.

The first course of action in this case would be using the Display Driver
Uninstaller from the below link :-

http://www.guru3d.com/files-details/display-driver-uninstaller-download.html

Once you have downloaded it, run it, uninstall the current driver set. Reboot.

After this, install the Display drivers (AMD/NVIDIA) from either the Driver
Media which you got with your Graphics Card (Mostly Desktops) or from
the Manufacturer’s Support Website(For Laptops. Here is OEM is the manufacturer
of your Laptop). In case of laptops, it is suggested to install the drivers only
from the Manufacturer as they tweak the drivers to work with the switching
between the external Graphics Card and the Internal Graphics processor embedded
onto the motherboard.

That should fix your problem.

In case the problem is still there then there is a registry tweak available. It
is purely a WORKAROUND and not a proper solution to the problem. Basically, it
will simply delay the Timeout. You can download the Registry Fix ( TDR Fix
) below –

TDRFix
[http://omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/TDRFix.reg]



Note :- Kindly note that modifying registry is a risky process and even a small
change can make the PC unbootable. So, think twice before making any change to
the Registry. (Thanks dc3)

The file has been scanned with VirusTotal
[https://www.virustotal.com/en/file/fbcfd1c1406d8d4eac5aacbfbafc2bece8464d1e8ed65368129287177efe11d7/analysis/1411837971/]
. In case you are still having problems, please do not hesitate to contact me or
post in the comments section.