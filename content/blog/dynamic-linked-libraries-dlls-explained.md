+++
title = "Dynamic Linked Libraries, DLLs Explained"
description = ""
date = 2014-11-01T01:07:24
updated = 2018-08-22T08:21:16
draft = false
slug = "dynamic-linked-libraries-dlls-explained"
aliases = ['2014/11/01/dynamic-linked-libraries-dlls-explained/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "DLLs", "Windows"]
+++


Dynamic Link Library? Some of you might say that seriously what am I talking
about but you would be amazed to know that the Dynamic Link Libraries play a
very important role in the proper functioning of the Operating System and other 
Win32 Applications. I decided to write this article because of the fact that I
recently had a missing DLL Error when trying to run Deus Ex Human Revolution
which was related to Steam and was fixed simply by re-checking the files using
Steam.

[![Loading...](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/11/DLL-File-Error.jpg?resize=474%2C175)](http://i2.wp.com/omgdebuggingblog.cloudapp.net/wp-content/uploads/2014/11/DLL-File-Error.jpg)Aww
some file is missing :(So let us begin the journey by understanding the meaning
of the DLL or the Dynamic Link Library. In terms of Computers, Dynamic refers to
the fact that it can be loaded/unloaded into/from the memory while the
application is running. Link means that there is a linkage between more than one
file (Generally, the executable and DLL Files). And Library means that it is a
place where the functions are defined and can be called in the application which
has loaded them. The DLL is Microsoft’s implementation of the shared library
concept in the Microsoft Windows. 
Before we proceed further, we must note that the Dynamic Link Libraries (DLLs)
**generally have an extension** of “dll” but **can be of other extensions** as
well like the “ocx” (Libraries for containing ActiveX Controls), “drv” (for
legacy system drivers) or even “**sys**” (Export Drivers which I would be
talking about a bit as well below).So basically, the question arises that what
is a DLL File?
The answer to this question is that it is nothing but function definitions along
with declaration which perform operations depending on what is defined inside
those functions.

I think it would generate more interest if we check out the advantages and
disadvantages of the DLL Files.

Advantages :

 1. Saves memory and reduces swapping.
    
    
 2. Saves Disk Space.
    
    
 3. Upgrades to the applications is easy.
    
    
 4. Debugging and Bug Fixing is eased if the code is available in the DLL since
    the application is not needed to be re-compiled. This is true only if the
    function’s parameters and return types are not changed.
    
    

Disadvantages:

• The only disadvantage I could think up was that the application becomes
dependent on the existence of the DLL file else it won’t run.

• Malicious DLL’s can be loaded as well which is very popular these days.

Let’s discuss the advantages now. Let’s start with the point number 1 in the
advantages. For understanding this point, we need to understand the basic
concepts of how applications run. Whenever an application runs, the source code
is copied to the memory. The variables which store the data are given a
different set of address space (Stack if declared statically and Heap if
declared dynamically) whereas the functions which process the data & deal with
variables are allocated with memory from Stack. When a function is called inside
the application, the call is made to the functions inside the DLL File. These
functions are also stored in the memory. Windows makes sure that at any given
time, only one copy of the Dynamic Link Library is loaded into the memory for
access purposes and the system makes sure that the other copies of the DLLs are
not loaded. The system maintains a per-process reference count for each DLL.
When a thread loads the DLL, the reference count is incremented by one. When the
process terminates, or when the reference count becomes zero, the DLL is
unloaded from the virtual address space of the process. Some DLLs and
executables which are required by the Windows Operating System, are kept in the
memory constantly and cannot be unloaded so even if there reference count
reaches zero, they are not unloaded. So, using DLLs saves the Memory.

Let’s talk about the point number 2 now which is how using DLLs we can save the
storage space. Suppose that I develop 4 programs using a DLL which leverage the
power of the functions from “d3dx9_43.dll” in order to utilize Direct X. Now, I
am not required to integrate the code of the given DLL file into each of my
application. Just bundle the setup and the DLL file. Have the Setup of all the 4
applications to the same location on the File System and reference the DLLs from
there. Hence, saving the storage space.

I think that the points 3 & 4 should be explained simultaneously. Suppose you
create 3 modules for a single application. You observe that the Application is
having problem in a particular area, so you can easily find the problem in the
DLL file which is handling that part of the application. Also, suppose I have
created 2 applications in Visual C++ and the other 2 applications are created in 
Visual C# but the DLL is written in VB.Net . Don’t worry, we can use the same
DLL File in such cases no matter the language in which it is written in it and
which application is calling it. (As long as the programs follow the function’s
calling convention)

A DLL can define two kinds of functions: exported and internal. The exported
functions are intended to be called by other modules, as well as from within the
DLL where they are defined. Internal functions are typically intended to be
called only from within the DLL where they are defined. Although a DLL can
export data, its data is generally used only by its functions. However, there is
nothing to prevent another module from reading or writing that address.

The DLL files can be loaded into either the User Space of the Memory or the 
Kernel Space of the memory. The DLL Files loaded into the Kernel Space cannot
access any of the functions which are present in the User Mode/Space or the User
Mode API’s. The vice-versa of this is also true. Now, the question might arise
that another module can write at the address of Kernel Mode from User Mode but
the Operating System keeps a check on who is accessing whose memory address
space.

Now, into The Further [http://insidiousmovie.wikia.com/wiki/The_Further] we go…

Let’s pick up the question if this same can be achieved for the Drivers or not.
In the most fundamental sense, a driver is a software component that lets the
operating system and a device communicate with each other. For example, suppose
an application needs to read some data from a device. The application calls a
function implemented by the operating system, and the operating system calls a
function implemented by the driver.

The behaviour of the Dynamic Link Libraries can be achieved in Drivers as well
if the Driver is compiled as Export. The Kernel Mode Driver DLL has an extension
of “sys” and basically behaves the same as the previously discussed Dynamically
Linked Libraries, the only difference being that it works for the Drivers and is
present in the Kernel Mode. If you ask that why can’t I just load a DLL file
from User Mode (Extension : DLL) into the driver / kernel space is the same as
stated above that the Operating System (Windows) does not allow this. This is
required to ensure the security, integrity and confidentiality of the
information. The driver compiled using this would behave the same as the normal
DLL Files and the functions which are declared that can be imported are
available for other drivers to use.

I hope this helps you. The next time you encounter the missing DLL, you would
know why it is required. In my next post, I would be describing the process of
creating a Dynamic Linked Library and how to use it.

Thanks for reading ^_^.

References :

 * MSDN DLLs
   [http://msdn.microsoft.com/en-us/library/windows/desktop/ms682589(v=vs.85).aspx]
 * Kernel Mode DLL MSDN
   [http://msdn.microsoft.com/en-us/library/windows/hardware/dn613893(v=vs.85).aspx]

Feedback would be much appreciated ^_^. In case of any doubts, do not feel shy
to comment back.