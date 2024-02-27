+++
title = "Disable Edge Swipes while using Synaptics Touchpad Driver"
description = ""
date = 2015-04-17T18:08:58
updated = 2018-08-22T08:21:16
draft = false
slug = "disable-edge-swipes-while-using-synaptics-touchpad-driver"
aliases = ['2015/04/17/disable-edge-swipes-while-using-synaptics-touchpad-driver/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Edge Swipes", "Synaptics"]
+++


Tired of the charms bar of Windows 8/8.1 coming up when you swipe the touchpad?
Worry not! The permanent fix is here. Please follow this guide only in case you
are not able to disable the Edge Swipes by any other method since this enables
modification of the registry. This guide was written while keeping in mind the
Version 7.2 of the Synaptics Touchpad Driver. Furthermore, this version of the
driver on my laptop did not show any option for disabling the Edge Swipes and
even disabling the option via Windows did not help me.

Let’s disable those annoying swipes by following the below simple guide –

 1. Open up the Registry Editor by pressing “Windows Key + R” and type “regedit”
    in the Run Dialog box which opens up.
    
    
 2. Once the Registry Editor opens up, navigate to the below path from the side
    pane –
    
    

HKEY_LOCAL_MACHINE\SOFTWARE\Synaptics\SynTPEnh\PlugInConfig\Defaults\CustomZones

 3. Click on the CustomZone key and you would find a view similar to the below
    picture –

[![Loading....](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/04/Registry-Key-Location-1024x545.png?resize=730%2C389)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/04/Registry-Key-Location.png)That’s
the place you need to go to disable those pesky swipes!4. Once you have
completed the above steps, rename (By right clicking on the Key and clicking on
Rename) the key titled “**CustomZone113KeyMacroBin**” to
“**CustomZone113KeyMacroBin-bak**“. 5. Close the registry editor and then
    restart the machine.

Once the system has booted up after the restart, you would notice that the
charms bar does not come up howsoever you move your fingers across the touchpad.

In case of any problems, please feel free to post in the comments section below.