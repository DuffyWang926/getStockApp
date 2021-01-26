def getSetting(index):
    initData = [
        {
            'platformName':'Android',
            'platformVersion':'10',
            'deviceName':'2214c691',
            'noReset':True,
        }
    ]
    result = initData[index]

    return result

#     CREATE TABLE IF NOT EXISTS `huaShengTong0`(
#    `huaShengTongId` INT UNSIGNED AUTO_INCREMENT,
#    `allNum` VARCHAR(15) NOT NULL,
#    `availableNum` VARCHAR(15) NOT NULL,
#    `date` DATE,
#    PRIMARY KEY ( `huaShengTongId` )
# )ENGINE=InnoDB DEFAULT CHARSET=utf8;