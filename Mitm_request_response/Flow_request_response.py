import mitmproxy.http
from mitmproxy import ctx, http
import json,time


class Flow_request_response:
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
        if flow.request.host == "operate-web.icrypton.com":
            request_data, headers, param = {}, {}, {}

            request_data['method'] = flow.request.method

            # GET请求参数：判断请求模式为get，获取get url 参数
            if request_data['method'] == "GET":
                for k, v in flow.request.query.items():
                    # k：get url参数键
                    print("参数键：%s" % k)
                    # v：get url参数值
                    print("参数值：%s" % v)
                    param[k] = v

            # POST请求参数：post 请求body内容:flow.request.content.decode('utf-8')
            is_body = Joker.loads(flow.request.content.decode('utf-8'))
            print("$$$$$$$$$$$$$$$$$$$$$%s:"%is_body)
#            is_body_dict=json.loads(is_body)
#            print("is_body 类型是:%s" % type(is_body_dict))
#            print("is_body 类型是:%s" % is_body_dict)
            if is_body:
                if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                    body = {'json': is_body}
                    print("jsonjsonjsonjsonjsonjsonjsonjsonjsonjsonjsonjson%s:" % is_body)
                else:
                    body = {'data': is_body}
                    print("datadatadatadatadatadatadatadatadatadatadatadatadata%s:" % is_body)
 #               request_data.update(body)
  #          ctx.log("request_data是:%s" % request_data)

            # 遍历请求头信息放入headers数组
            for key, value in flow.request.headers.items():
                # k：get url参数键
                print("请求头参数键：%s" % key)
                # v：get url参数值
                print("请求头值：%s" % value)
                headers[key] = value

            # 请求解析结束，json保存
            request_data['method'] = flow.request.method
            request_data['url'] = flow.request.url
            request_data['headers'] = headers
            request_data['param'] = param
            request_data = json.dumps(request_data, ensure_ascii=False)
            print("处理后的值为：%s" % request_data)






        if flow.request.host=='www.hebeiza.cn':
            request_data, headers,param = {}, {},{}

            request_data['method'] = flow.request.method

            #判断请求模式为get，获取get url 参数
            if request_data['method'] =="GET":
                for k, v in flow.request.query.items():
                    # k：get url参数键
                    print("参数键：%s"%k)
                    # v：get url参数值
                    print("参数值：%s"%v)
                    param[k]=v

            # 遍历请求头信息放入headers数组
            for key, value in flow.request.headers.items():
                # k：get url参数键
                print("请求头参数键：%s" % key)
                # v：get url参数值
                print("请求头值：%s" % value)
                headers[key] = value

            #请求解析结束，json保存
            request_data['method'] = flow.request.method
            request_data['url'] = flow.request.url
            request_data['headers'] = headers
            request_data['param']=param
            request_data=json.dumps(request_data,ensure_ascii=False)
            print("处理后的值为：%s"%request_data)


            is_body = Joker.loads(flow.request.content.decode('utf-8'))
            if is_body:
                if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                    body = {'json': is_body}
                else:
                    body = {'data': is_body}
                request_data(body)
            ctx.log("request_data是:%s" % request_data)



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

            # POST请求参数：post 请求body内容:flow.request.content.decode('utf-8')
            is_body = Joker.loads(flow.request.content.decode('utf-8'))
            print("$$$$$$$$$$$$$$$$$$$$$%s:" % is_body)
            #            is_body_dict=json.loads(is_body)
            #            print("is_body 类型是:%s" % type(is_body_dict))
            #            print("is_body 类型是:%s" % is_body_dict)
            if is_body:
                if isinstance(is_body, dict):  # isinstance() 函数，来判断一个函数是否是一个已知的类型
                    body = {'json': is_body}
                    print("post模式 json值为%s:   类型为%s:" % (is_body,type(is_body)))
                else:
                    body = {'data': is_body}
                    print("post模式 data值为%s:   类型为%s"  % (is_body,type(is_body)))
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