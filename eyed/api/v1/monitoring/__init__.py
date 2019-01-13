#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http

#
# Bootstrap Code
#
def bootstrap(config):
	#
	# Scan controller
	#
	config.add_route('api::v1:monitoring:http', '/http/')
        config.include(http.bootstrap)

#
# Make bootstrap attribute
#
__all__ = [bootstrap]

