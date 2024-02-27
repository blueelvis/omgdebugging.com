+++
title = "Installing New Relic PHP Agent in Azure Web App for Containers"
description = ""
date = 2018-08-31T08:38:06
updated = 2018-09-01T17:36:32
draft = false
slug = "how-to-install-new-relic-agent-in-azure-web-app-for-containers"
aliases = ['2018/08/31/how-to-install-new-relic-agent-in-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "Web App for Containers", "New Relic", "php"]
+++


In this post, I would install and then configure New Relic's PHP agent to work
with Azure Web App for Containers. The custom container image is based on Debian
but you should get a rough idea to install it on other flavors. The version of
PHP which was utilized while building the image was 7.2.5.

 1. By default, the sources available in the base PHP image are very limited and
    the agent installation requires gnupg2. To add the general sources, add the
    following lines to your Dockerfile -

# Add to sources the general Debian List
RUN set -ex \    && echo "deb http://deb.debian.org/debian stretch main contrib non-free" | tee /etc/apt/sources.list \    && apt-get update


 2. While building the Docker images, we cannot input or respond to prompts.
    That's why, we are going to use the unattended installation. Passing 
    DEBIAN_FRONTEND=noninteractive before the installation would achieve this.
    Add the following lines of code to your Dockerfile -

#Symlink New Relic Configuration File and Install the New Relic Agent
RUN set -ex \
   	&& apt-get install -y gnupg2 \
   	&& echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list \
   	&& wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - \
   	&& apt-get update \
   	&& DEBIAN_FRONTEND=noninteractive apt-get -y install newrelic-php5 \
   	&& newrelic-install install

COPY newrelic.ini /usr/local/etc/php/conf.d/newrelic.ini


You can find a copy of the code inside newrelic.ini file at the bottom of this
post. Feel free to customize it as per your needs. Reference over here
[https://docs.newrelic.com/docs/agents/php-agent/configuration/php-agent-configuration]
.

 3. Now, we need to add a few commands to our container init script which is
    also known as ENTRYPOINT in Dockerfile (In my case, it is init_container.sh
    ). This will allow us to pass in the Application Name & New Relic License
    key via Application Settings in Azure. Ensure that you put the following
    code block before starting your webserver -

# Add Application name & license key to New Relic
echo -e "\nnewrelic.appname=${NEW_RELIC_APPLICATION_NAME}" >> /usr/local/etc/php/conf.d/newrelic.ini
echo -e "\nnewrelic.license=\"${NEW_RELIC_LICENSE}\"" >> /usr/local/etc/php/conf.d/newrelic.ini


 4. Build the image and then push it to the registry from where your Web App for
    Container is pulling the image. Now, go into your Application Settings blade
    for the Web App for Containers and add the following keys and values -
    
     * NEW_RELIC_APPLICATION_NAME = Your Application Name
     * NEW_RELIC_LICENSE = Your New Relic License Key
    
    Now, hit the Save button and ensure that you reboot your Web App to ensure
    changes take place.
    
    

Also, do note that the Reboot of a Web App in Azure is an asynchronous operation
which means that once you press the Reboot button in portal, it might take some
time (from few seconds to a couple of minutes) for the actual reboot to happen.

Feel free to let me know in case you encounter any issues with this and I would
be happy to help!


--------------------------------------------------------------------------------

Text of my newrelic.ini -

# First of all enable the extension
extension=newrelic.so

# Enable this if you configured your account for High Security
#newrelic.high_security=true