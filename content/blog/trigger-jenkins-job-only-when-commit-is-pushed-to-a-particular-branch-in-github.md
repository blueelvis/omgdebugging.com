+++
title = "Trigger Jenkins Job only when commit is pushed to a particular branch in Github"
description = ""
date = 2018-01-31T22:11:50
updated = 2018-08-22T08:21:16
draft = true
slug = "trigger-jenkins-job-only-when-commit-is-pushed-to-a-particular-branch-in-github"
aliases = ['2018/01/31/trigger-jenkins-job-only-when-commit-is-pushed-to-a-particular-branch-in-github/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++




Setup Webhook trigger in Github as -- http://JENKINS_SERVER_URL/github-webhook/

and set application/json . above ending slash is also mandatory.