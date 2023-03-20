import mitmproxy.http
from mitmproxy import ctx, http
import json,time
from  Post_param.Param_str import Param_str
from mitmproxy.http import HTTPFlow
from urllib.parse import urlparse
from mitmdump import DumpMaster, Options
from Httprequest.Request_data import requests_data


class Joker:
    def dumps(txt, beaut=0):
        """ json序列化：dict -> json """
        try:
            if beaut:
                txt = json.dumps(txt, sort_keys=True, indent=4, ensure_ascii=False)
            else:
                txt = json.dumps(txt, ensure_ascii=False)
        except:
            txt = txt
        return txt


    def loads(txt):
        """ json反序列化：json -> dict """
        try:
            txt = json.loads(txt, encoding='UTF-8')
        except:
            txt = txt
        return txt



    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host=='www.meeting-vip.com':

            request_data, headers, param = {}, {}, {}
            request_data['method'] = flow.request.method

            # GET请求参数：判断请求模式为get，获取get url 参数
            if request_data['method'] == "GET":
                for k, v in flow.request.query.items():
                    # k：get url参数键
                    #                print("参数键：%s" % k)
                    # v：get url参数值
                    #                print("参数值：%s" % v)
                    param[k] = v
                if param:
                    print("成功获取到GET参数,参数为：%s"%param)
                else:
                    print("没有GET参数")

            elif request_data['method'] == "POST":
                is_body = Joker.loads(flow.request.content.decode('utf-8'))  # POST请求参数：post 请求body内容:flow.request.content.decode('utf-8')
                print("$$$$$$$$$$$$$$$$$$$$$%s:" % is_body)
                if is_body:
                    print("成功获取到POST参数,参数为：%s" % is_body)
                    if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                        body = {'json': is_body}
                        print("post模式 json值为%s:   类型为%s" % (is_body, type(is_body)))
                    else:
                        body = {'data': is_body}
                        print("post模式 data值为%s:   类型为%s" % (is_body, type(is_body)))
                        Param_str.Param_str_Format.Str_Dict(is_body)
                else:
                    print("POST参数为空")

            #               request_data.update(body)
            #          ctx.log("request_data是:%s" % request_data)

            # 遍历请求头信息放入headers数组
            for key, value in flow.request.headers.items():
                # k：get url参数键
                #              print("请求头参数键：%s" % key)
                # v：get url参数值
                #              print("请求头值：%s" % value)
                headers[key] = value

            # 请求解析结束，json保存
            request_data['method'] = flow.request.method
            request_data['url'] = flow.request.url
            request_data['headers'] = headers
            request_data['param'] = param
            request_data = json.dumps(request_data, ensure_ascii=False)
            print(urlparse(flow.request.url))
            url=flow.request.url
            header= headers
            requests_data().rquests_data_injection(url,header)
            print("处理后的值为：%s" % request_data)







        if flow.request.host=='www.hebeiza.cn':
            request_data, headers, param = {}, {}, {}
            request_data['method'] = flow.request.method

            # GET请求参数：判断请求模式为get，获取get url 参数
            if request_data['method'] == "GET":
                for k, v in flow.request.query.items():
                    # k：get url参数键
                    #                print("参数键：%s" % k)
                    # v：get url参数值
                    #                print("参数值：%s" % v)
                    param[k] = v
                if param:
                    print("成功获取到GET参数,参数为：%s"%param)
                else:
                    print("没有GET参数")

            elif request_data['method'] == "POST":
                is_body = Joker.loads(flow.request.content.decode('utf-8'))  # POST请求参数：post 请求body内容:flow.request.content.decode('utf-8')
                print("$$$$$$$$$$$$$$$$$$$$$%s:" % is_body)
                if is_body:
                    print("成功获取到POST参数,参数为：%s" % is_body)
                    if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                        body = {'json': is_body}
                        print("post模式 json值为%s:   类型为%s" % (is_body, type(is_body)))
                    else:
                        body = {'data': is_body}
                        print("post模式 data值为%s:   类型为%s" % (is_body, type(is_body)))
                else:
                    print("POST参数为空")

            #               request_data.update(body)
            #          ctx.log("request_data是:%s" % request_data)

            # 遍历请求头信息放入headers数组
            for key, value in flow.request.headers.items():
                # k：get url参数键
                #              print("请求头参数键：%s" % key)
                # v：get url参数值
                #              print("请求头值：%s" % value)
                headers[key] = value

            # 请求解析结束，json保存
            request_data['method'] = flow.request.method
            request_data['url'] = flow.request.url
            request_data['headers'] = headers
            request_data['param'] = param
            request_data = json.dumps(request_data, ensure_ascii=False)
            print("处理后的值为：%s" % request_data)


        if flow.request.host == 'rdi.org.cn':
            request_data, headers, param = {}, {}, {}
            request_data['method'] = flow.request.method

            # GET请求参数：判断请求模式为get，获取get url 参数
            if request_data['method'] == "GET":
                for k, v in flow.request.query.items():
                    # k：get url参数键
                    #                print("参数键：%s" % k)
                    # v：get url参数值
                    #                print("参数值：%s" % v)
                    param[k] = v
                if param:
                    print("成功获取到GET参数,参数为：%s" % param)
                else:
                    print("没有GET参数")

            elif request_data['method'] == "POST":
                is_body = Joker.loads(
                    flow.request.content.decode('utf-8'))  # POST请求参数：post 请求body内容:flow.request.content.decode('utf-8')
                print("$$$$$$$$$$$$$$$$$$$$$%s:" % is_body)
                if is_body:
                    print("成功获取到POST参数,参数为：%s" % is_body)
                    if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                        body = {'json': is_body}
                        print("post模式 json值为%s:   类型为%s" % (is_body, type(is_body)))
                    else:
                        body = {'data': is_body}
                        print("post模式 data值为%s:   类型为%s" % (is_body, type(is_body)))
                else:
                    print("POST参数为空")

            #               request_data.update(body)
            #          ctx.log("request_data是:%s" % request_data)

            # 遍历请求头信息放入headers数组
            for key, value in flow.request.headers.items():
                # k：get url参数键
                #              print("请求头参数键：%s" % key)
                # v：get url参数值
                #              print("请求头值：%s" % value)
                headers[key] = value

            # 请求解析结束，json保存
            request_data['method'] = flow.request.method
            request_data['url'] = flow.request.url
            request_data['headers'] = headers
            request_data['param'] = param
            request_data = json.dumps(request_data, ensure_ascii=False)
            print("处理后的值为：%s" % request_data)

        return


    def response(self, flow: mitmproxy.http.HTTPFlow):
        return
        text = flow.response.get_text()
        text = text.replace("搜索", "请使用谷歌")
        flow.response.set_text(text)
'''
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "www.google.com":
            flow.response = http.HTTPResponse.make(404)
            '''

addons = [
    Joker()
]

if __name__ == '__main__':
    opts = Options(listen_host='0.0.0.0', listen_port=8888, scripts=__file__)
    m = DumpMaster(opts)
    m.run()