+++
title = "Convert a PSObject to a Hashtable in PowerShell"
description = ""
date = 2019-02-25T12:15:11
updated = 2019-02-25T12:16:52
draft = false
slug = "convert-a-psobject-to-a-hashtable-in-powershell"
aliases = ['2019/02/25/convert-a-psobject-to-a-hashtable-in-powershell/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This is just for myself when I forget in the future...

An object returned by the ConvertFrom-JSON usually returns a PSObject but I need
a hash table to properly manipulate and easily pass the hashtable to be consumed
by the ARM Template as a parameter.

function ConvertTo-HashtableFromPsCustomObject { 
    param ( 
        [Parameter(  
            Position = 0,   
            Mandatory = $true,   
            ValueFromPipeline = $true,  
            ValueFromPipelineByPropertyName = $true  
        )] [object] $psCustomObject 
    );
    Write-Verbose "[Start]:: ConvertTo-HashtableFromPsCustomObject"

    $output = @{}; 
    $psCustomObject | Get-Member -MemberType *Property | % {
        $output.($_.name) = $psCustomObject.($_.name); 
    } 
    
    Write-Verbose "[Exit]:: ConvertTo-HashtableFromPsCustomObject"

    return  $output;
}