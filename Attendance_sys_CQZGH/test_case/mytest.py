class cc():
    def __init__(self):
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.hostaddress = "http://192.168.1.105:9009/face-door-guard/"
        self.match = "api/v1/face/matchrecord/sync"

c = cc("123","23","url","match")


print(c.hostaddress)