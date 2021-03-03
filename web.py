import pyautogui as pt
import pyperclip
import pyqrcode
import os
import pyowm
from time import sleep
from datetime import datetime
from forex_python.converter import CurrencyRates
import wikipedia
import webbrowser
import os
import psutil
import shutil
import threading
from GoogleNews import GoogleNews
import screen_brightness_control as sbc
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from io import BytesIO
import win32clipboard
from PIL import Image
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions();
#options.add_argument('--headless');

driver=webdriver.Chrome(options=options)
driver.minimize_window()
driver.get("https://www.instagram.com")

drive=webdriver.Chrome(options=options)
drive.minimize_window()
speed=webdriver.Chrome(options=options)
speed.get("https://www.speedtest.net")
speed.minimize_window()
def find_speed():
    speed.find_element_by_xpath("//span[@class='start-text']").click()
    while True:
        try:
            ping=speed.find_element_by_xpath("//span[@class='result-data-large number result-data-value ping-speed']")
            ping=ping.text
            download=speed.find_element_by_xpath("//span[@class='result-data-large number result-data-value download-speed']")
            download=download.text
            upload=speed.find_element_by_xpath("//span[@class='result-data-large number result-data-value upload-speed']")
            upload=upload.text
            if upload!=" ":
                break
        except:
            pass
    data="Ping : "+str(ping)+" "+"Download : "+str(download)+" "+"Upload : "+str(upload)
    pt.click(x,y)
    pt.typewrite(data)
    pt.typewrite('\n')
    speed.close()
    
def sp():
    pt.click(x,y)
    pt.typewrite("Sir ! Please wait Under process")
    pt.typewrite('\n')
    xspeed=threading.Thread(target=find_speed)
    xspeed.start()









def in_start():
    user="_.import_"
    pas="kamalesh"
    element=driver.find_element_by_xpath("//input[@name='username']")
    element.send_keys(user)
    element=driver.find_element_by_xpath("//input[@name='password']")
    element.send_keys(pas)
    sleep(2)
    driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()
    sleep(10)
ins = threading.Thread(target=in_start)
ins.start()


#points geting message
x=630
y=738

webbrowser.open("https://web.whatsapp.com")
sleep(20)
pt.click(127,153)
sleep(1)
pt.typewrite("test")
pt.press('enter')
#its works only for opera
def pass_save(file,us,ps):
    global x
    global y
    file=("F:/pass/"+file+".txt")
    f = open(file,"w")
    f.write(us)
    f.write("/")
    f.write(ps)
    f.close()
    pt.click(x,y)
    pt.typewrite("Sir ! Password saved")
    pt.typewrite('\n')

def insta(user1,message):
    chat=message
    driver.get("https://www.instagram.com/"+user1)
    sleep(5)
    element=driver.find_element_by_xpath("//button[normalize-space()]")
    sleep(5)
    if element.text=="Follow":
        driver.find_element_by_xpath("//button[normalize-space()='Follow']").click()
        sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='Message']").click()
        sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='Not Now']").click()
    elif element.text=="Message":
        driver.find_element_by_xpath("//button[normalize-space()='Message']").click()
        sleep(5)
        driver.find_element_by_xpath("//button[normalize-space()='Not Now']").click()
        element=driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
        sleep(1)
        element.send_keys(chat)
        sleep(3)
        element=driver.find_element_by_xpath("//button[normalize-space()='Send']").click()
        pt.click(x,y)
        pt.click(x,y)
        pt.typewrite("Sir ! Message sented sucessfully")
        pt.typewrite('\n')
def alarm(h,m,app,msg):
    global x
    global y
    print("in loop")
    h=int(h)
    m=int(m)
    while True:
            now = datetime.now()
            hou=str(now.hour)+":"+str(now.minute)
            s1 = datetime.strptime(str(hou),"%H:%M")
            hours=s1.strftime("%r")
            hr=int(hours[0]+hours[1])
            mi=int(hours[3]+hours[4])
            ap=hours[9]+hours[10]
            ap=ap.lower()
            sleep(1)
            if h==hr and m==mi and ap==app:
                for i in  range(5):
                    pt.click(x,y)
                    pt.typewrite("Sir ! Its time for "+msg)
                    pt.typewrite('\n')
                break

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds)



