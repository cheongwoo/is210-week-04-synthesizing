#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mortgage Calculator"""

import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount of your principal? ')
PRINCIPAL = int(PRINCIPAL)
DURATION = raw_input('For how many years is this loan being borrowed? ')
DURATION = int(DURATION)
PRE_QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
PRE_QUALIFIED = PRE_QUALIFIED.lower()
PRE_QUALIFIED = PRE_QUALIFIED[:1]

if PRINCIPAL <= 199999 and PRINCIPAL >= 0:
    if DURATION <= 15 and DURATION >= 1:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('3.63')
        elif PRE_QUALIFIED == 'n':
            RATE = decimal.Decimal('4.65')
    elif DURATION <= 20 and DURATION >= 16:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('4.04')
        elif PRE_QUALIFIED == 'n':
            RATE = decimal.Decimal('4.98')
    elif DURATION <= 30 and DURATION >= 21:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('5.77')
        elif PRE_QUALIFIED == 'n':
            RATE = decimal.Decimal('6.39')
elif PRINCIPAL <= 999999 and PRINCIPAL >= 200000:
    if DURATION <= 15 and DURATION >= 1:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('3.02')
        elif PRE_QUALIFIED == 'n':
            RATE = decimal.Decimal('3.98')
    elif DURATION <= 20 and DURATION >= 16:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('3.27')
        elif PRE_QUALIFIED == 'n':
            RATE = decimal.Decimal('4.08')
    elif DURATION <= 30 and DURATION >= 21:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('4.66')
        elif PRE_QUALIFIED == 'n':
            RATE = None
elif PRINCIPAL >= 1000000:
    if DURATION <= 15 and DURATION >= 1:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('2.05')
        elif PRE_QUALIFIED == 'n':
            RATE = None
    elif DURATION <= 20 and DURATION >= 16:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('2.62')
        elif PRE_QUALIFIED == 'n':
            RATE = None
    elif DURATION <= 30 and DURATION >= 21:
        if PRE_QUALIFIED == 'y':
            RATE = None
        elif PRE_QUALIFIED == 'n':
            RATE = None
elif PRINCIPAL < 0:
    RATE = None

if RATE is not None:
    TOTAL = int(round(PRINCIPAL * (1 + ((decimal.Decimal(RATE) / 100) / 12))
                      ** (12 * DURATION)))
elif RATE is None:
    TOTAL = None

if PRE_QUALIFIED == 'y':
    PRE_QUALIFIED = 'Yes'
elif PRE_QUALIFIED == 'n':
    PRE_QUALIFIED = 'No'

REPORT = ('Loan Report for: ' + NAME +
          '\n-------------------------------------------------------------' +
          '\n      {:<19}'.format('Principal:') + '$' + '{:>7,}'.
          format(PRINCIPAL) +
          '\n      {:<19}'.format('Duration:') + '{:>5}'.format
          (DURATION) + 'yrs' +
          '\n      {:<19}'.format('Pre-qualified?:') + '{:>8}'.format
          (PRE_QUALIFIED) +
          '\n\n      {:<19}'.format('Total:') + '$' + '{:>7}'.format
          (str(TOTAL)))

print REPORT
