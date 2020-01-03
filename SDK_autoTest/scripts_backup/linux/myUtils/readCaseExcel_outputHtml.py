#!/usr/bin/python3
# Time : 2019/10/26 20:10 
# Author : zcl
import collections,logging,time
from excel_operate import *
from analyse_sdk_result import *
logging.debug(os.getcwd())
log_path = "./result.log"
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filename = log_path,
    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
console.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console)


# caseManger管理一二三列标题 ，模块名称	子模块名称	测试用例主标题
caseManger_dic = collections.OrderedDict([
                        ("人脸检测跟踪",[
                            {"对指定路径的图片人脸检测":
                                ["单线程对指定路径的图片做人脸检测","多线程对指定路径的图片做人脸检测","单线程对指定路径的图片做人脸检测与多线程对指定路径的图片做人脸检测结果比对"]},
                            {"使用给定的图片进行人脸检测":
                                 ["单线程对给定的图片进行人脸检测","多线程对给定的图片进行人脸检测","单线程对给定的图片进行人脸检测与多线程对给定的图片进行人脸检测结果比对",
                                  "单线程人脸跟踪","多线程人脸跟踪","单线程人脸跟踪与多线程人脸跟踪结果比对"]},
                            {"人脸关键点检测":["单线程人脸关键点检测","多线程人脸关键点检测","单线程人脸关键点检测结果与多线程人脸关键点检测结果对比"]},
                        ]),

                        ("提取特征",[
                            {"提取特征":["单线程提取特征","多线程提取特征","单线程提取特征与多线程提取特征结果对比"]},
                            {"获取图片中指定坐标中的人脸特征":["单线程从指定坐标中的人脸特征提取","多线程从指定坐标中的人脸特征提取",
                                                               "单线程从指定坐标中的人脸特征提取与多线程从指定坐标中的人脸特征提取结果对比"]},
                        ]),

                        ("人脸确认指标（1:1）",[
                                        {"1:1对比数据准备":["1:1测试前的数据准备"]},
                                        {"单线程下1:1对比":["单线程下1:1对比"]},
                                        {"多线程下1:1对比":["多线程下1:1对比"]},
                                    ]),

                        ("人脸辨认指标（1:N）",[           {"1:N对比数据准备":["1:N测试前的数据准备"]},
                                                            {"1:N对比": ["单线程下1:N对比","多线程下1:N对比"]},
                                                            {"特征值预先载入1:N对比": ["单线程下特征值预先载入1:N对比","多线程下特征值预先载入1:N对比"]},
                                                        ]),

                        ("特殊场景测试",[
                                    {"特殊场景测试": ["对小尺寸图片的识别", "无输入图片情况下的识别","无检测通道情况下的识别","对输入图片检测不到人脸时的识别",
                                                       "对输入图片提取不到特征的识别","对错误特征值的图片识别","MN比对过大","对特征长度值超出范围的图片识别",
                                                       "图片里超过15个人脸","图片中有多个人脸时，先后识别出人脸的顺序","对文件夹内多个子文件夹里对应放入一张现场照和一张人脸人证比对",
                                                        "对文件夹内多个子文件夹里对应放入一张现场照和一张人脸人证分步识别比对"
                                                      ]},
                                ]),

                        ("流程测试",[
                                    {"流程测试": ["单线程人脸检测+特征提取+1:1对比", "单线程人脸检测+特征提取+1:N对比", "单线程人脸检测+特征提取+1:N快速比对", "多线程人脸检测+特征提取+1:1对比",
                                                "多线程人脸检测+特征提取+1:N对比", "多线程人脸检测+特征提取+1:N快速比对",
                                                ]},
                                ]),

                        ])


def get_pos_from_cellValue(str,colNum,rd_xls):
    """
    :param str: 三级标题,注意不能重复
    :param colNum: 读取第一列，索引从0开始
    :param rd_xls:
    :return: n 行号，j 列号
    """
    n,j = 0,colNum
    pos_list = []
    # logging.debug(rd_xls.get_col_data(j))
    for i in rd_xls.get_col_data(j):
        if str == i:
            # logging.debug(i)
            pos_list.append((n,j))
        n = n + 1
    return pos_list

