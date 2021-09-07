"""
  UI - General User Interface module and class.
"""

import sys

version = '0.1.0'



# Export list.
__all__ = [ 'UI' ]


class UI:
    '''User Interface class definition'''
    def __init__(self, args = sys.argv):
        self.args = args
    def parse(self):
        print("Ah la", self.args)
