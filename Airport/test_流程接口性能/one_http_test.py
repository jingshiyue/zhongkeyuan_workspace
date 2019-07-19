# coding:utf-8
import time
from locust import TaskSequence,HttpLocust,task


class User(TaskSequence):
    @task
    def a(self):
        pass


if __name__ == '__main__':
    print()