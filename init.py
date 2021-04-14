import asyncio
from src.zunJia import buyZunJia, getZunJiaProperty
from src.fuTu import buyFuTu, getFuTuProperty, tradeFuTu
from src.huaShengTong import buyHuaShengTong, getHuaShengTongProperty
from src.aiDe import buyAiDe, getAiDeProperty
from src.fuYuan import buyFuYuan, getfuYuanProperty
from src.tiger import buyTiger, getTigerProperty
from src.dongCai import buyDongCai, getDongCaiProperty
from src.yingLi import buyYingLi, getYingLiProperty
from src.zhangLe import buyZhangLe, getZhangeLeProperty
from src.jiaTou import buyJiaTou, getJiaTouProperty
from src.dongFang import buyDongFang, getDongFangProperty
from src.yaoCai import buyYaoCai, getYaoCaiProperty
from src.youYu import buyYouYu, getYouYuProperty
from src.aErFa import buyAErFa, getAErFaProperty
from src.changQiao import buyChangQiao, getChangQiaoProperty
from src.yiSheng import buyYiSheng
from src.hengZhengTong import buyHengZhengTong
from src.guoDu import buyGuoDu
from src.yiTaoJin import buyYiTaoJin
from src.liTongTianXia import buyLiTongTianXia
from src.fangDe import buyFangDe
from src.xueYing import buyXueYing
from src.ruiFeng import buyRuiFeng

from src.test import tryTest
from mysql.initDB import initMysql
from src.mainland.zhaoShang import operateZhaoShang
from time import sleep
def  buyStock():
    typeApp = {
        'tiger':True,
        'dongCai':True,
        'fuTu':True
    }
    isCash = False
    # isCash = True
    isFinancingAll = False
    
    param = {
        'setIndex':0,
        'code':'09961',
        'codeName':'携程集团-S',
        'oneNum':'50',
        'num':'350',
        'isCash':isCash,
        'isCashAll':False,
        # 'isCashAll':True,
        'numVal':'1手',
        'isFinancingAll':isFinancingAll,
    }
    # buyZunJia(param)
    # buyFuTu(param)
    # buyHuaShengTong(param)
    # buyAiDe(param)
    # buyFuYuan(param)
    # buyTiger(param)
    # buyDongCai(param)
    # buyYingLi(param)
    
    # buyJiaTou(param)
    # buyDongFang(param)
    # buyYaoCai(param)
    # buyChangQiao(param)
    # buyYouYu(param)
    # buyFangDe(param)
    # buyRuiFeng(param)

    # ？
    # buyAErFa(param)
    # buyYiSheng(param) 
    # buyYiTaoJin(param)
    # 验证码
    # buyXueYing(param)

    
    # buyGuoDu(param)
    # buyZhangLe(param)
    # unused
    # buyHengZhengTong(param)
    # buyLiTongTianXia(param)

    # tryTest(param)
    
def operateMainland():
    param = {
        'setIndex':0,
        'code':'06668',
        'num':1000,
        'isCash':True,
        'isCashAll':False,
        'numVal':'1手',
        'isFinancingAll':False,
    }
    operateZhaoShang(param)
def trade():
    param = {
        'setIndex':0,
        'code':'01413',
        'num':'500',
        'numVal':'1手',
        'isAll':False,
        'priceInit':0.28,
        'tradeUp':6.1,
        'tradeDown':1,
        'tradeSum':5000,
        
    }
    tradeFuTu(param)
def getProperty():
    param = {
        'setIndex':0,
    }
    # getZunJiaProperty(param)
    # getFuTuProperty(param)
    # getHuaShengTongProperty(param)
    # getAiDeProperty(param)
    # getfuYuanProperty(param)
    # getTigerProperty(param)
    # getDongCaiProperty(param)
    # getYingLiProperty(param)
    # getZhangeLeProperty(param)?
    # getJiaTouProperty(param)?
    # getDongFangProperty(param)
    # getYaoCaiProperty(param)?
    # getYouYuProperty(param)
    # getAErFaProperty(param)
    # getChangQiaoProperty(param)
    
    

    
    
    
    
    
    
    
    
    
    
    # initMysql()

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(buyStock())
    # loop.close()
    # buyStock()
    trade()
    # operateMainland()
    # getProperty()