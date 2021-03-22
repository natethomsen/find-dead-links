# find-dead-links
Run this program to find the dead links of a website(NOT BVUS)

## Installing
install python3 and virtualenv before running. After use code `make install INSTALL_DIR = <ENTER WHERE YOU WANT TO STORE PROGRAM>` or type `make install` to install in the home directory. 

## Running program
use the wrapper script to run thr program. Use code `find-dead-links <url>` or `find-dead-links <search depth> <url>`
The search depth will allow you to go through other child links on the site, or if no search depth is entered the original url will be tested.
