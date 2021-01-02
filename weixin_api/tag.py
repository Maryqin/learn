import json
import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        # 获取token
        ID = 'ww303ac182e755c088'
        SECRET = '0YWyhEflHpgDiq0Mwy8BQ0JCeSdiArrNk1Cc6y2N8AQ'
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': ID, 'corpsecret': SECRET})
        access_token = r.json()['access_token']
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        return access_token

    def add(self, group_name, name1, name2):
        # 添加企业标签
        payload = {
            "group_id": None,
            "group_name": group_name,
            "order": 1,
            "tag": [{
                "name": name1,
                "order": 1
            },
                {
                    "name": name2,
                    "order": 2
                }
            ],
            "agentid": None
        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json=payload)
        print(json.dumps(r.json(), indent=2))

    def get_tag(self):
        # 获取企业的标签
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={'access_token': self.token},
                          json={"tag_id": []})
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, name):
        # 编辑客户标签
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={'access_token': self.token},
                          json={"id": id,
                                "name": name,
                                "order": 1,
                                "agentid": None})
        print(json.dumps(r.json(), indent=2))

    def delete(self, TAG_ID_1, TAG_ID_2, GROUP_ID_1, GROUP_ID_2):
        # 删除企业客户标签
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={"tag_id": [TAG_ID_1, TAG_ID_2],
                                "group_id": [GROUP_ID_1, GROUP_ID_2],
                                "agentid": None})
        print(json.dumps(r.json(), indent=2))
        return r
