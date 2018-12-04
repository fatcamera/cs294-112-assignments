#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import logging
import traceback


def main(args):
    logging.info(args)


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', help='verbose level')
    args = parser.parse_args()
    # setup logging
    date_format = '%Y-%m-%d %H:%M:%S'
    logging_level = logging.INFO
    if args.verbose >= 1: logging_level = logging.DEBUG
    logging.basicConfig(datefmt=date_format, level=logging_level,
            format='%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s')
    # main procedure
    try:
        main(args)
    except:
        logging.error(traceback.format_exc())

