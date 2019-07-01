title: 关于此博客
date: 2016-09-30 10:11:01
tags: 
- 测试
- 样例
- Markdown
---

此博客开源， 可以修改下自己用。 完全自由开发.

![JackeyGao 的博客](/assets/images/blog.png "cover")

<p class="code"><i class="github grey icon"></i><a href="https://github.com/jackeygao">jackeyGao</a> <b>/</b> <a href="https://github.com/jackeygao/jackeygao.github.io">jackeyGao.github.io</a></p>

此博客为静态博客， 直接对 markdown 文件生成的 html 静态文件。 请参考 script 目录的脚本。

优化了打印输出， 可以试试<a onclick="print()" style="cursor: pointer;">打印</a>效果.

## 标题

```md
# 我是H1标题
## 我是H2标题
### 我是H3标题
#### 我是H4标题
##### 我是H5标题
```

# 我是H1标题
## 我是H2标题
### 我是H3标题
#### 我是H4标题
##### 我是H5标题

## 片段

```md
这是第一篇日记， 仅仅为了测试.
```

这是第一篇日记， 仅仅为了测试.

## 列表

```md
- 文本1
- 文本2
- 文本3
```

- 文本1
- 文本2
- 文本3

```md
1. 文本1
2. 文本2
3. 文本3
```

1. 文本1
2. 文本2
3. 文本3

## 链接

```md
我是[JackeyGao](/)
```

我是[JackeyGao](/)

## 图片

```md
![黎明](/uploads/images/photo-1415931633537-351070d20b81.jpeg "黎明的阳光")
```

![黎明](/uploads/images/photo-1415931633537-351070d20b81.jpeg "黎明的阳光")


## 粗体、行代码、斜体

```md
我**并不会**用`C`来写*前端*
```

我**并不会**用`C`来写*前端*

## 表格

```md
| Tables        | Center        | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```

| Tables        | Center           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


## 标准块

```md
> 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。
```

> 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。

## 标准警告块

```md
> %warning 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。
```
> %warning 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。

## 标准错误块

```md
> %error 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。
```

> %error 一盏灯， 一片昏黄； 一简书， 一杯淡茶。 守着那一份淡定， 品读属于自己的寂寞。 保持淡定， 才能欣赏到最美丽的风景！ 保持淡定， 人生从此不再寂寞。


## 分割线

```html
<hr>
```

<hr>


## 引用块内标签

> 很多标签都可以在内部内容里面套用其他标签的, 我只是在在通用md标准上加了一些功能

```md
> %error **请注意:** 防火、防盗、*防经纪人*
```

> %error **请注意:** 防火、防盗、*防经纪人*

## 中间引用块

> %warning **请注意:** 设计的目的是为了更好的显示诗歌体. 如果在这里引用`**`粗体内标签会默认认为标题. `*`斜体内标签默认认为作者信息. 因为这两个内标签加入了特殊的样式, 所以不建议在诗歌内容里面加这两个内标签. 最好按照这个设定来. 详情看下面的案例

```md
> %center
> **浣溪沙**
> *纳兰性德·清*
> 谁道飘零不可怜，
> 旧游时节好花天，
> 断肠人去自经年。
> 一片晕红才著雨，
> 几丝柔绿乍和烟，
> 倩魂销尽夕阳前。
```

> %center
> **浣溪沙**
> *纳兰性德·清*
> 谁道飘零不可怜，
> 旧游时节好花天，
> 断肠人去自经年。
> 一片晕红才著雨，
> 几丝柔绿乍和烟，
> 倩魂销尽夕阳前。

## 代码

<div class="code-wrapper">
  <span class="lang-label">markdown</span>
  <div class="title-label empty">&nbsp;</div>
  <div class="highlight">
    <pre>```python
#! -*- coding: utf-8 -*-
"""
   Python Hello world
"""

import sys

if sys.version_info[0] == 3:
    print("Hello world!")
else:
    print "Hello world!"

```</pre>
  </div>
</div>



```python
#! -*- coding: utf-8 -*-
"""
   Python Hello world
"""

import sys

if sys.version_info[0] == 3:
    print("Hello world!")
else:
    print "Hello world!"

```

