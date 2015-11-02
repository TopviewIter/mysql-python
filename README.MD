###python对mysql的调用
1. 下载__MySQL-python-1.2.3.win32-py2.7.exe__或__MySQL-python-1.2.3.win-amd64-py2.7.exe__
	这里要注意自己安装的python的版本,不对应的话会报错.
2. 在__eclipse__中重新引用__python__的库:__window__ -> __preferences__ -> __pydev__ 
	-> __interpreters__ -> __python...__
	这是在你的eclipse打开的状态下才用重新引入
3. 在项目中引入相关的库,并获取__connection__
	```python
	import MySQLdb
	conn = MySQLdb.Connect(host="127.0.0.1", 
                           user="root", passwd="root", port=3306,
                           db="python")
	```
4. 几个重要的方法
`Connect()`、`cursor()`、`cursor.execute(sql)`、`fetchall()`、`fetchone()`、`fetchmany()`
5. 记得为文件设置编码
`#coding:utf8`

