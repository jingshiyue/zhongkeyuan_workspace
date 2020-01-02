#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from goto import with_goto
import psutil
import os,datetime,time
import threading
import logging

# os.chdir(os.path.dirname(__file__)+"/Export/build/Target")
os.chdir(os.getcwd()+"/Export/build/Target")

log_path = "../../result/tmp/Monitor_CPU_RAM_%s.txt" % time.strftime('%Y%m%d%H%M%S',time.localtime())
# logging.basicConfig(level=logging.DEBUG,
    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # filename = log_path,
    # filemode='a')
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
# console.setFormatter(formatter)
# logger = logging.getLogger()
# logger.addHandler(console)


def getMemCpu():
    data = psutil.virtual_memory()
    # total = data.total #总内存,单位为byte
    # free = data.available #可以内存
    memory = "Memory:%d"%(int(round(data.percent)))+"%"+" "
    cpu = "CPU:%0.2f"%psutil.cpu_percent(interval=1)+"%"
    logging.info(memory+cpu)
    timer = threading.Timer(2*60,getMemCpu)
    timer.start()
################



@with_goto
def test():
    label .home
    print("1.standard single thread flow")
    print("2.standard multi thread flow")
    print("3.ftISDetTrack*")
    print("4.ftISFeature*")
    print("5.ftISCompare*")
    print("6.ftError*")
    print("7.ftAppliance*")
    print("8.All Above")
    print("q.Quit")
    # h = input("please enter your choice: ")
    h = "8"
    label .singleflow
    if h == "1":
        print("1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare")
        print("2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN")
        print("3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster")
        print("4.Back Home")
        s = input("please enter your choice: ")
        if s == "1":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompare_SingleThread")
            goto .singleflow
        if s == "2":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMN_SingleThread")
            goto .singleflow
        if s == "3":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMNfaster_SingleThread")
            goto .singleflow
        if s == "4":
            goto .home

    label .multiflow
    if h == "2":
        print("1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare")
        print("2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN")
        print("3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster")
        print("4.Back Home")
        m = input("please enter your choice: ")
        if m == "1":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompare_MultiThread")
            goto .multiflow
        if m == "2":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMN_MultiThread")
            goto .multiflow
        if m == "3":
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
            os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMNfaster_MultiThread")
            goto .multiflow
        if m == "4":
            goto .home

    label .detect
    if h == "3":
        print("1.ISFaceDetectPath")
        print("2.ISFaceDetectRgb")
        print("3.ISCalFaceInfoPath")
        print("4.All Above")
        print("5.Back Home")
        d = input("please enter your choice: ")
        if d == "1":
            os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISFaceDetectPath*")
            goto .detect
        if d == "2":
            os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISFaceDetectRgb*")
            goto .detect
        if d == "3":
            os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISCalFaceInfoPath*")
            goto .detect
        if d == "4":
            os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.*")
            goto .detect
        if d == "5":
            goto .home

    label .feature
    if h == "4":
        print("1.ISGetFeaturePath")
        print("2.ISGetFeatureWithFacePosPath(Run ISFaceDetectPath Earlier)")
        print("3.Back Home")
        f = input("please enter your choice: ")
        if f == "1":
            os.system("./FaceSDKTest --gtest_filter=ftISFeature.ISGetFeaturePath*")
            goto .feature
        if f == "2":
            os.system("./FaceSDKTest --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath*")
            goto .feature
        if f == "3":
            goto .home

    label .compare
    if h == "5":
        print("1.Run This Case First, Which Generate Feature And Pca Files For Other Cases")
        print("2.ISCompare")
        print("3.ISCompareMN")
        print("4.ISCompareMNfaster")
        print("5.All Above")
        print("6.Back Home")
        c = input("please enter your choice: ")
        if c == "1":
            os.system("./FaceSDKTest --gtest_filter=ftISCompare.prepareFeatureAndPcaRapidlyUsingMultiThread")
            goto .compare
        if c == "2":
            os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompare_*")
            goto .compare
        if c == "3":
            os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompareMN_*")
            goto .compare
        if c == "4":
            os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompareMNfaster_*")
            goto .compare
        if c == "5":
            os.system("./FaceSDKTest --gtest_filter=ftISCompare.*")
            goto .compare
        if c == "6":
            goto .home

    label .error
    if h == "6":
        print("1.inputImagesWithATooSmallSize")
        print("2.inputImagesCanNotBeFound")
        print("3.detectWithOutCreatingDectectChannel")
        print("4.inputImagesDetectedNoFace")
        print("5.inputImagesGetNoFeature")
        print("6.whatImageLeadsToGetFeatureError")
        print("7.whatIsCompareMNError")
        print("8.All Above")
        print("9.Back Home")
        e = input("please enter your choice: ")
        if e == "1":
            os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesWithATooSmallSize")
            goto .error
        if e == "2":
            os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesCanNotBeFound")
            goto .error
        if e == "3":
            os.system("./FaceSDKTest --gtest_filter=ftError.detectWithOutCreatingDectectChannel")
            goto .error
        if e == "4":
            os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesDetectedNoFace")
            goto .error
        if e == "5":
            os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesGetNoFeature")
            goto .error
        if e == "6":
            os.system("./FaceSDKTest --gtest_filter=ftError.whatImageLeadsToGetFeatureError")
            goto .error
        if e == "7":
            os.system("./FaceSDKTest --gtest_filter=ftError.whatIsCompareMNError")
            goto .error
        if e == "8":
            os.system("./FaceSDKTest --gtest_filter=ftError.*")
            goto .error
        if e == "9":
            goto .home

    label .appliance
    if h == "7":
        print("1.dumpVersionNo")
        print("2.ISGetFeatureLength_Check")
        print("3.dumpConfigIni")
        print("4.theGivenPictureHasMoreThan15FacesBeDetected")
        print("5.whatFaceReturnsEarlierInOutResultAndWhatLater")
        print("6.personAndIdCardCompareOfOneDirectory")
        print("7.personAndIdCardCompareOfOneDirectorySteply")
        print("8.camera")
        print("9.All Above")
        print("10.Back Home")
        a = input("please enter your choice: ")
        if a == "1":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.dumpVersionNo")
            goto .appliance
        if a == "2":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.ISGetFeatureLength_Check")
            goto .appliance
        if a == "3":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.dumpConfigIni")
            goto .appliance
        if a == "4":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.theGivenPictureHasMoreThan15FacesBeDetected")
            goto .appliance
        if a == "5":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.whatFaceReturnsEarlierInOutResultAndWhatLater")
            goto .appliance
        if a == "6":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.personAndIdCardCompareOfOneDirectory")
            goto .appliance
        if a == "7":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.personAndIdCardCompareOfOneDirectorySteply")
            goto .appliance
        if a == "8":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.camera")
            goto .appliance
        if a == "9":
            os.system("./FaceSDKTest --gtest_filter=ftAppliance.*")
            goto .appliance
        if a == "10":
            goto .home
