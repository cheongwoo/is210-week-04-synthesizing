#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Alarm Clock with Snooze Function"""


DAY = raw_input('What day is it?: ')
DAY = DAY.lower()
DAY = DAY[:3]

TIME = raw_input('What time is it?: ')
TIME = int(TIME)

SNOOSE = True if (DAY == 'sat' or DAY == 'sun') or TIME < 600 else False

if SNOOSE is False:
    print 'Beep! ' * 5
