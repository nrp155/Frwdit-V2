#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "4608228"))
    API_HASH = os.environ.get("API_HASH" , "7d2ccae297d9bddc2c1a704f4db9051a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1879736366:AAEgEsv8L90BmNn5IamLJbQFa2H4AXg-WuY") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQBGUOQAtTs0DCQaBM305xJX8cz0AiJJ6qu2jwpCSMPUZ8qegKFUAoNymJ_nkRuGG_kO-aSjLm49QzIFp9fU5oxCPn3fn9Vnj3VUH7Nj_pH2yirUA-pZuxF6xuVxS-3JBlPWGFdszr2bdJQut2hhtGAr6uwUxUipjU8LcTYGfrMachpabmQlIdEdfGN6-HFBvGjJ_rPK-7G_5W1hqcFk4Wd_CTDbqv5Qq3ICcRBHr-vd4wdFp-xnes45hgC4VZrUDkEiaKjmyD9g5-f3-lxVkJPfovLrdeX0085ABUe7Ge3L2Wez30Z6fHIOixxPKiZ6pth4uZMrX04M7Zh5Hg58i2rceb9rFQAAAABwCoAuAQ ") 
    CAPTION = os.environ.get("CAPTION", "subscenelk")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 1553961614 , 1002913884)
    SESSION = os.environ.get("BQBGUOQAtTs0DCQaBM305xJX8cz0AiJJ6qu2jwpCSMPUZ8qegKFUAoNymJ_nkRuGG_kO-aSjLm49QzIFp9fU5oxCPn3fn9Vnj3VUH7Nj_pH2yirUA-pZuxF6xuVxS-3JBlPWGFdszr2bdJQut2hhtGAr6uwUxUipjU8LcTYGfrMachpabmQlIdEdfGN6-HFBvGjJ_rPK-7G_5W1hqcFk4Wd_CTDbqv5Qq3ICcRBHr-vd4wdFp-xnes45hgC4VZrUDkEiaKjmyD9g5-f3-lxVkJPfovLrdeX0085ABUe7Ge3L2Wez30Z6fHIOixxPKiZ6pth4uZMrX04M7Zh5Hg58i2rceb9rFQAAAABwCoAuAQ ")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
