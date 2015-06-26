#!/usr/bin/python

# Copyright 2014 Ankur Sinha
# Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# File : generate-blue-cards.py
#

from scribus import *

if newDocument((148,210), (10,10,10,10), LANDSCAPE, 1, UNIT_MM, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
    spx=142
    spy=29 + 4
    width=57
    height=9.5

    selectfile = fileDialog("Select file")
    file = open (selectfile,"r")

    date_year = file.readline()
    date_year = date_year.rstrip('\n')

    while 1:
        name = file.readline()
        number = file.readline()

        if not name:
            break

        if name == '\n':
            continue

        name = name.rstrip('\n')
        number = number.rstrip('\n')

        name_box = createText(spx,spy,width,height)
        setText(name, name_box)
        setTextAlignment(ALIGN_CENTERED, name_box)
        setFont("DejaVu Sans Book", name_box)
        setFontSize(13, name_box)
        setLineWidth(0, name_box)

        number_box = createText(spx,(spy+height),width,height)
        setText(number, number_box)
        setTextAlignment(ALIGN_CENTERED, number_box)
        setFont("DejaVu Sans Book", number_box)
        setFontSize(13, number_box)
        setLineWidth(0, number_box)

        month_box = createText(spx,(spy+(2*height)),width,height)
        setText(date_year, month_box)
        setTextAlignment(ALIGN_CENTERED, month_box)
        setFont("DejaVu Sans Book", month_box)
        setFontSize(13, month_box)
        setLineWidth(0, month_box)

        newPage(-1)
        name = ''
        number = ''

    saveDocAs("blue-cards-" + date_year + ".sla")

