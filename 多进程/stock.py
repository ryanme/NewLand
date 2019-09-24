# coding:utf8
"""
多进程测试迸发测试
"""
import requests
import time
from multiprocessing import Process


MHOST = {
    "prd": "https://m.f6car.com",
    "pre": "https://m-pre.f6car.com",
    "sit": "http://m-sit.f6car.org",
    "sst": "http://m-sst.f6car.org",
    "trial": "https://m-trial.f6car.com",
    "prdcn": "https://m.f6car.cn",
    "precn": "https://m-pre.f6car.cn",
    "sitcn": "http://m-sit.f6car.org.cn",
    "sstcn": "http://m-sst.f6car.org.cn",
    "trialcn": "https://m-trial.f6car.cn"
}

ERPHOST = {
    "prd": "https://yunxiu.f6car.com",
    "pre": "https://yunxiu-pre.f6car.com",
    "sit": "http://yunxiu-sit.f6car.org",
    "sst": "http://yunxiu-sst.f6car.org",
    "trial": "https://yunxiu-trial.f6car.com",
    "prdcn": "https://yunxiu.f6car.cn",
    "precn": "https://yunxiu-pre.f6car.cn",
    "sitcn": "http://yunxiu-sit.f6car.org.cn",
    "sstcn": "http://yunxiu-sst.f6car.org.cn",
    "trialcn": "https://yunxiu-trial.f6car.cn"
}

env = "sit"
login_path = "/kzf6/user/newLogin"
# login_path = "/kzf6/user/login.do"
# interface_path = "/stock/allot/send"

interface_path = "/purchase/inquiry/publishOrder"


login_url = ERPHOST.get(env)+login_path
allot_url = ERPHOST.get(env)+interface_path

login_paranms = {
    "username": "adam01",
    "password": "96e79218965eb72c92a549dd5a330112",
    "uuid": "",
    "deviceInfo": "",
    "alias": "",
    "imageCode[isTrusted]:": "true",
    "mobile": ""
}
#
# login_paranms = {
#     "username": "adam01",
#     "password": "96e79218965eb72c92a549dd5a330112",
#     "mac": "",
#     "mobile": "18711290001"
# }
# login_paranms = {
#     "username": "liujuanliujuan",
#     "password": "96e79218965eb72c92a549dd5a330112",
#     "mac": "",
#     "scanStr": "",
#     "imageCode": ""}

# allot_params = {
#     "idAllot": "10546443563738666591",
#     "version": "1"
# }

data= {"inquiryOrderVo": {"userId":"25965086392721495","userName":"adam01","idOwnOrg":"25965086392721329","isInvoice":1,"inquiryDesc":"","clientType":0},"inquiryOrderFittingQualityList":["3","2","0","1"],"inquiryOrderSupplierVoList":[{"supplierId":"6223168623129678205","supplierName":"酱排骨"},{"supplierId":"6223168623129676778","supplierName":"TOYATA"}],"inquiryCarVo":{"vinCode":"WBAVL3101DVS33386","carName":"宝马 X1 2.0 AMT 2013 X1 sDrive18i","carPlate":"","idCar":"","brandId":"31","carBrand":"宝马","factoryId":"20","exhaustVolume":"2.0","transmissionDesc":"AMT","carSeries":"X1","year":"2013","carManufactor":"进口宝马"},"inquiryOrderFittingVoList":[{"standardName":"火花塞","fittingNum":1,"fittingName":"火花塞","fittingOeCode":"","ssssAmount":""}],"inquiryOrderattchList":[]}


session = requests.Session()
session.post(url="http://m-sit.f6car.org/mobile/user/login/1", params=login_paranms)



def worker(n):
    while n > 0:
        # res = session.post(url=allot_url, data=str(allot_params))
        res = session.post(url="http://yunxiu-sit.f6car.org/purchase/inquiry/publishOrder", data=str(data).encode("utf-8"))

        try:
            print(res.json(), time.time())
        except:
            print(res.content, time.time())
        finally:
            n -= 1


if __name__ == "__main__":
    p = Process(target=worker, args=(1,))
    p.start()

