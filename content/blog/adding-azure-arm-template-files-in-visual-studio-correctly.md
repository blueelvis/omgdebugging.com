+++
title = "Adding Azure ARM Template Files in Visual Studio Correctly"
description = ""
date = 2017-08-13T19:51:41
updated = 2018-08-22T08:21:16
draft = false
slug = "adding-azure-arm-template-files-in-visual-studio-correctly"
aliases = ['2017/08/13/adding-azure-arm-template-files-in-visual-studio-correctly/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Recently, I was tasked with a project which dealt with Azure ARM Templates. For
those who don't know, ARM Templates are basically JSON files which allow you to
define infrastructure and then deploy it on Azure. Very similar to AWS
CloudFormation and very awesome. Although debugging the templates is a lot of
pain :(

The basic structure of the project when created in Visual Studio (File -> New
Project -> Templates -> Visual C# -> Cloud -> Azure Resource Group) is as below
-


Now, when I was working with VS, I had to create several templates to isolate
resources so that debugging is easier. In order to add another template, I
simply right clicked on the Project -> Add -> New Item -> Azure Resource Manager
Deployment Template and clicked on OK. A new template was added. Visual Studio
is kind enough to show you the newly added template when you are trying to
Deploy/Validate the template as per the below screenshot (azuredeploy1.json is
the newly added Deployment Template)


Now, if you select the newly created template file and try to Deploy/Validate,
you would would receive the following error from Visual Studio -
01:34:05 - [ERROR] The running command stopped because the preference variable
"ErrorActionPreference" or common parameter is set to Stop: Could not find file
'c:\users\pranav\documents\visual studio
2015\Projects\AzureResourceGroup2\AzureResourceGroup2\bin\Debug\staging\AzureResourceGroup2\azuredeploy1.json'.
[ERROR] + CategoryInfo : CloseError: (:) [Test-AzureRmResourceGroupDeployment],
FileNotFoundException [ERROR] + FullyQualifiedErrorId :
Microsoft.Azure.Commands.ResourceManager.Cmdlets.Implementation.TestAzureResourceGroupDeploymentCmdlet
01:34:05 - 01:34:05 - Validating template using PowerShell script failed.
01:34:05 - Tell us about your experience at
https://go.microsoft.com/fwlink/?LinkId=691202

Well, that was strange. I right clicked on the file and yes, it was Included In
the Project as well. If you would check the output directory of the project, you
would find that file is not there. It seems that by default Visual Studio was
not adding the file while building the project.

The fix was to right click on the newly added template file -> Properties and
then change the Build Action to Content from None.