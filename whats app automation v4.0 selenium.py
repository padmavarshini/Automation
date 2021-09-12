from tkinter import filedialog
from tkinter import * 
b=[]
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from string import Template
from time import sleep
# create a new Chrome session
def read_template(filename):

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return template_file_content

message_template = read_template('D:/project/edc/msg.txt')



def browse_button():
    global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    print(filename)
    data = pd.read_csv(filename)
    no=data["Phone"]
    df = pd.DataFrame(no)
    print(df.isnull().sum())
    df = df.fillna(0)
    l=len(df)
    b.append(l)
    driver = webdriver.Chrome("D:/project/edc/chromedriver.exe")
    driver.get('https://web.whatsapp.com/')

    def webapp():
        try:
            check = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/ol/li[1]')
            elem = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/ol/li[1]')
    #imgcheck = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
            if(check == elem):
                return True
            else:
                return False
        except:
            #will come to this clause when page will throw error.
            return False
        
    
    def login_check():
        try:
            imgcheck = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
            img = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
    #imgcheck = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
            if(imgcheck == img):
                return False
            else:
                return True
        except:
            #will come to this clause when page will throw error.
            return True
        
        
    while(True):
        if webapp():
            print('Pls log in')
            webapp()
        else:
            print('Logged in successfully and while loop breaked') 
            break
    
    print('Logged in successfully and while loop breaked**********')    
    
    
    while(True):
        if login_check():
            print('logging in')
            login_check()
        else:
            print('Success and while loop breaked') 
            break
    print('Successsssssss')  

    for i in range(l):
        driver.execute_script("window.open('');")
        sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://api.whatsapp.com/send?phone=91"+str(no[i]))
        sleep(3)
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        sleep(3)
        
        messagebox = driver.find_element_by_xpath('//*[@id="action-button"]')
        messagebox.click()                               
        sleep(5)                 
        whatsappweb = driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
        whatsappweb.click()
        
        def home_page():
            try:
                typebarcheck = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                typebar = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        #imgcheck = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img')
                if(typebarcheck == typebar):
                    return False
                else:
                    return True
            except:
                #will come to this clause when page will throw error.
                return True
        
        
        while(True):
            if home_page():
                print('loading...')
                home_page()
            else:
                print('Loaded') 
                break
        
        print('Main Page loaded')
        typebar = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        typebar.send_keys(message_template)
        
        driver.find_element_by_tag_name('body').send_keys(Keys.ENTER) 
        
root = Tk()

#lbl1 = Label(root,textvariable=folder_path)
#lbl1.grid(row=0, column=1)
folder_path = StringVar()
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)
