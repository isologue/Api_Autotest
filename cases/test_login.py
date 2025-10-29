import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conftest import global_data
from core.client import *
from util.util import *
# from cases.conftest import *
# def test_login01():
#     '''
#     登录用例1-正确登录
#     '''
#     # res = requests.post(url='http://123.56.99.53:9000/event/api/login',
#     #                 headers={"content-Type":"application/x-www-form-urlencoded"},
#     #                 data={"username":"zhangsan","password":"123"},timeout=1)
#     # print(res,text)
#     # assert res.status_code == 200, '状态码非200'

#     client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
#     client.set_datas({"username": "test","password": "123456"})
#     client.send()
#     client.check_code_200()
#     client.check_res_time_less_than(1000)
#     client.check_json_value('data.user_id',1)


# def test_login02():
#     '''
#     错误登录
#     '''
#     # res = requests.post(url='http://123.56.99.53:9000/event/api/login',
#     #                 headers={"content-Type":"application/x-www-form-urlencoded"},
#     #                 data={"username":"zhangsan","password":"12313"},timeout=1)
    
#     # assert res.status_code == 200, '状态码非200'
#     client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
#     client.set_datas({"username": "test","password": "1234567"})
#     client.send()
#     client.check_code(401)
#     client.check_res_time_less_than(1000)
#     # client.check_json_value('data.user_id',1)


# @pytest.mark.parametrize('username,password,code,msg',get_file('login.csv'))
# @allure.feature('用户登录接口测试') # 模块
# @allure.title('登录数据测试') # 每个用例的标题
# @pytest.mark.run(order=1) # 用例运行顺序，越小越先运行（报告中无体现）
# @paramdata('username,password,code,msg',get_file('login.csv')) # util里改名了paramdata
# def test_login(api,global_set,username,password,code,msg):
#     '''
#     参数化登录用例
#     '''
#     # client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
#     client = api('登录')
#     client.set_datas({"username":username ,"password":password })
#     client.send()
#     client.check_code(code)
#     client.check_res_time_less_than(1000)
#     # client.check_json_value('data.user_id',1)
#     client.check_json_value('message',f'{msg}')
#     # 获取变量
#     token = client.json_path_value('data.access_token')
#     global_set('token', token)


@allure.feature('用户登录接口测试') # 模块
@allure.title('登录数据测试') # 每个用例的标题
@pytest.mark.run(order=1) # 用例运行顺序，越小越先运行（报告中无体现）
@paramdata('case_info',get_excel_apitestcase('登录')) # util里改名了paramdata
def test_login(api,global_set,case_info):
    '''
    excel驱动
    '''
    # client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
    client = api('登录')
    client.set_datas(eval(case_info['正文参数']))
    client.send()
    client.check_code(case_info['状态码'])
    client.check_res_time_less_than(1000)
    # client.check_json_value('data.user_id',1)
    client.check_json_value('message',f'{case_info['断言1']}')
    # 获取变量
    token = client.json_path_value('data.access_token')
    global_set('token', token)
    print(global_data)

if __name__ == '__main__':
    # test_login01()
    pytest.main()


