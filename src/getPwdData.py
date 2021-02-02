def getPwd(name):
    initData = {
        'huaShengTong':{
            'account':'10408453',
            'logInPwd':'Wef19910926',
            'tradePwd':'324872',
        },
        'dongFang':{
            'account':'100285572',
            # 'logInPwd':'Wef19910926',
            'tradePwd':'Wef19919',
        },
        'yaoCai':{
            'account':'M396811P',
            'logInPwd':'Wef1991926',
            # 'tradePwd':'Wef19919',
        },
        'zunJia':{
            'account':'62257658',
            # 'logInPwd':'Wef1991926',
            'tradePwd':'Wef1991926',
        },
        'fuTu':{
            'account':'17994525',
            'logInPwd':'Wef1991926',
            'tradePwd':'324872',
        },
        'zhangLe':{
            'account':'682280736',
            'logInPwd':'Wef1991926',
            'tradePwd':'Wef1991926',
        },
        'fuYuan':{
            'account':'80102771',
            'logInPwd':'Wef1991926',
            'tradePwd':'Wef19919',
        },
        'phone':'17319075327'
        
    }
    result = initData[(name)]

    return result

def getKeyCode(driver, val):
    initData = {
        '0':7,
        '1':8,
        '2':9,
        '3':10,
        '4':11,
        '5':12,
        '6':13,
        '7':14,
        '8':15,
        '9':16,
        'STAR':17,
        'POUND':18,
        'DPAD_UP':19,
        'DPAD_DOWN':20,
        'DPAD_LEFT':21,
        'DPAD_RIGHT':22,
        'DPAD_CENTER':23,
        'VOLUME_UP':24,
        'VOLUME_DOWN':25,
        'POWER':26,
        'CAMERA':27,
        'CLEAR':28,
        'A':29,
        'B':30,
        'C':31,
        'D':32,
        'E':33,
        'F':34,
        'G':35,
        'H':36,
        'I':37,
        'J':38,
        'K':39,
        'L':40,
        'M':41,
        'N':42,
        'O':43,
        'P':44,
        'Q':45,
        'R':46,
        'S':47,
        'T':48,
        'U':49,
        'V':50,
        'W':51,
        'X':52,
        'Y':53,
        'Z':54,        
    }

    for i in val:
        if i.isdigit():
            code = initData[(i)]
            driver.press_keycode(code)
        elif i.islower():
            code = initData[(i.upper())]
            driver.press_keycode(code)
        elif i.isupper():
            code = initData[(i)]
            driver.press_keycode(code,64,59)
