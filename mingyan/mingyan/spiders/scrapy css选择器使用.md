### Scrapy sss选择器使用

---

本篇介绍scrapy的第一种数据提取工具：css提取工具的用法  

那我们要提取那个数据呢？就提取：http://lab.scrapyd.cn 这个页面的title里面的数据，我们来看一下他的html结构：  

```html
<!DOCTYPE HTML>
<html class="no-js">
<head>
    ……
    <meta name="applicable-device" content="pc,mobile">

    <title>爬虫实验室 - SCRAPY中文网提供</title>
    ……
```

我们要提取的就是上面：  

```html
<title>爬虫实验室 - SCRAPY中文网提供</title>
```

这个标签里面的数据，我们最终要得到的是：  
```text
“爬虫实验室 - SCRAPY中文网提供”
```

首先我们需要在命令行输入:  
```shell script
scrapy shell http://lab.scrapyd.cn
```

然后我们继续在命令行输入如下命令：response.css('title') ，这个格式是scrapy固定的格式照着写就行了；response.css('标签名')，标签名的话可以是html标签比如：title、body、div，也可以是你自定义的class标签，这里的话先看我们提取一下简单的，后面我们会讲解如何提取复杂的；
那当我们输入以上命令之后，你会发现已经很给力的提取了一些数据：  

```shell script
>>> response.css('title')

 [<Selector xpath='descendant-or-self::title' data='<title>爬虫实验室 - S
CRAPY中文网提供</title>'>]
```

那你会发现，我们使用这个命令提取的一个Selector的列表，并不是我们想要的数据；那我们再使用scrapy给我们准备的一些函数来进一步提取，那我们改变一下上面的写法，输入：  
```shell script
>>> response.css('title').extract()
 ['<title>爬虫实验室 - SCRAPY中文网提供</title>']
```

我们只是在后面加入了：extract() 这么一个函数你就提取到了我们标签的一个列表，更近一步了，那如果我们不要列表，只要title这个标签，要怎么处理呢，看我们的输入：  
```shell script
>>>  response.css('title').extract()[0]
 '<title>爬虫实验室 - SCRAPY中文网提供</title>'
```

这里的话，我们只需要在后面添加：[0]，那代表提取这个列表中的第一个元素，那就得到了我们的title字符串；这里的话scrapy也给我提供了另外一个函数，可以这样来写，一样的效果：  
```shell script
>>>  response.css('title').extract_first()
 '<title>爬虫实验室 - SCRAPY中文网提供</title>'
```

extract_first()就代表提取第一个元素，和我们的：[0]，一样的效果，只是更简洁些，至此我们已经成功提取到了我们的title，但是你会发现，肿么多了一个title标签，这并不是你需要的，那要肿么办呢，我们可以继续改变一下以上的输入：  
```shell script
>>> response.css('title::text').extract_first()
'爬虫实验室 - SCRAPY中文网提供'
```

我们在title后面加上了 ::text ,这代表提取标签里面的数据，至此，我们已经成功提取到了我们需要的数据：  
```shell script
'爬虫实验室 - SCRAPY中文网提供'
```

总结一下，其实就这么一段代码：  
```shell script
response.css('title::text').extract_first()
```
