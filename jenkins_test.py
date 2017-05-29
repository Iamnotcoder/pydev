#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?

__author__ = 'v'
__date__ = '2017/5/27'
import jenkins

_url = 'http://localhost:8080'
_passwd = '090ec1f06fd7fab84430c8fc2e3b5ad6'
_user = 'admin'


server = jenkins.Jenkins(_url, username=_user, password=_passwd)
plugins = server.get_plugins()
print(plugins)
