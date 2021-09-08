"""
  Pyxample
  A little example on how to make a Python package.
"""

__version__ = '0.1.0'


# Export list.
__all__ = [ 'pyxample', 'help', 'version', 'test' ]


class pyxample:
    '''This is a standard help message.'''
    def __init__(self, msg = 'Pyxample'):
        self.name = 'Pyxample'
        self.version = version
        self.id = 0
        self.msg = msg
    
    def run(self):
        '''Run is the main runtime function.'''
        print("Hello %s!\n" % self.msg)


def help():
    '''This is a standard help message.'''
    print("Usage:\n\t\$ pyxpl [option1, ...] arg1 ...\n")

def version(vs = 'some text'):
    '''This is a standard help message.'''
    print("Pyxample version %s.\n" % vs)


def test():
    k = pyxample('Test')
    k.run()
    '''General Unit Tests function.'''
    print("Se chegou ate aqui, funcionou ...\n")



if __name__ == '__main__':
    test()
