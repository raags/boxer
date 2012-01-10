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
        self.txt = txt
        self.length = len(self.txt)

        " Looks bad, but it works! "

    def drawline(self, char):
        for i in self.txt:
            sys.stdout.write(char)

    def display(self):
        sys.stdout.write(" -")
        self.drawline("-")
        sys.stdout.write("-\n")
        sys.stdout.write("|")
        self.drawline(" ")
        sys.stdout.write("  |\n")

        print "| %s |" % self.txt

        sys.stdout.write("|")
        self.drawline(" ")
        sys.stdout.write("  |\n")

        sys.stdout.write(" -")
        self.drawline("-")
        sys.stdout.write("-\n")

def getargs():
        parser = argparse.ArgumentParser(description='Add a description here')

        parser.add_argument('--option', action='store_true')
      
        parser.add_argument('commands', metavar='commands', nargs='?', type=str, help =
                            'Accepts one or two', choices=['one', 'two'])
        parser.add_argument('--version', action='version', version='VERSION',
                            help= 'Show version')
        args = parser.parse_args()

        if args.option:
            print "You chose an optoin"
        
        if args.commands  == 'write':
           print "Command one"
        elif args.commands == 'read':
            print "Command two"

def main():
    getargs()

if __name__ == '__main__':
    main()
    exit(0)

# vim: autoindent tabstop=4 expandtab smarttab shiftwidth=4 softtabstop=4 tw=0
