+++
title = "Unable to start/init Azure Storage Emulator after fresh installation"
description = ""
date = 2021-10-01T10:37:40
updated = 2021-10-01T11:06:49
draft = false
slug = "unable-to-start-init-azure-storage-emulator"
aliases = ['2021/10/01/unable-to-start-init-azure-storage-emulator/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "azure storage emulator"]
+++


Azure Storage Emulator is an important piece of my developer toolkit and I
recently got a new laptop from work and while I was getting it setup, I
installed the Azure Storage Emulator from the official download page over here
[https://docs.microsoft.com/en-us/azure/storage/common/storage-use-emulator].

You could argue why I am not using the latest Azurite
[https://github.com/Azure/Azurite] which is now recommended by Microsoft. But,
last time (2-3 months back) I tried it, I ran into issues while trying to run
Azure Durable Functions against it since the Table API didn't support all the
features. Additionally what I like the most with the Storage Emulator is that it
comes as an MSI file so after installation, I know exactly where it is located.

As usual, I installed it and started it only to be greeted with the following -

C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator>AzureStorageEmulator.exe start
Windows Azure Storage Emulator 5.10.0.0 command line tool
Autodetect requested. Autodetecting SQL Instance to use.
Looking for a LocalDB Installation.
Probing SQL Instance: '(localdb)\MSSQLLocalDB'.
Found a LocalDB Installation.
Probing SQL Instance: '(localdb)\MSSQLLocalDB'.
Found SQL Instance (localdb)\MSSQLLocalDB.
Creating database AzureStorageEmulatorDb510 on SQL instance '(localdb)\MSSQLLocalDB'.
Cannot create database 'AzureStorageEmulatorDb510' : The database 'AzureStorageEmulatorDb510' does not exist. Supply a valid database name. To see available databases, use sys.databases..
One or more initialization actions have failed. Resolve these errors before attempting to run the storage emulator again.
Error: The storage emulator needs to be initialized. Please run the 'init' command.


Ideally, it should be creating the database and then populating the schema but
it wasn't doing that. I then tried running the init command manually like it
said and got -

C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator> AzureStorageEmulator.exe init
Windows Azure Storage Emulator 5.10.0.0 command line tool
Found SQL Instance (localdb)\MSSQLLocalDB.
Creating database AzureStorageEmulatorDb510 on SQL instance '(localdb)\MSSQLLocalDB'.

Granting database access to user LOCAL\Pranav.Jituri.
Database access for user LOCAL\Pranav.Jituri was granted.

Initialization successful. The storage emulator is now ready for use.
The storage emulator was successfully initialized and is ready to use.


I then started it again and got the following -

C:\Program Files (x86)\Microsoft SDKs\Azure\Storage Emulator> AzureStorageEmulator.exe start /inprocess
Windows Azure Storage Emulator 5.10.0.0 command line tool
Invalid object name 'dbo.Account'.
Service Status: Blob http://127.0.0.1:10000/ True
Service Status: Queue http://127.0.0.1:10001/ True
Service Status: Table http://127.0.0.1:10002/ True


That gave me a clue to check the database and I didn't see any schema objects
which it generally has.

After troubleshooting for quite some time, I gave up and just decided to get the
DACPAC export of the database from a colleague and import the DACPAC. As soon as
the DACPAC was restored, the Storage Emulator started working.

You can download the DACPAC directly from here
[https://gist.github.com/blueelvis/75464e09b77326fee840c038fd4cc949/raw/e05c546692be4e371b134562a9949c33d094fed3/AzureStorageEmulatorDb510.dacpac]
.