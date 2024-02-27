+++
title = "Is There Any Benefit in Refreshing The Desktop in Windows?"
description = ""
date = 2014-10-13T00:35:39
updated = 2018-08-22T08:21:16
draft = false
slug = "benefit-refreshing-desktop-windows"
aliases = ['2014/10/13/benefit-refreshing-desktop-windows/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Process Monitor", "RAM", "Windows"]
+++


I encounter so many people everyday who simply love pressing F5 button on the
Keyboard when they are on the Desktop. I have seen some people actually right
clicking and then hitting the Refresh Button as well. Yea, I am talking about
the Geeks as well. In this case, I would be referring Desktop as the Desktop of
Windows Operating System.

So, I thought for a while as to why the people keep on doing this? I had this
question come up many times during my childhood as well. Later on, I started
hearing people saying that doing the Refresh actually speeds up the system by
freeing up the RAM Cache. And finally, I decided to find an answer to this
question as to whether this is true or not.

So, this time as well I turned to one of my favourite tools for troubleshooting
i.e. Process Monitor
[http://technet.microsoft.com/en-in/sysinternals/bb896645.aspx] developed by
Mark Russinovich & Bryce Cogswell. First of all, below is a screenshot of my
Desktop –

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Desktop-Screenshot-1024x575.png?resize=730%2C409)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Desktop-Screenshot.png)That’s
my desktop. Yea, I know it is clean ;)In case you also would like to enable the
Watermark to show the Windows Version and it’s build number go to this link – [
http://omgdebuggingblog.cloudapp.net/enabledisable-watermark-desktop-windows/
](http://omgdebuggingblog.cloudapp.net/enabledisable-watermark-desktop-windows/)
After excluding all of the un-necessary executables, I captured a log while I
was refreshing the Desktop.

I refreshed multiple times so as to get consistent results. I got the below log
file –

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Process-Monitor-Log-1024x575.png?resize=730%2C409)](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/10/Process-Monitor-Log.png)Oh
Process Monitor So, can you guess what can we see from the Highlighted Entry?If
you guessed it right, then congratulations else worry not, I will tell you. The
Explorer.exe is querying for information about the available Icons on Desktop. I
checked the entire log, and it queried the information regarding every Desktop
Icon.

Furthermore, I searched the almost the entire log and I was not able to see any
trace of any function to clear the RAM or which would benefit the system
performance. During a Refresh, the graphics drivers are asked to repaint the
desktop using the latest information about the themes, icons and other visual
changes and that is why there is a flicker of icons when we hit Refresh. While I
was refreshing multiple times during the capture of Process Monitor Log, I
noticed that the time to open the Right Click menu was the same. If the Refresh
was actually clearing the RAM, there would have been a significant faster
response during subsequent Right Clicks which was not noticed.

When we hit Refresh, several calls are made to the Graphics Drivers, other core
components of the Operating System which causes a sudden spike as well.

Although, the load of Refreshing is not considered a heavy load for today’s
processors, so there is almost NIL Activity from the Processor. Hence, proved
that the Refresh is not used to increase the performance but to refresh the
properties and information about and on the Desktop.

I hope you enjoyed the article ^^. In case of any doubts, do not hesitate to
post back in the comments section or Contact me ^^.