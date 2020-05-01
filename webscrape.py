from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

GitaDict={
'1':'46',
'2':'72',
'3':'43',
'4':'42',
'5':'29',
'6':'47',
'7':'30',
'8':'28',
'9':'34',
'10':'42',
'11':'55',
'12':'20',
'13':'35',
'14':'27',
'15':'20',
'16':'24',
'17':'28',
'18':'78'
}

driver = webdriver.Chrome("C:\\Users\\vaijr\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\chromedriver")
filename = 'holy_gita_complete1.txt'

try:
    file = open(filename,'a+',encoding='utf-8')

    for chapter_no in GitaDict.keys():
            for verse_no in range(1,int(GitaDict.get(chapter_no))+1):

                    url = 'https://www.holy-bhagavad-gita.org/chapter/'+chapter_no+'/verse/'+str(verse_no)

                    print('Date Time:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),':',url)
                    
                    verseMain, verses_literal,verse_descript = [],[],[]
                   
                    driver.get(url)

                    content = driver.page_source

                    soup = BeautifulSoup(content, features='html.parser')
                    for a in soup.findAll(attrs={'class':'article'}):
                            v_verseMain       = a.find('div', attrs={'id':'transliteration'})
                            v_verses_literal  = a.find('div', attrs={'id':'translation'})
                            v_verse_descript  = a.find('div', attrs={'id':'commentary'})
                            
                            if v_verseMain is not None:
                                    verseMain.append(v_verseMain.text)

                            if v_verses_literal is not None:
                                    verses_literal.append(v_verses_literal.text)
                            
                            if v_verse_descript is not None:
                                    verse_descript.append(v_verse_descript.text) 

                    file.write(''.join([str(i) for i in verseMain + verses_literal + verse_descript]))
                   
except:
    print('Error:',Exception)
    
finally:                
    file.close()
    driver.close()