---
title: "Gotchas for Azure Web App For Containers!"
date: 2018-01-23T22:30:35+00:00
lastmod: 2018-08-22T08:21:16+00:00
---

Recently, I have been spending a lot of time doing deployments and performing migrations to Azure Web App for Containers. Following are some of the gotchas which I have found after a lot of search and I hope are helpful to you as well.

- Local Git deployment to KUDU SCM GIT Url always needs to point to `master` branch

In other words, when you have setup a local git repository as your `Deployment Source`, always ensure that you push to the master branch in the remote. For example `git push azure <local_branch_name>:master` where `master` is the remote Azure Git Branch.

- 

Always set the =WEBSITES_ENABLE_APP_SERVICE_STORAGE= and set it to `true` in App Settings.

- 

During the Build/Release process for deploying from `Local Git` as a deployment option use `git config http.postBuffer 524288000`. This helps out a lot in projects with large number of repository files and considerably speeds up the process.

- 

Kudu Deployment script utilizes the App Settings as it is. You don't need to prepend `APPSETTING_` to access them.

I will keep updating this document as I find more so stay tuned!