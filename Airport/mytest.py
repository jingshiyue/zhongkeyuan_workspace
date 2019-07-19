#! / usr / bin / python3
# -*- encoding: utf-8 -*-
# Time : 2019/7/10 15:43 
# Author : zcl
from datetime import datetime,timedelta
from _datetime import timedelta
next_time = (datetime.now() - timedelta(hours=1)).strftime("%Y%m%d%H%M%S")
print(next_time)