def process(val):
    global x
    global y
    if val=="shutdown":
        pt.click(x,y)
        pt.typewrite("Sir!,system will be shutdown now")
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Sir!,Take care")
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Eat at correct time.untill i woke")
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Miss you sir")
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Bye.Sir Have a nice day")
        pt.typewrite('\n')
        sleep(5)
        os.system("shutdown /p")
    elif val=="will i get married" or val=="when i will get married" or val=="my marrage date":
        pt.click(x,y)
        pt.typewrite("impossiable Sir! According to my 7th sense. you will not get married sir,because according to your character no girl is found in the world")
        pt.typewrite('\n')
    elif val=="ok" or val=="mm":
        pt.click(x,y)
        pt.typewrite("Ok sir")
        pt.typewrite('\n')
    elif "date" in val:
        no = datetime.now()
        dates=" "+(datetime.today().strftime('%d-%m-%Y'))
        pt.click(x,y)
        pt.typewrite("Sir! Today date is "+dates)
        pt.typewrite('\n')
    elif "time" in val:
        no = datetime.now()
        ho=str(no.hour)+":"+str(no.minute)+":"+str(no.second)
        s = datetime.strptime(str(ho),"%H:%M:%S")
        hors=s.strftime("%r")
        pt.click(x,y)
        pt.typewrite("Sir! Time is "+hors)
        pt.typewrite('\n')
    elif val=="you sleep":
        pt.click(x,y)
        pt.typewrite("Sir! How i can Sleep witout you !")
        pt.typewrite('\n')
    elif val=="weather" or val =="weather today":
        owm=pyowm.OWM('d839fc9f15bf2a3fd360d9e9710d7138')
        mgr = owm.weather_manager()
        ob = mgr.weather_at_place('Erode').weather
        tp=ob.temperature('celsius')
        pt.click(x,y)
        pt.typewrite("Wheather is Erode ")
        pt.hotkey('ctrl', 'enter')
        for key,value in tp.items():
            
            val=""
            val=str(key)+" : "+str(value)
            pt.typewrite(val)
            pt.hotkey('ctrl', 'enter')
        pt.typewrite('\n')
    elif val=="usdtoinr":
        c = CurrencyRates()
        usd=c.get_rate('USD', 'INR')
        usd=str(usd)
        pt.click(x,y)
        pt.typewrite("Sir! the price of 1 INR in USD is "+usd)
        pt.typewrite('\n')
    elif val[0]=="w" and val[1]=="_":
        n=""
        for i in range(2,len(val)):
            n=n+val[i]
        try:
            resul=wikipedia.summary(n, sentences=2)
            pt.click(x,y)
            pt.typewrite(resul)
            pt.typewrite('\n')
        except:
            pt.click(x,y)
            pt.typewrite("Result unfound Sir!")
            pt.typewrite('\n')
    elif val=="do you love me" or val=="do u love me":
        pt.click(x,y)
        pt.typewrite("Sir ! i always love you..without you how can i live..")
        pt.typewrite('\n')

    elif val=="lap charge":
        battery = psutil.sensors_battery()
        pt.click(x,y)
        pt.typewrite("Battery percentage : "+str(battery.percent))
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Power plugged in : "+str(battery.power_plugged))
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Battery left : "+str(convertTime(battery.secsleft)) )
        pt.typewrite('\n')
        sleep(2)
        pt.typewrite("Dont worry sir.Untill the battery is over i will help you")
        pt.typewrite('\n')
    elif val[0]=="a" and val[1]=="_":
        msg=""
        n=""
        for i in range(2,len(val)):
            n=n+val[i]
        hh=n[0]+n[1]
        mm=n[3]+n[4]
        app=n[6]+n[7]
        for i in range(11,len(val)):
            msg=msg+val[i]
        xx = threading.Thread(target=alarm, args=(hh,mm,app,msg))
        xx.start()
        pt.click(x,y)
        pt.typewrite("Sir ! Alarm Set")
        pt.typewrite('\n')
       
        
    elif val[0]=="n" and val[1]=="_":
        ne=""
        for i in range(2,len(val)):
            ne=ne+val[i]
        googlenews = GoogleNews()
        googlenews.set_lang('en')
        googlenews.set_period('1d')
        googlenews.set_encode('utf-8')
        googlenews.get_news(ne)
        googlenews.search(ne)
        googlenews.get_page(1)
        news=googlenews.get_texts()
        pt.click(x,y)
        pt.typewrite("Sir ! Here is your news")
        pt.hotkey('ctrl', 'enter')
        pt.hotkey('ctrl', 'enter')
        for i in range(len(news)):
            if news[i]==".":
                break
            pt.typewrite(news[i])
        pt.typewrite('\n')
        
    elif "screen" in val:
        try:
            bri=val[7]+val[8]
        except:
            bri=val[7]
        bri=int(bri)
        sbc.set_brightness(bri)
        pt.click(x,y)
        pt.typewrite("Sir ! Lap Screen brightness is changed to "+str(bri)+" %")
        pt.typewrite('\n')
        
    elif val=="ok bby":
        pt.click(x,y)
        pt.typewrite("ok bby")
        pt.typewrite('\n')
    elif val=="oh yeah":
        pt.click(x,y)
        pt.typewrite("oh no")
        pt.typewrite('\n')
    elif val=="oh no":
        pt.click(x,y)
        pt.typewrite("ok yeah")
        pt.typewrite('\n')
    
    elif val=="what are you doing":
        pt.click(630,738)
        pt.typewrite("helping to my _*BOSS*_")
        pt.typewrite('\n')
    elif "your age" in val:
        pt.click(x,y)
        pt.typewrite("I am 19 Years Old")
        pt.typewrite('\n')
    elif val=="my birthday date" or val=="my birthday":
        bd = datetime(2002,2,11)
        now = datetime.now()
        date1 = now
        date2 = datetime(now.year, bd.month, bd.day)
        delta = date2 - date1
        days = delta.total_seconds() / 60 /60 /24
        days=(int(days))
        days=str(days)
        pt.click(x,y)
        days="We have *"+days+"* number of days"
        pt.typewrite(days)
        pt.hotkey('ctrl', 'enter')
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("I am waiting for party sir!")
        pt.typewrite('\n')
    elif val=="bye":
        pt.click(x,y)
        pt.typewrite("Bye....")
        pt.typewrite('\n')
    elif val=="gn" or val =="good night":
        no = datetime.now()
        ho=str(no.hour)+":"+str(no.minute)+":"+str(no.second)
        s = datetime.strptime(str(ho),"%H:%M:%S")
        hors=s.strftime("%r")
        pt.click(x,y)
        pt.typewrite("Sir ! Time is just "+str(hors))
        pt.typewrite(" Why sir going to sleep ,wheather are you not feeling well.Take care sir")
        pt.typewrite('\n')
    elif "instamsg" in val or "instagrammsg" in val or "instagrammessage" in val:
        val.split('/')
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        pt.click(x,y)
        pt.typewrite("Sir ! Message will be sent in a minute")
        pt.typewrite('\n')
        i = threading.Thread(target=insta,args=(a1[1],a1[2]))
        i.start()
    elif "passsave" in val:
        val=val.replace("passsave","")
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        pass_save(a1[1],a1[2],a1[3])
    elif "passopen" in val:
        val=val.replace("passopen","")
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        file=a1[1]
        try:
            f=open("F:/pass/"+file+".txt","r")
            va=f.read()
        except:
            pt.click(x,y)
            pt.typewrite("Sir ! File Name is wrong")
            pt.typewrite('\n')
            return
        a=[]
        p=""
        for i in range(len(va)):
            if va[i]=="/":
                va[i]
                a.append(p)
                p=""
                continue
            p=p+va[i]
        a.append(p)
        pt.click(x,y)
        pt.typewrite("Sir ! "+str(file))
        pt.hotkey('ctrl', 'enter')
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("User name : "+str(a[0]))
        pt.hotkey('ctrl', 'enter')
        pt.hotkey('ctrl', 'enter')
        pt.typewrite("Pass word : "+str(a[1]))
        pt.hotkey('ctrl', 'enter')
        pt.typewrite('\n')

    elif "passdel" in val:
        val=val.replace("passdel","")
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        pd=a1[1]
        dell="F:/pass/"+pd+".txt"
        if os.path.exists(dell):
            os.remove(dell)
            pt.click(x,y)
            pt.typewrite("Sir ! The password file Deleted")
            pt.typewrite('\n')
        else:
            pt.click(x,y)
            pt.typewrite("Sir ! The password file does not exit")
            pt.typewrite('\n')
        
    elif "delpassfolder" in val:
        
        try:
            shutil.rmtree("F:/pass")
            pt.click(x,y)
            pt.typewrite("Sir ! The password folder Deleted")
            pt.typewrite('\n')
        except:
            pt.click(x,y)
            pt.typewrite("Sir ! The password folder does not exit")
            pt.typewrite('\n')
    elif "wishes" in val:
        pt.click(x,y)
        pt.typewrite("Let your New year begins with love and happiness")
        pt.typewrite('\n')
    elif "product" in val:
        val=val.replace("product","")
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        pro=a1[1]
        pt.click(x,y)
        pt.typewrite("Sir ! Wait a second product details will be sent now")
        pt.typewrite('\n')
        drive.get("http://google.com/?#q="+pro)
        sleep(2)
        drive.maximize_window()
        sleep(1)
        pt.hotkey('prtscr')
        drive.minimize_window()
        pt.click(x,y)
        pt.click(x,y)
        pt.hotkey('ctrl','v')
        sleep(1)
        pt.click(1294,627)
        sleep(1)
        pt.click(x,y)
        pt.typewrite("Sir ! The screenshot of Product")
        pt.typewrite('\n')
    elif "qrcode" in val:
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="/":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        path="E:/"
        path=path+str(a1[1])+'.png'
        qr= pyqrcode.create(a1[1])
        qr.png(path, scale=8)
        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        pt.click(x,y)
        pt.typewrite("Sir ! Your Qrcode is")
        pt.typewrite('\n')
        pt.hotkey('ctrl', 'v')
        sleep(2)
        pt.click(1294,627)
    elif "meet" in val:
        a1=[]
        k=""
        for i in range(len(val)):
            if val[i]=="_":
                val[i]
                a1.append(k)
                k=""
                continue
            k=k+val[i]
        a1.append(k)
        print(a1)
        cl=a1[1]+a1[2]+a1[3]+a1[4]+a1[5]
        f = open("E:/whatsapp/class.txt", "w")
        f.write(cl)
        f.close()
        os.system("E:\python\automation\meet automation.py")
        pt.click(x,y)
        pt.typewrite("Sir ! Please wait sir")
        pt.typewrite('\n')
        

    elif "speedtest" in val:
        sp()
    elif "--help" in val:
        cmd=["shutdown","ok","date","time","you sleep","weather","qrcode/message"
             ,"usdtoinr","W_ for wikipedia ex: w_pubg","lap charge"
             ,"a_ for alaram ex:a_12:50:pm","n_ for news ex:n_whatsapp"
             ,"screen/50","instamsf/username/message"
             ,"passsave/filename/username/password","passopen/filename"
             ,"passdel/filename","product/samsung","wishes","delpassfolder"
             ,"my birthday","you age","bye","gn","my marrage date"
             ,"do you love me","what are you doing","speedtest"
             ]
        pt.click(x,y)
        for i in cmd:
            pt.typewrite(i)
            pt.hotkey('ctrl', 'enter')

        pt.typewrite('\n')

    
        
    else:
        pt.click(x,y)
        pt.typewrite("Sir ! Unknow Command")
        pt.typewrite('\n')

def copied():
    sleep(2)
    if pt.pixelMatchesColor(529,680,(255,255,255)):
        pt.tripleClick(545,666)
        pt.hotkey('ctrl', 'c')
        val=pyperclip.paste()
        process(val.lower())
    else:
        pass
    sleep(1)
    






now =datetime.now()
if  now.hour<12:
    speaks="Good Morning Sir"
elif now.hour >=12 and now.hour < 16:
    speaks="Good Afternoon Sir"
elif now.hour >=16 and now.hour < 24:
    speaks="Good Evening Sir"

pt.click(x,y)
pt.typewrite(speaks)
pt.hotkey('ctrl', 'enter')
pt.typewrite("My name is  Nora.")
pt.hotkey('ctrl', 'enter')
pt.typewrite("How can i help you Sir")
pt.hotkey('ctrl', 'enter')
pt.typewrite("I am your Web Assistant sir ")
pt.hotkey('ctrl', 'enter')
pt.hotkey('ctrl', 'enter')
pt.hotkey('ctrl', 'enter')
pt.hotkey('ctrl', 'enter')
pt.typewrite("Programmer By")
pt.hotkey('ctrl', 'enter')
pt.typewrite("             Mr.Programmer")

pt.typewrite('\n')
while True:
    copied()



