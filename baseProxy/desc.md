BaseProxy

文档地址：https://github.com/qiyeboy/BaseProxy


BaseProxy项目的本意是为了使HTTP/HTTPS拦截更加纯粹,更加易操作,学习成本更低。

在Python领域,中间人工具非常强大和成功的是MitmProxy,但是有些地方不是很喜欢。

Windows上安装比较费时费力
功能太多了,可惜我用不到这么多(似乎不是它的错，哈哈)
随着版本升级,采用插件化框架,需要定制功能,需要写个插件成为它的一部分(我只是想集成它而已).
因此BaseProxy就诞生了,不仅支持HTTPS透明传输,还支持HTTP/HTTPS拦截,简单易用,可以很好地集成到你们的项目中。


安装CA证书
1.将chrome浏览器代理服务器设置为127.0.0.1:8788,推荐使用SwitchyOmega插件.



2.设置好代理,并将baseproxy运行后,访问www.baidu.com.



3.这时候访问被拒绝,需要安装证书.在当前网页访问 baseproxy.ca,下载证书.



4.双击下载的证书,并安装到合法机构中.

