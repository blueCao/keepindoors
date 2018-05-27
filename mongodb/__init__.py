#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
init an return the unique global mongo cli
"""

from mongodb.mongo_cli import *

if MongoCli.cli == None :
    MongoCli.cli = mongo_cli.__get__()
cli = MongoCli.client