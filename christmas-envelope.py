#!/usr/bin/python

import sys
import os
import cairo
import csv

# Check arguments
# (note 2 includes arg 0 which is this script!)
if len(sys.argv) != 3:
    print "\n***",sys.argv[0], "***\n"
    print 'Incorrect number of arguments, please run script as follows:'
    print '\n'+str(sys.argv[0])+' <csv address file> <csv return address>'
    sys.exit(0)

# Setup variables etc
INCHES_TO_POINTS = 72

def write_envelopes(out, from_addrs, to_addrs):
    surface = cairo.PDFSurface(out,
                               5.2 * INCHES_TO_POINTS,
                               5.2 * INCHES_TO_POINTS)
    cr = cairo.Context(surface)
    cr.select_font_face('Apple Chancery')
    cr.set_font_size(14)

    MARGIN = 0.25

    for to_addr in to_addrs:

        cr.set_font_size(11)
        for from_addr in from_addrs:
            for i, line in enumerate(from_addr):
                cr.move_to(MARGIN * INCHES_TO_POINTS,
                           (MARGIN * INCHES_TO_POINTS) + 12 + (12 * i))
                if line != "":
                    cr.show_text(line)

        cr.set_font_size(14)
        for i, line in enumerate(to_addr):
            cr.move_to(1.5 * INCHES_TO_POINTS,
                       (2.0* INCHES_TO_POINTS) + 12 + (22 * i))
            cr.show_text(line)

        cr.show_page()

    surface.flush()
    surface.finish()


def load_send_csv(filename):
    # Note the first row is ignored as it is assumed to have a header row
    with open(filename) as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue

            type = ''
           # if len(row) > 3:
           #     type = row[3].strip()
           # if type != 'yes':
           #     continue
            yield row[1:7]

def load_ret_csv(filename):
    # Note the first row is ignored as it is assumed to have a header row
    with open(filename) as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue

            type = ''
           # if len(row) > 3:
           #     type = row[3].strip()
           # if type != 'yes':
           #     continue
            yield row[0:7]


if __name__ == '__main__':
    INFILE = sys.argv[1]
    RETFILE = sys.argv[2]
    OUTFILE = 'envelopes.pdf'
    with open(OUTFILE, 'w') as f:
        write_envelopes(f, list(load_ret_csv(RETFILE)), list(load_send_csv(INFILE)))
    print 'wrote %s.' % OUTFILE
