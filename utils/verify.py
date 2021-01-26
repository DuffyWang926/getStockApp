import re
# def isExist(driver, element):
#     source = driver.page_source
#     if element in source:
#         return True
#     else:
#         return False

def isExist(driver, type, value):
    try:
        if type == 1:
            driver.find_element_by_android_uiautomator(value)
        elif type == 2:
            driver.find_element_by_xpath(value)
        elif type == 3:
            driver.find_element_by_class_name(value)
        elif type == 4:
            driver.find_element_by_id(value)
    except Exception as e:
        print(e)
        print(value)
        return False
    else:
        return True

def numFromStr(str):
    numList = []
    initList = re.findall(r"\d+\.?\d*",str)
    for s in initList:
        c = float(s)
        temp = round(c,2)
        numList.append(temp)

    if len(numList) == 1:
        result = numList[0]
    else:
        result = numList

    return result

# def numFromStr(str):
#     numList = []
#     initList = re.findall(r"\d+\.?\d*",str)
#     for s in initList:
#         c = float(s)
#         temp = round(c,2)
#         numList.append(temp)

#     if len(numList) == 1:
#         result = numList[0]
#     else:
#         result = numList

#     return result   