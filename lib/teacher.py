import json
from pprint import pprint
from cfg.cfg import *
import requests


class teacher:
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

    def teacher_list1(self, subjectid=None):
        params = {
            "vcode": vcode,
            "action": list_aciton,
            "subjectid": subjectid
        }

        if subjectid is not None:
            params["subjectid"] = subjectid

        res = requests.get(taecherAddress, params=params)
        self._printResponse(res)
        return res

    def teacher_list2(self, json):
        res = requests.get(taecherAddress, params=json)
        self._printResponse(res)
        return res

    def teacher_add1(self, username, realname, subjectid, classlist, phonenumber, email, idcardnumber):
        idlist = classlist.split(',')
        classlist2 = [{'id': int(classid.strip())} for classid in idlist]
        # 对classlist的json做处理，只入参classid即可
        data = {
            "vcode": vcode,
            "action": add_action,
            "username": username,
            "realname": realname,
            "subjectid": subjectid,
            "classlist": json.dumps(classlist2),
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }
        res = requests.post(taecherAddress, data=data)
        self._printResponse(res)
        return res

    def teacher_add2(self, data, classlist):
        idlist = classlist.split(',')
        classlist2 = [{'id': int(classid.strip())} for classid in idlist]

        data["classlist"] = json.dumps(classlist2)
        # 对classlist的json做处理，只入参classid即可

        res = requests.post(taecherAddress, data=data)

        self._printResponse(res)
        return res

    def teacher_modify1(self, teacherid, realname=None, subjectid=None, classlist=None, phonenumber=None, email=None,
                        idcardnumber=None):
        idlist = classlist.split(',')
        classlist2 = [{'id': int(classid.strip())} for classid in idlist]
        data = {
            "teacherid": teacherid,
            "vcode": vcode,
            "action": modify_action,
            "realname": realname,
            "subjectid": subjectid,
            "classlist": classlist2,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }

        res = requests.put(f"{taecherAddress}/{classlist2}", data=data)
        self._printResponse(res)
        return res

    def teacher_modify2(self, data, classlist):
        idlist = classlist.split(',')
        classlist2 = [{'id': int(classid.strip())} for classid in idlist]

        data["classlist"] = json.dumps(classlist2)
        # 对classlist的json做处理，只入参classid即可

        res = requests.put(f"{taecherAddress}/{data['teacherid']}", data=data)
        self._printResponse(res)
        return res

    def teacher_del1(self, teacherid):
        data = {
            "teacherid": teacherid,
            "vcode": vcode
        }

        res = requests.delete(f"{taecherAddress}/{teacherid}", data=data)
        self._printResponse(res)
        return res

    def teacher_del2(self, data):
        res = requests.delete(f"{taecherAddress}/{data['teacherid']}", data=data)
        self._printResponse(res)
        return res

    def teacher_delall(self):
        teacherlist = self.teacher_list1()
        retlist = teacherlist.json()

        # 如果接口返回了正确的数据，则提取出teacherid并删除
        if retlist:
            for i in retlist:
                self.teacher_del1(i['id'])


