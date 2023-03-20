import ast


class Param_str_Format:

    #loginname=12323&password=MTIzMTIz&validateCode=1111
    def Str_Dict(Post_param):
        Post_param_dict=ast.literal_eval(Post_param)
        print("Post_param_dict 值是:%s 类型是:%s"%(Post_param_dict,type(Post_param_dict)))
        if isinstance(Post_param_dict, dict):
            for key, value in Post_param_dict.items():
                if isinstance(value, str):           #一、请求参数转换后为最终节点，为str类型，直接输出结果值
                    print("终端值是字符:%s"%value)
                elif isinstance(value,dict):         #二、请求参数转换后为不是最终节点，为dict类型，继续循环取其中得值
                    for key, value in value.items():
                        print("POST参数处理格键值是:%s,字符串值是:%s,类型是：%s" % (key, value,type(value)))
                        if isinstance(value,list):     #2、请求参数转换后为不是最终节点，为list类型，继续循环取其中得值
                            data_zhi=value
                            for k in data_zhi:         #3、输出第2步中得list值
                                print(k)
                elif isinstance(value,list):        #三、请求参数转换后为不是最终节点，为list类型，继续循环取其中得值
                    data_zhi = value
                    for k in data_zhi:
                        print(k)
                elif isinstance(value, int):        #四 、请求参数转换后为是最终节点，为int类型，直接输出结果值
                    print("终端值是数字:%s" % value)

        return Post_param_dict


    def loads(txt):
        """ json反序列化：json -> dict """
        try:
            txt = json.loads(txt, encoding='UTF-8')
        except:
            txt = txt
        return txt