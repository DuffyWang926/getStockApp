from PIL import Image
import pytesseract
 

def readNum():
    image = Image.open('./guodu.png')
    content = pytesseract.image_to_string(image)   # 解析图片
    print(content)
