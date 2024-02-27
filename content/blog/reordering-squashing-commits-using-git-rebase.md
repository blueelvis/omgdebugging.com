+++
title = "Reordering & squashing commits using Git Rebase"
description = ""
date = 2024-02-27T06:47:04
updated = 2024-02-27T07:30:21
draft = false
slug = "reordering-squashing-commits-using-git-rebase"
aliases = ['2024/02/27/reordering-squashing-commits-using-git-rebase/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I was working on a PR
[https://github.com/data-integrations/firestore-plugins/pull/18] for Google's
CDAP Firebase Plugin to add support for Named Databases
[https://cloud.google.com/blog/products/databases/manage-multiple-firestore-databases-in-a-project] 
and some other fixes.

After completing the development, testing and addressing review comments, I was
happy that finally the PR was LGTM but with a caveat. I was required to squash
all the commits into a single commit which totally made sense since there were a
number of small commits and some upstream changes had been merged as well.
Here is a look at the commit history -



You see the 4 commits on 27th Feb 2024? They were not supposed to be there but
somehow ended there. My guess would be when pulling upstream changes, I ran a
wrong command which caused all these merge commits and also the other commits. I
wanted to preserve all my changes, the upstream changes and then compress my
commits in a single commit.

I rarely see situations like this and thought that this requires documenting
because I am sure I would forget this soon. Something which required me to
re-arrange commits, preserve changes in my branch, make sure upstream changes
are in sync in my branch is something I had to do first time.

Let's get started with git rebase [https://git-scm.com/docs/git-rebase].

I executed git rebase HEAD~10 to make sure I am seeing all the history for my
branch. It opened the following text file in Notepad for git-rebase-todo -

pick 9e4c312 Create separate plugin repository for Cloud Firestore plugins. (#1)
pick ea11389 Remote snaphsot
pick f2f179b Revert "Remote snaphsot"
pick e0bb69c Update pom.xml
pick 54db280 bump dependency to 2.5.0 instead of 2.5.0-SNAPSHOT
pick c3d8a87 [PLUGIN-1465] Bump Hadoop dependency version to fix log4j vulnerabilities
pick 9e1a825 [CDAP-20182] Create SECURITY.md
pick 33079a1 Update Github Actions and checkstyle
pick 44f1b0a Added databaseName & fixed UI with several other fixes
pick 38af05c [CDAP-20182] Create SECURITY.md
pick ae8cae7 Update Github Actions and checkstyle
pick 4373af9 Added databaseName & fixed UI with several other fixes
pick 8550f0c Removed vs code files and added to gitignore
pick ea0c0bd Fixed as per review comments and fixed bug with widget and blank databasename
pick 80a0c21 Updated tests and fixed typos
pick 4328415 Addressed review comments and added more tests
pick 629cd5d Fixed database name comparison
pick b2a3bcf Reverted change to getting service account
pick 4ba67aa fix checkstyle configurtion
pick c18e86b Fixed checkstyle warnings
pick e9fd442 Addressed review comments
pick 8510826 Separated java imports
pick 5a5bed6 Addressed review comments

# Rebase 6ec1d64..809cd9c onto 6ec1d64 (23 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#



As you can see, the following commits are twice (albeit with different commit
hash) -

pick 9e1a825 [CDAP-20182] Create SECURITY.md
pick 33079a1 Update Github Actions and checkstyle
pick 44f1b0a Added databaseName & fixed UI with several other fixes
pick 38af05c [CDAP-20182] Create SECURITY.md
pick ae8cae7 Update Github Actions and checkstyle
pick 4373af9 Added databaseName & fixed UI with several other fixes


Now, after comparing the hashes with the upstream branch and my branch, I
identified that the following commits had to be removed -

pick 9e4c312 Create separate plugin repository for Cloud Firestore plugins. (#1)
pick ea11389 Remote snaphsot
pick f2f179b Revert "Remote snaphsot"
pick e0bb69c Update pom.xml
pick 54db280 bump dependency to 2.5.0 instead of 2.5.0-SNAPSHOT
pick c3d8a87 [PLUGIN-1465] Bump Hadoop dependency version to fix log4j vulnerabilities
pick 9e1a825 [CDAP-20182] Create SECURITY.md
pick 33079a1 Update Github Actions and checkstyle


I also had to remove this commit -

pick 44f1b0a Added databaseName & fixed UI with several other fixes


and then squash the others on 4373af9 Added databaseName & fixed UI with several
other fixes

After being confused and searching around on how to do this, I did the squashing
but that resulted in a lot of merge conflicts so had to abort the rebase using 
git rebase --abort.

Then... I saw the following lines in the git-rebase-todo -

# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.


This is exactly what I needed! I wanted to remove some commits and then
rearrange the order a bit to ensure there are no merge conflicts. After
re-arranging, my git-rebase-todo looked like below -

pick 4373af9 Added databaseName & fixed UI with several other fixes
squash 8550f0c Removed vs code files and added to gitignore
squash ea0c0bd Fixed as per review comments and fixed bug with widget and blank databasename
squash 80a0c21 Updated tests and fixed typos
squash 4328415 Addressed review comments and added more tests
squash 629cd5d Fixed database name comparison
squash b2a3bcf Reverted change to getting service account
squash c18e86b Fixed checkstyle warnings
squash e9fd442 Addressed review comments
squash 8510826 Separated java imports
squash 5a5bed6 Addressed review comments


# Rebase 6ec1d64..809cd9c onto 6ec1d64 (23 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#


Saved the file and then git asked me to enter the commit message, did that and
voila! I could see a single commit in the git log which was mine. After that,
did a rebase with upstream - git rebase upstream/develop and did a force push
using git push --force.

That removed all the duplicated commits and cleaned the commits. Here is the
updated view of all the commits -


This answer from SO helped a lot in understanding as well - 
https://stackoverflow.com/a/2740812/2758198

Till next time!