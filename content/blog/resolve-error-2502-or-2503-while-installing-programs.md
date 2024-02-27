+++
title = "Resolve Error 2502 or 2503 While Installing Programs"
description = ""
date = 2015-10-15T10:23:43
updated = 2018-08-22T08:21:16
draft = false
slug = "resolve-error-2502-or-2503-while-installing-programs"
aliases = ['2015/10/15/resolve-error-2502-or-2503-while-installing-programs/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["2502", "2503", "Error", "Windows"]
+++


Recently while trying to install programs, I started getting the Error 2502 
pop-up which was followed by Error 2503. The pop-up for Error 2503 followed
Error 2502.

The problem occurs because of permission issues. In order to resolve the
permission issues for Executable (.EXE) is –

 1. Right click on the Executable.
 2. Run as Administrator

Unfortunately, the program which I was trying to install had its installation
files wrapped in a MSI installer. The problem was that on Right Clicking the
executable, I did not find any option to run the file as Administrator. So, to
resolve this, what I did was to put the MSI installer file in the C: drive and
then launch the executable from a Command Prompt (CMD.exe) which had
Administrator Privileges.

Hope this helps.