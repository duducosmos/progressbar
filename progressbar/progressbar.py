#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = "Simple Progress Bar"
__author__ = "Eduardo S. Pereira"
__email__ = "pereira.somoza@gmail.com"
__data__ = "01/07/2015"
__versio__ = "0.1"

import sys


def progress_bar(value, max, barsize, extraInfo=None):
    """Simple text mode progress bar:
        Example:
>>print "processing..."
>>for i in xrange(11):
   progress_bar(i, 10, 40)
   time.sleep(1)
>>print "ok"
    """
    chars = int(value * barsize / float(max))
    percent = int((value / float(max)) * 100)
    sys.stdout.write("#" * chars)
    sys.stdout.write(" " * (barsize - chars + 2))
    if value >= max:
        sys.stdout.write("done. \n\n")
    else:
        if(extraInfo is not None):
            sys.stdout.write("[%3i%%]  %s \r" % (percent, extraInfo))
            sys.stdout.flush()
        else:
            sys.stdout.write("[%3i%%]\r" % (percent))
            sys.stdout.flush()
