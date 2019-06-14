#encoding:utf-8
import requests
import time
from phantom import init_phantomjs_driver
from PIL import  Image
import io
from functools  import partial
from bs4  import BeautifulSoup as BS
from  jscode import patch_eval_code
import execjs
import json

class GT:
    def __init__(self):
        self.session=requests.Session()
        self.session.get=partial(self.session.get,verify=False)
        self.challenge=None
        self.gt=None
    def set_cookie_by_execjs(self):
        headers={
         "Host": "www.gsxt.gov.cn",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url="http://www.gsxt.gov.cn/index.html"
        response=self.session.get(url,headers=headers)
        if response.status_code==200:
            return 
        html=response.text
        soup=BS(html,"html.parser")
        script=soup.find("script")
        assert script is not None
        print(script.text)
        exec_code='var eval_code="";'+script.text.replace("eval(","eval_code=(")
        ctx=execjs.compile(exec_code)
        eval_code=ctx.eval("eval_code");#获取到eval后生成cookie的代码
        print(eval_code)
        print("we get z:",ctx.eval("z"))
        ctx=execjs.compile(patch_eval_code+eval_code)
        try:
            cookie_str=ctx.eval("document.cookie")
            print("get cookie from requests:",cookie_str);#获取到cookie
            __jsl_clearance=dict(map(lambda s:s.split("="),cookie_str.strip(";").split(";"))).get("__jsl_clearance")
            assert __jsl_clearance is not None
            requests.utils.add_dict_to_cookiejar(self.session.cookies,{"__jsl_clearance":__jsl_clearance})
        except:
            import traceback
            traceback.print_exc()
        return self.session.cookies
    def set_cookie_by_browser(self):
        driver=init_phantomjs_driver()
        driver.get("http://www.gsxt.gov.cn/index.html")
        time.sleep(6)
        Image.open(io.BytesIO(driver.get_screenshot_as_png())).show()
        driver.save_screenshot("browser1.jpg")
        driver_cookies=driver.get_cookies()
        cookie_dict={}
        for c  in driver_cookies:
            cookie_dict[c["name"]]=c["value"]
        cookie_jar=requests.utils.cookiejar_from_dict(cookie_dict)
        self.session.cookies=cookie_jar
    @property
    def challenge(self):
        if hasattr(self,"_challenge") and self._challenge:
            return self._challenge
        raise AttributeError("challenge is None")
    @challenge.setter
    def challenge(self,challenge):
        self._challenge=challenge
    @property
    def gt(self):
        if hasattr(self,"_gt") and self._gt:
            return self._gt
        raise AttributeError("gt is None")
    @gt.setter
    def gt(self,gt):
        self._gt=gt
    def get_challenge(self):
        params={
        "t": int(time.time()*1000)
        }
        headers={
         "Host": "www.gsxt.gov.cn",
         "Connection": "keep-alive",
         "Pragma": "no-cache",
         "Cache-Control": "no-cache",
         "Accept": "application/json,text/javascript,*/*;q=0.01",
         "X-Requested-With": "XMLHttpRequest",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
        }
        url="http://www.gsxt.gov.cn/SearchItemCaptcha"
        response=self.session.get(url,headers=headers,params=params)
        res_json=response.json()
        self.challenge=res_json["challenge"]
        self.gt=res_json["gt"]
        return self.challenge,self.gt
    def get_captcha_url(self):
        params={
         "is_next": "true",
         "type": "click",
         "gt": self.gt,
         "challenge": self.challenge,
         "lang": "zh-cn",
         "https": "false",
         "protocol": "http://",
         "offline": "false",
         "product": "embed",
         "api_server": "api.geetest.com",
         "isPC": "true",
         "width": "100%",
         "callback": "geetest_1555656547227"
        }
        headers={
         "Host": "api.geetest.com",
         "Connection": "keep-alive",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Accept": "*/*",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
         "Cookie": "GeeTestUser=3dfb2dc4bbfed2cc6231aa32fd209a1b;GeeTestAjaxUser=cd7440e3272bac580324c1afe043ac6d"
        }
        url="http://api.geetest.com/get.php"
        response=self.session.get(url,headers=headers,params=params)
        jsonp=response.text
        print(jsonp[21:-1])
        res_json=json.loads(jsonp[22:-1])
        print(response.text)
        print(res_json["data"]["pic"])
    def get_captcha(self,challenge):
        params={
         "challenge": challenge
        }
        headers={
         "Host": "static.geetest.com",
         "Connection": "keep-alive",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
         "Referer": "http://www.gsxt.gov.cn/corp-query-search-1.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
        }
        url="http://static.geetest.com/nerualpic/phrase_l1_zh_2018.10.9/harley1/954667d6e6b3bbde22ae2a1490662caa.jpg"
        response=self.session.get(url,headers=headers,params=params)
        bytes_image=response.content
        if response.headers["Content-Type"]=="image/jpeg":
            return bytes_image
        raise Exception("get_captcha exception")
    def get_type(self):
        params={
             "gt": self.gt,
             "callback": "geetest_%s"%int(time.time()*1000)
            }
        headers={
         "Host": "api.geetest.com",
         "Connection": "keep-alive",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Accept": "*/*",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url="http://api.geetest.com/gettype.php"
        response=self.session.get(url,headers=headers,params=params)
        print(response.text)
    def corp_query_custom_geetest(self):
        params={
            "v": "100"
        }
        headers={
         "Host": "www.gsxt.gov.cn",
         "Connection": "keep-alive",
         "Accept": "application/json,text/javascript,*/*;q=0.01",
         "X-Requested-With": "XMLHttpRequest",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
        }
        url="http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif"
        response=self.session.get(url,headers=headers,params=params)
        print(response.text)
    def corp_query_geetest_validate(self):
        params={
            "token": "4583021037"
            }
        headers={
         "Host": "www.gsxt.gov.cn",
         "Connection": "keep-alive",
         "Accept": "application/json,text/javascript,*/*;q=0.01",
         "X-Requested-With": "XMLHttpRequest",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
        }
        url="http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html"
        response=self.session.get(url,headers=headers,params=params)
    def search_test(self):
        params={
         "searchword": "腾讯"
        }
        headers={
         "Host": "www.gsxt.gov.cn",
         "Connection": "keep-alive",
         "Accept": "application/json,text/javascript,*/*;q=0.01",
         "X-Requested-With": "XMLHttpRequest",
         "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.121Safari/537.36",
         "Referer": "http://www.gsxt.gov.cn/index.html",
         "Accept-Encoding": "gzip,deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
        }
        url="http://www.gsxt.gov.cn/corp-query-search-test.html"
        response=self.session.get(url,headers=headers,params=params)
        print(response.text)
    def get_geetest_ajax(self):
        pass
if __name__=="__main__":
    spider=GT()
    spider.set_cookie_by_execjs()#通过执行js获取cookie
    spider.set_cookie_by_execjs()#通过访问首页获取cookie
    print(spider.session.cookies)
    print(spider.get_challenge())#获取challenge
    spider.corp_query_custom_geetest()
    spider.get_type()
    spider.get_captcha_url()#获取验证码链接
    spider.search_test()
    #image=spider.get_captcha()
    #with open("1.jpg","wb") as f:
    #    f.write(image)
