import pytest
from requests import session
from run import *
from util.util import *
from core.client import *

result_data = {'total':0,'pass':0,'fail':0,'error':0}
global_data = {}

# 重写的pytest里的一个钩子函数，这个方法会在用例执行前执行一次，在用例执行中执行一次， 在用例执行完成后执行一次
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    result = yield # 这个打印的result结果看不出东西
    result2 = result.get_result()  # 所以需要这样转一下
#     print(result2)
#     print(result2.when)
#     print(result2.outcome)
    #  <TestReport 'cases/test_getteventlist.py::test_geteven01' when='setup' outcome='passed'>
    #  <TestReport 'cases/test_getteventlist.py::test_geteven01' when='call' outcome='failed'>
    #  <TestReport 'cases/test_getteventlist.py::test_geteven01' when='teardown' outcome='passed'> 
    if result2.when == 'call':
        result_data['total'] += 1
        if result2.outcome == 'passed':
                result_data['pass'] += 1
        elif result2.outcome == 'failed':
                result_data['fail'] += 1
        elif result2.outcome == 'error':
                result_data['error'] += 1

# 读取模块(文件)名称，匹配yaml文件内同名的标题，然后拿到标题内的参数数据，生成一个client对象
# @pytest.fixture
# def api(request):
#         url, method, body_type = get_api_info(request.module.__name__.split(".")[1][5])
#         client = Client(url=url, method=method,body_type=body_type)
#         return client

# 这个夹具方法就是少引一个包
# 获取变量
# @pytest.fixture
# def global_get():
#          return global_data
# 可以进化一下，让取值从global_data['name'] 变成 global_data('name'),字典取值变成方法取值
@pytest.fixture
def global_get():
        def __global_get(name):
                return global_data[name]
        return __global_get
        
# 设置变量
# @pytest.fixture
# def global_set(name, value):
#         global_data[name] = value
#         return global_set
# 进化
@pytest.fixture
def global_set():
        def __global_set(name, value):
                global_data[name] = value
        return __global_set


# 根据获取的接口模板创建client
@pytest.fixture
def api():
        def __api(name):
                url,method,body_type = get_apitemplate(name)
                client = Client(url=url,method=method,body_type=body_type)    
                return client
        return __api


# @pytest.fixture(scope="class")
# def excel_global():
#         def __excel_global(name):
#                 value = get_excel_global(name)
#                 return value
#         return __excel_global

