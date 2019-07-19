# -*- coding: utf-8 -*-
"""
读取yaml测试数据

"""
import yaml
import os
import os.path
from https_20190709.common.Log_z import mylog
logger = mylog.get_log().get_logger()

class params:
    def __init__(self,yaml_file,func_name):
        self.yaml_file = os.path.join(os.path.abspath(os.pardir),'Params\\Param\\',yaml_file)
        self.func_name = func_name
        try:
            self.url = self.load_yaml()["url"]
        except:
            logger.error("func_name:%s  can not find in yaml", self.func_name)
            os._exit(0)
        self.data = self.load_yaml()["data"]
        self.all_params = self.get_all_params()
        self.must_params = self.get_must_params()

    def load_yaml(self):
        pages = {}
        try:
            with open(self.yaml_file, 'rb') as f:
                page = yaml.safe_load(f)
                pages.update(page)
        except:
            logger.error("yaml_file:%s  can not open",self.yaml_file)
            os._exit(0)
        pages = pages[self.func_name]
        return pages

    def get_single_param(self,name):
        value = self.load_yaml()
        try:
            value = value["data"][name]
        except:
            logger.error("key:%s not exist",name)
            value = ""
        return value
    def get_all_params(self):
        all_params = {}
        params = self.data
        for key,value in self.data.items():
                all_params.update({key:value[0]})
        return all_params

    def get_must_params(self):
        must_params = {}
        params = self.data
        for key,value in self.data.items():
            if self.data[key][1] == 1:
                must_params.update({key:value[0]})
        return must_params




if __name__ == '__main__':
    data = params("my_interface_test.yml","test_api_face_security_face_check")
    # print(data.url)
    # print(data.data)
    # print(data.func_name)
    print(data.get_all_params())
