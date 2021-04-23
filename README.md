# Bing Pictures
**必应每日一图**

必应每天都会更新一张高清图片，如果想要添加到固定的DOM中，并且每天使用最新的图片，在不使用JS的情况下可以使用本程序来完成。
## 用法
```html
<!DOCTYPE html>
<html lang="zh-hans">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>必应每日一图</title>
</head>
<body>
    <img src="https://bing-rosy.vercel.app/api/bing" alt="">
</body>
</html>
```
将` https://bing-rosy.vercel.app/api/bing `作为img标签的src属性。

这样在不更改DOM的情况下就可以实现每日更新图片了。
## 原理
python程序会从[必应的接口](https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN)中获取当天的图片链接，然后将请求重定向到图片的链接。