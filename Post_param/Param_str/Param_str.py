import mitmproxy.http
from mitmproxy import ctx, http
import json,time


class Param_str_Format:

    #loginname=12323&password=MTIzMTIz&validateCode=1111
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