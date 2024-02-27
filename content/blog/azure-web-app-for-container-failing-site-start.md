+++
title = "Azure Web App For Container failing site start"
description = ""
date = 2017-12-22T19:49:12
updated = 2018-08-22T08:21:16
draft = false
slug = "azure-web-app-for-container-failing-site-start"
aliases = ['2017/12/22/azure-web-app-for-container-failing-site-start/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This happened with me where I was working with Docker on Windows & then pushing
the image to Azure Container Registry which in turn was being used by Azure Web
App for Containers. This post also serves as reminder to me :0) for future.

After performing some updates to the DockerFile (I did a git clone from a Github
repository) and pushing the new docker image to ACR, I started seeing the
following error in Kudu Docker Logs with the container refusing to start up -

> 2017-12-22 19:40:17.976 INFO - Starting container for site
2017-12-22 19:40:17.976 INFO - docker run -d -p 47885:80 --name linux__9885_0 -e
WEBSITES_ENABLE_APP_SERVICE_STORAGE=true -e WEBSITE_SITE_NAME=linux -e
WEBSITE_AUTH_ENABLED=False -e PORT=80 -e WEBSITE_ROLE_INSTANCE_ID=0 -e
WEBSITE_INSTANCE_ID=69e8837849c1f64efde6a16e27e80702b636e76f3187c575565bb2b8f8a626ab
-e HTTP_LOGGING_ENABLED=1 azpranav.azurecr.io/test/linux/drupal/drush:latest
init_container.sh


> 2017-12-22 19:40:19.218 ERROR - Container linux __9885 _0 for site linux __9885
has exited, failing site start


This error is particularly caused because the line endings in files are
different and docker is very picky about it. Yep, heard me right. I cloned the
repository using Git and git on Windows by default converts the line endings of
all files so that Windows can understand (CR LF) instead of the one which Linux
understands (LF)

I converted all files related to the Docker Image to have Line Endings in LF 
format using Notepad++ and voila, the containers started working...

You can also turn off this auto change of line endings on Git for Windows by -

 1. Open up a terminal which can access Git.
 2. Type in git config core.autocrlf false & hit Enter.

A lot of information is available when you click on Diagnose & Solve Problems ->
Container Initialization in Azure Web App for Containers. That contains a lot
more information than what is available in Kudu.

That's it for today...