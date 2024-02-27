+++
title = "Splunk KV Store process terminated abnormally (exit code 100, status exited with code 100)"
description = ""
date = 2019-08-22T11:06:05
updated = 2019-08-22T12:23:10
draft = false
slug = "splunk-kv-store-process-terminated-abnormally-exit-code-100-status-exited-with-code-100"
aliases = ['2019/08/22/splunk-kv-store-process-terminated-abnormally-exit-code-100-status-exited-with-code-100/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Howdy!

I was doing Splunk development (On Windows) for External Lookups when I
encountered this issue. I like to turn off the Splunkd service so that it
doesn't keep on consuming my precious resources.

I started the service like normal after a few days and I saw the following after
logging in -


This was pretty strange as to why it started happening all of a sudden when it
was working previously. I started going through the logs as mentioned in the
screenshot (splunkd.log & mongod.log). These logs are located in 
%SPLUNK_HOME%/var/log/splunk.

Interesting snippets from the logs -

08-22-2019 16:22:19.408 +0530 ERROR KVStoreConfigurationProvider - Could not get ping from mongod. 
08-22-2019 16:22:19.408 +0530 ERROR KVStoreConfigurationProvider - Could not start mongo instance. Initialization failed.
08-22-2019 16:22:19.408 +0530 ERROR KVStoreBulletinBoardManager - Failed to start KV Store process. See mongod.log and splunkd.log for details.
08-22-2019 16:22:27.791 +0530 WARN  MultiFactorAuthManager - Multi Factor Authentication is not supported by this license
08-22-2019 16:22:30.110 +0530 WARN  HttpListener - Socket error from 127.0.0.1 while accessing /en-US/static/@5a7a840afcb3/img/skins/default/loading_medium_green.png: Winsock error 10053


 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] MongoDB starting : pid=12324 port=8191 dbpath=C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo 64-bit host=DESKTOP-7RDHA6M
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] targetMinOS: Windows 7/Windows Server 2008 R2
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] db version v3.4.10-splunk
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] git version: 078f28920cb24de0dd479b5ea6c66c644f6326e9
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2o-fips  27 Mar 2018
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] allocator: tcmalloc
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] modules: none
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] build environment:
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten]     distmod: 2008plus-ssl
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten]     distarch: x86_64
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten]     target_arch: x86_64
 2019-08-22T10:45:45.303Z I CONTROL  [initandlisten] options: { net: { port: 8191, ssl: { PEMKeyFile: "C:\Program Files\Splunk\etc\auth\server.pem", PEMKeyPassword: "<password>", allowInvalidHostnames: true, disabledProtocols: "noTLS1_0,noTLS1_1", mode: "requireSSL", sslCipherConfig: "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RS..." } }, replication: { oplogSizeMB: 200, replSet: "7270A617-724D-40B8-948F-D03909CBD852" }, security: { javascriptEnabled: false, keyFile: "C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo\splunk.key" }, setParameter: { enableLocalhostAuthBypass: "0", oplogFetcherMaxFetcherRestarts: "0" }, storage: { dbPath: "C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo", engine: "mmapv1", mmapv1: { smallFiles: true } }, systemLog: { timeStampFormat: "iso8601-utc" } }
 2019-08-22T10:45:45.310Z W -        [initandlisten] Detected unclean shutdown - C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo\mongod.lock is not empty.
 2019-08-22T10:45:45.337Z I JOURNAL  [initandlisten] journal dir=C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo\journal
 2019-08-22T10:45:45.338Z I JOURNAL  [initandlisten] recover begin
 2019-08-22T10:45:45.338Z I STORAGE  [initandlisten] In File::open(), CreateFileW for 'C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo\journal\lsn' failed with Access is denied.
 2019-08-22T10:45:45.338Z I -        [initandlisten] Assertion failure f.is_open() src\mongo\db\storage\mmap_v1\dur_journal.cpp 599
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x1dc493
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x177418
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x169fb3
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      ???
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x7bef18
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x7c0fc7
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x7c29f6
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x7c4425
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] mongod.exe      index_collator_extension+0x7e70e5
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] KERNEL32.DLL    BaseThreadInitThunk+0x14
 2019-08-22T10:45:45.344Z I CONTROL  [initandlisten] 
 2019-08-22T10:45:45.347Z F JOURNAL  [initandlisten] dbexception during recovery: 13611 can't read lsn file in journal directory : assertion src\mongo\db\storage\mmap_v1\dur_journal.cpp:599
 2019-08-22T10:45:45.348Z I STORAGE  [initandlisten] exception in initAndListen: 13611 can't read lsn file in journal directory : assertion src\mongo\db\storage\mmap_v1\dur_journal.cpp:599, terminating
 2019-08-22T10:45:45.348Z I NETWORK  [initandlisten] shutdown: going to close listening sockets...
 2019-08-22T10:45:45.348Z I NETWORK  [initandlisten] shutdown: going to flush diaglog...
 2019-08-22T10:45:45.348Z I REPL     [initandlisten] shutting down replication subsystems
 2019-08-22T10:45:45.348Z W REPL     [initandlisten] ReplicationCoordinatorImpl::shutdown() called before startup() finished.  Shutting down without cleaning up the replication system
 2019-08-22T10:45:45.348Z I STORAGE  [initandlisten] shutdown: waiting for fs preallocator...
 2019-08-22T10:45:45.348Z I STORAGE  [initandlisten] shutdown: final commit...
 2019-08-22T10:45:45.348Z I STORAGE  [initandlisten] shutdown: closing all files...
 2019-08-22T10:45:45.349Z I STORAGE  [initandlisten] closeAllFiles() finished
 2019-08-22T10:45:45.349Z I CONTROL  [initandlisten] now exiting
 2019-08-22T10:45:45.349Z I CONTROL  [initandlisten] shutting down with code:100


As you can see, the Mongo DB instance is not able to access the file located in 
C:\Program Files\Splunk\var\lib\splunk\kvstore\mongo\journal\lsn

I checked the permissions on the kvstore\mongo\journal folder (& the objects
within) and strangely I saw only my user who had the permissions.


Well, now I know the problem, I turned out to Process Monitor (Procmon!) to see
who was the user which was being used by Splunk to access this file -


After seeing that, I gave full permissions on this folder - 
%SPLUNK_HOME%\var\lib\splunk\kvstore\mongo\ to the SYSTEM user and restarted
Splunk which fixed the issue!

Till next time!