def read_flow_result(flowCase,rd_result_xls):
    """
    :param flowCase: 流程名
    :param rd_result_xls:  结果分析得出的表格
    :return:
    """
    pos = get_pos_from_cellValue(flowCase, 0, rd_result_xls)
    pos = pos[0]
    totalTime = 0.0
    result = []
    result_str = ""
    for i in range(3):
        tmp = rd_result_xls.get_cell_value(pos[0]+i,pos[1]+2)
        if "平均时间:" in tmp:
            m = tmp.find("平均时间:")
            n = tmp.find("ms")
            time = tmp[m+len("平均时间:"):n]
            time = float(time)
            totalTime = totalTime + time
        if i == 2:
            rest = rd_result_xls.get_cell_value(pos[0] + i, pos[1] + 2)
            rest = rest.split(",")
            for res in rest:
                if "首选识别率:" in res:
                    m = res.find("首选识别率:")
                    n = res.find("%")
                    shouXuanShiBieLv = res[m:n+1]
                    result.append(shouXuanShiBieLv)
                if "误警率:" in res:
                    m = res.find("误警率:")
                    n = res.find("%")
                    wuJingLv = res[m:n+1]
                    result.append(wuJingLv)
                if "正确率:" in res:
                    m = res.find("正确率:")
                    n = res.find("%")
                    zhengQueLv = res[m:n+1]
                    result.append(zhengQueLv)
                if "正确接收率:" in res:
                    m = res.find("正确接收率:")
                    n = res.find("%")
                    zhengQueJieShouLv = res[m:n+1]
                    result.append(zhengQueJieShouLv)
                if "错误接收率:" in res:
                    m = res.find("错误接收率:")
                    n = res.find("%")
                    cuoWuJieShouLv = res[m:n+1]
                    result.append(cuoWuJieShouLv)

    totalTime_str = "流程平均耗时:" + str(("%.2f" % totalTime))  + "ms"
    for i in result:
        result_str = result_str + i + "<br>"
    return result_str + str(totalTime_str)


#从case excel模板里读取数据，构造html内容
def get_html_for_Case(sanJiName,rd_xls,rd_result_xls):
    """
    :param sanJiName:  测试用例主标题(三级)。该列不能重复
    :param rd_xls: 用例管理表格
    :param rd_result_xls: 结果分析表格
    :return:
    """
    EngName = ""
    qianti = ""
    jieguo = ""
    conHtml = ""
    Num = ""
    num = ""
    yiJiName_has = False
    erJiName_has = False
    jieguo_str = ""
    _2colNum = get_pos_from_cellValue(sanJiName,2,rd_xls) #3级标题位置(x,y)
    _2colNum = _2colNum[0]
    siJiName = rd_xls.get_cell_value(_2colNum[0], _2colNum[1] + 1)  #4级标题。流程名
    leiMing = rd_xls.get_cell_value(_2colNum[0], _2colNum[1] + 1)
    fuBiaoTi = rd_xls.get_cell_value(_2colNum[0], _2colNum[1] + 2)
    yiJiName = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]-2)
    erJiName = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]-1)
    EngName = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]+2)
    qianti = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]+3)
    mudi = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]+4)
    buzhou = rd_xls.get_cell_value(_2colNum[0],_2colNum[1]+5)
    try:
        if siJiName in suites_name:
            jieguo_str = read_flow_result(siJiName,rd_result_xls)
        else:
            jieGuoIdx_list = get_pos_from_cellValue(fuBiaoTi, 1, rd_result_xls)  # 从数据excel里读取对应三级标题的结果
            for jieGuoIdx in jieGuoIdx_list:
                if rd_result_xls.get_cell_value(jieGuoIdx[0],jieGuoIdx[1]) in fuBiaoTi and rd_result_xls.get_cell_value(jieGuoIdx[0],jieGuoIdx[1]-1) in leiMing:
                    jieguo = rd_result_xls.get_cell_value(jieGuoIdx[0],jieGuoIdx[1]+1)
                    jieguo_list = jieguo.strip("[").strip("]").split(",")
                    # logging.debug(jieguo_list)
                    if "'失败'" in jieguo_list:
                        jieguo_str = "失败" + "<br>"
                    else:
                        for i in jieguo_list:
                            if len(jieguo_list) >1:
                                if "通过" not in i:
                                    jieguo_str = jieguo_str + i.replace("'","") + "<br>"
                            else:
                                jieguo_str = jieguo_str + i.replace("'","") + "<br>"
    except:
        jieguo_str = ""
        logging.warning("测试的表格里，结果一栏为空")
    Num,num = 0,0 #一级二级标题跨越行号统计
    for key, val in caseManger_dic.items():
        if yiJiName == key:
            for ii in caseManger_dic[yiJiName]:
                for kk,vv in ii.items():
                    Num = Num + len(vv)
        for i in val:    #val 列表    i 字典      v 列表    key 一级   k 二级
            for k, v in i.items():
                if erJiName == k:
                    erJiName_has = True
                    num = len(i[erJiName])
    if yiJiName:
        conHtml = conHtml + "<tr>"+"\n"
        conHtml = conHtml + '<td rowspan="%d" class="mokuai">%s</td>' %(Num,yiJiName) +"\n"
        conHtml = conHtml + '<td rowspan="%d" class="mokuai">%s</td>' %(num,erJiName) +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %sanJiName +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %EngName +"\n"
        conHtml = conHtml + '<td  class="qianti">%s</td>' %qianti +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %mudi +"\n"
        conHtml = conHtml + '<td  class="buzhou">%s</td>' %buzhou +"\n"
        conHtml = conHtml + '<td colspan="1" class="jieguo" >%s</td>' %jieguo_str +"\n"
        if "失败" in jieguo_str:
            conHtml = conHtml.replace('class="jieguo"','class="jieguo_failed"')
        return conHtml
    if erJiName:
        conHtml = conHtml + "<tr>" +"\n"
        conHtml = conHtml + '<td rowspan="%d" class="mokuai">%s</td>' %(num,erJiName) +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %sanJiName +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %EngName +"\n"
        conHtml = conHtml + '<td  class="qianti">%s</td>' %qianti +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %mudi +"\n"
        conHtml = conHtml + '<td  class="buzhou">%s</td>' %buzhou +"\n"
        conHtml = conHtml + '<td colspan="1" class="jieguo" >%s</td>' % jieguo_str + "\n"
        if "失败" in jieguo_str:
            conHtml = conHtml.replace('class="jieguo"','class="jieguo_failed"')
        conHtml = conHtml + "</tr>" +"\n"
        return conHtml
    else:
        conHtml = conHtml + "<tr>" +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %sanJiName +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %EngName +"\n"
        conHtml = conHtml + '<td  class="qianti">%s</td>' %qianti +"\n"
        conHtml = conHtml + '<td  class="yongli_or_mudi">%s</td>' %mudi +"\n"
        conHtml = conHtml + '<td  class="buzhou">%s</td>' %buzhou
        conHtml = conHtml + '<td colspan="1" class="jieguo" >%s</td>' % jieguo_str + "\n"
        if "失败" in jieguo_str:
            conHtml = conHtml.replace('class="jieguo"','class="jieguo_failed"')
        conHtml = conHtml + "</tr>" +"\n"
        return conHtml

