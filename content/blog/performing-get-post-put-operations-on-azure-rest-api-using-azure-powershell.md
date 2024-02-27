+++
title = "Making HTTP Requests on Azure REST API using Azure PowerShell"
description = ""
date = 2018-09-16T17:27:17
updated = 2018-09-16T18:57:53
draft = false
slug = "performing-get-post-put-operations-on-azure-rest-api-using-azure-powershell"
aliases = ['2018/09/16/performing-get-post-put-operations-on-azure-rest-api-using-azure-powershell/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "rest", "api", "powershell", "microsoft", "http"]
+++


All of the operations which you perform on Microsoft Azure are backed by a
robust set of APIs. Be it accessing resources via the Portal or invoking
commandlets from Azure Powershell modules, all are powered by Azure REST APIs
behind the scenes.

The problem which happens sometimes is that the Azure PowerShell commandlets get
broken which can take quite some time to get fixed but this is not the case with
the REST endpoints as they are fixed pretty quickly because of the number of
things which depend on them. Furthermore, you can always select the version of
API to target.

In order to consume the Azure REST Api, you would require some setup
[https://blog.jongallant.com/2017/11/azure-rest-apis-postman/] which revolves
around getting a BearerToken from the Azure Active Directory for authentication
& authorization purposes. In this blog post, I will show that once you have
connected (Using Login-AzureRmAccount) your Azure account using the PowerShell
commandlets, it is possible to consume the Azure REST API without the need to
explicitly generate BearerToken.

 1. In order to make a PUT request (Below example is about enabling NSG
    Diagnostics), get the ==Resource Id== of the resource and you could use
    something like -

$nsgId = $subnet.NetworkSecurityGroup.Id

New-AzureRmResource -ResourceId $nsgId + "/providers/microsoft.insights/diagnosticSettings/service") -Properties $azureDiagnosticsRestApiPayload -IsFullObject -ApiVersion "2017-05-01-preview" -Force -Confirm:$false


The $azureDiagnosticsRestApiPayload is a hashtable containing the properties
which are needed for the operation. You would have to consult the API reference
over here [https://docs.microsoft.com/en-us/rest/api/azure/] to get the correct
API Version because otherwise, you might receive a PATH not found error. I had
issues with Set-AzureRmResource in some cases like creating a new diagnostic
setting for an NSG and hence had to resort to New-AzureRmResource. It simply
failed with the following -

2. In order to make a GET request on a resource,

$nsgId = $subnet.NetworkSecurityGroup.Id

Get-AzureRmResource -ResourceId $nsgId -ApiVersion "2017-05-01-preview"

3. To make a DELETE request on a resource,

$nsgId = $subnet.NetworkSecurityGroup.Id

Remove-AzureRmResource -ResourceId $nsgId -ApiVersion "2017-05-01-preview"

4. To make a POST request on a resource, you can use the following code sample.
Please do note that, the URI which is hit is the string concatenation of value
of ResourceId & value of Action so you would have to play a bit to get the
correct URI.

$nsgId = $subnet.NetworkSecurityGroup.Id

Invoke-AzureRmResourceAction -Action "Microsoft.Insights/DiagnosticSettings/Write/mysetting" -Parameters $azureDiagnosticsRestApiPayload -ResourceId $nsgId -ApiVersion "2017-05-01-preview"

5. To make a PATCH (which basically means update a few properties on an existing
resource) request on a resource,

$nsgId = $subnet.NetworkSecurityGroup.Id

Set-AzureRmResource -ResourceId $nsgId + "/providers/microsoft.insights/diagnosticSettings/service") -Properties $azureDiagnosticsRestApiPayload -UsePatchSemantics -ApiVersion "2017-05-01-preview"



These methods should cover the majority of the work but there are a couple like 
HEAD of which I am not aware of.

Oh and one nice handy tip while debugging these is use the -Debug switch. 

Till next time!