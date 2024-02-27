+++
title = "Sony Wireless Headset 7.1 Not Charging via PC USB Port"
description = ""
date = 2014-12-23T22:39:39
updated = 2018-08-22T08:21:16
draft = false
slug = "sony-wireless-headset-7-1-not-charging-via-pc-usb-port"
aliases = ['2014/12/23/sony-wireless-headset-7-1-not-charging-via-pc-usb-port/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "case", "Headset", "Sony"]
+++


I use a Sony Wireless 7.1 Headset with my laptop which I originally bought for
using with my PlayStation 3 to complement my gaming experience. But, since
gaming these days is now limited to the laptop only, I use the Headset to it’s
best with the laptop since it provides me with the most useful features i.e.
Wireless and Excellent Sound Quality (I am no audiophile…).

Recently, I had to reinstall the Windows because of Hard Disk failure. After the
reinstallation of Windows, I started to listen to songs online and soon the
headset started crying because it was out of juice. I plugged the headset into
the USB port of my laptop and it started charging (Indicated by a red light on
the Mic of this Headset). After around 10 seconds, I put down the headset and
noticed that the headset was not charging. I quickly re-inserted the charging
cable into the USB and observed that around 5-6 seconds later, the headset
stopped charging.

Now, this issue started getting on my nerves and I immediately fired up Device
Manager and uninstalled the driver for the headset. Reboot.

[![Loading](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/12/Device-Manager-Uninstallation.png?resize=730%2C531)](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/12/Device-Manager-Uninstallation.png)Uninstalling
Headset Driver via Device ManagerHoping that the issue to be resolved after
doing this, I plugged in the headset and noticed the same thing happening again.
After trying this for several times, I started searching on Google to see if
there are any people having problems like me. Sadly, I was not able to find one
regarding this specific issue.After changing a few terms, I came across this
blog post –

http://blogs.msdn.com/b/usbcoreblog/archive/2013/11/08/help-after-installing-windows-8-1-my-usb-device-doesn-t-charge-or-it-disconnects-and-reconnects-frequently.aspx

Warning : Modifying Registry Can Be Dangerous if not done correctly. Kindly
follow the above link at your own risk!

So, Microsoft introduced a new feature with Windows 8 called Enhanced Power
Management. With this feature, Windows cuts off the power to the device in case
it sees that there is no response from the device or there is no activity going
on which is utilizing the device. But, why have it in the first place?

This feature was added so as to save the power and hence increase the battery
life in Mobile Devices.

You might wonder as to why this does not happen with Pen Drives. The answer to
this question according to me would be that Windows queries the devices attached
to the system from time to time and awaits a response. In the case of the
Headset, the port is only configured so that only the battery is charged and
nothing happens.

On following the above post, my problem was solved. Also, SONY has released the
updated driver on the Windows Update. So, kindly download the update and see if
you are still having problems or not.

I hope you enjoyed this post. In case of any feedback, do not hesitate to post
in comments ^_^.