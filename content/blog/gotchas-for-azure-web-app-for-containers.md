+++
title = "Gotchas for Azure Web App For Containers!"
description = ""
date = 2018-01-23T21:07:55
updated = 2018-08-22T08:21:16
draft = false
slug = "gotchas-for-azure-web-app-for-containers"
aliases = ['2018/01/23/gotchas-for-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Recently, I have been spending a lot of time doing deployments and performing
migrations to Azure Web App for Containers. Following are some of the gotchas
which I have found after a lot of search and I hope are helpful to you as well.

 1. Local Git deployment to KUDU SCM GIT Url always needs to point to master 
    branch

In other words, when you have setup a local git repository as your Deployment
Source, always ensure that you push to the master branch in the remote. For
example git push azure <local_branch_name>:master where master is the remote
Azure Git Branch.

 2. Always set the =WEBSITES_ENABLE_APP_SERVICE_STORAGE= and set it to true in
    App Settings.
    
    
 3. During the Build/Release process for deploying from Local Git as a
    deployment option use git config http.postBuffer 524288000. This helps out a
    lot in projects with large number of repository files and considerably
    speeds up the process.
    
    
 4. Kudu Deployment script utilizes the App Settings as it is. You don't need to
    prepend APPSETTING_ to access them.
    
    

I will keep updating this document as I find more so stay tuned!