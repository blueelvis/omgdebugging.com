+++
title = "Debugging \"Microsoft.EntityFrameworkCore: A second operation was started on this context instance before a previous operation completed.\""
description = ""
date = 2023-12-15T08:02:26
updated = 2023-12-15T09:05:44
draft = false
slug = "debugging"
aliases = ['2023/12/15/debugging/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


For almost an year I have been working on a Trading bot which does all the
shenanigans of placing orders, checking them, creating stop loss orders as per
my strategies.
Since this was a personal project, I wanted to keep the costs as low as possible
and hence decided to use Azure Functions
[https://azure.microsoft.com/en-in/products/functions] (Azure has a very
generous free tier for Azure Functions) along with Azure Storage Account File
Shares
[https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-portal?tabs=azure-portal] 
to save persistent data. Because of the free tier, I run my code for free and I
have to shell out few Rupees for data storage.

I also decided to use SQLite [https://www.sqlite.org/index.html] as my database
because during the time of starting, I checked out few managed databases but
they were not in my budget and hosting my own database meant too much
operational overhead.

This database kept on working fine until I added more strategies which started
delaying the execution of the Functions by several minutes which started causing
irregularities as compared to the backtest. Also, the performance issue is
because whenever the Function decides to read from this database, it has to
query Azure Files which is not meant for very fast transactions.

This is when I decided to switch over to a self hosted Postgresql database
hosted in a droplet from DigitalOcean. (Now, my bot is managing decent money so
decided that it is worth the switch).

As I was using Entity Framework for all my database operations, I switched the
following -

builder.Services.AddDbContext<BotDbContext>(options =>
                options
                .EnableDetailedErrors()
                .UseSqlite(dbConnectionString)
            );


to

builder.Services.AddDbContext<BotDbContext>(options =>
                options
                .EnableSensitiveDataLogging(true)
                .EnableDetailedErrors()
                .UseNpgsql(dbConnectionString)
            );


I was expecting this to work without any issues but as soon as my bot executed
one strategy while testing, I got the following -

[2023-12-15T07:19:51.956Z] Host started (1287ms)
[2023-12-15T07:19:51.959Z] Job host started
[2023-12-15T07:19:55.326Z] Host lock lease acquired by instance ID '00000000000000000000000094310C57'.
[2023-12-15T07:20:28.563Z] Executing HTTP request: {
[2023-12-15T07:20:28.567Z]   requestId: "3cff1941-7ca2-4b8f-9cb4-68f05ef6ea19",
[2023-12-15T07:20:28.571Z]   method: "POST",
[2023-12-15T07:20:28.573Z]   userAgent: "PostmanRuntime/7.36.0",
[2023-12-15T07:20:28.574Z]   uri: "/admin/functions/Strangle"
[2023-12-15T07:20:28.576Z] }
[2023-12-15T07:20:29.184Z] Executed HTTP request: {
[2023-12-15T07:20:29.187Z]   requestId: "3cff1941-7ca2-4b8f-9cb4-68f05ef6ea19",
[2023-12-15T07:20:29.189Z]   identities: "(WebJobsAuthLevel:Admin, WebJobsAuthLevel:Admin)",
[2023-12-15T07:20:29.191Z]   status: "202",
[2023-12-15T07:20:29.193Z]   duration: "617"
[2023-12-15T07:20:29.195Z] }
[2023-12-15T07:20:29.756Z] Executing 'Strangle' (Reason='This function was programmatically called via the host APIs.', Id=fc03253f-50f3-4622-a840-df60c3f5b142)
[2023-12-15T07:20:34.307Z] Strangle function started at: 15-12-2023 12:50:34
[2023-12-15T07:20:46.610Z] Executed 'Strangle' (Failed, Id=fc03253f-50f3-4622-a840-df60c3f5b142, Duration=17396ms)
[2023-12-15T07:20:46.614Z] System.Private.CoreLib: Exception while executing function: Strangle. Microsoft.EntityFrameworkCore: A second operation was started on this context instance before a previous operation completed. This is usually caused by different threads concurrently using the same instance of DbContext. For more information on how to avoid threading issues with DbContext, see https://go.microsoft.com/fwlink/?linkid=2097913.


That's strange.

I have seen this issue and if you also see here
[https://go.microsoft.com/fwlink/?linkid=2097913], it states that there are
multiple operations running on the same DbContext before the previous ones are
completed. This means that there is an await missing for an async function call.

You know what this calls for? Debugging step by step to see where it is missing.
Within minutes, I found the offending code block -

var instrumentFromMasterList = _dbContext.Instruments
                    .Where(x => x.TradingSymbol.ToLower() == tradingSymbol.ToLower())
                    .Where(x => x.Exchange.ToLower() == exchange.ToLower())
                    .SingleOrDefaultAsync();


You see that I am calling the SingleOrDefaultAsync but the call is not awaited?
After adding the await, the code started working as expected.

Now, onto why this was not happening with SQLite. Turns out, by default
[https://github.com/dotnet/efcore/issues/5466], SQLite is compiled with the 
Serialized mode [https://www.sqlite.org/threadsafe.html] where multiple calls
are queued and executed one by one. Whereas for Postgresql, this is not the case
and hence Entity Framework started complaining.

Till next time!