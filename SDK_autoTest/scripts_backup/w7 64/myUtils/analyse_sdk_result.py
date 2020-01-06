import os
import sys
import collections
import xlrd
import xlwt
import logging
import datetime,time
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        filename = "./result.log",
        filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
console.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console) 

# os.chdir(os.path.dirname(__file__))
######################套件和用例管理##########################################################
suites_name = ["SingleThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)",
                "SingleThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)",
                "SingleThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)",
                "MultiThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)",
                "MultiThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)",
                "MultiThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)",
                ]


suite_dict = collections.OrderedDict([
    ("ftISDetTrack.ISFaceDetectPath*",["ftISDetTrack.ISFaceDetectPath_SingleThread",
        "ftISDetTrack.ISFaceDetectPath_MultiThread",
        "ftISDetTrack.ISFaceDetectPath_OutResultCheck",]),

    ("SingleThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)",["ftISDetTrack.ISFaceDetectRgb_SingleThread","ftISFeature.ISGetFeatureWithFacePosPath_SingleThread","ftISCompare.ISCompare_SingleThread"]),
    ("SingleThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)",["ftISDetTrack.ISFaceDetectRgb_SingleThread","ftISFeature.ISGetFeatureWithFacePosPath_SingleThread","ftISCompareMN.ISCompareMN_SingleThread"]),
    ("SingleThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)",["ftISDetTrack.ISFaceDetectRgb_SingleThread","ftISFeature.ISGetFeatureWithFacePosPath_SingleThread","ftISCompareMN.ISCompareMNfaster_SingleThread"]),
    ("MultiThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)",["ftISDetTrack.ISFaceDetectRgb_MultiThread","ftISFeature.ISGetFeatureWithFacePosPath_MultiThread","ftISCompare.ISCompare_MultiThread"]),
    ("MultiThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)",["ftISDetTrack.ISFaceDetectRgb_MultiThread","ftISFeature.ISGetFeatureWithFacePosPath_MultiThread","ftISCompareMN.ISCompareMN_MultiThread"]),
    ("MultiThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)",["ftISDetTrack.ISFaceDetectRgb_MultiThread","ftISFeature.ISGetFeatureWithFacePosPath_MultiThread","ftISCompareMN.ISCompareMNfaster_MultiThread"]),

    ("ftISDetTrack.ISFaceDetectRgb*",["ftISDetTrack.ISFaceDetectRgb_SingleThread",
        "ftISDetTrack.ISFaceDetectRgb_MultiThread",
        "ftISDetTrack.ISFaceDetectRgb_OutResultCheck",]),
    ("ftISDetTrack.ISFaceDetectPath*",["ftISDetTrack.ISFaceDetectPath_SingleThread",
        "ftISDetTrack.ISFaceDetectPath_MultiThread",
        "ftISDetTrack.ISFaceDetectPath_OutResultCheck",]),
    ("ftISDetTrack.ISFaceDetTrackRgb*",["ftISDetTrack.ISFaceDetTrackRgb_SingleThread",
        "ftISDetTrack.ISFaceDetTrackRgb_MultiThread",
        "ftISDetTrack.ISFaceDetTrackRgb_OutResultCheck",]),
    ("ftISDetTrack.ISCalFaceInfoPath*",["ftISDetTrack.ISCalFaceInfoPath_SingleThread",
    "ftISDetTrack.ISCalFaceInfoPath_MultiThread",
    "ftISDetTrack.ISCalFaceInfoPath_OutResultCheck",]),

    ("ftISFeature.ISGetFeaturePath*",["ftISFeature.ISGetFeaturePath_SingleThread",
        "ftISFeature.ISGetFeaturePath_MultiThread",
        "ftISFeature.ISGetFeaturePath_OutResultCheck"]), 
    ("ftISFeature.ISGetFeatureWithFacePosPath*",[
        "ftISFeature.ISGetFeatureWithFacePosPath_SingleThread",
        "ftISFeature.ISGetFeatureWithFacePosPath_MultiThread",
        "ftISFeature.ISGetFeatureWithFacePosPath_OutResultCheck"]),
    ("ftISCompare.prepareFeatureAndPcaRapidlyUsingMultiThread",["ftISCompare.prepareFeatureAndPcaRapidlyUsingMultiThread",]),
    ("ftISCompare.ISCompare_*",["ftISCompare.ISCompare_SingleThread","ftISCompare.ISCompare_MultiThread"]),
    ("ftISCompareMN.prepareFeatureAndPcaRapidlyUsingMultiThread",["ftISCompareMN.prepareFeatureAndPcaRapidlyUsingMultiThread",]),
    ("ftISCompareMN.ISCompareMN_*",["ftISCompareMN.ISCompareMN_SingleThread","ftISCompareMN.ISCompareMN_MultiThread"]),
    ("ftISCompareMN.ISCompareMNfaster_*", ["ftISCompareMN.ISCompareMNfaster_SingleThread","ftISCompareMN.ISCompareMNfaster_MultiThread" ]),
    ("ftError.inputImagesWithATooSmallSize",["ftError.inputImagesWithATooSmallSize",]),
    ("ftError.inputImagesCanNotBeFound",["ftError.inputImagesCanNotBeFound"]),
    ("ftError.detectWithOutCreatingDectectChannel",["ftError.detectWithOutCreatingDectectChannel",]),
    ("ftError.inputImagesDetectedNoFace",["ftError.inputImagesDetectedNoFace",]),
    ("ftError.inputImagesGetNoFeature",["ftError.inputImagesGetNoFeature",]),
    ("ftError.whatImageLeadsToGetFeatureError",["ftError.whatImageLeadsToGetFeatureError",]),
    ("ftError.whatIsCompareMNError",["ftError.whatIsCompareMNError",]),
    ("ftAppliance.dumpVersionNo",["ftAppliance.dumpVersionNo",]),
    ("ftAppliance.ISGetFeatureLength_Check",["ftAppliance.ISGetFeatureLength_Check",]),
    ("ftAppliance.dumpConfigIni",["ftAppliance.dumpConfigIni",]),
    ("ftAppliance.theGivenPictureHasMoreThan15FacesBeDetected",["ftAppliance.theGivenPictureHasMoreThan15FacesBeDetected",]),
    ("ftAppliance.whatFaceReturnsEarlierInOutResultAndWhatLater",["ftAppliance.whatFaceReturnsEarlierInOutResultAndWhatLater",]),
    ("ftAppliance.personAndIdCardCompareOfOneDirectory",["ftAppliance.personAndIdCardCompareOfOneDirectory",]),
    ("ftAppliance.personAndIdCardCompareOfOneDirectorySteply",["ftAppliance.personAndIdCardCompareOfOneDirectorySteply",]),
    ])
