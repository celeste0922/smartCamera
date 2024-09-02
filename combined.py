import time

from PIL import Image  # 引用PIL里的Image函数


def combined(ppath:str,bpath:str,epath:str):
    people = Image.open(ppath)  # 获取图片-人像'kun.jpg'
    background = Image.open(bpath)  # 获取图片-背景'background.jpg'
    people = people.convert('RGBA')  # 把图片格式转化为RGBA
    # w, h = people.size  # 取出图片大小参数
    # for x in range(0, w):  # 遍历图片的每一个像素点
    #     for y in range(0, h):
    #         r, g, b, a = kun.getpixel((x, y))  # 取出每个像素点的颜色和透明度参数
    #         if (g + 1) / (r + g + b + 3) > 0.4 and g > 60:  # 如果像素点偏绿色
    #             a = 0  # 把像素点的透明度设为0，也就是完全透明
    #             kun.putpixel((x, y), (r, g, b, a))  # 修改图片像素的参数
    # kun.save('kun.png')  # 把抠好的图保存为'kun.png'

    background.paste(people, (0, 0), mask=people.split()[3])  # 把背景和图片粘贴在一起
    background.save(epath+str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + ".png")  # 保存为最后的图片
