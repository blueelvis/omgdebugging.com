+++
title = "Unable to install com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.21 on Azure Databricks"
description = ""
date = 2022-04-15T07:31:51
updated = 2022-04-15T19:10:43
draft = false
slug = "unable-to-install"
aliases = ['2022/04/15/unable-to-install/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I was trying to install the
`com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.21` library from Maven on an
Azure Databricks Cluster which was running `9.1 LTS (includes Apache Spark
3.1.2, Scala 2.12)` version. The cluster was connected to our VNET and the
strange thing was that all the other libraries were getting installed from Maven
correctly but only this was having an issue. Uploading the JAR file manually to
the cluster was also working.

Link to the library -
https://search.maven.org/artifact/com.microsoft.azure/azure-eventhubs-spark_2.12/2.3.21/jar

Whenever I was trying to install the library from Maven, it was giving me the
following error -

Library resolution failed. Cause: java.lang.RuntimeException: javax.mail:mail download failed.
at com.databricks.libraries.server.MavenInstaller.$anonfun$resolveDependencyPaths$5(MavenLibraryResolver.scala:275)
at scala.collection.immutable.HashMap$HashTrieMap.getOrElse0(HashMap.scala:596)
at scala.collection.immutable.HashMap$HashTrieMap.getOrElse0(HashMap.scala:589)
at scala.collection.immutable.HashMap.getOrElse(HashMap.scala:73)
at com.databricks.libraries.server.MavenInstaller.$anonfun$resolveDependencyPaths$4(MavenLibraryResolver.scala:275)
at scala.collection.TraversableLike.$anonfun$map$1(TraversableLike.scala:286)
at scala.collection.mutable.ArraySeq.foreach(ArraySeq.scala:75)
at scala.collection.TraversableLike.map(TraversableLike.scala:286)
at scala.collection.TraversableLike.map$(TraversableLike.scala:279)
at scala.collection.AbstractTraversable.map(Traversable.scala:108)
at com.databricks.libraries.server.MavenInstaller.resolveDependencyPaths(MavenLibraryResolver.scala:271)
at com.databricks.libraries.server.MavenInstaller.doDownloadMavenPackages(MavenLibraryResolver.scala:481)
at com.databricks.libraries.server.MavenInstaller.$anonfun$downloadMavenPackages$3(MavenLibraryResolver.scala:400)
at com.databricks.backend.common.util.FileUtils$.withTemporaryDirectory(FileUtils.scala:468)
at com.databricks.libraries.server.MavenInstaller.$anonfun$downloadMavenPackages$2(MavenLibraryResolver.scala:399)
at com.databricks.logging.UsageLogging.$anonfun$recordOperation$1(UsageLogging.scala:366)
at com.databricks.logging.UsageLogging.executeThunkAndCaptureResultTags$1(UsageLogging.scala:460)
at com.databricks.logging.UsageLogging.$anonfun$recordOperationWithResultTags$4(UsageLogging.scala:480)
at com.databricks.logging.UsageLogging.$anonfun$withAttributionContext$2(UsageLogging.scala:232)
at scala.util.DynamicVariable.withValue(DynamicVariable.scala:62)
at com.databricks.logging.AttributionContext$.withValue(AttributionContext.scala:94)
at com.databricks.logging.UsageLogging.withAttributionContext(UsageLogging.scala:230)
at com.databricks.logging.UsageLogging.withAttributionContext$(UsageLogging.scala:212)
at com.databricks.libraries.server.MavenInstaller.withAttributionContext(MavenLibraryResolver.scala:61)
at com.databricks.logging.UsageLogging.withAttributionTags(UsageLogging.scala:276)
at com.databricks.logging.UsageLogging.withAttributionTags$(UsageLogging.scala:261)
at com.databricks.libraries.server.MavenInstaller.withAttributionTags(MavenLibraryResolver.scala:61)
at com.databricks.logging.UsageLogging.recordOperationWithResultTags(UsageLogging.scala:455)
at com.databricks.logging.UsageLogging.recordOperationWithResultTags$(UsageLogging.scala:375)
at com.databricks.libraries.server.MavenInstaller.recordOperationWithResultTags(MavenLibraryResolver.scala:61)
at com.databricks.logging.UsageLogging.recordOperation(UsageLogging.scala:366)
at com.databricks.logging.UsageLogging.recordOperation$(UsageLogging.scala:338)
at com.databricks.libraries.server.MavenInstaller.recordOperation(MavenLibraryResolver.scala:61)
at com.databricks.libraries.server.MavenInstaller.downloadMavenPackages(MavenLibraryResolver.scala:398)
at com.databricks.libraries.server.MavenInstaller.downloadMavenPackagesWithRetry(MavenLibraryResolver.scala:153)
at com.databricks.libraries.server.MavenInstaller.resolveMavenPackages(MavenLibraryResolver.scala:117)
at com.databricks.libraries.server.MavenLibraryResolver.resolve(MavenLibraryResolver.scala:48)
at com.databricks.libraries.server.ManagedLibraryManager$GenericManagedLibraryResolver.resolve(ManagedLibraryManager.scala:252)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$.$anonfun$resolvePrimitives$1(ManagedLibraryManagerImpl.scala:1226)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$.$anonfun$resolvePrimitives$1$adapted(ManagedLibraryManagerImpl.scala:1221)
at scala.collection.Iterator.foreach(Iterator.scala:943)
at scala.collection.Iterator.foreach$(Iterator.scala:943)
at scala.collection.AbstractIterator.foreach(Iterator.scala:1431)
at scala.collection.IterableLike.foreach(IterableLike.scala:74)
at scala.collection.IterableLike.foreach$(IterableLike.scala:73)
at scala.collection.AbstractIterable.foreach(Iterable.scala:56)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$.resolvePrimitives(ManagedLibraryManagerImpl.scala:1221)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$ClusterStatus.installLibsWithResolution(ManagedLibraryManagerImpl.scala:723)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$ClusterStatus.installLibs(ManagedLibraryManagerImpl.scala:709)
at com.databricks.libraries.server.ManagedLibraryManagerImpl$InstallLibTask$1.run(ManagedLibraryManagerImpl.scala:390)
at com.databricks.threading.NamedExecutor$$anon$2.$anonfun$run$1(NamedExecutor.scala:359)
at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
at com.databricks.logging.UsageLogging.$anonfun$withAttributionContext$2(UsageLogging.scala:232)
at scala.util.DynamicVariable.withValue(DynamicVariable.scala:62)
at com.databricks.logging.AttributionContext$.withValue(AttributionContext.scala:94)
at com.databricks.logging.UsageLogging.withAttributionContext(UsageLogging.scala:230)
at com.databricks.logging.UsageLogging.withAttributionContext$(UsageLogging.scala:212)
at com.databricks.threading.NamedExecutor.withAttributionContext(NamedExecutor.scala:287)
at com.databricks.threading.NamedExecutor$$anon$2.run(NamedExecutor.scala:358)
at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
at java.base/java.lang.Thread.run(Thread.java:834)


After checking all the Firewall rules, the support rep from Microsoft said that
it was working on his cluster.

So, in the end, the solution was to simply delete the cluster and recreate it.
This is the first time I have seen the old adage "Reboot or Recreate" work.

Till next time!