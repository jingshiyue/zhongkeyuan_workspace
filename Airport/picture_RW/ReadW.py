# coding:utf-8
import os
import shutil
import time
import base64


class ReadW(object):
    """
    封装一个对照片文件处理与提取特征公共文件夹适应的读写类
    """
    def __init__(self, live_p_path, id_p_path, common_p_path):
        self.live_picture_path = live_p_path
        self.id_picture_path = id_p_path
        self.common_picture_path = common_p_path

    def get_live_list_name(self):
        live_list_name = os.listdir(self.live_picture_path)
        return live_list_name

    def get_id_list_name(self):
        id_list_name = os.listdir(self.id_picture_path)
        return id_list_name

    def copy_all_picture_to_common(self, i):
        shutil.copy((self.live_picture_path+"/"+self.get_live_list_name()[i]),
                    self.common_picture_path)
        shutil.copy((self.id_picture_path+"/" +
                     self.get_id_list_name()[i]),
                    (self.common_picture_path+"/" +
                     self.get_id_list_name()[i].replace(".", "%d." % i)))

    def get_live_feature_str(self, i):
        if os.path.exists((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt")):

            with open((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"), "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"))
        else:
            time.sleep(2)
            with open((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"), "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_live_list_name()[i]+".txt"))
        return data

    def get_id_feature_str(self, i):

        if os.path.exists((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt")):
            with open((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"),
                      "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"))
        else:
            time.sleep(2)
            with open((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"),
                      "r") as fp:
                data = fp.read().rstrip()
            os.unlink((self.common_picture_path+"/"+self.get_id_list_name()[i].replace(".", "%d." % i)+".txt"))
        return data

    def get_live_picture_base64(self, i):
        """获取现场照的base64编码"""
        with open(file=(self.live_picture_path+"/"+self.get_live_list_name()[i]), mode="rb") as fp:
            image_data = fp.read()
            base64_data = base64.b64encode(image_data)
            return str(base64_data, encoding="utf-8")

    def get_id_picture_base64(self,i):
        """获取证件照的base64编码"""
        with open(file=(self.id_picture_path+"/"+self.get_id_list_name()[i]), mode="rb") as fp:
            image_data = fp.read()
            base64_data = base64.b64encode(image_data)
            return str(base64_data, encoding="utf-8")

    def copy_id_picture(self, i, newpath, k=0):
        id_list = self.get_id_list_name()
        for a in range(k, i):
            shutil.copy((self.id_picture_path + "/" + id_list[a]), newpath)

    def copy_live_picture(self, i, newpath, k=0):

        id_list = self.get_id_list_name()
        for a in range(k, i):
            shutil.copy((self.live_picture_path + "/" + id_list[a]), newpath)


if __name__ == '__main__':
    live_p_path = "E:/picture"
    id_p_path = "E:/IDcard"
    common_p_path = r"D:\work file\project\zhihuipanshi\特征批量提取工具\work_folder"
    opera = ReadW(live_p_path, id_p_path, common_p_path)
    opera.copy_id_picture(10000,"E:/idphoto")
    opera.copy_live_picture(10000,"E:/livephoto")







