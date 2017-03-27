# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from pootle.core.delegate import log
from pootle.core.plugin import getter
from pootle_store.models import Store, Unit

from .utils import StoreLog, UnitLog


@getter(log, sender=Store)
def store_log_getter(**kwargs_):
    return StoreLog


@getter(log, sender=Unit)
def unit_log_getter(**kwargs_):
    return UnitLog
