# Bing
## 必应每日一图
必应每天都会更新一张高清图片，如果想要添加到固定的DOM中，并且每天使用最新的图片，在不使用JS的情况下可以使用本程序来完成。
### 用法
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

## 一言
使用一言可以达到每次刷新页面，随机展示网络语言的效果。

### 用法
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>一言</title>
</head>
<body>
    <div id="voneword">
    </div>
    <script src="https://bing-rosy.vercel.app/api/oneword"></script>
</body>
</html>
```
添加id为`voneword`的div并引入javaScript `https://bing-rosy.vercel.app/api/oneword` 即可。
js会将随机文字添加到div中。