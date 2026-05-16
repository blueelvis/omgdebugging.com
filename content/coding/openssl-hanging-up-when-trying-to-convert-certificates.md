---
title: "OpenSSL Hanging Up When Trying to Convert Certificates on Windows"
date: 2019-03-17T19:47:02+00:00
lastmod: 2019-03-17T20:11:47+00:00
tags: ["Azure", "Windows", "openssl", "winpty", "git bash"]
---

This post is more about me needing this again in the future because I keep on forgetting this from time to time. I was recently trying to convert certificates from `PEM` format to `PFX` format so that they could be uploaded to the Azure Web Apps. I have the [Git Bash](https://gitforwindows.org/) Command running which by default has the `OpenSSL` package so I don't have to install it separately.

From what I know, when you purchase a certificate from a Certificate Authority (CA), they provide you with multiple certificates including intermediate certificates. You would have to combine all the certificates along with the intermediate certificate to obtain the required certificate. Some providers are also kind enough to include this already in `PEM` file. This file contains the certificates in the proper order and includes the intermediate certificates as well.

The command to convert the `PEM` certificate file to `PFX` is as below -

```shell
openssl pkcs12 -inkey omgdebugging.com.key -in omgdebugging.pem -export -out omgdebugging.pfx

```

After typing the command, the screen will just sit and stare you with no option and no output -

![hung-up-openssl](/content/images/2019/03/hung-up-openssl.PNG)

The only option now is to kill the command prompt and reopen it.

This issue arises because in the difference how input is passed to the `OpenSSL` command by `Git Bash` console. The fix to this issue is adding the word `winpty` before the entire command. Doing this will make the prompt enter your password, confirm the password again and once done, you will notice that a `PFX` file has been generated.

So, the command becomes -

```shell
winpty openssl pkcs12 -inkey omgdebugging.com.key -in omgdebugging.pem -export -out omgdebugging.pfx

```

![working-openssl](/content/images/2019/03/working-openssl.PNG)

You might be wondering what `WinPTY` is and as per [this](https://stackoverflow.com/a/48200434) SO thread,

> > `winpty` is A Windows software package providing an interface similar to a Unix pty-master for communicating with Windows console programs.

That is why you need it as [described here](https://stackoverflow.com/a/32599341/6309):

> > The software works by starting the `winpty-agent.exe` process with a new, hidden console window, which bridges between the console API and terminal input/output escape codes. It polls the hidden console's screen buffer for changes and generates a corresponding stream of output.