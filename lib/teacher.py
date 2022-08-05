from pprint import pprint
from cfg.cfg import *
import requests


class Teacher:
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

    def teacher_list(self, vcode=x_vcode, subjectid=None, action=teacher_or_studentlist_action):
        params = {
            "vcode": vcode,
            "action": action,
            "subjectid": subjectid
        }

        res = requests.get(taecherAddress, params=params)
        self._printResponse(res)
        return res

    def teacher_add(self, vcode, username, realname, subjectid, classlist, phonenumber, email, idcardnumber, action=add_action):
        idlist = classlist.split(',')
        classlist2 = [{"id": int(cid.strip())} for cid in idlist]
        # 将classlist的json格式内的id转换成int类型

        data = {
            "vcode": vcode,
            "action": action,
            "username": username,
            "realname": realname,
            "subjectid": subjectid,
            "classlist": classlist2,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }

        res = requests.post(taecherAddress, data=data)
        self._printResponse(res)
        return res

    def teacher_modify(self, teacherid, vcode, realname, subjectid, classlist,
                       phonenumber, email, idcardnumber, action=modify_action):
        idlist = classlist.split(',')
        classlist2 = [{"id": int(cid.strip())} for cid in idlist]
        # 将classlist的json格式内的id转换成int类型

        data = {
            "teacherid": teacherid,
            "vcode": vcode,
            "action": action,
            "realname": realname,
            "subjectid": subjectid,
            "classlist": classlist2,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }

        res = requests.put(f"{taecherAddress}/{teacherid}", data=data)
        self._printResponse(res)
        return res

    def teacher_del(self, teacherid, vcode=x_vcode):
        data = {
            "teacherid": teacherid,
            "vcode": vcode
        }

        res = requests.delete(f"{taecherAddress}/{teacherid}", data=data)
        self._printResponse(res)
        return res

    def teacher_delall(self):
        res = self.teacher_list()
        retlist = res.json()['retlist']
        # 先获取导师列表，返回数据转换成json

        if retlist:
            # 导师列表获取成功
            for i in retlist:
                # 获取所有老师id 删除所有老师
                self.teacher_del(i['id'])


