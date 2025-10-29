# 待实现功能
1.读取yaml文件内容，指定运行自定义的用例，主要用来跳过一些不想运行的用例，或者只运行某些用例，效果等同于
pytest.main(['./cases/test_login.py','../cases/test_login2.py','./cases/test_login3.py','-s','--alluredir=./report/json','--clean-alluredir'])


2.将接口公共部分参数写在yaml文件内，根据用例方法名称，自动读取yaml文件的参数，自动填写参数，生成一个Client对象
这一步 
def test_login(api,username,password,code,msg):
    client = Client(url='login',method=METHOD.POST,body_type=BODY_TYPE.JSON)
变成 
def test_login(api,username,password,code,msg):
    client = api('登录')
最后变成
def test_login(api,username,password,code,msg):
    <!-- client = api('登录') --> 这一步都省了，api这个方法根据配置的名称 test_login自动识别读取yaml文件里的内容

要实现这个，把读取yaml的操作，写在conftest.py内，带上@pytest.fixture 标签,就可以用了