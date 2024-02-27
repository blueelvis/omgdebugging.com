+++
title = "Setting up Logrotate, Rsyslog, Cron & Anacron in Stateful Azure Web App for Containers"
description = ""
date = 2018-08-09T10:11:05
updated = 2018-08-29T07:29:49
draft = false
slug = "setting-up-anacron-in-azure-web-app-for-containers"
aliases = ['2018/08/09/setting-up-anacron-in-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Web App for Containers", "Cron", "Anacron", "Azure", "Rsyslog", "Logrotate"]
+++


I had been trying to set up Cron & Anacron in Azure Web App for Containers
(Stateful) for some time. I call them these Web App for Containers as stateful 
when the WEBSITES_ENABLE_APP_SERVICE_STORAGE is set to true in Application
Settings. This means that /home/ will be persisted across instance reboots. But
do remember that any other directory is not persisted across reboots. This
persistent storage is mounted on Azure Storage in the backend. This is required
for applications like Drupal, Wordpress etc. In this post, we will use Apache as
the Web Server.

You might be wondering why I used both Cron & Anacron? It was because the Azure
Web App for Containers is a PaaS service and the instance could be moved from
one host to another quite frequently. This means that if an instance reboot
occurs when the cron is scheduled to run, it would skip the job. And here comes 
Anacron to the rescue. Anacron maintains a status file to keep track of when 
cron.daily,cron.weekly & cron.monthly. It doesnt keep track of hourly cron jobs
unfortunately. But, once the container instance is started, it stays active for
quite some time and you can be quite sure that your hourly cron jobs would run
multiple times (<=24) in a day. That's fine because my aim was to rotate the
logs which Apache generates daily (and a couple of other logs). If you have a
website serving decent traffic, you can be sure that the Logfiles (generally in 
/home/LogFiles) will consume several gigabytes. It is always a good idea to
store the logs rather than not having them at the time of need.

> To configure Logrotate, Cron & Anacron, follow the below steps -


 1. Add the following section to your Web App for Containers Dockerfile -
    
    # Install Logrotate & Rsyslog and then configure it
     RUN set -ex \
     	&& apt-get -y install logrotate rsyslog \
     	&& rm -f /var/log/syslog \
     	&& sed -i '/notifempty/a\ \tsu root root' /etc/logrotate.d/apache2 \
     	&& cp /etc/cron.daily/logrotate /etc/cron.hourly/logrotate
    
    
    You might see that I am running the Logrotate job every hour. This is good
    to test things and the default configuration file for Logrotate (Apache) is
    that it will rotate every day. Logrotate maintains its own status file to
    keep track.
    
    
 2. Add the following section to remove the apt-compat cron job. This is because
    this job contains various commands which are not available by default and it
    doesn't start immediately but a random time from 0-30 minutes. You can find
    more information over here
    [https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=829443].
    
    # Remove apt-compat job from cron because it is stalling the cron jobs and we are anyways doing package cleaning later on in the image
     RUN set -ex \
     	&& rm -f /etc/cron.daily/apt-compat
    
    
    
 3. Install Anacron -
    
    # Install Anacron to run jobs even if containers stop/reboot at the time of execution
     RUN set -ex \
     	&& apt-get -y install anacron \
     	&& chmod 777 /var/spool/anacron \
     	&& mkdir -p /home/LogFiles/anacron \
     	&& rm -f /var/spool/anacron/* \
     	&& rmdir /var/spool/anacron \
     	&& ln -s /home/LogFiles /var/spool/anacron 
    
    
    
 4. Now, we need to fix the following error which comes up when trying to start
    anacron -
    
    > Fix anacron not starting up because of policy.d stating --
    "root@e12b813a8804:/home/LogFiles# /usr/sbin/invoke-rc.d anacron start
    invoke-rc.d: could not determine current runlevel
    invoke-rc.d: policy-rc.d denied execution of start."
    
    You can find more information as to why it is there over here
    [https://stackoverflow.com/questions/26938684/docker-io-init-d-script-not-working-on-start-container]
    . Add the following section as well -
    
    RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d
    
    
    
 5. Now, in the ENTRYPOINT script (mine is init_container.sh), add the following
    lines -
    
    # Create symlink to Syslog so that we store logs as well
     touch /home/LogFiles/syslog
     ln -s /home/LogFiles/syslog /var/log/syslog
    
    # Create symlink to Logrotate status. We need to store the status file persistently because otherwise, Logrotate won't know.
     touch /var/lib/logrotate/status
     ln --symbolic /var/lib/logrotate/status /home/LogFiles/logrotate.status
     
    # Run Anacron to do the jobs. It will assume a random delay (check /etc/anacron for more details) before actually executing the jobs. Plus jobs automatically go to background.
     /usr/sbin/invoke-rc.d anacron start
     
    # Fire up necessary services
     service ssh start
     service cron start
     service rsyslog start 
    
    
    

Once you push the image with these changes, after a couple of days, you would
notice that logs are being rotated -