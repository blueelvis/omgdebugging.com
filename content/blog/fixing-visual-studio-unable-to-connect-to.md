+++
title = "Fixing Visual Studio 2017 unable to connect to Web Server 'IIS Express'"
description = ""
date = 2019-09-05T10:25:53
updated = 2019-09-05T15:30:00
draft = false
slug = "fixing-visual-studio-unable-to-connect-to"
aliases = ['2019/09/05/fixing-visual-studio-unable-to-connect-to/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


There are so many days in our lives as developers that something is working
exactly fine one day and the next day you login and start your project and it
just refuses to work! This has been one of the issues which have been like this
and to be honest, has plagued me in the past as well. Last time, I remember that
rebooting the system fixed the issue but I am not going to restart it this
time...

All of a sudden, I started getting the following issue when trying to start up a
project (written in .Net Core) -


After trying various solutions like deleting the .vs folder, restarting IIS
Services, cleaning the entire solution, I was still getting this error. I
searched for stray IIS processes using Process Explorer
[https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer] as
well but nothing came up. Moreover, after this error came up, I could actually
see the site running locally and I got the icon for IIS Express in my taskbar
but Visual Studio still refused to start debugging.

Eventually my mind said, hey! why not try checking the Event Viewer logs? And to
my surprise, I did find the following event -


Fortunately, on searching about this error code, there is a really nice TECHNET 
article
[https://social.technet.microsoft.com/wiki/contents/articles/21750.event-id-2269-iis-worker-process-availability.aspx] 
which details the procedure on resolving the issue.

Here are the steps which I followed (with a bit of modifications) -

 1. I added the IIS_IUSRS group to the security setting for Bypass Traverse
    Checking as the others were already added. If you want to read more about
    what Traverse Checking in Windows is then I would suggest you to read over
    here. In a gist, it checks whether a user (or a process acting behalf on a
    user) will be allowed to traverse the path in NTFS or registry without
    actually checking if it has the permissions. It only gives traversing
    permission & that doesn't mean the process or user will be actually able to
    access content.
 2. Next, I stopped the W3SVC service net stop w3svc and it stopped
    successfully.
 3. After this, I tried stopping the HTTP service but I was not able to stop it
    -

PS C:\WINDOWS\system32> net stop w3svc
The World Wide Web Publishing Service service is not started.

More help is available by typing NET HELPMSG 3521.

PS C:\WINDOWS\system32> net stop http
The following services are dependent on the HTTP Service service.
Stopping the HTTP Service service will also stop these services.

   SSDP Discovery
   Print Spooler

Do you want to continue this operation? (Y/N) [N]: Y
The SSDP Discovery service is stopping.
The SSDP Discovery service was stopped successfully.

The Print Spooler service is stopping.
The Print Spooler service was stopped successfully.

The HTTP Service service is stopping........
The HTTP Service service could not be stopped.

PS C:\WINDOWS\system32> net stop http
The service is starting or stopping.  Please try again later.


Well, that was strange. It probably meant that some process/service still had
handles opened in HTTP. I jumped on to Process Explorer and searched (Ctrl+F)
for the string \Device\Http\ which gave me the following -

For some reason, RedGate.Client.Service.exe still had handles open. I had to
stop the Redgate Client service (RedgateClient) which then allowed HTTP service
to stop successfully.
4. net start w3svc
5. net start http
6. Deleted the .vs folder inside the solution and also deleted 
%USERPROFILE%\Documents\IISExpress
7. Restarted Visual Studio and cleaned the solution and rebuilt it.
8. After this, I ran the site's DLL file using dotnet <PATH_TO_DLL> which
started the site on a different port.

After this, the solution started working properly.