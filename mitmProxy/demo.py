# import mitmproxy.http
# from mitmproxy import ctx
# import traceback, os
#
# filter_host = "holmes.taobao.com"
# url_path = "holmes.taobao.com"
#
#
# class catch_cookies(object):
#     '''
#     利用mitmproxy模拟一个完整的HTTP通信周期获取\修改数据
#     '''
#
#     def __init__(self):
#         self.cookie = ""
#         self.num = 0
#
#     # 与服务器建立代理连接,仅仅是client与proxy连接,不会触发request,response以及其他http事件
#     def http_conn(self, flow: mitmproxy.http.HTTPFlow):
#         pass
#
#     # 来自client的 HTTP 请求的头部被成功读取, body还是空的
#     def request_headers(self, flow: mitmproxy.http.HTTPFlow):
#         pass
#
#     # 来自client的 HTTP 请求被成功完整读取(包括请求头cookie以及body)
#     def request(self, flow: mitmproxy.http.HTTPFlow):
#         global filter_host, url_path
#         if (flow.request.host != filter_host) and (url_path not in str(flow.request.url)):
#             return
#         self.num += 1
#         if self.num > 1:
#             pass
#         else:
#             ctx.log.info(u"处理第 %d 个请求" % self.num)
#             print("处理第 %d 个请求" % self.num)
#             try:
#                 for key, value in flow.request.cookies.items():
#                     print(key,value)
#                     # if "wengine_vpn_ticket" not in key:
#                     #     pass
#                     # else:
#                     # coo = "{}={}; ".format(key, value)
#                     # self.cookie += coo
#                     # self.cookie += flow.request.cookies[i]
#                 # print("cookie", self.cookie)
#                 # 将cookie写进文本里,再写一个程序读取,直接在此模块导入redis会报没有redis模块(未解决)
#                 # with open(r'./cookies_ei_bit.txt', 'w', encoding="utf-8") as file:
#                 #     file.write(self.cookie)
#                 #     print("cookie写入成功\033[0m")
#             except:
#                 print(traceback.print_exc())
#
#     # 来自server的 HTTP的响应头部被成功读取, body还是空的
#     def response_headers(self, flow: mitmproxy.http.HTTPFlow):
#         pass
#
#     # 来自server的 HTTP 响应被成功完整读取
#     def response(self, flow: mitmproxy.http.HTTPFlow):
#         print(flow)
#         pass
#
#     # 处理响应异常, HTTP错误
#     def error(self, flow: mitmproxy.http.HTTPFlow):
#         pass
#
#
# addons = [
#     catch_cookies()
# ]


import mitmproxy.http
from mitmproxy import ctx
from mitmproxy import flowfilter


class Interceptor:
    def __init__(self):
        # 添加网址过滤器
        self.filter = flowfilter.parse("holmes.taobao.com")

    def request(self, flow: mitmproxy.http.HTTPFlow):

        if "holmes.taobao.com" not in flow.request.url:
            return
        else:
            print("捕获到：", flow.request.url)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        print(flow.response.content)


addons = [
    Interceptor()
]
if __name__ == '__main__':
    from mitmproxy.tools.main import mitmweb

    mitmweb()
