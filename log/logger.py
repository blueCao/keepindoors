#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple log print to console for stdout and stderr
"""

import logging
import sys

def getLogger(logger_name):
    """
    get a specified named logger
    :param logger_name:
            string of the logger name
    :return:
            logger
    """
    # initialize logging class
    logger = logging.getLogger(logger_name)
    # set default logging configuration
    logger.setLevel(logging.DEBUG)  # default log level
    format = logging.Formatter("### %(asctime)s #%(name)s #Line %(lineno)d#%(levelname)s### %(message)s")  # output format
    sh = logging.StreamHandler(stream=sys.stdout)  # output to standard output
    sh.setFormatter(format)
    sh2 = logging.StreamHandler(stream=sys.stderr)  # output to standard output
    sh2.setFormatter(format)
    logger.addHandler(sh2)
    return logger