# 启动脚本
import pytest
import os
from dingtalkchatbot.chatbot import DingtalkChatbot
import time
from conftest import *

if __name__ == '__main__':

    tmp = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

    # pytest.main(['./cases/test_login.py','./cases/test_order.py','-s'])
    # cmd命令行这样：pytest ./cases/test_login.py ./cases/test_order.py -s
    # --rerurs 重跑次数 --reruns-delay 等待运行秒数
    # pytest.main(['./cases','-s','--rerurs=2','--reruns-delay=2','--alluredir=./report/json','--clean-alluredir'])
    pytest.main(['./cases','-s','--alluredir=./report/json','--clean-alluredir'])
    # 用例结果数
    # print(result_data)

    # 钉钉机器人通知
    ding_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=efd03834fdfd353b3e712d57964b82fcbaf2053e352851d8c14e3d627a7a99a9'
    dingding = DingtalkChatbot(ding_webhook)
    dingding.send_text(msg=f'接口测试结果:{result_data}',is_at_all=True) # at_mobiles=['17300000001']可以艾特某个人

       # 在线报告
    # os.system(r"allure serve ./report/json")
        # 本地报告
    os.system(fr"allure generate ./report/json -c -o ./report/localreport/{tmp}")
    # os.system(fr"allure open ./report/localreport/{tmp}")

    
    
    