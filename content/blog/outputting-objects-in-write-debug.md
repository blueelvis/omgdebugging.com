+++
title = "Outputting Objects in Write-Debug"
description = ""
date = 2018-05-02T11:48:54
updated = 2018-08-22T08:21:16
draft = false
slug = "outputting-objects-in-write-debug"
aliases = ['2018/05/02/outputting-objects-in-write-debug/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


When you are writing PowerShell scripts for the enterprise environment (I will
urge to follow the guideline even when writing personal scripts), you need to
have proper logging to ensure that the script can be debugged in case of any
issues. For such scenarios, we have Write-Verbose (For trace messages) & 
Write-Debug (Generally used to print values of Variables) to print the
information on the Debug Stream.

I use the [cmdletbinding()] with every function I write in PowerShell which
allows to turn on/off the Verbose & Debug messages at the flick of a switch.

As one will find out, Write-Debug does not support outputting a PowerShell
Object and if you try doing it, you will get the following error -

PS C:\Users\Pranav> $DebugPreference = 'Continue'
$assemblies = [appdomain]::currentdomain.getassemblies()

Write-Debug "Currently Loaded Assemblies - "
Write-Debug ($assemblies | Get-Member)
DEBUG: Currently Loaded Assemblies - 
Write-Debug : Cannot convert 'System.Object[]' to the type 'System.String' required by parameter 'Message'. Specified method is not supported.
At line:5 char:13
+ Write-Debug ($assemblies | Get-Member)
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Write-Debug], ParameterBindingException
    + FullyQualifiedErrorId : CannotConvertArgument,Microsoft.PowerShell.Commands.WriteDebugCommand


I found a SO post over here - 
https://stackoverflow.com/questions/6590116/powershells-write-debug-wont-output-arrays-but-write-output-does-is-this-on

The answer said to use Out-String and then pipe the result from this to 
Write-Debug. This was working fine but when you are using [cmdletbinding()] ,
the above answer will ignore the $DebugPreference and still print the Debug
Messages.

To avoid that, you can do something like this -

Write-Debug ([array]$assemblies | Out-String)


You will notice that this is then respected by PowerShell and Debug messages
will only be printed when you have flipped the switch to Debug.