################################################################################

colors = {
        1: 'red',
        2: 'green',
        3: 'blue',
        4: 'brown',
        5: 'cyan',
        6: 'orange',
        7: 'pink',
        8: 'purple',
        9: 'royalblue',
        10: 'yellow',
        11: 'darkgray',
        12: 'gold',
        13: 'gray',
        14: 'navy',
        15: 'violet'}

def find_str(str,searchStr,offset):
        start = str.find(searchStr) + len(searchStr)
        content = str[start+1:start+offset]
        return content

def str2timestamp(time_str,format="%Y-%m-%d %H:%M:%S"):   #格式 ："%Y-%m-%d %H:%M:%S"
        timeArray = time.strptime(time_str, format)  # 先转换为时间数组
        timeStamp = int(time.mktime(timeArray))  #转换为时间戳 单位是秒
        return timeStamp

def timestamp2str(timestamp,format="%Y-%m-%d %H:%M:%S"):
        return time.strftime(format,time.localtime(timestamp))

class wt_excel:
    def __init__(self,sheet_name,exl_f_path):
        self.exl_f_path = exl_f_path
        self.book = xlwt.Workbook()
        self.sheet = self.book.add_sheet(sheet_name)
        
    def wt_cell(self,row,col,content):
        """写入单元格"""
        # try:
        self.sheet.write(row,col,content)
        self.book.save(self.exl_f_path)
        # except:
            # raise "write into cell failed !!!"

