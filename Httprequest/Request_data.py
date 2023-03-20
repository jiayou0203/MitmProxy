import requests

#url = "https://operate-web.icrypton.com/post/9900/"
class  requests_data:

        def rquests_data_injection(self,url,header):
            payload={}
            '''
            headers = {
              'Host': '"operate-web.icrypton.com"',
              'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"',
              'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"',
              'Accept-Language': '"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"',
              'Accept-Encoding': '"gzip, deflate, br"',
              'Connection': '"keep-alive"',
              'Cookie': '"servicelanguage=zh_CN; _uab_collina=167807684684436423068138; lan=en_US; _ga=GA1.2.1416458213.1678084403; changeSkin=2; defSkin=2; cusSkin=2; LOGIN_SESSION_ADMIN=ecd77500-9aff-422c-8a43-7cd8dafcafb6"',
              'Upgrade-Insecure-Requests': ' "1"',
              'Sec-Fetch-Dest': '"document"',
              'Sec-Fetch-Mode': '"navigate"',
              'Sec-Fetch-Site': '"none"',
              'Sec-Fetch-User': '"?1"'
            }
            '''
            headers=header
            print("请求测试")
            print(url)
            print(headers)
            response = requests.request("GET", url, headers=headers)
            print(response.text)
