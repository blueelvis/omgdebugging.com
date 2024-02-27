+++
title = "Copying & Compressing Files Via Shell32 in C#"
description = ""
date = 2015-12-14T00:06:26
updated = 2018-08-22T08:21:16
draft = false
slug = "copying-compressing-files-via-shell32-in-c"
aliases = ['2015/12/14/copying-compressing-files-via-shell32-in-c/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["C#", "Shell32", "Windows", "ZIP"]
+++


There are often times when you have to copy files from one place to another in a
C# application. While developing BSOD Inspector, I did not use the methods which
are available in the Dot Net Framework to create ZIP file which contained
multiple files so that the application would run on Windows 7. The ZipFile
[https://msdn.microsoft.com/en-us/library/system.io.compression.zipfile(v=vs.110).aspx] 
method arrived with the .Net Framework 4.5 & 4.6 which is not pre-installed with
Windows 7.

On searching around, I found that there is another way to create a ZIP file
using the Shell32 provided by Windows. There is a very detailed guide on
utilizing the Shell32 to create a ZIP file at CodeProject over here – 
http://www.codeproject.com/Articles/12064/Compress-Zip-files-with-Windows-Shell-API-and-C

The problem occurred when I tried compiling and running the code given on the
CodeProject link on my Windows 10 machine. The error which was popping up was –

> Unable to cast COM object of type “Shell32.ShellClass” to interface type
“Shell32.IShellDispatch5”


After searching a lot, I found that there was a change in the Shell32 starting
from Windows 7. I found this written in a blog post over here
[http://techitongue.blogspot.in/2012/06/shell32-code-compiled-on-windows-7.html]
.

The reason behind the problem as per the blog post is –

> The Shell library comes with a new library in Windows 7. The problem with this
is that, in XP, the Shell32.ShellClass is not casted to Shell32.IShellDispatch5
but to Shell32.IShellDispatch4 which is deprecated or obsolete (or whatever term
MSFT uses)


After a small workaround, the code compiled well and the application completed.
This is when I noticed that some of the files were missing from the ZIP file
even though they were present in the source folder. After tweaking the code a
few times, I found that CopyHere method of Shell32 creates a separate thread to
copy the file. The problem behind the scenes was that the program was executing
so fast that it did not give enough time to the Shell32 to invoke the thread
properly. So, on making the Main thread sleep for a second, I was able to get
all the files from the source folder inside the ZIP file like below –

foreach (var file in zipInput.Items()) { if (file != null)
zipOutput.CopyHere(file, 4 | 16); Thread.Sleep(1000); //Added This }

Hope this helps! Happy Coding!