+++
title = "How To Deploy Blackfire in Azure Web App for Containers"
description = ""
date = 2018-07-24T11:38:47
updated = 2018-08-22T08:21:16
draft = false
slug = "how-to-deploy-blackfire-in-azure-web-app-for-containers"
aliases = ['2018/07/24/how-to-deploy-blackfire-in-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


In this post, I will show you how to deploy Blackfire in Azure Web App for
Containers. For those who don't know, Blackfire is a tool used to profile PHP
applications. This is especially useful when your PHP application is having
performance issues. You can read more about its features over here
[https://blackfire.io/features].

It was interesting to figure this out because as of writing this article, Azure
Web App for Containers only exposes 1 port to the outside world. I configured
the container and then installed the Blackfire Google Chrome (pretty awesome!)
extension to do profiling of a website.

Pre-Requisites -
 1. Knowledge of Azure Web App for Containers. We would be using a custom Docker
    image.
 2. Blackfire account with an environment setup

Installation Procedure -
 * Go over here [https://blackfire.io/my/settings/credentials] and then take a
   note of the following things as they would be required later on - * Client ID
    * Client
      Token
    * Server ID
    * Server
      Token
   
   
 * Now, in your Dockerfile of Azure Web App for Containers, add the following
   section -

RUN set -ex \
	&& git clone https://github.com/blackfireio/docker.git \
	&& mv docker/blackfire /usr/bin \
	&& mv docker/blackfire-agent /usr/bin \
	&& rm -rf docker
	
ENV BLACKFIRE_SOCKET tcp://127.0.0.1:8707

RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \
    && mkdir -p /tmp/blackfire \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp/blackfire \
    && mv /tmp/blackfire/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so \
    && printf "extension=blackfire.so\nblackfire.agent_socket=tcp://127.0.0.1:8707\n" > $PHP_INI_DIR/conf.d/blackfire.ini \
    && rm -rf /tmp/blackfire /tmp/blackfire-probe.tar.gz


> For Alpine variants of the PHP Docker images, please replace linux with alpine 
in the URL of the downloaded file.


> If you are using a zts (Zend Thread Safety) version of PHP, please add -zts to
the version name.


 * Now, in your Docker initialization/startup script, add the following lines
   before your Apache/Nginx processes -

# Start Blackfire Agent and send it to background...
cd /usr/bin
nohup ./blackfire agent &


 * Build the image and push it to your container registry
 * Change the version of the image accordingly in Azure Web App for Containers
   to use this latest built image.
 * Now, go to your Azure Web App for Container and open the Application Settings
   blade.
 * Add the following Application Settings with the values from above - 1. 
       BLACKFIRE_CLIENT_ID
    2. 
       BLACKFIRE_CLIENT_TOKEN
    3. 
       BLACKFIRE_SERVER_ID
    4. 
       BLACKFIRE_SERVER_TOKEN
   
   
 * Reboot the Web App for Container and if everything is successful as planned,
   you would see the following in the default logs for Azure Web App for
   Containers -

2018-07-24T09:39:21.576610688Z Agent listening on 127.0.0.1:8707
2018-07-24T09:39:21.576630788Z You can set the BLACKFIRE_AGENT_SOCKET environment variable to:
2018-07-24T09:39:21.576649388Z [0;32mexport BLACKFIRE_AGENT_SOCKET=tcp://127.0.0.1:8707

2018-07-24T10:50:06.808815856Z Tue Jul 24 10:50:06 2018 (63): [Debug] pub:{adaaaaaaaaa/ID8ya75+NFYGgB/UTSFTQjWhWoKSRSmY4H29dWclV}(56)
2018-07-24T10:50:06.808839856Z Tue Jul 24 10:50:06 2018 (63): [Debug] sig:{aaaaaaaaaaaaaaaUKaye07wu4xvY9iyharHiTKRRDdWFWlcPboAZc7oDnPuzfQ14sAKZIFQQ=}(100)
2018-07-24T10:50:06.808931556Z Tue Jul 24 10:50:06 2018 (63): [Debug] msg:{expires=1532433005&userId=aaaaa-bbbb-4d64-bbbb-db49dd6020c4&agentIds=aaaaa-aaaa-bbbb-ad65-eae306207b76%2C202e1740-9bc3-4410-9fe6-532cd24f3605%2C-%2Crequest-id-2732811e-c7b5-4683-b977-54c99d604a30&profileSlot=00000000-0000-0000-0000-000000000000&collabToken=aaaaaa-1111-1111-2222-61944a9afc9c}(299)


If you get something like below,

root@b72d2bfaee27:/usr/bin# blackfire agent
The Blackfire API answered with a 401 HTTP error ()
Error while fetching credentials from API: The Blackfire API rejected your credentials.


ensure that your tokens are correct and they are actually visible inside the Web
App for Container (By typing in printenv | grep BLACKFIRE.