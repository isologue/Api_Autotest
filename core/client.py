import requests
import jsonpath
import allure
import json
from util.util import *
class Client(object):
    base_url = get_excel_global('base_url')
    def __init__(self,url,method,body_type=None,timeout=3):
        # self.base_url = excel_global('base_url')
        self.url = Client.base_url + url
        self.method = method
        self.body_type = body_type
        self.timeout = timeout
        self.headers = {}
        self.data = {}
        self.params = {}
        self.res = None
    
    @allure.step('接口信息内容')
    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers, params=self.params,timeout=self.timeout)

        elif self.method == 'POST':
            if self.body_type == 'form':
                self.set_header('Content-Type','application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers,params=self.params,data=self.data,timeout=self.timeout)

            elif self.body_type == 'files':
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,files=self.data,timeout=self.timeout)

            elif self.body_type == 'json':
                self.set_header('Content-Type','application/json')
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,json=self.data,timeout=self.timeout)

            else:
                raise Exception('请求方式错误！')

        # 报告内的步骤内容输出
        allure.attach(self.url,'请求url',allure.attachment_type.JSON)
        allure.attach(self.method,'请求方法',allure.attachment_type.JSON)
        allure.attach(json.dumps(self.headers),'请求头',allure.attachment_type.JSON)
        allure.attach(json.dumps(self.data),'请求正文',allure.attachment_type.JSON)
        allure.attach(str(self.res.status_code),'响应状态码',allure.attachment_type.JSON)
        allure.attach(json.dumps(self.res.text),'响应内容',allure.attachment_type.JSON)


    # 设置请求头
    def set_header(self,key,value):
        self.headers[key] = value

    def set_headers(self,data):
        if isinstance(data, dict): # 判断传入参数是否是字典
            self.headers = data
        else:
            raise Exception('头信息参数有误，应为字典')

    # 设置请求正文内容
    def set_data(self,key,value):
        self.data[key] = value

    def set_datas(self,data):
        if isinstance(data, dict): # 判断传入参数是否是字典
            self.data = data
        else:
            raise Exception('正文参数有误，应为字典')
    
    # 获取状态码
    @property # 让方法当成变量调用，a() 变成 a
    def status_code(self):
        if self.res is not None:
            return self.res.status_code
        else:
            print('状态码获取失败')
            return None
    # 获取响应时间
    @property
    def res_times(self):
        if self.res is not None:
             return round(self.res.elapsed.total_seconds() * 1000)
        else:
            print('响应时间获取失败')
            return None
    # 获取响应内容json格式
    @property
    def res_text(self):
        if self.res is not None:
             return self.res.text
        else:
            print('响应内容获取失败')
            return None
    @property
    # 获取响应内容并转为dict格式
    def res_json_to_dict(self):
        if self.res is not None:
            print(f'获取响应内容：{self.res.text}')
            return self.res.json()
        else:
            print('响应内容获取失败')
            return None

    # 获取cookies
    @property
    def cookies(self):
        if self.res is not None:
             return self.res.cookies
        else:
            print('cookies获取失败')
            return None

    # jsonpath取值
    def json_path_value(self,value):
        if not value.startswith('$.'):
            value = '$.' + value
        result = jsonpath.jsonpath(self.res_json_to_dict, value)
        if result:
            return result[0]
        else:
            print(f'取值失败，不存在该路径{value}')
            return None

    @allure.step # allure报告里的执行步骤详情会带有参数内容
    # 断言状态码是否是200
    def check_code_200(self):
        assert self.status_code == 200, f'响应状态码不为200.实际结果【{self.status_code}】,预期结果【200】'
    @allure.step
    # 自定义断言状态码
    def check_code(self, status_code):
        assert str(self.status_code) == str(status_code), f'响应状态码不为200.实际结果【{self.status_code}】,预期结果【{status_code}】'
    @allure.step
    # 断言响应时间小于多少
    def check_res_time_less_than(self, times):
        assert self.res_times < times, f'响应状态码不为200.实际结果【{self.res_times}】,预期结果：小于【{times}】'
    @allure.step
    # 响应内容全等断言
    def check_res_equal(self, b):
        assert self.res_text == b ,f'响应内容不全等，实际结果【{self.res_text}】，预计结果【{b}】'
    @allure.step
    # 响应内容是否包含预期结果
    def check_res_contains(self, b):
        assert b in self.res_text ,f'响应内容不包含预期内容，实际结果【{self.res_text}】，预计结果【{b}】'
    @allure.step('断言返回值内容')
    # 是否存在某个预期值
    def check_json_value(self,path ,b):
        value = self.json_path_value(path)
        assert str(value) == str(b) ,f'预期值断言失败，实际结果【{value}】，预计结果【{b}】'


# 枚举
class METHOD(object):
    POST = 'POST'
    GET = 'GET'

class BODY_TYPE():
    FORM = 'form'
    JSON = 'json'
    Files = 'files'
