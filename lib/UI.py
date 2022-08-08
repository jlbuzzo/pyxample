#!/usr/bin/env python3
"""
  UI - General User Interface module and class.

Usage:
    __name__ cmd [-h | -? | --help] [-v | --verbose] <arg ...>

Option:
    -a, --annotation, --ant, --bed      Annotation file, in general.
    -A, --args                          Recursive or reserved arguments.
    -b, --build, --batch, --ci          Building, Batch or CI/CD instructions file.
    -B, --buildir                       Directory where build or pipeline will run.
    -c, --config                        Configuration file. [default: 'config.yml']
    -C, --configdir                     Configuration directory.
    -d, --data, --database, --db        Database file or URL.
    -D, --datadir, --assets             General purpose data directory or bucket.
    -e, --environ, --expression
    -E, --envdir, --extension
    -f, --file, --logfile               A general resource path, file or URL.
    -F, --filedir, --logdir             Secondary activity directory or bucket.
    -g, --group, --subsample            Primary group definition.
    -G, --group2, --sample              Secondary group definition.
    -h, -?, --help                      Print this help message.
    -H, --headerdir, --includedir       Directory where to find header files.
    -i, --input                         Input file or URL.
    -I, --inputdir                      Input directory or bucket
    -j, --jobs,                         Number of parallel process. [default: 1]
    -J, --stageddir                     Main local installation directory. [default: '.local/']
    -k, --key
    -K, --keydir, --creddir 
    -l, --library
    -L, --libdir
    -m, --module
    -M, --moduledir
    -n, --name, --node
    -N, --number, --mode
    -o, --output
    -O, --outputdir
    -p, --passwd, --param
    -P, --prefixdir
    -q, --quiet, --list
    -Q, --query, --filter
    -r, --reference, --recursive
    -R, --rootdir, --repository, --remote
    -s, --source
    -S, --sourcedir
    -t, --tmp, --tarball
    -T, --tmpdir, --tag
    -u, --user, --id
    -U, --userdir, --usermode
    -v, --version                       Print package version.
    -V, --volume, --vpath
    -w, --tarball 
    -W, --workdir
    -x, --extra, --extract
    -X, --extradir, --compress
    -y, --template, --yes
    -Y, --templatedir
    -z, --test
    -Z, --testdir
    -@, --daemonize                     Turn this module into a running daemon.
    --force
    --automate
    --containerize
    --cloud

Environment:
    PONGA_VAR                           Controls ...

"""


import sys
#import docopt

__version__ = '0.1.0'



# Export list.
__all__ = [ 'UI' ]



class UI:
    '''User Interface class definition'''
    
    def __init__(self, args = sys.argv):
        self.args = args
        print("Package: %s." % __name__)
        return
    
    def parse(self):
        print("Ah la", self.args)
    
    def test_all(self):
        print("Testing ...")


if __name__ == '__main__':
    #__name__()
    print("Direto: %s." % __name__)
else:
    print("Indireto: %s." % __name__)
