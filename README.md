
Python3.6，爬取1000部豆瓣电影海报+名字+评分，方便寻找值得一看的电影！
---

### [代码详情]()
爬虫基本结构+一个小重点：JSON数据处理。

#### 首先导入json包

```
import json
```

#### 在拿到网站传回的客户端对象以后将其转化为json数据的字典
```
json =json.load(jsonText)
```
接下来就用处理字典的方式来获取想要的信息。

### screenshorts
![image](/doubanMovieSpider/screenshorts/first.png)

![image](/doubanMovieSpider/screenshorts/second.png)

### 合成蒙太奇马赛克拼图
拿到图片数据以后借助工具Foto-Mosaik-Edda，效果如下：

![image](/doubanMovieSpider/screenshorts/output.jpg)

### 拓展
json包中有几个常用但易混淆的方法：load(),loads()和dump(),dumps()

load()和loads()是将str转化为json数据的字典，而dump()和dumps()是将json字典转化为str。

loads()和dumps()都是对str直接操作的，而load()和dump()是对文件或者urlopen()拿下来的页面信息包括一些具有read()的文本对象进行操作。

### 用到的小知识
#### 深拷贝和浅拷贝简单介绍
浅拷贝：只复制地址，不复制内容
深拷贝：物理存储器开辟新空间，再将内容复制放入
#### 表达方式
```
import copy
#浅拷贝的两种方法。
a = 'ssss'
b = a
#② b = copy.copy(a)

#深拷贝
b = copy.deepcopy(a)
```
