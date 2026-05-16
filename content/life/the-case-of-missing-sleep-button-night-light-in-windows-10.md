---
title: "The case of missing Sleep button & Night Light in Windows 10"
date: 2025-02-07T16:12:25+00:00
lastmod: 2025-02-07T16:12:25+00:00
---

After almost 9 years of service, my NVIDIA GTX 970 finally died. I think it knew that I am planning to build a new PC this year and now that the RTX 5000 series is available, it just gave up. Thank you my trusted GPU for so many good memories!

After removing the GPU, I plugged my display to the onboard display (Intel HD 530) and assumed that everything would be working as expected which it did for a while.

After a while, there was a flicker on the screen and it came back and I thought that it was maybe a glitch and everything was fine.

But, not everything was fine. I started observing 2 issues -

- **Night Light** was not working. Tried turning it on and off and nothing. Windows just refused to change the display color to a warm light.
- The **Sleep** button was missing from the Power options. I usually have quite some workloads open and so I usually make my PC sleep to save some time.

This was very surprising so I tried reboots, some hacks mentioned on Google but nothing worked until one which suggested to check the Graphics Driver in Device Manager.

Here is what I did to fix the issue -

- Open **Device Manager**
- Expand **Display Adapters**
- Under Display Adapters, I saw that it is showing as **Microsoft Basic Display Adapter**.
- This was strange considering I had rebooted my machine and earlier it was working fine.
- Right clicked on **Microsoft Basic Display Adapter**, clicked on **Update Driver** -> **Search Automatically for Drivers**.
- After a few minutes, it said that it installed the Graphics Driver for **Intel(R) HD Graphics  530**.
- Reboot the computer.

And voila! Everything was back to normal. Sleep button is visible again and night light also started working without any issue!

Till next time!