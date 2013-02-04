#!/usr/bin/env python

# main function of program
# author: Prakash Gamit <prakashgamit23@gmail.com>
#         Indian Institute of Technology, Roorkee

import threading, Queue, getopt, time, sys
import topports, parseoptions, scanner, ScannerThread


def main():
    
    print "TCP-SYN-Scanner", scanner.version

    parseoptions.parseOptions(sys.argv[1:])

    # check if portlist is empty or not
    # if empty, scan top ten default ports
    if scanner.portlist.empty():
        for p in topports.topports:
            scanner.portlist.put(p)

    print "Scanning started..."
    print "%5s\tSTATE" %("PORT")

    threads = []
    for i in range(0, scanner.totalThreads):
        t = ScannerThread.ScannerThread(scanner.portlist)
        t.setDaemon(True)
        t.start()
        threads.append(t)

    scanner.portlist.join()

    # wait for all threads to finish
    for item in threads:
        item.join()

    print "Finished scanning..."


if __name__ == "__main__":
    main()