def find_suites(txt,sutes_name,sute_div1="SingleThread:",sute_div2="MultiThread:"):  
    """适用于单线程、多线程的几个特殊用例"""
    content_list = open(txt,"rb").readlines()
    suites_content_list = []
    start_indx = 0
    end_indx = 0
    indx = 0
    suites_has = False
    # print(sutes_name)
    for line in content_list:
        if sutes_name in str(line):
            #logging.debug(suites_name)
            #logging.debug(line)
            start_indx = indx
            suites_has = True
            break
        indx += 1
    offset = 0

    for line in content_list[start_indx+1:]:
        if sute_div1 in str(line) or sute_div2 in str(line):
                end_indx = start_indx + 1 + offset
                break
        offset += 1
        end_indx = start_indx + 1 + offset
    # print(start_indx,end_indx)
    if suites_has:
        suites_content_list = content_list[start_indx:end_indx]
    else:
        suites_content_list = []
    #logging.debug(suites_content_list)
    return suites_content_list


def find_suite(txt,sute_name,sute_div = "Note: Google Test filter"):
    content_list = open(txt,"rb").readlines()
    suite_content_list = []
    start_indx = 0
    end_indx = 0
    # raw_suite = f.readlines()
    indx = 0
    for line in content_list:
        if sute_name in str(line) and sute_div in str(line):
            start_indx = indx
            break
        indx += 1
    offset = 0

    for line in content_list[start_indx+1:]:
        if sute_div in str(line):
                end_indx = start_indx + 1 + offset
                break
        offset += 1
        end_indx = start_indx + 1 + offset    
    suite_content_list = content_list[start_indx:end_indx]
    return suite_content_list


def find_case(suite_content_list,case_name,case_div = "[ RUN      ]"):
    case_content = []
    start_indx,end_indx,indx1,indx2 = 0,0,0,0
    for line in suite_content_list:
        if case_name in str(line) and case_div in str(line):
            start_indx = indx1
            break
        indx1 += 1
    for line in suite_content_list[start_indx+1:]:
        if case_div in str(line):
            end_indx = start_indx+1 + indx2
            break
        indx2 += 1
        end_indx = start_indx+1 + indx2
    # print(start_indx,end_indx)
    case_content = suite_content_list[start_indx:end_indx]
    # print(case_content)
    return  case_content
    

