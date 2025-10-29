
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from pymysql import cursors
import pytest
import pymysql
from string import Template
from xToolkit import xfile

paramdata = pytest.mark.parametrize # 改名，方便

# 读取csv文件
def get_file(filename):
    result = []
    with open('D:/pytest_api1/data/'+filename,'r',encoding='utf-8') as f:
        for i in csv.reader(f):
            result.append(i)
    return result[1:]# range 剔除第一行


# 读取yaml文件里接口参数的数据
def get_api_info(title):
    pass  

# 读取yaml文件里全局变量的数据，关联用
def get_global_info(title):
    return 


# # 操作数据库
# # 创建一个链接
# connect = pymysql.connect(host='',port='',user='',passwd='',db='')
# #创建一个游标(指针)
# cursor = connect.cursor()
# #执行语句（返回的是变更条数数据）
# cursor.execute('select * from table')
# # 获取结果,返回一个多维元组
# cursor.fetchall()


# 操作excel
# excel_case = xfile.read("./data/接口测试用例.xlsx").excel_to_dict(sheet=0)
# print(excel_case)
# 获取指定接口模板数据
def get_apitemplate(name):
    excel_case = xfile.read("./data/接口测试用例.xlsx").excel_to_dict(sheet=1)
    # 初始化变量
    url = ''
    method = ''
    body_type = ''
    # 遍历数据列表
    for item in excel_case:
        if item['接口名称'] == name:
            if item['请求头'] is not None:
                url = item['地址']
                method = item['方法类型']
                body_type = item['参数类型']
                break  # 找到后退出循环
    return url, method, body_type
    

# print(get_apitemplate('查询活动'))

# 获取指定全局变量数据
def get_excel_global(name):
    excel_case = xfile.read("./data/接口测试用例.xlsx").excel_to_dict(sheet=0)
    value = ''
    # 遍历数据列表
    for item in excel_case:
        if item['变量名'] == name:
            value = item['变量值']
            break  # 找到后退出循环
    
    return value

# print(get_excel_global('base_url'))


# 获取指定接口用例数据
def get_excel_apitestcase(name):
    excel_case = xfile.read("./data/接口测试用例.xlsx").excel_to_dict(sheet=2)
    case_list = []
    # 遍历数据列表
    for item in excel_case:
        if item['模板名称'] == name:
            case_list.append(item)
            continue
    
    return case_list



info = get_apitemplate('登录')
print(info)