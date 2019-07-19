# coding:utf-8
import requests

a = "http://192.168.0.234:9090/data-platform-server/api/v1/resource/group1/M00/B0/8B/ooYBAFvr0yGAMFWYAAAJMj3S3HA514.jpg"


def get_picture():
    """
    文件服务器中图片下载接口
    :param piceurename:
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/resource/group1/M00/B0/8B/ooYBAFvr0yGAMFWYAAAJMj3S3HA501.jpg"
    res = requests.get(url)
    print(res.text)
    return res.content


if __name__ == '__main__':
    m = get_picture()
    # with open("1.jpg", "wb") as fp:
    #     fp.write(m)
