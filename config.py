#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5867145679:AAFHLW1hK3k3TlSRvdYG7GGRodBMpucuCBg")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID","13197673"))
    API_HASH = os.environ.get("API_HASH","052ce58975f187e3ab08d9fbaa66dfc8")
    AUTH_USERS = os.environ.get("OWNER","5686364473")

