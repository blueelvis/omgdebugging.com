+++
title = "BSOD - Kernel_Data_Inpage_Error / Page_Fault_In_Nonpaged_Area"
description = ""
date = 2014-10-19T01:16:05
updated = 2018-08-22T08:21:16
draft = false
slug = "bsod-kernel_data_inpage_error-page_fault_in_nonpaged_area"
aliases = ['2014/10/19/bsod-kernel_data_inpage_error-page_fault_in_nonpaged_area/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["case", "Debugging", "Windows"]
+++




BugCheck Codes –

 * Kernel_Data_Inpage_Error (0x7a)
 * Page_Fault_In_NonPaged_Area (0x50)

Issues Faced by OP –

 * Lots of bad sector errors in the Event Log
 * Random BSODs
 * Used chkdsk /f /r but this did not fix the issue.

What Fixed The Problem –

[quote]Then please run the following DISM commands to see if there’s any
problems with the system (from an elevated (Run as administrator) Command
Prompt). Press Enter after each one:
Code:[code]

Dism /Online /Cleanup-Image /ScanHealth
[/code]Code:[code]

Dism /Online /Cleanup-Image /CheckHealth
[/code]If the problem is fixable, you can use this command to repair it (from an
elevated (Run as administrator) Command Prompt). Press Enter after typing it:
Code:[code]

Dism /Online /Cleanup-Image /RestoreHealth
[/code]From this article: Repair a Windows Image
[http://technet.microsoft.com/en-us/library/hh824869.aspx]

Once this is done, also run sfc.exe /scannow from an elevated (Run as
administrator) Command Prompt to check for further corruption.[/quote]



Link – 
http://www.eightforums.com/bsod-crashes-debugging/55624-bsod-windows-8-1-inpage-errors.html