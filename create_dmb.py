# Copyright (c) 2024 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""create a dbm for Energy+.schema.epJSON

Usage::

    python create_dbm.py epJSON_filename dbmfilename

"""
import sys
from eppy3000.dbm_functions import json2dbm



if __name__ == "__main__":
    sys.argv[1:]
    fname = sys.argv[1]
    dbmname = sys.argv[2]
    json2dbm.createall(fname, dbmname)
