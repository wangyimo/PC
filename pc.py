from urllib import request
import re
#  每一本书的信息都需要爬取，
#  包括书名、作者、内容简介...等。
class Spider():
    url = 'http://d81fb43e-d.parkone.cn/book/'
    #书名
    book_pattern = '<h2>([\s\S]*?)</h2>'
    #作者
    author_pattern = '<a href="/author/[\s\S]*?">([\s\S]*?)</a>'
    #出版社
    press_pattern = '<span>出版社:([\s\S]*?)</span>'
    #简介
    brief_pattern = '<div class="publishers">([\s\S]*?)</div>'
    #出版日期
    date_pattern = '<p>出版日期:([\s\S]*?)</p>'
    

    def __fetch_content(self):
        url = Spider.url + str(i)
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __anaysis(self,htmls):
        anchors = []
        author = re.findall(Spider.author_pattern,htmls)
        press = re.findall(Spider.press_pattern,htmls)
        anchor = {'作者':author,'出版社':press} 
        anchors.append(anchor)
        print(anchors)

    def go(self): 
        htmls = self.__fetch_content()
        self.__anaysis(htmls)

for i in range(1,254):
    spider = Spider()
    spider.go()