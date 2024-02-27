+++
title = "File Associations and Shell Spawning"
description = ""
date = 2015-08-10T22:36:19
updated = 2018-08-22T08:21:16
draft = false
slug = "file-associations-and-shell-spawning"
aliases = ['2015/08/10/file-associations-and-shell-spawning/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "Malware", "OTL", "Shell", "Windows"]
+++


Howdy! It has been a long time since I have written a blog post. Well here I am
with another blog post in which Gary (Oh My! from BleepingComputer
[http://www.bleepingcomputer.com/forums/u/450558/oh-my/]) explains File
Associations and Shell Spawning in Windows or in other words, how Windows
decides how to open a particular file. He also discusses how malware can mess
with it and have Windows run the malware every time you run any file.

Each file extension has 2 related Registry keys under HKCR. Handling a file
extension is a 2 step process. The first addresses the File Association and the
second pertains to Shell Spawning. Let’s use the .exe file extension as an
example. Here are the 2 Registry keys for .exe:

File Association key: [HKEY_CLASSES_ROOT.exe]
Shell Spawning key: [HKEY_CLASSES_ROOT\exefile\shell\open\command]

Step 1 – File Associations
When you double click an .exe file Windows will go to the (file association) 
HKCR.exe Registry key to look for the default Value under that key in order to
start the process of handling the launch request. The default Value of this key
will point to the second Shell Spawning Registry key (detailed later). On a
healthy computer the default Value under HKCR.exe (file association) will point
to the HKCR\exefile (shell spawning) Registry key. Here is what it should look
like:

[HKEY_CLASSES_ROOT.exe] "(Default)"="exefile" "Content
Type"="application/x-msdownload"

**Note **the (Default) value i.e. exefile.

In case you would like to read more about the Default value (Also sometimes
represented by the @ symbol), refer this article – 
http://blogs.msdn.com/b/oldnewthing/archive/2008/01/18/7145021.aspx

Step 2 – Shell Spawning
What is Shell Spawning?

“The Shell Spawning procedure spawns a child process to execute a command or
series of commands.”

The default Value of **exefile **in the first file association key is actually
pointing to the HKEY_CLASSES_ROOT\exefile\shell\open\command shell spawning key.
Below we can see what a healthy key should look like. We see the shell part and
the spawning part. In other words, Shell Spawning.

[HKEY_CLASSES_ROOT\exefile<span style="color:Green;">shell\open\command]
@=”\”%1\” %”
“IsolatedCommand”=”\”%1\” %”

P.S. – Can you guess what is the meaning of the @ symbol? Yep. You guessed it
right, it is the Default Value like discussed above. Also, I have emphasized the
above code part because I am still awaiting the perfect CODE plugin for
WordPress 

On a healthy computer that Default value (“\”%1\” %*”) is telling the system the
.exe file can execute itself, it doesn’t need anything else. For a more detailed
explanation of the Default Value see here
[http://spth.virii.lu/29a6/29A-6.216.txt](And no, the file is not a virus in
case you get an alert like I got).

Gary explained this whole part while I was completing the exercise under him in
the BleepingComputer Malware Study Hall
[http://www.bleepingcomputer.com/forums/t/532535/malware-removal-training-program/]
. (You can also join the training. It is free and is awesome!)

So, now he explains how this knowledge can be utilized in understanding the
entries in the OTL Log File.

Applying that to our log
Sometimes one of the problems with logs is that the format of the information
produced is not as clear as it could be because there is an assumption the
underlying dynamics are already fully understood. While on training, and even
beyond in all honesty, that is not always the case. This is one of those
occasions, in my opinion.

[HKEY_USERS\S-1-5-21-974959715-1046243335-397612234-1232\SOFTWARE\Classes<extension>]
.exe [@ = secfile] -- C:\Users\HelloWorld\AppData\Local\Screensaver.exe ()

So now, in our case the default Value for the first Registry key (file
association) is being hijacked and points to the (shell spawning) secfile 
Registry key instead of the normal exefile Registry key. So the computer goes to
the secfile key (actually the HKEY_CLASSES_ROOT\secfile\shell\open\command 
Registry key) to find instructions regarding what to do with the .exe file
extension. The Value in the second key (secfile) is telling the computer to
launch C:\Users\HelloWorld\AppData\Local\Screensaver.exe instead of allowing the
.exe file to launch itself by means of the normal default Value. The result? The
malware file will block the launching of the .exe file and will typically show a
warning that the .exe file attempting to be launched is malware and is being
stopped from running. It will do that for all .exe files thereby blocking all
executables including malware tools with an .exe extension. That is why you will
find some tools have additional options
[http://www.bleepingcomputer.com/download/rkill/] to download the file with
different file extensions.

Credits – Once again, thanks a lot Gary
[http://www.bleepingcomputer.com/forums/u/450558/oh-my/] for sharing your
valuable knowledge ^_^