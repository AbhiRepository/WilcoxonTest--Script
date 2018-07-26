import os
import re
import time
import string
import numpy as np
import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.color import Color

totalRun = 25
Alpha = 2
Tails = 2

curr_dir = os.getcwd()
filename = os.listdir(curr_dir)

algoOne = 'algoOne.txt'
algoTwo = 'algoTwo.txt'

numValOne = []
valOne = []
i = 1
res = ''
numRes = []
f = open(algoOne,'r')
for line in f:
    numRes.append(float(line))
    res = res + line
    if i == 25:
        valOne.append(res)
        numValOne.append(numRes)
        res = ''
        numRes = []
        i = 0
    i = i+1
f.close()


numValTwo = []
valTwo = []
i = 1
res = ''
numRes = []
f = open(algoTwo,'r')
for line in f:
    numRes.append(float(line))
    res = res + line
    if i == 25:
        valTwo.append(res)
        numValTwo.append(numRes)
        res = ''
        numRes = []
        i = 0
    i = i+1
f.close()



numValOne = np.array(numValOne)
numValTwo = np.array(numValTwo)

if numValTwo.shape == numValOne.shape:
    print 'Correct sample size'
else:
    print 'Check your sample size'



times1 = len(valTwo)

driverPath = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path = driverPath)

driver.get("http://www.socscistatistics.com/tests/signedranks/Default2.aspx")

for times in range(times1):
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_name("ctl00$MainContent$TextBox1"), valOne[times])
    
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_name("ctl00$MainContent$TextBox2"), valTwo[times])
    
    driver.find_element_by_name("ctl00$MainContent$Button1").click()
    time.sleep(5)
    rgb = driver.find_element_by_id("ctl00_MainContent_Label9").value_of_css_property('color')
    hex = Color.from_string(rgb).hex
    
    #print times
    #print hex
    if hex == '#0000ff':
        #print 'Significant'
        elem = driver.find_element_by_id("ctl00_MainContent_Label1")
        txtScrape = elem.text
        f = open('resultSign.txt', 'w')
        f.write(txtScrape)
        f.close
        f = open('resultSign.txt','r')
        txtScrape = f.read()
        txt = string.split(txtScrape,'\n')
        txt = filter(None, txt)

        vals = []
        for i in range(len(txt)):
            if i == 2 or i == 3:
                vals.append(string.split(txt[i],':')[-1])
        if vals[0]>vals[1]:
            print '+'
        else:
            print '-'
    else :
        #print 'Not Significant'
        print '='

