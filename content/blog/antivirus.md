+++
title = "You Are Your Computer Security!"
description = ""
date = 2015-02-16T22:12:06
updated = 2018-08-22T08:21:16
draft = false
slug = "antivirus"
aliases = ['2015/02/16/antivirus/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Security", "Windows"]
+++


It has been a long time now since I wrote an article. In this blog post, I will
explain (and teach as well) how and why people need to be aware of the Malware
spreading in the wild and how you are your own computer security.

Sounds interesting? Well, then read on.

Let me tell you on how things are arranged on my system for giving me the
maximum protection against Malware. It has now been close to an year since I
decided to change from a licensed antivirus solution and switch to Windows
Defender to see if malware is able to infect my system. Wait. Did I hear “Are
you crazy? You are just too dumb!”?

[![Antivirus](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/55466648.jpg?resize=250%2C250)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/55466648.jpg)Well
that’s funny!Don’t worry people. I have turned on my Windows Defender (I don’t
think that it is a better idea to run simply Windows Defender in a Corporate
Environment though!) and do a monthly scan with [](https://www.malwarebytes.org/
"MalwareBytes") and [](http://www.gmer.net/ "GMER"). Yup. That’s it. For
security purposes, I have turned on Windows Defender alongside the Windows
Firewall. Now, keeping the software aside, the best defence is having common
sense and asking questions to yourself.Let me tell you an incident which
happened a few days ago. I get a message on Steam Chat from a friend claiming
that the below picture is extremely funny. Since it was from one of my trusted
friends, I decided to open the link which was basically a shortened link
(bit.ly). On clicking on the link, Internet Explorer opened and it asked me to
download and save a file. I saw that the extension was “.scr” which is the
Windows Screensaver file. I asked myself as to why an image has got a
Screensaver Extension and so I decided not to download the file. Turns out after
a few days, I see that this is malware spreading through Steam Chat. You can
read more over here – 
https://blog.malwarebytes.org/online-security/2014/09/steam-threats-what-they-are-and-what-you-can-do-to-protect-your-account/

So, here are the best tips I could think of which could teach you self defense –

1. Start asking yourself the question before doing anything on the computer.
Even though computers have simplified each and every task by heaps. This has got
both it’s positive and negative effects. You obviously know the positive aspect
of this so let me tell you about the negative aspect. For example let us
consider the way we install something from an Installer Package. Admit it. Most
of us would simply click on Next -> Next -> I Accept -> Next -> Finish. Did you
ever spend some time before checking and asking yourself what the program
actually installs? (If you really don’t have time, you might find Unchecky
[http://unchecky.com/] very useful).

2. Disable that nasty Autorun. 
Windows makes it very convenient for you in the sense that it could
automatically launch applications when a disk (CD, DVD, Hard Disk etc) are
attached to the system and launch the appropriate program. Malware can easily
modify the autorun entries and whenever you attach something to the system, the
malware would run and bingo, you have got yourself an infected system! If you
don’t know how to disable the Autorun, follow this link – 
http://www.redmondpie.com/how-to-disable-autorun-autoplay-in-windows-7-and-windows-8/

3. Have the habit of scanning external drives whenever they are plugged in.
That sounds time consuming right? But, trust me. It is worth the effort. Since
you have already disabled the nasty autorun, the malware inside the attached
drive won’t run until you explicitly ask it to run.

4. Don’t trust/start downloading anything from the Search Results you get. 
The heading might not help you understand what I really mean. Suppose I want to
download the drivers for my laptop and I do a simple search on Google as below.
Can you guess which one is the valid and trusted link?

[![Antivirus](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/Search-Result-1024x448.png?resize=730%2C319)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2015/02/Search-Result.png)That’s
confusing. If you said that it is the 3rd link, then that’s correct. If you did
not get the answer then try asking yourself (Like I said in the first point) –
Why is a 3rd party providing links to the drivers? What do they gain? What if
something goes awry, who will take the responsibility then? I hope you got the
point. Once you start looking carefully through the search results, you would
automatically tend to skip the useless links which would also save your time and
a lot of headache. ### 5. Don’t download illegally and from 3rd parties. This is
said by all of the Security people around the globe but well who listens? In
today’s world, obfuscating any file on the system is simple and very hard to
crack. For example, I download the trial version of a legal application, embed
it with another malicious executable and then repack it to give the executable
the exact look of the legit application. Now, whenever one runs this
application, the malware is executed and copied to the appropriate directories
and simultaneously, the legit application is launched. This way, even if an
Antivirus detects that there is another file which is malicious, the user thinks
that it is a false positive and asks the Antivirus to shut up. So, now who is at
fault?

6. Keep the software updated. 
It has been said again and again to keep the software on the system updated. It
turns out that most of the people don’t do this. According to 
[http://www.networkworld.com/article/2226451/microsoft-subnet/third-party-software--not-microsoft-s--blamed-for-76--of-vulnerabilities-on-average.html] 
today’s malware makers don’t try much on exploiting the Operating System but
rather the applications which are installed on the system. New versions of the
software are released frequently so make sure that you update them. You could
also have a day once every two weeks where you update everything on the system.

I hope this post made you aware at least a bit on how you could protect your
system with minimal software.

Special Thanks – Corrine Chorney
[http://www.sysnative.com/forums/members/corrine.html] (Microsoft MVP
[http://mvp.microsoft.com/en-us/mvp/corrine-33416]) of Security Garden
[http://securitygarden.blogspot.in/] for keeping me updated on the latest trends
in Malware.