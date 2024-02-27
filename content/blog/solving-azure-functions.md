+++
title = "Solving Azure Functions - \"cannot find function:\" with Event Grid Trigger"
description = ""
date = 2019-03-17T20:17:54
updated = 2019-03-17T20:50:50
draft = false
slug = "solving-azure-functions"
aliases = ['2019/03/17/solving-azure-functions/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "functions", "microsoft", "event grid", "storage account", "kudu"]
+++


Well well well... 2 posts in 1 day! (Pats myself on back...)

I have been trying to automate the provisioning and deployments of Azure
Functions using ARM Templates & PowerShell scripts for quite some time and this
error literally took few hours of my time. Anyways, time spent to solve an issue
is never wasted ;)

You might know that in order to register an Azure Event Grid subscription with
the Azure Function, it requires an endpoint. In my case, I was using the WebHook 
endpoint type. In this type of endpoint, the Event Grid validates the endpoint
before it starts delivering the messages. More information over here
[https://docs.microsoft.com/en-us/azure/event-grid/security-authentication#webhook-event-delivery]
.

I was also sure that I was using the correct endpoint format for the V2 Function
Trigger -
https://{functionappname}.azurewebsites.net/runtime/webhooks/eventgrid?functionName={functionname}&code={systemkey}

I tried using Postman to send a POST request but that was giving me the error as
mentioned above -


If the function was working as expected, it would have returned an HTTP 400 BAD
Request and not HTTP 404 NOT FOUND. Even trying to subscribe using the Azure
Portal was giving the same issue.

After spending quite some time trying to sync triggers, rebooting the app and
what not, I turned to Kudu's (Thanks Kudu for saving me!!!) Logfiles folder.
From there, I navigated to this path - Application\Functions\Host. After
invoking the function, a log file was generated with this format -
"2019-03-17T19-11-29Z-7f6b22cf89.log". On opening that log file, I saw one
particular thing -

2019-03-17T19:11:29.297 [Information] Host Status: {
  "id": "omgdebugging",
  "state": "Running",
  "version": "2.0.12342.0",
  "versionDetails": "2.0.12342.0 Commit hash: 283114581dddb53d7d072265cfbca4c8154770ea"
}
2019-03-17T19:12:31.650 [Information] cannot find function: 'FuncReceiveRawSpendBlob', available function names: []
2019-03-17T19:20:04.848 [Information] Stopping JobHost
2019-03-17T19:20:04.865 [Information] Job host stopped
2019-03-17T19:20:28.432 [Error] Error indexing method 'FuncReceiveRawSpendBlob'
Microsoft.Azure.WebJobs.Host.Indexers.FunctionIndexingException : Error indexing method 'FuncReceiveRawSpendBlob' ---> System.InvalidOperationException : Storage account 'Storage' is not configured.
   at Microsoft.Azure.WebJobs.StorageAccountProvider.Get(String name) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Extensions.Storage\StorageAccountProvider.cs : 43
   at Microsoft.Azure.WebJobs.StorageAccountProvider.Get(String name,INameResolver resolver) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Extensions.Storage\StorageAccountProvider.cs : 28
   at Microsoft.Azure.WebJobs.Host.Blobs.Bindings.BlobsExtensionConfigProvider.GetClientAsync(BlobAttribute blobAttribute,CancellationToken cancellationToken) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Extensions.Storage\Blobs\Config\BlobsExtensionConfigProvider.cs : 292
   at Microsoft.Azure.WebJobs.Host.Blobs.Bindings.BlobsExtensionConfigProvider.<>c__DisplayClass23_0.<ToBlobDescr>b__0() at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Extensions.Storage\Blobs\Config\BlobsExtensionConfigProvider.cs : 334
   at System.Threading.Tasks.Task`1.InnerInvoke()
   at System.Threading.Tasks.Task.<>c.<.cctor>b__278_1(Object obj)
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext,ContextCallback callback,Object state)
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext,ContextCallback callback,Object state)
   at System.Threading.Tasks.Task.ExecuteWithThreadLocal(Task& currentTaskSlot)
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at Microsoft.Azure.WebJobs.Host.Blobs.Bindings.BlobsExtensionConfigProvider.ToBlobDescr(BlobAttribute attr,ParameterInfo parameter,INameResolver nameResolver) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Extensions.Storage\Blobs\Config\BlobsExtensionConfigProvider.cs : 334
   at Microsoft.Azure.WebJobs.Host.Bindings.BindToInputBindingProvider`2.ExactBinding.TryBuild(BindToInputBindingProvider`2 parent,BindingProviderContext context) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Bindings\BindingProviders\BindToInputBindingProvider.cs : 190
   at Microsoft.Azure.WebJobs.Host.Bindings.BindToInputBindingProvider`2.TryCreateAsync(BindingProviderContext context) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Bindings\BindingProviders\BindToInputBindingProvider.cs : 54
   at async Microsoft.Azure.WebJobs.Host.Bindings.GenericCompositeBindingProvider`1.TryCreateAsync[TAttribute](BindingProviderContext context) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Bindings\BindingProviders\GenericCompositeBindingProvider.cs : 61
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at async Microsoft.Azure.WebJobs.Host.Bindings.CompositeBindingProvider.TryCreateAsync(BindingProviderContext context) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Bindings\BindingProviders\CompositeBindingProvider.cs : 25
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at async Microsoft.Azure.WebJobs.Host.Indexers.FunctionIndexer.IndexMethodAsyncCore(MethodInfo method,IFunctionIndexCollector index,CancellationToken cancellationToken) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Indexers\FunctionIndexer.cs : 252
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at async Microsoft.Azure.WebJobs.Host.Indexers.FunctionIndexer.IndexMethodAsync(MethodInfo method,IFunctionIndexCollector index,CancellationToken cancellationToken) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Indexers\FunctionIndexer.cs : 167 
   End of inner exception
   at async Microsoft.Azure.WebJobs.Host.Indexers.FunctionIndexer.IndexMethodAsync(MethodInfo method,IFunctionIndexCollector index,CancellationToken cancellationToken) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Indexers\FunctionIndexer.cs : 175
   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   at async Microsoft.Azure.WebJobs.Host.Indexers.FunctionIndexer.IndexTypeAsync(Type type,IFunctionIndexCollector index,CancellationToken cancellationToken) at C:\projects\azure-webjobs-sdk-rqm4t\src\Microsoft.Azure.WebJobs.Host\Indexers\FunctionIndexer.cs : 103
2019-03-17T19:20:27.450 [Information] registered EventGrid Endpoint = https://omgdebugging.azurewebsites.net/runtime/webhooks/eventgrid
2019-03-17T19:20:27.678 [Information] Initializing Host.
2019-03-17T19:20:27.679 [Information] Host initialization: ConsecutiveErrors=0, StartupCount=1
2019-03-17T19:20:27.746 [Information] LoggerFilterOptions
{
  "MinLevel": "None",
  "Rules": [
    {
      "ProviderName": null,
      "CategoryName": null,
      "LogLevel": null,
      "Filter": "<AddFilter>b__0"
    },
    {
      "ProviderName": "Microsoft.Azure.WebJobs.Script.WebHost.Diagnostics.SystemLoggerProvider",
      "CategoryName": null,
      "LogLevel": "None",
      "Filter": null
    },
    {
      "ProviderName": "Microsoft.Azure.WebJobs.Script.WebHost.Diagnostics.SystemLoggerProvider",
      "CategoryName": null,
      "LogLevel": null,
      "Filter": "<AddFilter>b__0"
    }
  ]
}
2019-03-17T19:20:27.746 [Information] FunctionResultAggregatorOptions
{
  "BatchSize": 1000,
  "FlushTimeout": "00:00:30",
  "IsEnabled": true
}
2019-03-17T19:20:27.746 [Information] SingletonOptions
{
  "LockPeriod": "00:00:15",
  "ListenerLockPeriod": "00:00:15",
  "LockAcquisitionTimeout": "10675199.02:48:05.4775807",
  "LockAcquisitionPollingInterval": "00:00:05",
  "ListenerLockRecoveryPollingInterval": "00:01:00"
}
2019-03-17T19:20:27.754 [Information] Starting JobHost
2019-03-17T19:20:27.758 [Information] Starting Host (HostId=omgdebugging, InstanceId=f79d44de-a684-4af3-96dd-c0ae193fd4ab, Version=2.0.12342.0, ProcessId=8176, AppDomainId=1, InDebugMode=True, InDiagnosticMode=False, FunctionsExtensionVersion=~2)
2019-03-17T19:20:27.785 [Information] Loading functions metadata
2019-03-17T19:20:27.921 [Information] 1 functions loaded
2019-03-17T19:20:28.148 [Information] Generating 1 job function(s)
2019-03-17T19:20:28.472 ==[Warning] Function 'FuncReceiveRawSpendBlob' failed indexing and will be disabled.==
2019-03-17T19:20:28.473 [Warning] No job functions found. Try making your job classes and methods public. If you're using binding extensions (e.g. Azure Storage, ServiceBus, Timers, etc.) make sure you've called the registration method for the extension(s) in your startup code (e.g. builder.AddAzureStorage(), builder.AddServiceBus(), builder.AddTimers(), etc.).
2019-03-17T19:20:28.473 [Information] Host initialized (708ms)
2019-03-17T19:20:28.481 [Information] Host started (717ms)
2019-03-17T19:20:28.481 [Information] Job host started
2019-03-17T19:20:29.536 [Information] cannot find function: 'FuncReceiveRawSpendBlob', available function names: []


Hmm... That's strange. Storage account 'Storage' is not configured.? After
comparing with a newly deployed function, I found that I had missed adding the 
AzureWebJobsStorage Application Setting with the connection string to a storage
account. After adding that, it started working immediately...

Pro Tips --
 1. If you are trying to automate the deployment of Azure Functions with Event
    Grid using ARM, ensure that you set both AzureWebJobsStorage & 
    AzureWebJobsSecretStorageType = Files because of an issue described over 
    here
    [https://github.com/Azure/azure-functions-host/wiki/Changes-to-Key-Management-in-Functions-V2]
    .
 2. The best way as of writing this is to get the Master key of the Function
    Host and then use that as code in the above Function Event Grid Endpoint.
    You would have to authenticate with Kudu to retreive the Master token.