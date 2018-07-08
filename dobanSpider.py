'''
    爬取1000部豆瓣电影海报+名字+评分
    json数据处理
    python3.6
'''
import urllib
import urllib.request
import urllib.error
import urllib.parse
import random
import json
subJsonURL = "https://movie.douban.com/j/search_subjects"

#json信息爬取类
class MoviePostCrawler(object):

    def __init__(self,sort):
        '''
        :param sort: 电影排序方式。
        '''
        self.sort = sort

    def getJsonURl(self,subURL,startpage):
        '''
        function: 拿到完整的json数据的URL
        :param subURL: URL基本部分
        :param startpage: form表单中的必要数据，控制爬取个数
        :return: 返回完整json数据的URL
        '''
        #https://movie.douban.com/j/search_subjects

        #表单参数
        data = {"page_limit":"20",
                "page_start":startpage,
                "sort":self.sort,
                "tag":"热门",
                "type":"movie"}
        formdata = urllib.parse.urlencode(data)

        FullJsonURL = subJsonURL + '?' + formdata

        return FullJsonURL

    def getMoviesInfor(self,jsonURL):
        '''
        :function: 爬取信息
        :param jsonURL: 信息来源
        :return: None
        '''

        #多个headers随机拼凑request，提高防封几率。
        headers = [{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"},
                   {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"},]
        header = random.choice(headers)
        request = urllib.request.Request(url=jsonURL,headers=header)

        #异常处理
        try:
            #response = urllib.request.urlopen(request).read().decode(encoding="utf-8")
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as e:
            print(e.reason)

        #将response对象转化为json字典，reponse.read()结果为具有json格式的字符串
        jsonText =json.load(response)
        #print(jsonText["subjects"])
        for i in jsonText["subjects"]:
            #print(i)
            #print(i['title'] + i['cover'])
            #print(i['cover'][-4:])
            #保存到本地
            self.save(i['rate'],i['title'],i['cover'])


    def save(self,rate,filmName,postURL):
        '''
        :function: 将获取的图片信息保存到本地文件夹中
        :param rate: 影片评分
        :param filmName: 影片名字
        :param postURL: 海报图片URL
        :return: None
        '''
        locatedPath = './moviePosts/'+ rate + filmName + postURL[-4:]
        print(locatedPath)
        urllib.request.urlretrieve(url=postURL,filename=locatedPath)

if __name__ == '__main__':

    print("爬取豆瓣排名前1000部豆瓣电影海报")
    print("-"*32)
    print("排名选择：")
    print("按热度排序：recommend")
    print("按时间排序：time")
    print("按评价排序：rank")

    #选择排序方式
    sort = input("请输入您的选择：")
    crawler = MoviePostCrawler(sort)

    #控制爬取个数需要仔细分析网站信息
    n = int(input('请输入您想获取的海报个数(为20的整数倍)：'))

    for i in range(int(n/20)):
        FullJsonURL = crawler.getJsonURl(subJsonURL,startpage=i*20)
        crawler.getMoviesInfor(FullJsonURL)

    print("ALL DONE!")

