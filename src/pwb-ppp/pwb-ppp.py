#!/usr/bin/env python

# Version: 2024-12-17: First version (v0.0.1)
#
# Author: matsco@bas.ac.uk
#
# Main processing package.

import argparse

 
def main():
    """
    cli entry point
    this entry point relies on being pointed to a file path or directory path
    """
    
    parser = argparse.ArgumentParser(description='perform processing of raw penguin weighbridge data')
    args = parser.parse_args()


    # Now kick off main

    pass


if __name__ == "__main__":
    main()