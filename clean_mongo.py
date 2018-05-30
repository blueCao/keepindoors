#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clean mongo db "keepindoors", collection "docs,distances,components"
"""
from mongodb import mongo_cli
cli = mongo_cli.__get__()

for coll in ["docs","distances","components"]:
    mongo_cli.deleteAll(cli,"keepindoors",coll)
