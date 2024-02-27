+++
title = "Resolving Issue with Logging Formatter & Unicode in Python 2.7"
description = ""
date = 2019-09-04T15:33:17
updated = 2019-09-04T15:44:58
draft = false
slug = "python-2-7-logging-with-formatter-unicode"
aliases = ['2019/09/04/python-2-7-logging-with-formatter-unicode/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


This would be a really short post for reference.

In Python 2.7 on Windows, I was using a RotatingFileHandler with a Formatter to
add contextual information to the logs.

For some reason, even when I was opening the file with the UTF-8 encoding during
the logging, I was getting an error with the following stack trace -

python r3.py
Traceback (most recent call last):
  File "C:\Python27amd64\lib\logging\handlers.py", line 76, in emit
    if self.shouldRollover(record):
  File "C:\Python27amd64\lib\logging\handlers.py", line 156, in shouldRollover
    msg = "%s\n" % self.format(record)
  File "C:\Python27amd64\lib\logging\__init__.py", line 734, in format
    return fmt.format(record)
  File "C:\Python27amd64\lib\logging\__init__.py", line 476, in format
    raise e
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 16: ordinal not in range(128)
Logged from file r3.py, line 160
Traceback (most recent call last):
  File "C:\Python27amd64\lib\logging\__init__.py", line 884, in emit
    stream.write(fs % msg.encode("UTF-8"))
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 16: ordinal not in range(128)
Logged from file r3.py, line 63
Traceback (most recent call last):
  File "C:\Python27amd64\lib\logging\handlers.py", line 76, in emit
    if self.shouldRollover(record):
  File "C:\Python27amd64\lib\logging\handlers.py", line 156, in shouldRollover
    msg = "%s\n" % self.format(record)
  File "C:\Python27amd64\lib\logging\__init__.py", line 734, in format
    return fmt.format(record)
  File "C:\Python27amd64\lib\logging\__init__.py", line 476, in format
    raise e


After searching for quite some time and even after setting the encoding at the
top of the script and manually saving the script files in UTF-8 format, it was
still not working. The code which I had in my logging package was as below -

FORMATTER = logging.Formatter("%(Host)s — %(asctime)s — %(name)s — %(levelname)s — %(message)s")
def getFileLoggingHandler():
    if FILE_ENABLE_LOGGER == Logging.TURN_ON_FILE_LOGGER.value:
        fileLoggingHandler = RotatingFileHandler(
            filename= LOG_FILE_PATH,
            maxBytes= LOG_FILE_MAX_SIZE_IN_BYTES,
            backupCount= LOG_FILE_BACKUP_COUNT,
            encoding= "UTF-8"
        )
        fileLoggingHandler.setLevel(FILE_LOGGING_LEVEL)
        fileLoggingHandler.formatter = FORMATTER
        return fileLoggingHandler
    else :
        return None


It seems that if you have defined the formatter, when an event is passed in 
<type 'unicode'>, it will try to decode it in ascii and then start throwing
errors. I couldn't find any way to set the decoding for the formatter to
Unicode.

The workaround? Change the formatter string so that it is interpreted as Unicode
like below -

FORMATTER = logging.Formatter(u"%(Host)s — %(asctime)s — %(name)s — %(levelname)s — %(message)s")


That additional u (which denotes Unicode) solved the issue!

Stay tuned as I will be writing a more detailed post on my logging experience in
Python!