# coding:utf-8
from locust import HttpLocust, TaskSequence, task, seq_task, TaskSet
from WuLanChaBuApi.TestApi.client_test.test_client import test_pull_alldata
import os


class XnMethod(TaskSequence):
    @task(1)
    def first_task(self):
        test_pull_alldata()


class User(HttpLocust):
    task_set = XnMethod
    max_wait = 500
    min_wait = 100
    host = "http://127.0.0.1"

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    command1 = "c:"
    command2 = r"cd %s" % current_path
    command3 = r"locust -f XnTestA.py --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)