def write_html(htmlPath,str):
    f = open(htmlPath,"w",encoding="utf-8")
    f.write(str)
    f.close()

def find_ver(path):
    f = open(path, "r")
    line = f.readline()
    while line:
        line = f.readline()
        if "ISGetDetTrackVersionInfo()" in line:
            idx = line.find("ISGetDetTrackVersionInfo(): ") + len("ISGetDetTrackVersionInfo(): ")
            version = line[idx:]
            f.close()
            return version

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read(r"./testbed.ini")
    env = config.get("testbed","env")
    rd_result_path = config.get("testbed","output_xls")
    sdklog = config.get("testbed","file")
    print("sdklog",sdklog)
    version = find_ver(sdklog)
    print("version",version)
    rd_result_xls = rd_excel("result",rd_result_path)
    casesNum = rd_result_xls.get_col_data(2)
    passedNum,failedNum,skippedNum = 0,0,0
    for result in rd_result_xls.get_col_data(2):
        if "失败" in result:
            failedNum = failedNum + 1
        if "[]" == result:
            skippedNum = skippedNum + 1
    passedNum = len(rd_result_xls.get_col_data(2)) - 1 - failedNum - skippedNum
    rd_xls = rd_excel("Sheet1", r"./myUtils/template/excel_case_manage.xlsx") #模板名称
    htmlTp = r"./myUtils/template/templet_auto.html"
    hf = open(htmlTp, "r", encoding='UTF-8')
    contentHtml = ""
    content = hf.readline()
    contentHtml = contentHtml + content
    
    while (content):
        content = hf.readline()
        contentHtml = contentHtml + content
        if 'id="systemName"' in content:
            if env == "win7_64":
                contentHtml = contentHtml + "WINDOWS 7 64 位"
            if env == "win7_32":
                contentHtml = contentHtml + "WINDOWS 7 32 位"
            if env == "Ubuntu 16.04.6 LTS":
                contentHtml = contentHtml + "Ubuntu 16.04.6 LTS"
        if 'id="sdkVer"' in content:
            contentHtml = contentHtml + version
        if '<span style="color:green;">' in content and '</span>' not in content:
            contentHtml = contentHtml + str(passedNum)
        if '<span style="color:orange;">' in content and '</span>' not in content:
            contentHtml = contentHtml + str(skippedNum)
        if '<span style="color:red;">' in content and '</span>' not in content:
            contentHtml = contentHtml + str(failedNum)
        if "<!--=content start===-->" in content:
            for yiji, val in caseManger_dic.items():  # zidian bianli
                for ii in caseManger_dic[yiji]:  # liebiao bianli
                    for erji, vv in ii.items():  # zidian bianli
                        for sanji in vv:  #
                            # logging.debug(sanji)
                            tmp = get_html_for_Case(sanji,rd_xls,rd_result_xls)
                            # logging.debug(yiji,erji,sanji)
                            contentHtml = contentHtml + tmp
                            # logging.debug(tmp)
    hf.close()
    config.set("testbed","html",config.get("testbed","resultPath")+"/"+"result.html")
    with open("./testbed.ini", 'w') as config_file:
        config.write(config_file)
    # config.write(open("./testbed.ini","w"))
    htmlPath = config.get("testbed","html")
    write_html(htmlPath,contentHtml)
    logging.debug("generate html successfully ...")


