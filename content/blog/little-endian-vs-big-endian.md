+++
title = "Little Endian vs Big Endian"
description = ""
date = 2016-11-06T10:15:11
updated = 2018-08-22T08:21:16
draft = false
slug = "little-endian-vs-big-endian"
aliases = ['2016/11/06/little-endian-vs-big-endian/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This is going to be a short post :(

For people who don't know the terms used in the title, they are nothing but ways
to format and store data in memory so that the computer can understand and
process it.

Recently, while browsing around, I found really nice one liners differentiating
them over the MSDN Documentation page. For easy reference in the future, I am
quoting them here -

> In little-endian format, a multi-byte value is stored in memory from the lowest
byte (the "little end") to the highest byte. For example, the value 0x12345678
is stored as (0x78 0x56 0x34 0x12) in little-endian format.


Similarly, for Big Endian -

> In big-endian format, a multi-byte value is stored in memory from the highest
byte (the "big end") to the lowest byte. For example, the value 0x12345678 is
stored as (0x12 0x34 0x56 0x78) in big-endian format.


L for Lowest Byte and L for Little Endian. Hope this helps!

Reference - 
https://msdn.microsoft.com/en-us/library/windows/desktop/ms724884(v=vs.85).aspx?f=255&MSPPError=-2147217396
[https://msdn.microsoft.com/en-us/library/windows/desktop/ms724884%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396]