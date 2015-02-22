#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Paint Color Choice Tool"""


BASE = raw_input('Which base color, "{}" or "{}"?: '
                 .format('Seattle Gray', 'Manatee'))

if BASE == 'Seattle Gray':
    ACCENT1 = 'Ceramic Glaze'
    ACCENT2 = 'Cumulus Nimbus'
elif BASE == 'Manatee':
    ACCENT1 = 'Platinum Mist'
    ACCENT2 = 'Spartan Sage'

ACCENT = raw_input('Which accent color, "{A1}" or "{A2}"?: '
                   .format(A1=ACCENT1, A2=ACCENT2))

if ACCENT == 'Ceramic Glaze':
    HIGHLIGHT1 = 'Basically White'
    HIGHLIGHT2 = 'White'
elif ACCENT == 'Cumulus Nimbus':
    HIGHLIGHT1 = 'Off-White'
    HIGHLIGHT2 = 'Paper White'
elif ACCENT == 'Platinum Mist':
    HIGHLIGHT1 = 'Bone White'
    HIGHLIGHT2 = 'Just White'
elif ACCENT == 'Spartan Sage':
    HIGHLIGHT1 = 'Fractal White'
    HIGHLIGHT2 = 'Not White'

HIGHLIGHT = raw_input('Which highlight color, "{H1}" or "{H2}"?: '
                      .format(H1=HIGHLIGHT1, H2=HIGHLIGHT2))

OUTPUT = 'Your selected colors are,{}, {}, and {}.'.format(BASE, ACCENT,
                                                           HIGHLIGHT)
print OUTPUT
