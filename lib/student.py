from pprint import pprint
from cfg.cfg import *
import requests


class Student:
    def _printResponse(self, response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}: {v}')

        print('')
        # body转utf8格式
        body = response.content.decode('utf8')
        # 把body从unicode转成中文
        print(body.encode().decode("unicode_escape"))

        print('-------- HTTP response * end -------\n\n')

    def student_list(self, vcode=x_vcode, action=teacher_or_studentlist_action):
        params = {
            "vcode": vcode,
            "action": action
        }

        res = requests.get(studentAddress, params=params)
        self._printResponse(res)
        return res

    def student_add(self, username, realname, gradeid, classid, phonenumber, vcode=x_vcode, action=add_action):
        data = {
            "vcode": vcode,
            "action": action,
            "username": username,
            "realname": realname,
            "gradeid": gradeid,
            "classid": classid,
            "phonenumber": phonenumber
        }

        res = requests.post(studentAddress, data=data)
        self._printResponse(res)
        return res



