#!/usr/bin/env python
# coding=utf-8
import json
import os
from flask import Flask
from flask import request
from flask import jsonify
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcr.request.v20160607 import GetImageLayerRequest,GetRepoTagsRequest
# 示例执行异常时建议升级aliyun-python-sdk-core到最新版本
# 设置Client


AK = os.getenv("ak")
SK = os.getenv("secret")

class AliyunCr():
    def __init__(self,endpoint="cn-shanghai"):

        self.apiClient = AcsClient(AK, SK, endpoint)
    def get_repo_tags(self,repo_namespace="ly_release",repo_name="",simple=False):

        # 构造请求
        request = GetRepoTagsRequest.GetRepoTagsRequest()
        # 设置参数
        request.set_RepoNamespace(repo_namespace)
        request.set_RepoName(repo_name)
        # request.set_Tag("tag")
        # 根据文档获取资源所在区域对应的RegionId
        # 请求地址格式为cr.{regionId}.aliyuncs.com
        # request.set_endpoint("cr.cn-shanghai.aliyuncs.com")
        # 发起请求
        try:
            response = self.apiClient.do_action_with_exception(request)
            response = json.loads(response)

            if not simple:
                return response["data"]["tags"]
            tags = ""
            for i in response["data"]["tags"]:
                tags += i["tag"]+"\n"
            return tags
        except ServerException as e:
            print(e)
        except ClientException as e:
            print(e)



app = Flask(__name__)

@app.route('/image')
def hello_world():
    print(request.args)
    endpoint = request.args.get('endpoint', 'cn-shanghai')
    repo_namespace = request.args.get('repo_namespace', 'ly_release')
    repo_name = request.args.get('repo_name', '')
    simple = request.args.get('simple', False) #精简显示
    if simple:
        simple = True
    if not repo_name:
        return '范例/inage?endpoint=cn-shanghai&repo_namespace=ops&repo_name=cmdb&simple=1'
    ali = AliyunCr(endpoint)
    data =  ali.get_repo_tags(repo_namespace,repo_name,simple)
    if not simple:
        return jsonify(data)
    return data
