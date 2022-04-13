import requests
import json

class TestInApi(object):
    def test_get_tasks(self):
        print('----測試用例執行-----------')
        url = "http://127.0.0.1:5000/tasks"
        headers = {
            'cache-control': "no-cache",
            }
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        assert response["result"][0]['name'] == '買早餐'

    def test_post_task(self):
        print('----測試用例執行-----------')
        url = "http://127.0.0.1:5000/task"
        payload = {"name": "買晚餐2"}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        response = response.json()
        assert response["result"]["name"] == payload["name"]


    def test_put_task(self):
        print('----測試用例執行-----------')
        url = "http://127.0.0.1:5000/task/2"
        payload = {"name": "買晚餐更新後","status":1,"id":2}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        response = response.json()
        assert response["result"]["name"] == payload["name"]
        assert response["result"]["status"] == payload["status"]


    def test_delete_task(self):
        print('----測試用例執行-----------')
        url = "http://127.0.0.1:5000/task/1"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
        response = requests.request("DELETE", url, headers=headers)
        response = response.json()
        assert response["status_code"]==200
