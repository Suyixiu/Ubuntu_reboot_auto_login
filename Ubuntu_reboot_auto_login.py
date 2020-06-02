import sys
import os
import time
import requests

def auto_login():
    login_url = "https://drcom.szu.edu.cn/"
    data = {"DDDDD": "你的DRcom账号", "upass": "你的DRcom密码", "R1": "0",
            "R2": "", "R6": "0", "para": "00", "0MKKey": "123456"}

    try:
        requests.post(login_url, data)
    except:
        pass

offline_count = 0

if __name__ == '__main__':
    auto_login()
    url = 'https://www.baidu.com'
    while True:
        # 每隔1分钟也就是60秒ping一次百度 若ping不通则重新auto_login 超过5次则重启电脑 #
        if(os.system(u"ping www.baidu.com -c 1 > 你下载这个包的路径/ping.log") != 0):
            print("offline")
            offline_count += 1
            auto_login()
            if(offline_count == 6):
                os.system("echo 你的ubuntu密码| sudo -S reboot")
        else:
            offline_count = 0
            print("good")
        # 每隔1分钟也就是60秒检查一下teamviewer是否正常 若网络正常而teamviewer没开则打开
        if(offline_count == 0 and os.system("ps -u 你的ubuntu账号 | grep TeamViewer") != 0):
            os.system("teamviewer & > 你下载这个包的路径/teamviewer_run.log")

        time.sleep(3)
