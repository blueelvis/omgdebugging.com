---
title: "How to add users to a trial instance of Dynamics 365"
date: 2018-08-09T15:05:48+00:00
lastmod: 2018-09-15T09:04:16+00:00
---

I have been testing Dynamics 365 in my personal Azure Active Directory where I have a couple of users. In order to test out the solution in hand, I had to add users with different roles to the same `trial` instance of Dynamics 365. It was pretty hard to find proper documentation on how to do that.

The below procedure assumes that you already have created a Dynamics 365 trial instance with one of the users in your AAD having enough privileges. It also assumes that you have created the users in your Azure Active Directory already and given them with **Global Administrator** role/privilege. This is required because if your AAD is not associated with Exchange setup (Like mine), the owner of the trial receives an email to approve the request to join whereas if the user has got **Global Administrator** role, they automatically get approved and hence no email is required. Once the trial is approved, you can change the role back to **User**. Be sure that you do this before setting up the trial organization.

Be wary that, in a trial instance, you can have a total of only 5 users which means you can add only 4 more users.

To add more users, just follow the below guide -

- Go to the Dynamics 365 Trial page over [here](https://trials.dynamics.com/).
- Scroll down below and enter your user's `Work Email`, a phone number which can be random and then click on **Get Started** button.![Dynamics 365 Trial Instance Signup Form](/content/images/2018/08/signup-form.PNG)
- You would be presented with a screen stating the following. Click on "Sign In" and then sign in using your credentials.

> > You have an account with us.

You’re using [john.smith@blueelvisrocksgmail.onmicrosoft.com](mailto:john.smith@blueelvisrocksgmail.onmicrosoft.com) with another Microsoft service already. To finish signing up for Dynamics 365, sign in with your existing password."

- After signing in, you would see the following screen. Hit **Create** button. - ![Dynamics 365 License Creation](/content/images/2018/08/dynamics-license-assignment.PNG)
- Click on **Join An Existing Organization**, select the organization to join and click on **Join** button as below -![Join organization in Dynamics 365](/content/images/2018/08/join-organization.PNG)
- A popup screen will ask you to select the app which fits best for you. I will just go with **All of these** and click on **Continue** - ![Select Dynamics 365 App](/content/images/2018/08/select-app.PNG)
- Once that is done, you would be able to access the Dynamics 365 instance.