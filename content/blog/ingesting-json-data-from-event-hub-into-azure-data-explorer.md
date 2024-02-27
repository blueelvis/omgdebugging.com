+++
title = "\"Stream_NoDataToIngest\" while ingesting data from Event Hub to Azure Data Explorer"
description = ""
date = 2019-10-07T08:02:53
updated = 2019-10-07T08:24:34
draft = true
slug = "ingesting-json-data-from-event-hub-into-azure-data-explorer"
aliases = ['2019/10/07/ingesting-json-data-from-event-hub-into-azure-data-explorer/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Since a couple of days, I got a chance to finally work with Azure Data Explorer.
Azure Data Explorer is a fast, fully managed data analytics service for
real-time analysis on large volumes of data streaming from applications,
websites, IoT devices, and more.

As part of a recent Proof of Concept, we had to use Azure Data Explorer and
ingest data into it with minimum costs. We also wanted to query the data in
almost real time and the schema of data which was going to come into this was
not well defined. Azure Data Explorer is pretty vast and I will do a separate
blog post to explain it.

For ingestion, there is very little documentation
[https://docs.microsoft.com/en-us/azure/kusto/api/rest/streaming-ingest] on
ingesting via the REST API. The part which is not mentioned in there is that you
need to specifically turn on Streaming Ingestion in the cluster -

The problem with this was that Streaming Ingestion was only supported on
instances with 8 vCPUs or greater
[https://docs.microsoft.com/en-in/azure/data-explorer/ingest-data-streaming#limitations] 
(As of this writing) which costs a lot!

We decided to go with the route of connecting Azure Event Hub -> Azure Data
Explorer and then using the REST API of Event Hubs to send in the data. This was
cheap as compared to streaming ingestion.