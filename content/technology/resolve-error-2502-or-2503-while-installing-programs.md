---
title: "Resolve Error 2502 or 2503 While Installing Programs"
date: 2015-10-15T10:23:43+00:00
lastmod: 2018-08-22T08:21:16+00:00
feature_image: "http://omgdebugging.com/wp-content/uploads/2015/10/Post-Image.png"
tags: ["2502", "2503", "Error", "Windows"]
---

Recently while trying to install programs, I started getting the **Error 2502** pop-up which was followed by **Error 2503**. The pop-up for Error 2503 followed Error 2502.

The problem occurs because of permission issues. In order to resolve the permission issues for Executable (.EXE) is –

- Right click on the Executable.
- **Run as Administrator**

Unfortunately, the program which I was trying to install had its installation files wrapped in a **MSI** installer. The problem was that on Right Clicking the executable, I did not find any option to run the file as Administrator. So, to resolve this, what I did was to put the MSI installer file in the **C: drive** and then launch the executable from a **Command Prompt (CMD.exe)** which had Administrator Privileges.

Hope this helps.