---
title: "Solving Operation is Not Valid Due to Current State of Object"
date: 2017-11-28T14:35:16+00:00
lastmod: 2018-08-22T08:21:16+00:00
---

This would be a quick post about solving an error which sometimes occurs while doing a Data/Schema comparison using the SQL Server tools which are available in Visual Studio. I use Visual Studio 2015.

As part of my day, I have to give deployments, do schema changes to a SQL database while ensuring that data is always preserved. Everything was working fine with one database in Azure until I had a requirement to publish the database schema changes to a different database on Azure. I started the usual process (Post coming up soon on this one as well...) but on doing Data Comparison, I started getting the following error -

![](/content/images/2017/11/2017-11-28.png)

The error was stated the following -

> > Data Information could not be retrieved because of the following error:

> > Operation is not valid due to the current state of the object.

I tried restarting the system, creating a fresh database in Azure but nothing worked. Strange thing was that on the same Azure SQL Server there was another database where this comparison worked fine.

In order to resolve this issue, follow the below steps -

- 

Uninstall the following products from your system (*appwiz.cpl* for latest Windows 10 build) -

Microsoft SQL Server Data-Tier Application Framework (x64)
- Microsoft SQL Server Data-Tier Application Framework (x86)

- 

Now, go over [here](https://www.microsoft.com/download/details.aspx?id=56048) and download the latest Microsoft® SQL Server® Data-Tier Application Framework. Ensure that you download and install both x64 and x86 versions on your machine.

- 

Once the above packages are installed, go over [here ](https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt) and download the latest version of SQL Server Data Tools depending on the version of Visual Studio installed on your system.

- 

I installed the package using the pre-selected defaults.

- 

Reboot the system. This is an important step to ensure the cache is cleared.

Following the above steps solved the problem for me.

==*Tip* - While performing schema change and data update operations using these tools, always take 2 backups. Before doing any operation on the production database, ensure that you perform the operation first on one of the backed up databases. This ensures that partial update don't happen on production DBs saving you a lot of time ;) ==

Till next time...