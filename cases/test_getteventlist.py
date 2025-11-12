import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.client import *
from util.util import *

@allure.feature('查询项目接口测试') # 模块
@allure.title('查询项目测试') # 每个用例的标题
@pytest.mark.order(2) # 用例运行顺序，越小越先运行（报告中无体现）
@paramdata('case_info',get_excel_apitestcase('查询')) # util里改名了paramdata
def test_login(api,global_set,case_info):
    '''
    excel驱动
    '''
    # client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
    client = api('查询')
    client.set_header(eval(case_info['请求头']))
    client.set_datas(eval(case_info['参数']))
    client.send()
    client.check_code(case_info['状态码'])
    client.check_res_time_less_than(1000)
    # client.check_json_value('data.user_id',1)
    client.check_json_value('message',f'{case_info['断言1']}')
    # 获取变量
    token = client.json_path_value('data.access_token')
    global_set('token', token)

if __name__ == '__main__':
    # test_login01()
    pytest.main()


