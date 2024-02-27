+++
title = "Problem with the Sound Decoder, Spotify Can't Play Music?"
description = ""
date = 2014-09-13T22:02:06
updated = 2018-08-22T08:21:16
draft = false
slug = "spotify_cannot_play_music"
aliases = ['2014/09/13/spotify_cannot_play_music/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Decoder", "Fraunhofer", "MP3", "Spotify"]
+++


I must admit that I am in love with Spotify [https://www.spotify.com/]. After
being accustomed to using it since an year now, I am extremely happy with it’s
interface and the collection of songs. There have been no bugs till now with
Spotify which I experienced. But, well every application has some exceptions
which are not handled and result in an error thrown out.

[![Loading...](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Error-Screen.png?resize=730%2C387)](http://i1.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/09/Error-Screen.png)There
was a problem with the Sound Decoder. Spotify cannot play this track.Above is
the screenshot of the error which started appearing when trying to play Local
Tracks stored on my system. After this I checked every setting of Spotify but
everything was correct. On failing to play the local track, I re-installed the
Spotify client but the problem was still not solved. So, finally I came to the
conclusion that something is wrong with my System.For like 2 days I kept on
trying to perform the tweaks suggested in various online forums but it did not
work. Finally, I contacted Spotify Support [https://twitter.com/SpotifyCares] on
Twitter which I must admit are a bunch of AWESOME people who are able to resolve
the problem. I will get straight to the point now. After some initial
diagnostics asked by the Spotify Support, they asked me to download Fraunhofer
MP3 Audio Decoder. On installing the Codec pack, the local tracks started
playing again. So, once again a HUGE THANKS to Spotify Support for being awesome
& solving the problem.

The Codec Pack can be downloaded from this LINK
[http://www.free-codecs.com/mpeg_layer_3_codec_download.htm].



EDIT :- Thanks to tw_mama
[http://community.spotify.com/t5/Help-Desktop-Linux-Mac-and/There-is-a-problem-with-the-sound-decoder-Spotify-can-t-play/m-p/959743#M100485] 
for providing further information on making the Spotify work after following
this Fix. Kindly download the batch file over here and run it –

http://www.komeil.com/blog/enable-fraunhofer-mp3-l3codecp-acm-windows

(P.S. that my issue was on Windows Platform)

In case of any problem do not hesitate to post back in the comments section!