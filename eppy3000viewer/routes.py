# Copyright (c) 2022 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
# -*- coding: utf-8 -*-
from bottle import Bottle

from .controllers.home import home_app


Routes = Bottle()
# App to render / (home)
Routes.merge(home_app)
