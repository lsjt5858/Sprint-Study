# coding:utf-8
import requests
import json

#get请求百度
# par = {"Keywords":"youyouketang"}
# parload_one = dict(ke1="value1",key2="value2")
# r = requests.get("https://www.baidu.com/",params=par)
# print(r.status_code)
# # print(r.text)

#post传参数
parload = {"yoyo":  "hello world",}
r = requests.post("http://httpbin.org/post",data=parload)
# print(r.headers)
# help(requests)
# print(r.text)

#转化成json格式
data_json = json.dump(parload)
r = requests.post("http://httpbin.org/post",json = data_json)
print(r.text)