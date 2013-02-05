TCP-SYN-scanner
=================

a simple multithreaded TCP syn scanner using scapy in python

This is just a wrapper around scapy to perform SYN scanning
on TCP ports


DEPENDENCIES
================
python - 2.7.3

scapy - Scapy is a powerful interactive packet manipulation program
        see http://www.secdev.org/projects/scapy/ for more details

libpcap, libdnet and their python wrappers

scapy requires root privileges, so program must be run as root


ISSUES
================
scapy does not work on localhost
see http://www.secdev.org/projects/scapy/doc/troubleshooting.html#faq
