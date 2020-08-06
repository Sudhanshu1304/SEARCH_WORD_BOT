from selenium import webdriver
import pyautogui

import pytesseract
import cv2
#import matplotlib.pyplot as plt
import time

url='http://word-search-puzzles.appspot.com/'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)


no_of_answers=driver.find_element_by_id('words_left').text

l=list(no_of_answers)
l=''.join(l)
l=int(l[-2:])


a=driver.find_element_by_id('word_list').text
time.sleep(1)
from selenium.webdriver.common.action_chains import ActionChains

'''                         If You Want the BOT THO SOLVE THE WHOLE GAME SET VAL=0                 '''

VAL=5

element = driver.find_element_by_xpath('//*[@id="word_list"]/li[{}]'.format(l-VAL))
actions = ActionChains(driver)
actions.move_to_element(element).perform()
b=driver.find_element_by_id('word_list').text


ll=[]
for i in range(len(a)):
    ll.append(a[i])


for i in range(len(b)):
    ll.append(b[i])

ll=''.join(ll)
ll=ll.split('\n')


##                                        Getting The Grid Of Search Word                                             ##

image=pyautogui.screenshot(region=(800,330,930,728))#800,330,930,728


image.save('imae.png')

img = cv2.imread('imae.png')
img2= cv2.imread('imae.png')
img3= cv2.imread('imae.png')

from skimage.filters import threshold_mean

from skimage.filters import threshold_triangle,threshold_otsu
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

img3>th3

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
custom_oem_psm_config = r'--oem 3 --psm 6'

p=pytesseract.image_to_string(img, config=custom_oem_psm_config)
p2=pytesseract.image_to_string(img2, config=custom_oem_psm_config)
p3=pytesseract.image_to_string(img3, config=custom_oem_psm_config)

if len(p2)<len(p) and len(p2)<len(p3):
    p=p2
elif len(p3)<len(p) and len(p3)<len(p):
    p=p3
else:
    p=p

print('Final len :',len(p))

p=p.split('\n')
col=16

for row in range(len(p)):
    #print(len(p[row]))
    l=len(p[row])
    x=list(p[row])
    for i in  p[row]:
        if i==' ' :
            x.remove(' ')
        if i=="'":
            x.remove("'")
    x=''.join(x)
    p[row]=x
    if l>col:
        p[row]=list(p[row])

        for elem in p[row]:

            if elem=='!':
                p[row].remove('!')
            elif elem=='|':
                p[row].remove('|')
            elif elem==')':
                p[row].remove(')')

        p[row]=''.join(p[row])

#print('Final \n\n',p)

for r in range(len(p)):
    if len(p[r])>col:
        #v=col-len(p[r])
        p[r]=p[r][:16]
    #print(len(p[r]),p[r])
    elif len(p[r])<col:
        p[r]=p[r]+"A"

p=''.join(p)
p=p.upper()

p=list(p)


for e in range(len(p)):

    if p[e]=='1' :
        p.pop(e)
        p.insert(e,'I')

    if p[e] == '!':
        p.pop(e)
        p.insert(e, 'I')
    if p[e] == '|':
        p.pop(e)
        p.insert(e, 'I')
    if p[e]=='0':
        p.pop(e)
        p.insert(e, 'O')
    if p[e]=='2':
        p.pop(e)
        p.insert(e, 'Z')
    if p[e]==')':
        p.pop(e)
        p.insert(e, 'O')
    if p[e]=='}':
        p.pop(e)
        p.insert(e, 'J')
p=''.join(p)
p=p[:224]
#print('\n\n',p,len(p))

