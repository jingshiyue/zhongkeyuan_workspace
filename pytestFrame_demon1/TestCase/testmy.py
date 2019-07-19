import sys
import os
path0 = os.path.realpath(__file__)  #'D:\\workfile\\workspace\\pytestFrame_demon1\\TestCase\\testmy.py'
path1 = os.path.dirname(path0)
GRANDFA = os.path.dirname(path1)
sys.path.append(GRANDFA ) # 将祖父路径加入sys中
print("ok")

sys.path.append(sys.path.append(sys.path[0] + r"\..\.."))
sys.path.append(sys.path.append(sys.path[0] + r"\.."))