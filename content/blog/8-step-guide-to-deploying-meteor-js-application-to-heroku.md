+++
title = "8 Step Guide to deploying Meteor JS Application to Heroku"
description = ""
date = 2016-09-14T18:42:26
updated = 2018-08-22T08:21:16
draft = false
slug = "8-step-guide-to-deploying-meteor-js-application-to-heroku"
aliases = ['2016/09/14/8-step-guide-to-deploying-meteor-js-application-to-heroku/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Have you ever wondered about the best and fastest way to host a Meteor JS
[https://www.meteor.com/] Web Application? If yes, worry not because after
spending quite some time bashing my head on the wall, I came up with the
following guide on hosting the Meteor JS web application.

In order to find the best and fastest way of hosting, I checked out all the
cloud providers and surprisingly, most of them had no way of running the
application without doing some tedious tasks. Plus, I like my stuff automated.

I came across Heroku (Thanks again to Tushar Mishra
[https://github.com/tmess567]) and I can say that it is the one of the best PaaS
vendors out there. Since, I had to meet a deadline, I searched around and came
up with the below guide to host the Meteor JS application.

Requirements
 1. Heroku Account which can be created over here [https://signup.heroku.com]
 2. Heroku Toolbelt
    [https://devcenter.heroku.com/articles/heroku-command-line#download-and-install]
 3. Meteor [https://www.meteor.com/install] (I hope you have this installed
    though)
 4. A Credit Card is required in order to add the MongoDB addon in Heroku

Before we get started, please make sure that you are inside your Meteor project
and running the command heroku is working properly inside the Terminal or CMD
(If it isn't working after installation on Windows, try rebooting the system).

Let's get going!

1. Run some Git commands
> git init


> git add .


> git commit -m "My first commit!"


2. Create Your Heroku Instance
> heroku login


> heroku apps:create prototype


3. Tell Heroku about the BuildPack which you would like to use
> heroku buildpacks:set https://github.com/AdmitHub/meteor-buildpack-horse.git


Buildpacks are nothing but some special scripts to prepare your application for
deployment. I used the Horse buildpack because that is what worked for me. The
other one mentioned in the Medium article
[https://medium.com/@leonardykris/how-to-run-a-meteor-js-application-on-heroku-in-10-steps-7aceb12de234#.655c4eru3] 
did not work for me :(

Before proceeding ahead, make sure that your Heroku account is Verified and a
valid Credit Card has been added.

4. Create a MongoDB instance to store data
> heroku addons:create mongolab:sandbox


5. Get your MongoLab URI
> heroku config | grep MONGOLAB_URI


> // Alternatively, run "heroku config" to display all your configuration
variables, but truthfully we only need the MONGOLAB_URI


> // Be careful of running "heroku config" and leaving your console in the open
since it displays all your important environment variables like Stripe API keys


6. Set the configurations of your Meteor app running on Heroku
> heroku config:add MONGO_URL="MONGOLAB__URI"


> heroku config:add ROOT_URL=https://foobar.herokuapp.com


7. Use NPM-Collect [https://www.npmjs.com/package/npm-collect] to make sure all
packages get installed correctly on Heroku
> meteor npm install npm-collect


> npm-collect --new --save


The 7th step is required because I kept getting errors in regards to missing
package dependencies.

8. Push Code to Heroku
> git push heroku master


It will show you the progress of building and deploying the application and it 
will take time. If your Meteor application is working correctly on your system,
chances are that it would work flawlessly on Heroku now as well ;)

==
A lot of help was provided by this Medium article by Leonardy Kristianto
(Thanks!) - 
https://medium.com/@leonardykris/how-to-run-a-meteor-js-application-on-heroku-in-10-steps-7aceb12de234#.655c4eru3
==