+++
title = "How To Export Environment Variables in Azure Web App for Containers"
description = ""
date = 2018-10-05T14:31:57
updated = 2018-10-05T15:03:05
draft = false
slug = "how-to-export-environment-variables-in-azure-web-app-for-containers"
aliases = ['2018/10/05/how-to-export-environment-variables-in-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "microsoft", "Web App for Containers"]
+++


Azure Web App for Containers is a nice offering from Microsoft Azure where you
could have a custom Docker image running your Web App. This is particularly
beneficial when you need to run your Web App in a Linux environment and custom
tools are required (I look at you Drush...).

Now, when you deploy an instance of Azure Web App for Container, what happens is
that there are 2 containers which are created on the backend. One is the actual
container which is running your Web App and responding to traffic and the other
one is the Kudu container. These are connected to each other using a private
network. When you use the SSH option, what actually happens is that you
technically login to the Kudu Container and are presented with an SSH connection
to your container which is actually running the container.

When you login via SSH to the actual, the environment variables which you added
in Application Settings or Connection Settings will not be shown to you which
makes it pretty difficult to debug issues or even run commands from the SSH
terminal (Again looking at running Drush from the SSH terminal...).

To resolve this and make the environment variables appear in your SSH terminal,
you would have to add the following line to your container initialization script
(In my case, it was init_container.sh) -

# Get environment variables to show up in SSH session
eval $(printenv | awk -F= '{print "export " "\""$1"\"""=""\""$2"\"" }' >> /etc/profile)


As you can see below, after adding that to the container init script, I am able
to see the environment variables including the ones which have spaces -



I know it is a bit messy but will ensure that if your values or settings contain
an = or whitespace, they will be exported properly.

Also, ensure that your Application Settings only contain (A-Z, a-z), numbers
(0-9), or the underscore character ( _ ) as per Microsoft documentation
[https://docs.microsoft.com/en-us/azure/app-service/containers/app-service-linux-faq#other-questions]
.

> I don't think that this will work with certain special symbols like " though and
needs a bit of more testing and reworking. I will update this once I get a nice
solution.