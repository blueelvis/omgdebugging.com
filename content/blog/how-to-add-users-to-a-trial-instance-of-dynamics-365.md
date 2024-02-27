+++
title = "How to add users to a trial instance of Dynamics 365"
description = ""
date = 2018-08-09T12:58:52
updated = 2018-09-15T09:04:16
draft = false
slug = "how-to-add-users-to-a-trial-instance-of-dynamics-365"
aliases = ['2018/08/09/how-to-add-users-to-a-trial-instance-of-dynamics-365/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I have been testing Dynamics 365 in my personal Azure Active Directory where I
have a couple of users. In order to test out the solution in hand, I had to add
users with different roles to the same trial instance of Dynamics 365. It was
pretty hard to find proper documentation on how to do that.

The below procedure assumes that you already have created a Dynamics 365 trial
instance with one of the users in your AAD having enough privileges. It also
assumes that you have created the users in your Azure Active Directory already
and given them with Global Administrator role/privilege. This is required
because if your AAD is not associated with Exchange setup (Like mine), the owner
of the trial receives an email to approve the request to join whereas if the
user has got Global Administrator role, they automatically get approved and
hence no email is required. Once the trial is approved, you can change the role
back to User. Be sure that you do this before setting up the trial organization.

Be wary that, in a trial instance, you can have a total of only 5 users which
means you can add only 4 more users.

To add more users, just follow the below guide -

 1. Go to the Dynamics 365 Trial page over here [https://trials.dynamics.com/].
 2. Scroll down below and enter your user's Work Email, a phone number which can
    be random and then click on Get Started button.
 3. You would be presented with a screen stating the following. Click on "Sign
    In" and then sign in using your credentials.

> You have an account with us.
You’re using john.smith@blueelvisrocksgmail.onmicrosoft.com with another
Microsoft service already. To finish signing up for Dynamics 365, sign in with
your existing password."


 4. After signing in, you would see the following screen. Hit Create button. - 
 5. Click on Join An Existing Organization, select the organization to join and
    click on Join button as below -
 6. A popup screen will ask you to select the app which fits best for you. I
    will just go with All of these and click on Continue - 
 7. Once that is done, you would be able to access the Dynamics 365 instance.