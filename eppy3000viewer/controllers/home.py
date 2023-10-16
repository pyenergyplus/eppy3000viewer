# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view


home_app = Bottle()


@home_app.route('/')
@jinja2_view('index.html')
def index():
    return {'get_url': home_app.get_url}


