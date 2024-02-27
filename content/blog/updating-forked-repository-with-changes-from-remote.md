+++
title = "Updating Forked Repository with Changes from Remote"
description = ""
date = 2016-07-26T21:24:57
updated = 2018-08-22T08:21:16
draft = false
slug = "updating-forked-repository-with-changes-from-remote"
aliases = ['2016/07/26/updating-forked-repository-with-changes-from-remote/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I have been using Git for quite some time now and recently started using GitHub
to increase my share of contribution to open source software.

On finding the perfect repository (Piwik [https://github.com/piwik/piwik]) to
start contributing to, I quickly forked the repository so that I could keep
track of local changes.

After some commits and pull requests, I noticed that GitHub said that my forked
repository was several commits (29, to be precise!) behind the original
repository.

In other words, I was working on code which was outdated. After a lot of
searching around on Google, I noticed that I had to pull changes from the remote
Piwik repository and then push them to my forked repository.

Before we can pull the changes from the remote repository, we need to add a
reference to it in our forked repository. The below command adds a reference to
the remote Piwik repository and the name of the reference is upstream -
git remote add upstream https://github.com/piwik/piwik.git

By default you should also have another one called origin which would point to
your fork in this case. Now, we need to fetch the changes from the remote
repository -
git fetch upstream

Finally, we switch to our master branch in our forked repository, merge the
changes and push them using the below commands -

 1. git checkout master
 2. git merge upstream/master
 3. git push origin master

The second command tells git to merge the changes from upstream's master branch
into the current repository. The third command pushes the changes to our
repository on GitHub.