def alynase_case_rest(case_content,**kwags): #OutResultCheck
    result = []
    Num_P, Num_N, Num_P_DP, Num_N_DP, P_in, P_out = 0, 0, 0, 0, 0, 0
    imgPathA_same = False
    imgPathB_same = False
    compare_fail = True
    for cont in case_content:
        cont = str(cont)
        for key,val in kwags.items():
            if val in cont:
                _result = ""
                if "success rate A:" in cont:
                    m = cont.find("success rate A:")
                    n = cont.find("%")
                    _result ="文件夹A检出率:" + cont[m+len("success rate A:"):n+1]
                    result.append(_result)
                if "success rate B:" in cont:
                    m = cont.find("success rate B:")
                    n = cont.find("%")
                    _result = "文件夹B检出率:" + cont[m + len("success rate B:"):n + 1]
                    result.append(_result)
                if "Wu Shi Lv:" in str(cont):
                    m = cont.find("Wu Shi Lv:")
                    n = cont.find("%")
                    _result = "误警率:" + cont[m + len("Wu Shi Lv:"):n + 1]
                    result.append(_result)
                if "average time cost:" in cont:
                    m = cont.find("average time cost:")
                    n = cont.find("ms")
                    _result = "平均时间:" + cont[m + len("average time cost:"):n + 2]
                    result.append(_result)
                if "total positive samples:" in cont:
                    m = cont.find("total positive samples:")
                    n = cont.find("\\r")
                    Num_P = cont[m + len("total positive samples:"):n]
                    Num_P = int(handle_str(Num_P))
                    P_in = Num_P
                if "total negative samples:" in cont:
                    m = cont.find("total negative samples:")
                    n = cont.find("\\r")
                    Num_N = cont[m + len("total negative samples:"):n]
                    Num_N = int(handle_str(Num_N))
                    P_out = Num_N
                if "for an identical person, but score less than compareFaceValue:" in cont:
                    m = cont.find("for an identical person, but score less than compareFaceValue:")
                    n = cont.find("\\r")
                    Num_P_DP_tmp = cont[m + len("for an identical person, but score less than compareFaceValue:"):n]
                    if "\\" in Num_P_DP_tmp:
                        idx1 = Num_P_DP_tmp.find("\\")
                        Num_P_DP_tmp = Num_P_DP_tmp[:idx1]
                    Num_P_DP = Num_P - int(handle_str(Num_P_DP_tmp))
                if "for two different persons, but score more than compareFaceValue:" in cont:
                    m = cont.find("for two different persons, but score more than compareFaceValue:")
                    n = cont.find("\\r")
                    Num_N_DP = cont[m + len("for two different persons, but score more than compareFaceValue:"):n]
                    Num_N_DP = int(handle_str(Num_N_DP))
                    try:
                        zhengQueLv = (Num_P_DP+Num_N-Num_N_DP)/(Num_P+Num_N)*100
                    except:
                        zhengQueLv = 0
                    result.append("正确率:%s" %(str(("%.2f" % zhengQueLv))+"%"))
                    try:
                        zhengQueJieShouLv = Num_P_DP/Num_P*100
                    except:
                        zhengQueJieShouLv = 0
                    result.append("正确接收率:%s" %str((("%.2f" % zhengQueJieShouLv))+"%"))
                    try:
                        cuoWuJieShouLv = Num_N_DP/Num_N*100
                    except:
                        cuoWuJieShouLv = 0
                    result.append("错误接收率:%s" %str((("%.2f" % cuoWuJieShouLv))+"%"))
                if "positive samples compare out max score:" in cont:
                    m = cont.find("positive samples compare out max score:")
                    n = cont.find("\\r")
                    Num_P_DP = cont[m + len("positive samples compare out max score:"):n]
                    Num_P_DP = int(handle_str(Num_P_DP))
                if "negative samples compare out exceed score:" in cont:
                    m = cont.find("negative samples compare out exceed score:")
                    n = cont.find("\\r")
                    Num_N_DP = cont[m + len("negative samples compare out exceed score:"):n]
                    Num_N_DP = int(handle_str(Num_N_DP))
                    try:
                        shouXuanShiBieLv = Num_P_DP/P_in*100
                    except:
                        shouXuanShiBieLv = 0
                    _result = "首选识别率:" + str((("%.2f" % shouXuanShiBieLv))+"%")
                    result.append(_result)
                if "are the same" in cont and "imgPathA" in cont:
                    imgPathA_same = True
                if "are the same" in cont and "imgPathB" in cont:
                    imgPathB_same = True
                if "FAILED" in cont:
                    compare_fail = False
                if "false" in cont:
                    compare_fail = False
                if "[  PASSED  ]" in cont:
                    result.append("通过")
                if "[  FAILED  ]" in cont:
                    result.append("失败")

    if imgPathA_same and imgPathB_same and compare_fail:
        result.append("单线程与多线程测试结果一致")
    if compare_fail == False:
        result.append("失败")
    return result

def write_rest(content_list):
    if not os.path.exists("result"):
        os.mkdir("result")
    f = open("./result/result_%s.ret" % (time.strftime('%Y%m%d%H%M%S',time.localtime())),"ab+")
    f.writelines(content_list)
    f.close()

