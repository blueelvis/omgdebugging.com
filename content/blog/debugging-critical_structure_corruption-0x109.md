+++
title = "Debugging Critical_Structure_Corruption (0x109)"
description = ""
date = 2014-12-23T03:23:35
updated = 2018-08-22T08:21:16
draft = false
slug = "debugging-critical_structure_corruption-0x109"
aliases = ['2014/12/23/debugging-critical_structure_corruption-0x109/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = ["Articles", "BSOD", "Debugging", "Windows", "Windows blue screen of death"]
+++


So, it has been a really long time since I have posted. Let’s get this started
quickly now, shall we? Today’s post is on Debugging a 0x109 bugcheck i.e.
Critical_Structure_Corruption. Let’s see what WinDBG tells us about this
bugcheck –

CRITICAL_STRUCTURE_CORRUPTION (109) This bugcheck is generated when the kernel
detects that critical kernel code or data have been corrupted. There are
generally three causes for a corruption: 1) A driver has inadvertently or
deliberately modified critical kernel code or data. See 
http://www.microsoft.com/whdc/driver/kernel/64bitPatching.mspx 2) A developer
attempted to set a normal kernel breakpoint using a kernel debugger that was not
attached when the system was booted. Normal breakpoints, "bp", can only be set
if the debugger is attached at boot time. Hardware breakpoints, "ba", can be set
at any time. 3) A hardware corruption occurred, e.g. failing RAM holding kernel
code or data.

So, this bug check is called when a driver modifies critical Kernel Mode
components of the Windows Operating System or a breakpoint was set without the
debugger being attached (I am yet to see this one happen) or the RAM modules are
failing? Now, a question might arise as to why the Kernel Code can’t be
modified? To answer this question, I would like to explain the Patchguard
protection which is enabled in the 64-Bit Windows Operating Systems. This
Patchguard is there to make sure that nothing in the Kernel Code is modified by
some 3rd party other than Microsoft. This means that only Microsoft signed
update patches can modify the code. The Patchguard was once considered to be
un-breakable but now, people have been able to bypass this protection. You can
read more from the links provided in the References Section.

Thread Link – 
http://www.eightforums.com/bsod-crashes-debugging/54944-multiple-bsods-while-playing-different-games.html

In this case the user was having problems while playing games most of the time.
The crashes were random in time. After the usual checkup and removal of the
possible suspects, the user was still experiencing the crashes because of which
I started to point the finger at the hardware or more specifically the memory.
But, even running the MEMTEST for 8 passes, no errors showed up.

Let’s start debugging the Blue Screen Of Death ^_^. On analyzing the dump file
using WinDBG, I got the below output –

CRITICAL_STRUCTURE_CORRUPTION (109) This bugcheck is generated when the kernel
detects that critical kernel code or data have been corrupted. There are
generally three causes for a corruption: 1) A driver has inadvertently or
deliberately modified critical kernel code or data. See Kernel patch protection
for x64-based operating systems 2) A developer attempted to set a normal kernel
breakpoint using a kernel debugger that was not attached when the system was
booted. Normal breakpoints, "bp", can only be set if the debugger is attached at
boot time. Hardware breakpoints, "ba", can be set at any time. 3) A hardware
corruption occurred, e.g. failing RAM holding kernel code or data. Arguments:
Arg1: a3a01f59123f66cd, Reserved Arg2: b3b72bdf64bca950, Reserved Arg3:
fffff8029c85fb2c, Failure type dependent information Arg4: 0000000000000001,
Type of corrupted region, can be 0 : A generic data region 1 : Modification of a
function or .pdata 2 : A processor IDT 3 : A processor GDT 4 : Type 1 process
list corruption 5 : Type 2 process list corruption 6 : Debug routine
modification 7 : Critical MSR modification

