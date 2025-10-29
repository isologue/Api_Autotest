import requests
def test_order01():
    '''
    预定活动
    '''
    res = requests.post(url='http://123.56.99.53:9000/event/api/order',
                    headers={"Content-Type":"application/x-www-form-urlencoded",
                            "uid":4,"key":"4dsafasd2fqwerwe4"},
                    data={"rstr":123,"eid":1},timeout=1)
    
    assert res.status_code == 200, '状态码非200'