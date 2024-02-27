+++
title = "Steam doing First Time Setup Every time?"
description = ""
date = 2014-09-13T12:46:50
updated = 2018-08-22T08:21:16
draft = false
slug = "steam-doing-first-time-setup-every-time"
aliases = ['2014/09/13/steam-doing-first-time-setup-every-time/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Monitor", "Problem", "Process", "Process Monitor", "Steam"]
+++


All hail GABE NEWELL [http://en.wikipedia.org/wiki/Gabe_Newell]. Why so? Well he
is the co-founder and the Managing Director of Valve. That is the same company
which created Steam and allowed me to play DOTA 2 and so many other games online
when I only dreamt of Single Player Games in my childhood.

Now, one thing which I really like in various activities is formatting my laptop
like every 5-6 months so that it is neat and clean while running at it’s best.
But, I hate to move the data back and forth so I have created a separate
partition on my laptop for saving the Data. One such folder on that partition is
STEAM where most of my games reside. Since, the bandwidth in India is very low,
downloading games can be a real pain. So I take extra precaution that my STEAM
folder is there always.

So, this one fine day, I formatted my laptop and after the format Steam was
there as usual on the partition not formatted. I do not do repeated
installations of Steam as it has got the Repair Utility to take care of any
missing registry entries or DLL’s after a format. After the necessary
installations, I was finally able to play a game of DOTA.

Next day, I immediately fired up Steam after coming home and looking forward to
play a game of DOTA, I pressed the PLAY button and to my surprise it began the 
First Time Installation Setup. I was like You Don’t Say? It was because I had
already done that. So, I thought that may it was a one time problem. But, the
problem persisted.

Now, since I did not want to reinstall the whole game for this one small thing
as it only took around 5 seconds to complete after clicking YES in the UAC
Window, I decided to solve the problem.



After watching Mark Russinovich’s [http://blogs.technet.com/b/markrussinovich/] 
‘The Case Of Unexplained’ and his blog, I was motivated to use the Process
Monitor [http://technet.microsoft.com/en-in/sysinternals/bb896645.aspx]. Process
Monitor is basically a tool for advanced monitoring which monitors File System,
Registry & Process/Thread activity. The main screen of the tool is like below :-

[![Loading...](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Process-Monitor-Basic-1024x545.png?resize=730%2C388)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Process-Monitor-Basic.png)WAO!
So, I started a trace with Process Monitor and launched DOTA 2 again to capture
what was happening. Once closing the game, I stopped the tracing activity of
Process Monitor and filtered the events to display only the events related to
STEAM. Process Monitor starts/stops capturing trace by clicking the button which
looks like a Magnifying Glass located just below the Event Button in the Menu
Bar. You can filter the events by right clicking on any Event which you would
like to filter like shown below :-

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Filtering-The-List-1024x544.png?resize=730%2C387)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Filtering-The-List.png)Filtering
the List in Process Monitor is easy but only once you know it ;)I captured the
trace and filtered the list for Steam and below was what I got :-
[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Filtered-List-1024x545.png?resize=730%2C388)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Filtered-List.png)Sadly,
it doesn’t make any sense to me :(Now, does this make any sense? Even if it
makes sense to you, it did not make any sense for me ^_^. One powerful option in
Process Monitor is to Count the Number of Occurrences of different types of
Results. This can be opened by going to “***Tools -> Count Occurrences***” as
shown below :-
[![Loading...](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Count-Occurrences-1024x545.png?resize=730%2C388)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Count-Occurrences.png)Counting
Occurrences is easy!On counting the number of occurrences for “***Name Not
Found***” and double clicking produced something sensible. Now, I started
scrounging through each entry and I came up with this entry below :-
[![Loading...](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Name-Not-Found-1024x543.png?resize=730%2C387)](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Name-Not-Found.png)Well
that seems weird. Let’s check the installation path of dota now.I asked myself
that why is this not found? Let’s check the installation directory for DOTA 2.
On checking, I found that there were two VDF files one of which was the “*
**installscript_575_windows.vdf***” (Note that it may be possible that there is
a similar file like that but named something else).
[![Loading...](http://i0.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Dota-2-Installation-Folder-1024x543.png?resize=730%2C387)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Dota-2-Installation-Folder.png)How
come?But, the query was for the “***installscript_570_windows.vdf***“. I opened
the original file and there was some gibberish written inside it.I simply
renamed the “installscript_575_windows.vdf” to “installscript_570_windows.vdf” &
VOILA the problem disappeared.



So, moral of the story? Don’t ever hesitate to ask questions to yourself and
keep on going!

Furthermore, for anyone who is interested in my articles, I have added a
Newsletter Page on the blog which can be accessed by clicking on the word 
NEWSLETTER in the side Pane. Subscribe yourself and you would receive mail
whenever I post a new article ^_^. Don’t worry, I don’t spam.



I hope you enjoyed this article. Any doubts/feedback? Use the Comments Section
below ^_^.