################
    if h == "8":
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.dumpConfigIni")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.dumpVersionNo")
        os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISFaceDetectPath*")
        print("SingleThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompare_SingleThread")
        print("SingleThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMN_SingleThread")
        print("SingleThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_SingleThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMNfaster_SingleThread")
        print("MultiThread:(1.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompare)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompare_MultiThread")
        print("MultiThread:(2.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMN)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMN_MultiThread")
        print("MultiThread:(3.ISFaceDetectRgb+ISGetFeatureWithFacePosPath+ISCompareMNfaster)")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISDetTrack.ISFaceDetectRgb_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath_MultiThread")
        os.system("./FaceSDKTest smartirsec2018 --gtest_filter=ftISCompare.ISCompareMNfaster_MultiThread")
        os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISFaceDetectRgb*")
        os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISFaceDetTrackRgb*")
        os.system("./FaceSDKTest --gtest_filter=ftISDetTrack.ISCalFaceInfoPath*")
        os.system("./FaceSDKTest --gtest_filter=ftISFeature.ISGetFeaturePath*")
        os.system("./FaceSDKTest --gtest_filter=ftISFeature.ISGetFeatureWithFacePosPath*")
        os.system("./FaceSDKTest --gtest_filter=ftISCompare.prepareFeatureAndPcaRapidlyUsingMultiThread")
        os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompare_*")
        os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompareMN_*")
        os.system("./FaceSDKTest --gtest_filter=ftISCompare.ISCompareMNfaster_*")
        os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesWithATooSmallSize")
        os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesCanNotBeFound")
        os.system("./FaceSDKTest --gtest_filter=ftError.detectWithOutCreatingDectectChannel")
        os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesDetectedNoFace")
        os.system("./FaceSDKTest --gtest_filter=ftError.inputImagesGetNoFeature")
        os.system("./FaceSDKTest --gtest_filter=ftError.whatImageLeadsToGetFeatureError")
        os.system("./FaceSDKTest --gtest_filter=ftError.whatIsCompareMNError")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.ISGetFeatureLength_Check")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.theGivenPictureHasMoreThan15FacesBeDetected")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.whatFaceReturnsEarlierInOutResultAndWhatLater")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.personAndIdCardCompareOfOneDirectory")
        os.system("./FaceSDKTest --gtest_filter=ftAppliance.personAndIdCardCompareOfOneDirectorySteply")
        exit()
################        
       

print("prepare pics first, and then update configuration to config.ini!")

# f = open("/proc/cpuinfo", "rt")
# namePrinted = False;
# coresPrinted = False;
# for line in f:
    # if "model name" in line and not(namePrinted):
        # print(line, end='')
        # namePrinted = True
    # if "cpu cores" in line and not(coresPrinted):
        # print(line, end='')
        # coresPrinted = True
# f.close()

query_timer = threading.Timer(0,getMemCpu)
query_timer.setDaemon(True)
query_timer.start()
test()