So, according to Argument 4 (Which is 1) in this case, a function or .pdata is
being modified or is corrupt(Thanks Patrick
[http://www.sysnative.com/forums/members/patrick.html] for the correction). This
can be caused by either some 3rd party software or a failing RAM Module.
Arguments 1 & 2 are reserved and hence not documented. So, all we have now with
us are Argument 3 & Argument 4. Argument 3 states that the address is failure
type dependent information. Let’s see if we can find any functions near this
address.

The nearest function can be found in WinDBG using the ln command followed by the
address at which we need to check if there is any function. Let’s run ln on the
Argument 3 –

4: kd> ln fffff8029c85fb2c (fffff8029c85fb2c) nt!KiAcquireSpinLockInstrumented |
(fffff8029c85fbdc) nt!KiReleaseSpinLockInstrumented Exact matches:
nt!KiAcquireSpinLockInstrumented ()

Bingo! we found an exact match for the function. So, this was the function which
became corrupted and caused the system to crash. Now, let’s see if we can find
anything if we unassemble the function using the u command of WinDBG –

4: kd> u nt!KiAcquireSpinLockInstrumented+0 nt!KiAcquireSpinLockInstrumented:
fffff8029c85fb2c 48895c2408 mov qword ptr [rsp+8],rbx fffff8029c85fb31
4a896c2418 mov qword ptr [rsp+r12+18h],rbp //Compare This Line With Below Line
fffff8029c85fb36 56 push rsi fffff8029c85fb37 57 push rdi fffff8029c85fb38 4156
push r14 fffff8029c85fb3a 4883ec30 sub rsp,30h fffff8029c85fb3e
65488b1c2520000000 mov rbx,qword ptr gs:[20h] fffff8029c85fb47 4533c9 xor
r9d,r9d

Hmm, nothing strange in there. The user was running Windows 8.1. Let’s check if
we can find anything from the Kernel Executable (ntoskrnl.exe) which hasn’t been
tampered with. In this bug check, you need to make sure that you open the
Executable as a Crash Dump in WinDBG instead of the usual method of opening as
Executable. It will take some time to load. Once, it is loaded we get the
terminal for access. Let’s check the un-assembly of the same above function in
the Kernel executable –

0:000> u ntoskrnl!KiAcquireSpinLockInstrumented+0
ntoskrnl!KiAcquireSpinLockInstrumented: 00000001401dbb2c 48895c2408 mov qword
ptr [rsp+8],rbx 00000001401dbb31 48896c2418 mov qword ptr [rsp+18h],rbp
//Compare This Line With Above Line 00000001401dbb36 56 push rsi 00000001
401dbb37 57 push rdi 00000001401dbb38 4156 push r14 00000001401dbb3a 4883ec30
sub rsp,30h 00000001401dbb3e 65488b1c2520000000 mov rbx,qword ptr gs:[20h]
00000001401dbb47 4533c9 xor r9d,r9d

Note that when dealing with the Kernel Executable as a Crash Dump, we need to
enter the full name of the executable i.e. “ntoskrnl” instead of just “nt” else
we won’t get the required output due to how symbols are handled by WinDBG.

On comparing the values in Line #2, we see that the second letter in the user’s
case is an ‘a’ whereas in the original file there is an ‘8’. Furthermore, there
is an additional register (r12) involved in the user’s case. So, the memory
values are not valid by 1 Bit. This only happens when there is a problem in the
RAM.

The user was asked to get new RAM Modules and Voila, the user and his system
lived happily ever after.

References –

1.Defeating PatchGuard McAFee White Paper
[http://www.mcafee.com/in/resources/reports/rp-defeating-patchguard.pdf]
2.Analyzing Uroburos Patchguard Bypass
[http://blogs.mcafee.com/mcafee-labs/analyzing-uroburos-patchguard-bypass]
3.*NTDebugging *
[http://blogs.msdn.com/b/ntdebugging/archive/2010/08/10/debugging-a-bugcheck-0x109.aspx]