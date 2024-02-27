+++
title = "Npgsql: 42P01: relation \"helloworld\" does not exist"
description = ""
date = 2023-12-14T11:22:20
updated = 2023-12-14T11:44:25
draft = false
slug = "npgsql-42p01-relation-helloworld-does-not-exist"
aliases = ['2023/12/14/npgsql-42p01-relation-helloworld-does-not-exist/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


[2023-12-14T11:26:50.419Z] Executed 'LoginDumper' (Failed, Id=51a219ad-31f0-4477-9c36-cf06ad8efcbe, Duration=5100ms)
[2023-12-14T11:26:50.429Z] System.Private.CoreLib: Exception while executing function: LoginDumper. Npgsql: 42P01: relation "helloworld" does not exist
[2023-12-14T11:26:50.433Z]
[2023-12-14T11:26:50.436Z] POSITION: 13.


This is a post for myself because I know that I am going to forget this again. I
started getting the above message for the following command even though I can
see the table existing in pgAdmin with the exact same case -

await _dbContext.Database.ExecuteSqlRawAsync("DELETE FROM HelloWorld;");




Turns out, in PostgreSQL world, if you don't double quote the name of the table,
or even the name of the columns, it will automatically change it to lowercase
and since the database engine itself is case-sensitive, it results in the above
error message.

This is pretty surprising for me since I come from the Microsoft SQL Server
world where this won't be an issue.

Changing the above statement to the following fixed the issue -

await _dbContext.Database.ExecuteSqlRawAsync("DELETE FROM \"HelloWorld\";");


On the bright side, Entity Framework Core has introduced bulk deletions and
updates
[https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-7.0/whatsnew#executeupdate-and-executedelete-bulk-updates] 
(Source [https://stackoverflow.com/a/15220460/2758198]) so I only have to deal
with this till I don't upgrade my project to use the latest EF Core.