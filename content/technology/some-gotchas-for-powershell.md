---
title: "Some Gotcha's for PowerShell!"
date: 2019-04-30T11:12:26+00:00
lastmod: 2019-04-30T11:13:16+00:00
---

I have been working with PowerShell for some time now and I love it! But, every language has its pros and cons. I am using PowerShell v5.1 on Windows 10 Enterprise. What I have noticed is that I encounter some problems which I remember that I had encountered in the past but now, I will be keeping a log so that I don't waste time.

This post serves me as a quick reference on various strange issues which could occur while creating scripts.

- 

If you are writing a Function in PowerShell using the [[cmdletbinding()]](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_cmdletbindingattribute?view=powershell-6) attribute (which I strongly suggest you use) and returning a value, ensure that you are not having any `Write-Output` statement in there because otherwise, whatever you output will be a part of the returned variable. This was pretty tricky to debug as well... You can notice in the image below how this got injected in a hashtable (which caused a lot of deployment failures) - ![Write-Output](/content/images/2019/04/Write-Output.PNG)

- 

When you are importing a module, always use the `-Force` parameter to re-import the module with the changes. When I was developing my custom PowerShell module, the changes were not reflecting for some reason. Forcing the import solved the issue.

I will keep updating this post from time to time so that I don't forget.