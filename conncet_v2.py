#coding:utf-8
__author__ = 'arthur'
from bs4 import BeautifulSoup
import time
import requests
import os

class Login:
    def login(self):
        try:
           os.system(''' curl -k -X POST -i -d "action=login&username=[学号]&password={B}[这部分经过编码，所以请直接从原始url中拷贝urlencoded(base64([密码]))]&ac_id=18&user_ip=&nas_ip=&user_mac=&ajax=1" http://172.20.13.100:804/include/auth_action.php''')
        except:
            print(self.getCurrentTime(), u"登陆函数异常")
        finally:
            pass

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #判断当前是否可以连网
    def canConnect(self):
        try:
            baidu_request=requests.get("http://www.baidu.com")
            if(baidu_request.status_code==200):
                baidu_request.encoding = 'utf-8'
                baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
                baidu_input = baidu_request_bsObj.find(value="百度一下")
                if baidu_input==None:
                    return False
                return True
            else:
                return False
        except:
            print ('error')

    #主函数
    def main(self):
        print (self.getCurrentTime(), u"Hi，ECUST自动登陆脚本正在运行")
        while True:
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print (self.getCurrentTime(),u"断网了...")
                    try:
                        self.login()
                    except:
                        print(self.getCurrentTime(), u"浏览器出了bug")
                    finally:
                        time.sleep(5)
                        if self.canConnect():
                            print(self.getCurrentTime(), u"重新登陆成功")
                        else:
                            print(self.getCurrentTime(), u"登陆失败，再来一次")
                    self.login()
                else:
                    print (self.getCurrentTime(), u"一切正常...")
                    time.sleep(5)

login = Login()
login.main()
