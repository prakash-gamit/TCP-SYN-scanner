# module to parse command line arguments

import sys
import Queue
import getopt
import topports
import scanner


def parseOptions(args):
    options, scanner.target = getopt.getopt(args, "hvt:p:")

    # check if target is empty
    if len(scanner.target) == 0:
        help()
        exit(1)

    for opt in options:
        if opt[0] == '-h':
            help()
            exit(0)

        elif opt[0] == '-v':
            scanner.verbose = True

        elif opt[0] == '-t':
            scanner.totalThreads = int(opt[1])

        # parse port list
        elif opt[0] == '-p':

            # split by ',' to get list of ports from string
            ports = opt[1].split(',')

            for p in ports:
                # split by '-' to get port range if given
                portragne = p.split('-')

                if len(portragne) == 1:
                    scanner.portlist.put(int(portragne[0]))
                else:
                    for r in range(int(portragne[0]), int(portragne[1]) + 1):
                        scanner.portlist.put(r)

        else:
            print "unknown option", opt[0]
            exit(1)

def help():
    print "usage:", sys.argv[0], "[options] <target ip address>"

    print """OPTIONS
    -h : show this help
    -p : specify port numbers to scan
         example:
            -p 21,22,23,50-100,443
    -t : numbers of threads to create
    -v : be verbose
    """

