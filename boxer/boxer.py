#!/usr/bin/python
# 
#  Copyright (C) 2011 Raghu Udiyar <raghusiddarth@gmail.com>
#  
#  This copyrighted material is made available to anyone wishing to use,
#  modify, copy, or redistribute it subject to the terms and conditions
#  of the GNU General Public License, either version 2 of the License, or
#  (at your option) any later version
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 
# 
#  Description:
#  
# 
#  Author: Raghu Udiyar <raghusiddarth@gmail.com>
#
# Example of usage:
# 
# $
#
import sys
import argparse


class Boxer:
    """Draw a ascii box around your text"""

    def __init__(self, txt):
        self._txt_ = txt
    
        "Find the largest string (separated by newline)"
        self.tlist = txt.split('\n')
        maxlength  = 1
        for string in self.tlist:
            slen = len(string)
            if (slen > maxlength):
                maxlength = slen

        self.width = maxlength

        "Looks bad, but it works! "

    def drawline(self, char):
        for i in xrange(self.width):
            sys.stdout.write(char)

    def display(self):

        sys.stdout.write(" -")
        self.drawline("-")
        sys.stdout.write("-\n")
        sys.stdout.write("|")
        self.drawline(" ")
        sys.stdout.write("  |\n")

        for string in self.tlist:
            sys.stdout.write("| ")
            
            sys.stdout.write(string) 
            spaces = self.width - len(string)
            for i in xrange(spaces):
                sys.stdout.write(" ")
            sys.stdout.write(" |\n")

        sys.stdout.write("|")
        self.drawline(" ")
        sys.stdout.write("  |\n")

        sys.stdout.write(" -")
        self.drawline("-")
        sys.stdout.write("-\n")

def getargs():
        parser = argparse.ArgumentParser(description='Draw boxes around text')

        parser.add_argument('text', metavar='text', type=str, help =
                            'Text to box')
        parser.add_argument('--version', action='version', version='VERSION',
                            help= 'Show version')
        args = parser.parse_args()

        if args.text:
            b1 = Boxer(args.text)
            b1.display()

def main():
    getargs()

if __name__ == '__main__':
    main()
    exit(0)

# vim: autoindent tabstop=4 expandtab smarttab shiftwidth=4 softtabstop=4 tw=0
