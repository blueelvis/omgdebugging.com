+++
title = "Case Of USB Tethering Driver Freezing the System"
description = ""
date = 2016-08-15T13:41:12
updated = 2018-08-22T08:21:16
draft = false
slug = "case-of-usb-tethering-driver-freezing-the-system"
aliases = ['2016/08/15/case-of-usb-tethering-driver-freezing-the-system/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I assembled a PC in January whose sole purpose was gaming. From Day 1, I had
been noticing several freezes on the system. The system used to freeze for a
second or so which also caused the mouse to lag behind.

Eventually I got used to it and ignored the problem. Recently, when the Windows
10 Anniversary Update was released, I thought of giving it a go since I really
wanted to try out it's feature - Windows Subsystem for Linux.

This feature allows the user to run native Linux commands inside Windows. In
other words, there is a Linux Subsystem which is isolated from Windows but can
be run inside Windows without the hassles of setting up a Virtual Machine (Note
that it is not a virtual machine) or a container.

Earlier I thought that the problem was being caused because of the extra MSI
software installed on this system. But, I was wrong since the problem returned
as soon as I started browsing the internet.

On looking around for a while and tinkering with Windows, I noticed that the
only thing which was common before and after the clean install was that I had
been using the internet by tethering my Android phone to this PC via USB.

Fingers crossed! I detach the phone and voila, the problem is gone. As soon as I
plugged the device back in, the system started acting up. In my case, the driver
that was being used was neither of these, but a special driver from Android SDK
ADT bundle.

Fortunately, I found a very helpful post over Reddit
[https://www.reddit.com/r/Windows10/comments/3v63qq/w10threshold_2windows_freezes_when_using_usb/d0bdbzz]
. On installing the Remote NDIS based Internet Sharing Device driver and the
problem vanished.