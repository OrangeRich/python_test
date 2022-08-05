from pprint import pprint
from cfg.cfg import *
import requests


class Sclass:
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

    def class_list(self, vcode=x_vcode, aciton=classlist_aciton, gradeid=None):
        params = {
            "vcode": vcode,
            "action": aciton,
            "gradeid": gradeid
        }

        res = requests.get(classAddress, params=params)

        self._printResponse(res)
        return res

    def class_add(self, grade, name, studentlimit, action=add_action, vcode=x_vcode):
        data = {
            "vcode": vcode,
            "action": action,
            "grade": grade,
            "name": name,
            "studentlimit": studentlimit
        }

        res = requests.post(classAddress, data=data)
        self._printResponse(res)
        return res

    def class_modify(self, classid, name, studentlit, action=modify_action, vcode=x_vcode):
        data = {
            "classid": classid,
            "vcode": vcode,
            "action": action,
            "name": name,
            "studentlimit": studentlit
        }
        res = requests.put(f'{classAddress}/{classid}', data=data)
        self._printResponse(res)
        return res

    def class_del(self, classid, vcode=x_vcode):
        data = {
            "classid": classid,
            "vcode": vcode
        }
        res = requests.delete(f"{classAddress}/{classid}", data=data)
        self._printResponse(res)
        return res

    def class_delall(self):
        list_res = self.class_list()
        retlist = list_res.json()['retlist']

        if retlist:
            for i in retlist:
                self.class_del(i['id'])


sclass = Sclass()
if __name__ == '__main__':
    listclass = sclass.class_list(3)
    pprint(listclass.json())


