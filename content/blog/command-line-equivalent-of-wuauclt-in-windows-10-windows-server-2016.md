+++
title = "Command Line Equivalent of wuauclt in Windows 10 / Windows Server 2016"
description = ""
date = 2017-10-09T13:11:19
updated = 2018-08-22T08:21:16
draft = false
slug = "command-line-equivalent-of-wuauclt-in-windows-10-windows-server-2016"
aliases = ['2017/10/09/command-line-equivalent-of-wuauclt-in-windows-10-windows-server-2016/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Windows Update with Windows 10 & Windows Server 2016 was modified so that it
could be integrated with the new UI. The old Windows Update is now gone from
Control Panel (I am so sad...) and if you have to view updates, all you can do
is

> Start -> Settings -> Update & Security -> Windows Update


With earlier versions of Windows, there used to be utility wuauclt but that does
not work anymore since it does not update the UI which is accessed through 
Settings.exe.


Now, if you try typing the following command in an Administrator command prompt
on Windows 10 or Windows Server 2016, nothing will happen - wuauclt /detectnow

Now, in order to force check Windows Update, follow the below instructions -

 1. Open a Command Prompt with Administrator privileges.
 2. Type in usoclient StartScan
 3. You will see that Windows Update in Settings.exe will start refreshing as
    below -
    

Note: USOClient.exe is located in C:\Windows\System32

This will also force the client to report its status to the WSUS server (if
configured).

On using Sysinternal's Strings on UsoClient.exe, I found that there are more
switches which can be used -

 * StartScan Used To Start Scan
 * StartDownload Used to Start Download of Patches
 * StartInstall Used to Install Downloaded Patches
 * RefreshSettings Refresh Settings if any changes were made
 * StartInteractiveScan May ask for user input and/or open dialogues to show
   progress or report errors
 * RestartDevice Restart device to finish installation of updates
 * ScanInstallWait Combined Scan Download Install
 * ResumeUpdate Resume Update Installation On Boot

> Note - Attempting to run the Interactive mode if WU is configured to be solely
non-Interactive, or on a non-Interactive server, should trigger an error
(something along the lines of "AU Can not perform non-interactive scan if AU is
interactive-only").


Recently, I was working with the Windows Update API on Server 2016 and initially
this caused a lot of trouble because patches were installed but were not being
reported properly in the UI. I found this executable by checking out the
following -

> C:\Windows\SoftwareDistribution\ReportingEvents.log


> Task Scheduler -> Microsoft -> Windows -> Update Orchestrator


Hope this helps!

Edit - Thanks Richard (niemiro) for telling about InteractiveScan