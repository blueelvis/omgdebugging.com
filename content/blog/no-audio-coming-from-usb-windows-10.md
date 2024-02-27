+++
title = "No Audio coming from USB Windows 10"
description = ""
date = 2023-08-14T11:39:36
updated = 2023-08-14T11:45:34
draft = false
slug = "no-audio-coming-from-usb-windows-10"
aliases = ['2023/08/14/no-audio-coming-from-usb-windows-10/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Quick post as always!

I was having a lot of trouble with my Audeze Mobius device not working when
connecting to a particular laptop as it was working fine over Bluetooth and USB
when connected to other devices.

The problem was that the system was recognizing that the Mobius was connected
and everything was showing as that was the default device for sound and
communications but still no sound!

After opening the Sounds panel and clicking on Test button, I got the Unable to
play test tone.

After trying various things like changing the Audio service's Log On account and
all, it was still not working.

Finally, I decided to roll back the Audio driver since the last update I was
seeing was back in 2022.

I went into

Sounds -> Right Click Audeze Mobius -> General -> Properties (Under Controller Information) -> Change Settings With UAC (If you see this) -> Driver Tab -> Rollback Driver.


As soon as I did this, the audio started working!