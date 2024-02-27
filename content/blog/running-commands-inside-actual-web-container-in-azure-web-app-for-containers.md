+++
title = "Running commands inside actual Web Container in Azure Web App for Containers"
description = ""
date = 2019-01-23T20:58:52
updated = 2019-01-23T21:28:04
draft = false
slug = "running-commands-inside-actual-web-container-in-azure-web-app-for-containers"
aliases = ['2019/01/23/running-commands-inside-actual-web-container-in-azure-web-app-for-containers/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Azure", "microsoft", "Web App for Containers", "kudu", "sshpass"]
+++


This post focuses on how we could run executables which are built as part of
your custom image which you use to host Web Apps using the Web App for
Containers offering of Azure.

To get an idea what the architecture looks like behind the scenes for this, do
read this [https://www.appliedis.com/azure-web-app-for-containers-part-one/].

You might be wondering as to when this situation could come. I faced this
situation when trying to run Drush (Used in Drupal applications) commands after
every deployment. What this meant was that once the deployment was complete, I
had to run Drush commands from the root path from where the website was being
served. We were using the Kudu's Git deployment feature to perform deployments.
Kudu generates the deployment scripts on the fly but you can override it
[https://github.com/projectkudu/kudu/wiki/Customizing-deployments#deployment-file] 
by using a .deployment file.

The major problem was that these deployment commands run inside the Kudu
container which is strictly locked down and not the actual container for which 
we know the root password
[https://docs.microsoft.com/en-us/azure/app-service/containers/app-service-linux-ssh-support#use-ssh-support-with-custom-docker-images]
.

If you try to read the contents of this file in Kudu (while the site is running)
- /appsvctmp/ipaddr_0, you will find the private IP address of the actual
container which is actually serving your site. Communicating over SSH in an
automated fashion without keys is pretty brutal but, we have a utility called 
SSHPass which helps in emulating the terminal which makes SSH think that someone
actually typed in the password. You can find more information over here
[https://linux.die.net/man/1/sshpass].

After tinkering around with this and the deployment script, I was able to
execute Drush commands in the actual Web container during deployments through
Kudu. A sample of the files used is below. Feel free to use them and adapt!

> .deployment


[config]
command = bash deploy.sh


> deploy.sh


#Pre-Requisite Configuration
## Ensure that Known_HOSTS file is always removed otherwise sometimes the script will error out because the host key for same IP changes from time to time in Azure.
rm -f '/home/'$(whoami)'/.ssh/known_hosts'

# 1. Install SSHPass
cd /home/site

if [ -d "/home/site/sshpass" ]; then rm -Rf "/home/site/sshpass"; fi

git clone https://github.com/kevinburke/sshpass
cd sshpass
cp README.md README
autoreconf -f -i && ./configure
make
chmod +x sshpass

# 2. Execute Drush Commands

# 3. Execute UpdateDB
/home/site/sshpass/sshpass -pDocker! ssh -o StrictHostKeyChecking=no 'root@'$(cat /appsvctmp/ipaddr_?) -p 2222 "cd /home/site/wwwroot/ ; drush updatedb -y -v ; exit ;"

# 4. Execute UpdateDB
/home/site/sshpass/sshpass -pDocker! ssh -o StrictHostKeyChecking=no 'root@'$(cat /appsvctmp/ipaddr_?) -p 2222 "cd /home/site/wwwroot/ ; drush entup -y -v ; exit ;"

# 5. Execute Configuration Import
/home/site/sshpass/sshpass -pDocker! ssh -o StrictHostKeyChecking=no 'root@'$(cat /appsvctmp/ipaddr_?) -p 2222 "cd /home/site/wwwroot/ ; drush cim -y -v ; exit ;"

# 6. Execute Drush Status
/home/site/sshpass/sshpass -pDocker! ssh -o StrictHostKeyChecking=no 'root@'$(cat /appsvctmp/ipaddr_?) -p 2222 "cd /home/site/wwwroot/ ; drush status -v ; exit ;"

echo "Finished Successfully!!!"


In case of any issues, feel free to reach out. Till next time!