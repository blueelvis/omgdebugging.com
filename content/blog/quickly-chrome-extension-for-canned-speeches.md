+++
title = "Quickly -- Chrome Extension for Canned Speeches"
description = ""
date = 2017-08-27T18:21:46
updated = 2018-08-22T08:21:16
draft = false
slug = "quickly-chrome-extension-for-canned-speeches"
aliases = ['2017/08/27/quickly-chrome-extension-for-canned-speeches/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This is a pet project on which I have been working on for quite some time.
Earlier, I made the project complex for unnecessary reasons (Experience matters!
) so I sat down once again and tried doing it in a different way this time and
seems like I have done it. After the promotion to Malware Response Team, I
thought it would be the best time to announce it.

Please find a recording of how this Chrome Extension works out over here - 
http://recordit.co/dQc7IwEVpf

This is a very basic version of the extension but it does it's job fairly good.
As you can see from the recording, it doesn't mess up with your clipboard.

Current Features -

 1. Canned Speeches need to be added manually.
 2. The extension does not collect any kind of telemetry data as of now.
 3. All data which is stored is offline only.
 4. Ability to export all of the canned speeches so that they can be stored
    easily.
 5. Ability to import canned speeches in bulk. Right now, importing a JSON dump
    in a defined format works. Export of canned speech is made in this format
    only. This is something which I have been thinking about. Would bulk import
    of text files work for you guys?
 6. All data is stored on your system. It doesn't go anywhere.

Features which I have planned -

 1. I will open source the project once I figure out bits of licensing and all.
 2. Google cloud sync? Need to look into this.
 3. Firefox extension :0)

Any other features which you would like to see or have any suggestions?

Download Link - 
https://chrome.google.com/webstore/detail/quickly/odbiclhecjmpbmbdgcmjjcadccdjibfd

How To Use?

 1. Install the extension in Google Chrome.
 2. In Chrome, navigate to chrome://extensions
 3. Locate Quickly and click on Options.
 4. This will open an options dialog where you can insert the name of the canned
    speech and the content of the canned speech.
 5. Add the title of the Canned Speech along with content of the Canned Speech
    and click on Submit button.
 6. Now, try visiting a website, click on the text box where you would like to
    paste the canned speech, press Alt + Shift + S , start typing the name of
    the canned speech and once you find the canned speech (Navigate using arrow
    keys), hit Enter to insert the canned speech.

> Warning - If you reset your chrome/clear extension data, the canned speeches
would be removed. I have few ideas in mind but if you have any, please feel free
to say so.


 * Kindly report any bugs/feature requests/suggestions over here or via PM.
 * Please feel free (I would motivate you) to post this across other forums as
   well if you think that this is useful and good.

Thanks aomaster for the motivation!