#!/usr/bin/python3
# Time : 2019/7/12 14:40 
# Author : zcl

import pytest
from https_20190709.common.Log_z import mylog
from https_20190709.common.params_init_z import *
logger = mylog.get_log().get_logger()
from https_20190709.common.params_init_z import *

# test_param = init_params("my_interface_test.yml", "test_api_face_security_face_check")
# test_param = test_param.all_params

@pytest.fixture()
def params_init():
    pass