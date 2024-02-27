+++
title = "Copying Folders in Ubuntu the correct way"
description = ""
date = 2017-05-11T11:05:03
updated = 2018-08-22T08:21:16
draft = false
slug = "copying-folders-in-ubuntu-the-correct-way"
aliases = ['2017/05/11/copying-folders-in-ubuntu-the-correct-way/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I had to restore a Wordpress Backup on a test site and I was using simple cp 
command with the -r (Recursive) switch.

While setting up the blog, I noticed that some of the files are missing from the
installation but were there in the source folder from where I was copying the
files.

I re-ran the command but it was no good. The command which I was running is as
below -
cp backup/wp-content destination/wp-content -r -v

The correct way to copy all of the files recursively in a folder and preserve
the file attributes, I had to use the below command -
cp backup/wp-content/. destination/wp-content -pfr -v

Notice the additional /. after the source directory and the additional switches 
-pf

After running the above command, all of the files from the backup got copied
successfully.

Source - https://askubuntu.com/a/312701