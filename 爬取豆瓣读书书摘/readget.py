import time
import requests
import numpy as np

np.set_printoptions(suppress=True)
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '''
                  'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
}

title = '//*[@id="wrapper"]/h1/span'

print('书摘如下：')
print('=================================')


def readget(url0, m):
    for j in range(0, m):
        j = j + 20
        url = url0 + 'blockquotes?sort=score&start=' + str(j)
        get = requests.get(url, headers=headers)  # get(url) 得到我们的网页, text将源网页转化为字符串
        time.sleep(5)
        selector = etree.HTML(get.text)  # 将源码转换为xpath可以识别的TML格式
        list()
        v1 = '//*[@id="content"]/div/div[1]/div/div[1]/ul/li['
        v2 = ']/figure/text()[1]'
        for i in range(0, 20):
            i = i + 1
            num = i
            v = v1 + str(num) + v2
            list2 = selector.xpath(v)[0].strip("(")
        f = open('书摘.txt', 'a')
        print(list2)
        print(list2, file=f)


print('输入图书页面：')
a = input()
readget(a, 4120)
