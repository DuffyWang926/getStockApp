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
        'phone':'17319075327'
        
    }
    result = initData[(name)]

    return result