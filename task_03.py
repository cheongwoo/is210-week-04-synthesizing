#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mortgage Calculator"""

import decimal
import fractions

NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount of your principal? ')
PRINCIPAL = int(PRINCIPAL)
DURATION = raw_input('For how many years is this loan being borrowed? ')
DURATION = int(DURATION)
PRE_QUALIFIED = raw_input('Are you pre-qualified for this loan? ')
PRE_QUALIFIED = PRE_QUALIFIED.lower()
PRE_QUALIFIED = PRE_QUALIFIED[:1]

if PRINCIPAL <= 199999:
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
elif PRINCIPAL >= 1000000:
    if DURATION <= 15 and DURATION >= 1:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('2.05')
    elif DURATION <= 20 and DURATION >= 16:
        if PRE_QUALIFIED == 'y':
            RATE = decimal.Decimal('2.62')

TOTAL = PRINCIPAL * (1 + fractions.Fraction(RATE, 100) / 12) ** (12 * DURATION)
TOTAL = round(TOTAL)

REPORT = 'Loan Report for: ' + NAME\n\
         '-' * 80\n\
         'Principal:'.format([[6]<[17]]) + PRINCIPAL.format([>[10]])\n\
         'Duration:'.format([[6]<[17]]) + DURATION.format([>[10]])\n\
         'Pre-qualified?:'.format([[6]<[17]]) +\
         PRE_QUALIFIED.format([>[10]])\n\
         \n\
         'Total:'.format([[6]<[17]]) + TOTAL.format([>[10]])

print REPORT
