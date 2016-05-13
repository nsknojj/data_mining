流程：
wikicrawl目录下 scrapy crawl wiki 爬取新闻至mirror目录下
然后复制mirror下的新闻到Bayes的mirror中。。
然后运行Bayes/test/GetTest 生成训练集 测试集
然后运行Bayes/Main 即可测试（暂时将训练和测试并在一起了，也可以记录训练数据到log/log.txt）

Environment:
python 2.7.0
scrapy 1.0.3
IDE: pycharm 5.0

参考资料：
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
http://www.jb51.net/article/57183.htm
http://doc.scrapy.org/en/1.0/intro/tutorial.html
https://docs.python.org/2/
网络数据挖掘课件