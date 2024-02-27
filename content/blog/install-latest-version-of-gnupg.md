+++
title = "Install Latest Version of GNU GPG on Ubuntu 16.04"
description = ""
date = 2019-08-04T09:45:11
updated = 2019-08-04T10:48:35
draft = false
slug = "install-latest-version-of-gnupg"
aliases = ['2019/08/04/install-latest-version-of-gnupg/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Ubuntu 16.04 comes with a pretty old version of GNU GPG. I was trying to setup
GPG key for my Github account. On checking the version, I saw the following -

blueelvis@DESKTOP:/mnt/d/dev/minikube$ gpg --version
gpg (GnuPG) 1.4.20
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: ~/.gnupg
Supported algorithms:
Pubkey: RSA, RSA-E, RSA-S, ELG-E, DSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2


Github provides instructions on how to do it with older versions as well but I
thought, lets install the latest version. In order to get the latest version, we
need to download the packages, build them and then install them.

Pre-Requisites
Before proceeding ahead, ensure that you have installed the build-essential,
zlib1g-dev make packages. Also, ensure that you have sudo privilleges. These can
be installed by typing in -
sudo apt-get install build-essential make zlib1g-dev

Downloading the latest versions
The latest versions of the packages are available over here
[https://www.gnupg.org/download/]. As of writing this, the latest versions are
as below -

Name			Version
GnuPG			2.2.17
Libgpg-error            1.36
Libgcrypt		1.8.4
Libksba			1.3.5
Libassuan		2.5.3
ntbTLS			0.1.2
nPth			1.6


For the below instructions, if you notice that the versions have changed, you
would have to edit the commands accordingly.

Install Libgpg-error
wget https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.36.tar.bz2
tar jxf libgpg-error-1.36.tar.bz2
cd libgpg-error-1.36
./configure
make
sudo make install
cd ..


Install Libgcrypt
wget https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.4.tar.bz2
tar jxf libgcrypt-1.8.4.tar.bz2
cd libgcrypt-1.8.4
./configure
make
sudo make install
cd ..


Install Libksba
wget https://www.gnupg.org/ftp/gcrypt/libksba/libksba-1.3.5.tar.bz2
tar jxf libksba-1.3.5.tar.bz2
cd libksba-1.3.5
./configure
make
sudo make install
cd ..


Install Libassuan
wget https://www.gnupg.org/ftp/gcrypt/libassuan/libassuan-2.5.3.tar.bz2
tar jxf libassuan-2.5.3.tar.bz2
cd libassuan-2.5.3
./configure
make
sudo make install
cd ..


Install Ntbtls
wget https://www.gnupg.org/ftp/gcrypt/ntbtls/ntbtls-0.1.2.tar.bz2
tar jxf ntbtls-0.1.2.tar.bz2
cd ntbtls-0.1.2
./configure
make
sudo make install
cd ..


Install Npth
wget https://www.gnupg.org/ftp/gcrypt/npth/npth-1.6.tar.bz2
tar jxf npth-1.6.tar.bz2
cd npth-1.6
./configure
make
sudo make install
cd ..


Configure Dynamic Linker
echo 'include /usr/local/lib/' | sudo tee -a /etc/ld.so.conf
sudo ldconfig -v


Install GnuPG
wget https://www.gnupg.org/ftp/gcrypt/gnupg/gnupg-2.2.17.tar.bz2
tar jxf gnupg-2.2.17.tar.bz2
cd gnupg-2.2.17/
./configure
make
sudo make install
cd ..


After this, if you run gpg --version, you will get the following -

blueelvis@DESKTOP:~/gnupg-2.2.17$ gpg --version
gpg (GnuPG) 2.2.17
libgcrypt 1.8.4
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/blueelvis/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB


Install Pinentry
When you run gpg --full-generate-key and fill in the options, you will get an
error like below -

blueelvis@DESKTOP-8TI9P3N:/mnt/d/dev/minikube$ gpg --full-generate-key
gpg (GnuPG) 2.2.17; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: AAA, AAA
Email address: aaa@aaa.com
Comment: Github GPG Key
You selected this USER-ID:
    "AAA, AAA <aaa@aaa.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: agent_genkey failed: No pinentry
Key generation failed: No pinentry


We need to install pinentry so that gpg can generate the key. Install &
configure Pinentry using the following commands -

sudo apt-get install pinentry-curses
echo 'pinentry-program /usr/bin/pinentry-curses' | tee -a ~/.gnupg/gpg-agent.conf
gpg-connect-agent reloadagent /bye


Till next time!