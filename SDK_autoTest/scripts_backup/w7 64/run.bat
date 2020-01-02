@echo off
color 02
pushd %~dp0

set "year=%date:~0,4%"
set "month=%date:~5,2%"
set "day=%date:~8,2%"
set "hour_ten=%time:~0,1%"
set "hour_one=%time:~1,1%"
set "minute=%time:~3,2%"
set "second=%time:~6,2%"

REM TASKKILL /F /IM python.exe /T
set name1=%year%%month%%day%0%hour_one%%minute%%second%
set name2=%year%%month%%day%%hour_ten%%hour_one%%minute%%second%
echo [testbed]>testbed.ini
echo env = win7_64>>testbed.ini

if "%hour_ten%" == " " (
	md "./result/tmp/W7_64_%name1%"
	echo file = ./result/tmp/W7_64_%name1%/SdkTestbed.log>>testbed.ini
	echo resultPath = ./result/tmp/W7_64_%name1%>>testbed.ini
	start .\myUtils\query_cpu_ram.py
    
) else (
	md "./result/tmp/W7_64_%name2%"
	echo file = ./result/tmp/W7_64_%name2%/SdkTestbed.log>>testbed.ini
	echo resultPath = ./result/tmp/W7_64_%name2%>>testbed.ini
	start .\myUtils\query_cpu_ram.py
    REM test.bat 2>&1 | tee   ./result/tmp/W7_64_%name2%/SdkTestbed.log
)

pushd %~dp0
REM start analyse_sdk_result.exe
REM TASKKILL /F /IM python.exe /T

