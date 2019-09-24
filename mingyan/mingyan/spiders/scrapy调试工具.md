scrapy到底有木有提取到数据的工具，其实说白了就是scrapy调试工具，如果木有它你根本不知道你写的规则到底有木有提取到数据，所以这个工具是个：刚需！其实也很简单，就是在命令行输入下面一行代码而已：  

```scrapy shell http://lab.scrapyd.cn ```

scrapy shell 固定格式，后面的话跟的是你要调试的页面，如果是百度就：  

```scrapy shell http://www.baidu.com```

如果是淘宝就：  

```scrapy shell http://www.taobao.com```

就这样一个格式，其实这段代码就是一个下载的过程，一执行这么一段代码scrapy就立马把我们相应链接的相应页面给拿到了，那接下来就可以任你处置了  

刚已输入：scrapy shell http://lab.scrapyd.cn命令行立马就显示为：  

```
2017-12-15 09:48:38 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2017-12-15 09:48:38 [scrapy.extensions.telnet] DEBUG: Telnet console listening o
n 127.0.0.1:6023
2017-12-15 09:48:38 [scrapy.core.engine] INFO: Spider opened
2017-12-15 09:48:38 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://lab.sc
rapyd.cn> (referer: None)
2017-12-15 09:48:39 [traitlets] DEBUG: Using default logger
2017-12-15 09:48:39 [traitlets] DEBUG: Using default logger
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x0000000004ED2940>
[s]   item       {}
[s]   request    <GET http://lab.scrapyd.cn>
[s]   response   <200 http://lab.scrapyd.cn>
[s]   settings   <scrapy.settings.Settings object at 0x0000000004FF8F98>
[s]   spider     <DefaultSpider 'default' at 0x525afd0>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default
, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local object
s
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
In [1]:
```

比如我们想提取    http://lab.scrapyd.cn   的  title，我们可以在  In[1]:  后面输入：response.css('title')   ，然后回车， 立马就得到如下结果：  

```
>>> response.css('title')

[<Selector xpath='descendant-or-self::title' data='<title>爬虫实验室 - S
CRAPY中文网提供</title>'>]
```

如果正确了，我们再把上面的代码放到我们蜘蛛里面，那这样就会正确的得到你想要的数据，而不会出现意外了，这就是scrapy调试工具的应用！  
