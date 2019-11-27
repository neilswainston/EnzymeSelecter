'''
(c) University of Liverpool 2019

All rights reserved.

@author: neilswainston
'''
import sys
from enzyme_select.app import APP


def main(argv):
    '''main method.'''
    if argv:
        APP.run(host='0.0.0.0', threaded=True, port=int(argv[0]),
                use_reloader=False)
    else:
        APP.run(host='0.0.0.0', threaded=True, use_reloader=False)


if __name__ == '__main__':
    main(sys.argv[1:])
