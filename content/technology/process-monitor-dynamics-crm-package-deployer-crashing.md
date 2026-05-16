---
title: "[Process Monitor] -- Dynamics CRM Package Deployer Crashing"
date: 2018-07-11T19:12:22+00:00
lastmod: 2018-08-22T08:21:16+00:00
---

This would be a pretty short post but I would like to attribute this win to Process Monitor. In my case, I was working with Dynamics CRM Package Deployer. As per the procedure, I copied the Dynamics CRM Package Deployer folder from the SDK and tried running the utility.

My cursor started spinning indicating it was loading something but after few seconds, the utility was not opening up.

![](/content/images/2018/07/iKS5TB0yxa.gif)

Well that was strange since there was no error message and the process was not even staying in Task Manager long enough for me to see it. At this point, I was not sure whether the task was even running or was it crashing at startup.

If you have watched the Sysinternals talks by Mark Russinovich, there's a motto which he says - `Keep calm & run procmon`. I recorded a trace of the problem and saw the following -

![](/content/images/2018/07/Procmon-CRMPackageDeployer.PNG)

There are too many `WerFault.exe` entries which means that the program was crashing. I fired up Event Viewer and checked the `Windows Logs -> Application` section and I found the below error -

![](/content/images/2018/07/CRMPackageDeployer-EventLogError.PNG)

And there you have it - `System.IO.FileNotFoundException` which in other words means that the tool was searching for a file which was not available. I copied all the files again and it started working. (Most likely some file was not copied or I over wrote it during copying other folders...)

Having Process Monitor with me on my Desktop generally saves me from such issues. Ironically, it took me around 20 minutes to write this but took just 5 minutes to solve the problem which otherwise could have easily eaten up more than that!