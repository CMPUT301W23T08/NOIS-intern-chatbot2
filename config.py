#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "d2e3978d-bd44-4cba-9dc4-d3f12998ff5f")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "vLf8Q~gDcVwviFhepbe2LAw2rtIH4_RPB._wXcJ.")