def handle_str(str):
    str = str.strip()
    if "\\" in str:
        idx = str.find("\\")
        str = str[:idx]
    return str

if __name__ == "__main__":
    import configparser
    config = configparser.ConfigParser()
    config.read(r".\testbed.ini")
    env = config.get("testbed","env")
    analyse_file = config.get("testbed","file")

    logging.info("[分析文件]  %s" %analyse_file)
    if not os.path.exists("result"):
        os.mkdir("result")
    resultPath = config.get("testbed","resultPath")
    excel = resultPath + "/result.xls"
    wt_exc = wt_excel("result",excel)
    wt_exc.wt_cell(0,0,"test suite".upper())
    wt_exc.wt_cell(0,1,"test case".upper())
    wt_exc.wt_cell(0,2,"test result".upper())
    j = 1
    for suite_name,cases_name in suite_dict.items():
        if suite_name in suites_name:
            suite = find_suites(analyse_file,suite_name)
        else:
            suite = find_suite(analyse_file,suite_name)
        for case_name in cases_name:
            case = find_case(suite,case_name)
            rest = alynase_case_rest(case,
                                    keyw1="rate",
                                    keyw2="average time",
                                    keyw3="[  PASSED  ]",
                                    keyw4="[  FAILED  ]",
                                    keyw5="are the same",
                                    keyw6="identical person",
                                    keyw7="two different persons",
                                    keyw8="Compare Score:",
                                    keyw9 = "positive samples",
                                    keyw10="Shou Xuan Shi Bie Lvs",
                                    keyw11="negative samples",
                                    keyw12="Wu Shi Lv",
                                     )
            for i in range(3):
                if i==0:
                    wt_exc.wt_cell(j,i,str(suite_name))
                if i==1:
                    wt_exc.wt_cell(j,i,str(case_name))
                if i==2:
                    # print(rest)
                    wt_exc.wt_cell(j,i,str(rest))
            j += 1
    output_xls = "." + excel[1:]
    config.set("testbed","output_xls",output_xls)
    with open("./testbed.ini", 'w') as config_file:
        config.write(config_file)
    logging.debug("[OUTPUT] %s" %output_xls)
    logging.debug("generate EXCEL complete...")
    
    monitorF = config.get("testbed","monitorlog")
    mf = open(monitorF, "r")
    cpu,ram,t = [],[],[]
    start_time = mf.readline()[0:19]
    _start = str2timestamp(start_time)
    _xticks = []
    line = mf.readline()
    while (line):
        if "Memory" in line:
            _memory = float((find_str(line, "Memory", 3)))
        if "CPU" in line:
            _cpu = float((find_str(line, "CPU", 5)))
        if "2019" in line:
            _t = '%.2f' % ((str2timestamp(line[0:19]) - _start) / 3600)
            _t = float(_t)
        cpu.append(_cpu)
        ram.append(_memory)
        t.append(_t)
        line = mf.readline()
    offset = t[-1] / 10
    for i in range(11):
        _xticks.append(offset * i)
    monitorPng = resultPath + "/monitor.png"
    plt.figure(dpi=128, figsize=(10, 7))
    plt.plot(t, cpu, label="CPU", color=colors[2], linestyle='-')
    plt.plot(t, ram, label="RAM", color=colors[10], linestyle='-')
    plt.xlabel("time(hour)")
    plt.ylabel("Occupancy rate")
    plt.title("Resource statistics")
    plt.legend(loc='upper left')
    plt.xticks(_xticks)
    plt.ylim(0, 100)
    plt.savefig(monitorPng)
    mf.close()
    
    config.set("testbed","monitorPng",monitorPng)
    with open("./testbed.ini", 'w') as config_file:
        config.write(config_file)
    logging.debug("generate monitor.png complete...")
    
    
    logging.debug("analyse successfully !!!")

